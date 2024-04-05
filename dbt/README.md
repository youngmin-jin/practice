## Ref
[Connect dbt to BigQuery](https://docs.getdbt.com/guides/bigquery?step=1)
<br/><br/>

## Concepts・Flow
<img src="https://github.com/youngmin-jin/practice/assets/135728064/8d780ba6-d339-47be-95d5-e4232d6a3d5e" width="700"> <br/>
- DBT (Data Building Tool) is an open source tool used in transforming data; the T in ELT
- Can transform data using SQL which is favor to analytics engineers
- Can write and execute the code **inside your data warehouse**

<br><br>

## Command
- dbt run <br/>
: reflect all changes to the destination (e.g., BigQuery)

- dbt test <br/>
: iterates through yml files  

- dbt docs generate
  - generate the docs for the project
  - dbt introspects the project and warehouse to generate a json file with rich docs about the project <br/><br/>
    <details>
      <summary>details here</summary>
        <img src="https://github.com/youngmin-jin/practice/assets/135728064/288e5d78-964a-4f74-bebe-77a18f3d9c28" width="700"> <br/><br/>
        <img src="https://github.com/youngmin-jin/practice/assets/135728064/4e7e4213-da29-4fed-9fce-fa8cf917bf44" width="600"> <br/><br/>
        <img src="https://github.com/youngmin-jin/practice/assets/135728064/5e27582e-7b30-4cb3-91f4-8ef67fb4a8e2" width="700"> <br/><br/>
    </details>
  
<br>

## Points・Cases
<details>
  <summary>No need to define the dependencies unlike Airflow</summary>
<br/>
customers.sql

```
with customers as (
    select * from {{ ref('stg_customers') }}
),
orders as (
    select * from {{ ref('stg_orders') }}
),
customer_orders as (
    select
        customer_id,
        min(order_date) as first_order_date,
        max(order_date) as most_recent_order_date,
        count(order_id) as number_of_orders
    from orders
    group by 1
),
final as (
    select
        customers.customer_id,
        customers.first_name,
        customers.last_name,
        customer_orders.first_order_date,
        customer_orders.most_recent_order_date,
        coalesce(customer_orders.number_of_orders, 0) as number_of_orders
    from customers
    left join customer_orders using (customer_id)
)
select * from final
```
<img src="https://github.com/youngmin-jin/practice/assets/135728064/c35ec984-1db0-469f-b552-9fc62d3bc318" width="600"> <br/>
-> customers.sql depends on stg_customers.sql and stg_orders.sql, dbt builds customers.sql last <br/>
-> no need to define these dependencies

</details>

<details>
  <summary>YAML files</summary>
<br/>
  
- dbt_project.yml
  - define model name, version, model`s materialized..
  ```  
  name: 'jaffle_shop'
  version: '1.0.0'
  config-version: 2
  
  profile: 'default'
  
  model-paths: ["models"]
  analysis-paths: ["analyses"]
  test-paths: ["tests"]
  seed-paths: ["seeds"]
  macro-paths: ["macros"]
  snapshot-paths: ["snapshots"]
  
  target-path: "target"  # directory which will store compiled SQL files
  clean-targets:         # directories to be removed by `dbt clean`
    - "target"
    - "dbt_packages"
  
  models:
    jaffle_shop:
      +materialized: table
  ```
<br>

- schema.yml
  - define model`s schema (name, description..) and test 
  ```
  version: 2
  
  models:
    - name: customers
      description: One record per customer
      columns:
        - name: customer_id
          description: Primary key
          tests:
            - unique
            - not_null
        - name: first_order_date
          description: NULL when a customer has not yet placed an order
  
    - name: stg_customers
      description: This model cleans up customer data
      columns:
        - name: customer_id
          description: Primary key
          tests:
            - unique
            - not_null
  
    - name: stg_orders
      description: This model cleans up order data
      columns:
        - name: order_id
          description: Primary key
          tests:
            - unique
            - not_null
        - name: status
          tests:
            - accepted_values:
                values: ['placed', 'shipped', 'completed', 'return_pending', 'returned']
        - name: customer_id
          tests:
            - not_null
            - relationships:
                to: ref('stg_customers')
                field: customer_id
  ```  
  -> it appears in the docs like below <br><br>
  <img src="https://github.com/youngmin-jin/practice/assets/135728064/2da8e110-5bcd-43d5-8d76-90f8f90f7d31" width="600"> <br/><br/>
  
  -> all 'tests' are tested when running 'dbt test' <br><br>
  <img src="https://github.com/youngmin-jin/practice/assets/135728064/e11b5339-5ee4-4b12-8b54-c5e44a9ec718" width="600">

</details>


<details>
  <summary>Change default setting from 'view' to 'table' by modyfing dbt_project.yml</summary>
  
### 1. Confirm that the default was a 'view' in dbt_project.yml and BigQuery UI
<img src="https://github.com/youngmin-jin/practice/assets/135728064/af730daf-9074-4ac0-a1f8-51f425dff041" width="700"> <br/><br/>
<img src="https://github.com/youngmin-jin/practice/assets/135728064/7e962a6f-c5a9-4f0c-9778-e1f6d0942002" width="700"> <br/><br/>

### 2. Change 'view' to 'table' in dbt_project.yml
<img src="https://github.com/youngmin-jin/practice/assets/135728064/828e3676-7538-4d19-bcd2-2724a145b429" width="700"> <br/><br/>

### 3. Commit and run 'dbt run'
<img src="https://github.com/youngmin-jin/practice/assets/135728064/123df0fb-95e7-4ce1-b376-5d9bf04af860" width="700"> <br/><br/>
<img src="https://github.com/youngmin-jin/practice/assets/135728064/aa70c682-7d06-4533-9437-7c8a504b3752" width="700"> <br/><br/>

### 4. Confirm the change
<img src="https://github.com/youngmin-jin/practice/assets/135728064/24796b1f-4b20-40c6-b547-da1cc36d0fc1" width="700"> <br/><br/>

*if 'dbt run' cannot be executed, restart IDE<br/>
<img src="https://github.com/youngmin-jin/practice/assets/135728064/1319f97e-7846-434c-83d9-49a330b94c1f" width="700"> <br/><br/>

### (Optional) Set differently upon a model by adding below to the top of the code
<img src="https://github.com/youngmin-jin/practice/assets/135728064/c99767ed-13f6-4dad-a46e-675ca85b9395" width="700"> <br/><br/>
<img src="https://github.com/youngmin-jin/practice/assets/135728064/a205671f-1820-42bc-9d99-858d9413b8ea" width="700"> <br/><br/>

</details>


<details>
  <summary>Deploy the project</summary>

### Ref
https://docs.getdbt.com/guides/bigquery?step=15

### 1. Create a deployment environment
1. In the upper left, select Deploy, then click Environments.
2. Click Create Environment.
3. In the Name field, write the name of your deployment environment. For example, "Production."
4. In the dbt Version field, select the latest version from the dropdown.
5. Under Deployment connection, enter the name of the dataset you want to use as the target, such as "Analytics".This will allow dbt to build and work with that dataset. For some data warehouses, the target dataset may be referred to as a "schema".
6. Click Save.

### 2. Create and run a job
1. After creating your deployment environment, you should be directed to the page for a new environment. If not, select Deploy in the upper left, then click Jobs.
2. Click Create one and provide a name, for example, "Production run", and link to the Environment you just created.
3. Scroll down to the Execution Settings section.
4. Under Commands, add this command as part of your job if you don't see it:
```
dbt build
```
5. Select the Generate docs on run checkbox to automatically generate updated project docs each time your job runs.
6. For this exercise, do not set a schedule for your project to run — while your organization's project should run regularly, there's no need to run this example project on a schedule. Scheduling a job is sometimes referred to as deploying a project.
7. Select Save, then click Run now to run your job.
8. Click the run and watch its progress under "Run history."
9. Once the run is complete, click View Documentation to see the docs for your project.

</details>













