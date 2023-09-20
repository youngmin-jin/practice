*on cmd<br/>

# Connect to Airflow and list existing DAGs and tasks
- start Apache Airflow<br/>
  > ![image](https://github.com/youngmin-jin/exercise/assets/135728064/dec25b00-a1d3-484d-b845-40ef8e49c60b)<br/>
  
  can access to the Airflow UI by the url

- list all DAGs
  > airflow dags list

- list all tasks in a DAG
  > airflow tasks list DAGnamehere

- unpause/ pause a DAG
  > airflow dags unpause DAGnamehere<br/>
  > airflow dags pause DAGnamehere<br/>
<br/>


# Building a DAG example
**download log file, extract, transform, and compress as a zip file**
  - connect to Airflow<br/>
    > start_airflow

  - create a DAG py file (ETL_Server_Access_Log_Processing.py ) 
    ```
    # import libraries
    from datetime import timedelta
    from airflow import DAG
    from airflow.operators.bash_operator import BashOperator
    from airflow.utils.dates import days_ago
    
    # DAG arguments
    default_args = {
        'owner':'Jin'
        , 'start_date':days_ago(0)
        , 'email':['youngmin7854@gmail.com']
        , 'email_on_failure':False
        , 'email_on_retry':False
        , 'retries':1
        , 'retry_delay':timedelta(minutes=5)
    }
    
    # DAG
    dag = DAG(
        'ETL_Server_Access_Log_Processing'
        , default_args=default_args
        , description='ETL_Server_Access_Log_Processing'
        , schedule_interval=timedelta(days=1)
    )
    
    # tasks
    download = BashOperator(
        task_id='download'
        , bash_command='wget -o web-server-access-log.txt "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Build%20a%20DAG%20using%20Airflow/web-server-access-log.txt"'
        , dag=dag
    )
    extract = BashOperator(
        task_id='extract'
        , bash_command='cut -d"#" -f1,4 web-server-access-log.txt > /home/project/airflow/dags/extracted_data.txt'
        , dag=dag
    )
    transform = BashOperator(
        task_id='transform'
        , bash_command='tr "[a-z]" "[A-Z]" < /home/project/airflow/dags/extracted_data.txt > /home/project/airflow/dags/transformed_data.txt'  # capitalize letter
        , dag=dag
    )
    load = BashOperator(
        task_id='load'
        , bash_command='zip log.zip transformed_data.txt'
        , dag=dag
    )
    
    # task pipeline
    download >> extract >> transform >> load
    ```

  - submit a DAG<br/>
    > cp ETL_Server_Access_Log_Processing.py $AIRFLOW_HOME/dags<br/>
   
  - verify dags list and tasks list<br/>
    > airflow dags list<br/>
    > airflow dags list|grep "ETL_Server_Access_Log_Processing"<br/>
    > airflow tasks list ETL_Server_Access_Log_Processing<br/>

  - in the Airflow UI<br/>
    ![image](https://github.com/youngmin-jin/exercise/assets/135728064/4139c3ac-d680-40d8-b792-4fe5f67a1f3c)





