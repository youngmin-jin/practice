# Dataform
- open-source framework for managing and orchestrating SQL-based transformations in BigQuery
- provides a way to build, test, and deploy data pipelines using SQL and JavaScript
- version control and collaboration
- automated code validation
- improved data pipeline maintainability
- dependency management


<br><br>
## Link to Git/ Authentication
1. Create a repository in Dataform and Git
2. Grant required roles to the service account in GCP
3. Generate an access token in Git, and register that to Security Manager in GCP
4. Connect Dataform repository and git repository using the registered git access token
- https://www.youtube.com/watch?v=285HnXL9_rk 10:38~


<br><br>
## Components
<image src="https://github.com/youngmin-jin/practice/assets/135728064/a63b493c-a203-4f79-8be7-deb18065eea0" width="600">

### 1. Repository
- 'git' <br>
  <kbd><image src="https://github.com/youngmin-jin/practice/assets/135728064/744da4ce-b4a9-4356-939f-efb595f69fff" width="600"></kbd> <br>
<br>

### 2. Workspace
- 'branch' in git <br>
  <kbd><image src="https://github.com/youngmin-jin/practice/assets/135728064/e24f2e28-ba49-4e7d-83d2-34991933f53d" width="600"></kbd> <br>
<br>

### 3. Files
- Definitions
  - sqlx or javascript files to create or increment new tables or views
  - e.g., test.sqlx <br>
    <kbd><image src="https://github.com/youngmin-jin/practice/assets/135728064/33556706-6807-456c-8cb6-e5fccd76fc6c" width="600"></kbd> <br>

- Includes
  - javascript files where you can define variables and functions to use in your project
  - e.g., date_config.js <br>
    <kbd><image src="https://github.com/youngmin-jin/practice/assets/135728064/fc61e915-f9d1-4378-8207-8476a2f2a4f8" width="600"></kbd> <br>

- dataform.json
  - define database and others
  - e.g., <br>
    <kbd><image src="https://github.com/youngmin-jin/practice/assets/135728064/ea0fb1a0-9fef-4725-be4e-1e49d8933bbd" width="600"></kbd>

<br><br>
## Assertions
- SQL query acting as a data quality check
- verifies whether specific conditions hold true for your data
- built-in assertions: nonNull, uniqueKey, rowConditions..
- e.g., built-in assertions
  - two assertions "uniqueKey" and "rowConditions" in source_table.sqlx <br>
    <kbd><image src="https://github.com/youngmin-jin/practice/assets/135728064/f78db4c5-9f3a-4ba3-9531-d0765f80a29e" width="300"></kbd> <br><br>
    <kbd><image src="https://github.com/youngmin-jin/practice/assets/135728064/cc970ff4-684a-4e3c-a994-f22809fa538b" width="600"></kbd> <br><br>
  - if the result is not qualified to the assertion, then it would fail <br>
    <kbd><image src="https://github.com/youngmin-jin/practice/assets/135728064/7c0d28d3-7569-40fd-82c0-adaf19825c8f" width="600"></kbd> <br>

- e.g., manual assertions
  ```
  config {
    type: "assertion"
    assertionName: "check_column_accepted_values"
  }
  
  SELECT *
  FROM `<your_dataset>.<your_table>`
  WHERE `<your_column>` NOT IN ('value1', 'value2', 'value3');
  ```
  -> this sqlx file itself is an assertion


<br><br>
## Declaration
- define and register external data sources or objects within the Dataform
- e.g.,
  - declare the external data (from BigQuery) <br>
    <kbd><image src="https://github.com/youngmin-jin/practice/assets/135728064/301a1281-6463-4ea8-97fc-a456c41b0045" width="500"></kbd> <br><br>
    <kbd><image src="https://github.com/youngmin-jin/practice/assets/135728064/6d8febb3-7c3a-427b-8e17-e263e84f26df" width="500"></kbd> <br><br>
  - use that as ref table <br>
    <kbd><image src="https://github.com/youngmin-jin/practice/assets/135728064/ca5e8aca-9862-4eec-b506-40839dd31e59" width="500"></kbd> <br><br>


<br><br>
## Scheduler/ Execution
<kbd><image src="https://github.com/youngmin-jin/practice/assets/135728064/ce0a183b-1b09-4f91-b2c6-1980263ce0f1" width="700"></kbd> <br><br>

### - Cloud Composer




<br><br>
## Use cases
<details>
  <summary>Join two ref tables</summary>
  
  ```
  config { type: "table" }
  select a.date
          , a.country_iso_code_2
          , a.airport_name
          , c.region_geom
  from ${ref("schema", "airport_traffic")} as a
      join ${ref("schema", "commercial_traffic")} as c on a.country_iso_code_2 = c.country_iso_code_2
  limit 100
  ```

</details>

<details>
  <summary>Add description to the column</summary>
  
  ```
  config { 
     type: "table" 
     , columns: {
         ratio_confirmed_cases: "ratio of confirmed cases compared to population"
     } 
  }
  ```

</details>

<details>
  <summary>Use js file variables and functions (pre_operations)</summary>
  date_config.js 
  
  ```
  const var1 = '2024-06-01';

  function getStartTs() {
      return '2025-06-01';
  }
  
  module.exports = {
      var1
      , getStartTs
  }
  ```

  test_date_config.sqlx

  ```
  config { 
      type: "table" 
  }
  
  pre_operations {
      DECLARE var1 TIMESTAMP;
      DECLARE startTs TIMESTAMP;
  
      SET var1 = TIMESTAMP('${date_config.var1}');
      SET startTs = TIMESTAMP('${date_config.getStartTs()}');
  }
  
  SELECT 
      var1
      , startTs
  ```

  result <br>
  <kbd><image src="https://github.com/youngmin-jin/practice/assets/135728064/f793076a-263f-4938-b149-db8f10ce1f6e" width="700"></kbd>

</details>

<details>
  <summary>EXECUTE IMMEDIATE FORMAT (pre_operations)</summary>
  test_date_config.sqlx 
  
  ```
  config { 
      type: "table" 
  }
  
  pre_operations {
      DECLARE var1 TIMESTAMP;
      DECLARE startTs TIMESTAMP;
  
      SET var1 = TIMESTAMP('${date_config.var1}');
      SET startTs = TIMESTAMP('${date_config.getStartTs()}');
  
      EXECUTE IMMEDIATE FORMAT("""
          DELETE FROM ${self()}
          WHERE var1 = TIMESTAMP('2024-06-01 00:00:00 UTC') 
      """);
  }
  
  SELECT 
      var1
      , startTs
  ```
</details>



























