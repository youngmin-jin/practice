# SQL queries
- ARRAY
  : it is possible to run ARRAY functions in BigQuery

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
    <img width="174" alt="image" src="https://github.com/youngmin-jin/practice/assets/135728064/7bd6d355-8173-4171-a1d3-628e4e97840d">


