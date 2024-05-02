# Dataform
- open-source framework for managing and orchestrating SQL-based transformations in BigQuery
- provides a way to build, test, and deploy data pipelines using SQL and JavaScript
- version control and collaboration
- automated code validation
- improved data pipeline maintainability
- dependency management <br><br>
  <image src="https://github.com/youngmin-jin/practice/assets/135728064/250e3b2e-ce93-451b-a961-8f2154f8e1d1" width="500">


<br><br>
## Workflow Execution Scheduling Options
- Workflow configurations in Dataform
- Workflows and Cloud Scheduler
- Cloud Composer


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
- centralized storage location for managing and version controlling code and related assets
- correspond to each git repository/ able to connect with git <br><br>
<image src="https://github.com/youngmin-jin/practice/assets/135728064/8934827f-ba84-4cb6-be77-4e870434b6c0" width="400">

### 2. Workspace
- 'branch' in git
- separate environment where changes can be made and tested independetly before merging them into main

### 3. Files
- Config files
  - config json, sqlx files to configure the SQL workflows 
  - contain general configuration, execution schedules, schema for new tables and views 
  - e.g.,
    - sqlx file <br>
      <kbd><image src="https://github.com/youngmin-jin/practice/assets/135728064/33556706-6807-456c-8cb6-e5fccd76fc6c" width="500"></kbd> <br>
    - dataform.json <br>
      <kbd><image src="https://github.com/youngmin-jin/practice/assets/135728064/ea0fb1a0-9fef-4725-be4e-1e49d8933bbd" width="500"></kbd>

- Definitions
  - sqlx, javascript files to define new tables and views/ additional SQL operations to run in BigQuery

- Includes
  - javascript files where you can define variables and functions to use in your project


<br><br>
## Assertions
- SQL query acting as a data quality check
- verifies whether specific conditions hold true for your data
- built-in assertions: nonNull, uniqueKey, rowConditions..
- e.g., built-in assertions
  - two assertions "uniqueKey" and "rowConditions" in source_table.sqlx <br>
    <kbd><image src="https://github.com/youngmin-jin/practice/assets/135728064/f78db4c5-9f3a-4ba3-9531-d0765f80a29e" width="200"></kbd> <br><br>
    <kbd><image src="https://github.com/youngmin-jin/practice/assets/135728064/cc970ff4-684a-4e3c-a994-f22809fa538b" width="500"></kbd> <br><br>
  - if the result is not qualified to the assertion, then it would fail <br>
    <kbd><image src="https://github.com/youngmin-jin/practice/assets/135728064/7c0d28d3-7569-40fd-82c0-adaf19825c8f" width="500"></kbd> <br>

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
    <kbd><image src="https://github.com/youngmin-jin/practice/assets/135728064/301a1281-6463-4ea8-97fc-a456c41b0045" width="400"></kbd> <br><br>
    <kbd><image src="https://github.com/youngmin-jin/practice/assets/135728064/6d8febb3-7c3a-427b-8e17-e263e84f26df" width="400"></kbd> <br><br>
  - use that as ref table <br>
    <kbd><image src="https://github.com/youngmin-jin/practice/assets/135728064/ca5e8aca-9862-4eec-b506-40839dd31e59" width="400"></kbd> <br>




<br><br>
## Ref
- https://www.youtube.com/watch?v=285HnXL9_rk

























