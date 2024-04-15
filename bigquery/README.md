## Functions
- **ARRAY** <br>
<img src="https://github.com/youngmin-jin/practice/assets/135728064/06e11c32-e36d-40cf-8391-78f44cfe4e43" width="300"><br><br>


- **STRUCT** <br>
<img src="https://github.com/youngmin-jin/practice/assets/135728064/26b78212-414e-4d01-bc37-58becb8220aa" width="150"><br><br>


- **UNNEST(RECORD)**: unnest an ARRAY <br>
  <img src="https://github.com/youngmin-jin/practice/assets/135728064/978be9ac-cc2b-43eb-801d-566794847d62" width="250">
  ```
  select protopayload_auditlog.authenticationInfo.principalEmail
        , pa.resource
  from `da-enjinia-onboarding.5254_test.cloudaudit_googleapis_com_data_access_20240412`
        , UNNEST(protopayload_auditlog.authorizationInfo) pa
  ```
  -> "UNNEST(protopayload_auditlog.authenticationInfo) pa1" is impossible as authenticationInfo is not an ****ARRAY****, it is a **STRUCT** <br><br>


- **JSON_EXTRACT_SCALAR(json_string_expr[, json_path])**: extract info from JSON format <br>
  <img src="https://github.com/youngmin-jin/practice/assets/135728064/98bd5276-1597-4577-baa6-351e11cf7036" width="250">
  ```
  select logname
        , resource
        , protopayload_auditlog.authenticationInfo.principalEmail
        , timestamp
        , json_extract_scalar(protopayload_auditlog.metadataJson, "$.jobChange.job.jobConfig.queryConfig.priority") as query_type
        , json_extract_scalar(protopayload_auditlog.metadataJson, "$.jobChange.job.jobStats.queryStats.totalBilledBytes") as total_billed_gb
        , json_extract_scalar(protopayload_auditlog.metadataJson, "$.jobChange.job.jobStats.queryStats.totalProcessedBytes") as total_processed_gb
        , json_extract_scalar(protopayload_auditlog.metadataJson, "$.jobChange.job.jobStats.queryStats.outputRowCount") as total_produced_rows
        , json_extract_scalar(protopayload_auditlog.metadataJson, "$.jobChange.job.jobConfig.queryConfig.query") as metadataquery      
        , severity
  from `da-enjinia-onboarding.5254_log.cloudaudit_googleapis_com_data_access_20240415`
  where json_extract_scalar(protopayload_auditlog.metadataJson, "$.jobChange.job.jobConfig.queryConfig.priority") is not null;
  ```

  
