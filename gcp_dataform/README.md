# Dataform
- open-source framework for managing and orchestrating SQL-based transformations in BigQuery
- provides a way to build, test, and deploy data pipelines using SQL and JavaScript
- version control and collaboration
- automated code validation
- improved data pipeline maintainability
- dependency management <br><br>
  <image src="https://github.com/youngmin-jin/practice/assets/135728064/250e3b2e-ce93-451b-a961-8f2154f8e1d1" width="500">


<br><br>
## Components
<image src="https://github.com/youngmin-jin/practice/assets/135728064/a63b493c-a203-4f79-8be7-deb18065eea0" width="600">

- Repository
  - centralized storage location for managing and version controlling code and related assets
  - correspond to each git repository/ able to connect with git <br><br>
    <image src="https://github.com/youngmin-jin/practice/assets/135728064/8934827f-ba84-4cb6-be77-4e870434b6c0" width="500"><br><br>
    <image src="https://github.com/youngmin-jin/practice/assets/135728064/33c2edfc-122c-43bc-af21-0cf6c87670fb" width="700">

- Workspace
  - 'branch' in git
  - separate environment where changes can be made and tested independetly before merging them into main

- Files
  - Config files
    - config json, sqlx files to configure the SQL workflows
    - contain general configuration, execution schedules, schema for new tables and views
  - Definitions
    - sqlx, javascript files to define new tables and views/ additional SQL operations to run in BigQuery
  - Includes
    - javascript files where you can define variables and functions to use in your project

<br>
*sqlx <br>
<image src="https://github.com/youngmin-jin/practice/assets/135728064/33556706-6807-456c-8cb6-e5fccd76fc6c" width="600">


<br><br>
## Workflow Execution Scheduling Options
- Workflow configurations in Dataform
- Workflows and Cloud Scheduler
- Cloud Composer


<br><br>
## Ref
- https://www.youtube.com/watch?v=285HnXL9_rk












