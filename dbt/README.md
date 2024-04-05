## Ref
[Connect dbt to BigQuery](https://docs.getdbt.com/guides/bigquery?step=1)
<br/><br/>

## Characteristics
- No need to explicitly define the dependencies unlike Airflow <br/><br/>
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

<br/><br/>

## Command
- dbt run
<br/><br/>

## Cases
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
  <summary></summary>



</details>













