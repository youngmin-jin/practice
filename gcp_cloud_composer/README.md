# Cloud Composer

## Grant a role before creation
https://cloud.google.com/composer/docs/composer-2/create-environments
<br>
### 1) when using the default service account
- When you enable Cloud Composer API in your project, the Composer Service Agent account is created in your project. 
- Add below roles manually.
  ```
  Cloud Composer v2 API Service Agent Extension role
  ```

### 2) when using a new user-managed service account 
- Create a new service account in IAM.
- Add below roles manually.
  ```
  Cloud Composer API Service Agent
  Cloud Composer v2 API Service Agent Extension role
  Composer Worker
  ```
