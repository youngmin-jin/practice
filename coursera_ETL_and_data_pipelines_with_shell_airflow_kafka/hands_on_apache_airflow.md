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
  - connect to Airflow<br/>
    > start_airflow

  - create a DAG py file (my_first_dag.py) 
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
        'my-first-dag'
        , default_args=default_args
        , description='My first DAG'
        , schedule_interval=timedelta(days=1)
    )
    
    # tasks
    extract = BashOperator(
        task_id='extract'
        , bash_command='cud -d":" -f1,3,6 /etc/passwd > /home/project/airflow/dags/extracted-data.txt'
        , dag=dag
    )
    transform_and_load = BashOperator(
        task_id='transform'
        , bash_command='tr ":" "," < /home/project/airflow/dags/extracted_data.txt > /home/project/airflow/dags/transformed_data.csv'
        , dag=dag
    )
    
    # task pipeline
    extract >> transform_and_load
    ```

  - submit a DAG<br/>
    > cp my_first_dag.py $AIRFLOW_HOME/dags<br/>
   
  - verify dags list and tasks list<br/>
    > airflow dags list<br/>
    > airflow dags list|grep "my-first-dag"<br/>
    > airflow tasks list my-first-dag<br/>

  - results<br/>
    ![image](https://github.com/youngmin-jin/exercise/assets/135728064/7fc6c4b3-4c60-4699-8a6a-71d2471efaba)




