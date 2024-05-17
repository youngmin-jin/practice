# Cloud Composer

## Grant a role before creation
https://cloud.google.com/composer/docs/composer-2/create-environments
<br>
### 1) when using the default service account
- When you enable Cloud Composer API in your project, the Composer Service Agent account is created in your project. 
- Need to add "Cloud Composer v2 API Service Agent Extension role" to Cloud Composer Service Agent account manually. 

### 2) when using a new user-managed service account 
- Create a new service account in IAM.
- Add "Cloud Composer API Service Agent" and "Cloud Composer v2 API Service Agent Extension role" to the new service account manually.
