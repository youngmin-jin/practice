## Functions
- UNNEST(RECORD)
  ```
  select p.permission
          , count(*)
  from `da-enjinia-onboarding.5254_test.cloudaudit_googleapis_com_data_access_20240412`, 
    UNNEST(protopayload_auditlog.authorizationInfo) p
  group by p.permission
  ```
  <img src="https://github.com/youngmin-jin/practice/assets/135728064/836242af-86d0-4461-b703-b7f2b97774df" width="300">

- 
