# SQL queries
- ARRAY: it is possible to run ARRAY functions in BigQuery

  - ARRAY_LENGTH
    ```
    WITH Sequences AS(
      SELECT [0,1,1,2,3,5] AS some_numbers
      UNION ALL SELECT [2,4,8,16,32] AS some_numbers
      UNION ALL SELECT [5,10] AS some_numbers
    )
    SELECT some_numbers, ARRAY_LENGTH(some_numbers) AS len
    FROM Sequences;
    ```
    <img width="174" alt="image" src="https://github.com/youngmin-jin/practice/assets/135728064/7bd6d355-8173-4171-a1d3-628e4e97840d"><br/>
    ref: https://cloud.google.com/bigquery/docs/arrays?hl=ja<br/><br/>

- OFFSET: add index
  ```
  SELECT *
  FROM UNNEST(['foo','sdfd','ss','dfd']) AS element
  WITH offset AS offset
  ORDER BY offset;
  ```
  <img width="248" alt="image" src="https://github.com/youngmin-jin/practice/assets/135728064/aa8a990b-cdf8-44ed-894a-aa18b5acb5e8"><br/>

- UNNEST
  ```
  SELECT 
    p.v2ProductName
    , p.v2ProductCategory
    , SUM(p.productQuantity) AS units_sold
    , ROUND(SUM(p.localProductRevenue), 2) AS revenue
  FROM 
    `data-to-insights.ecommerce.web_analytics`
    , UNNEST(hits) AS h
    , UNNEST(product) AS p
  GROUP BY p.v2ProductName, p.v2ProductCategory
  ORDER BY revenue DESC
  LIMIT 5
  ```
  *if the column is nested within another column
  
