## Functions
- ARRAY <br>
<img src="https://github.com/youngmin-jin/practice/assets/135728064/06e11c32-e36d-40cf-8391-78f44cfe4e43" width="300"><br>

- STRUCT <br>
<img src="https://github.com/youngmin-jin/practice/assets/135728064/26b78212-414e-4d01-bc37-58becb8220aa" width="150"><br>

- UNNEST(RECORD): unnest an ARRAY <br>
  <img src="https://github.com/youngmin-jin/practice/assets/135728064/978be9ac-cc2b-43eb-801d-566794847d62" width="300">
  ```
  select protopayload_auditlog.authenticationInfo.principalEmail
        , pa.resource
  from `da-enjinia-onboarding.5254_test.cloudaudit_googleapis_com_data_access_20240412`
        , UNNEST(protopayload_auditlog.authorizationInfo) pa
  ```
  -> 「UNNEST(protopayload_auditlog.authenticationInfo) pa1」is impossible as authenticationInfo is not an ****ARRAY****, it is a **STRUCT** <br>

