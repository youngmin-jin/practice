# ETL and ELT
- ETL
  - Extract: reading data from one or more sources including analog data/ e.g., OCR or ADC sampling for extracting analog data/ APIs, webscrapping, or data querying 
  - Transform: wrangling data to meet destination requirements/ e.g., data type, data structure (csv, json..), anonymizing, encrypting
      - schema-on-write: conventional ETL approach/ consistency, efficiency, limited versatility
      - schema-on-read: modern ELT approach/ versatility (obtain multiple views of the same source data using ad-hoc schemas)
  - Load: writing the data to its destination environment to explore, visualize, or transform again/ e.g., full loading, incremental loading, scheduled loading, on-demand loading, batch loading, streaming loading

- ELT: Extract, Load, Transform
  - loads the data in its raw format to platforms such as a data lake, allowing users to transform the data
  - suitable for the requirements of big data, cloud computing, streaming analytics, or integration of highly distributed data sources
  - used for cases where flexibility, speed, and scalability are important
  - big data-> cloud computing -> working with a replica of the source data, meaning no info loss
<br/>


# Data pipeline
- includes scheduling, triggering, monitoring (tracking latency, throughput, resource utilization..), maintenance, and optimization
- data flows through pipelines as a series of data packets
- latency and thoughput are kig design considerations for data pipelines/ therefore, parallelization and I/O buffers can help mitigate bottlenecks<br/>
  ![image](https://github.com/youngmin-jin/exercise/assets/135728064/0ab9e89e-34c5-40ac-b34c-7370dd4240e0)

<br/>

- types
1. Batch
   - Apache Airflow
   - usually run periodically like hours, days, weeks..
   - when latest data is not needed/ accuracy is critical
   - data cleaning improves quality but increases latency
   - e.g., data backups, transaction history loading, long-range forecasting..
<br/>

2. Streaming
   - Apache Kafka
   - ingest data packets in rapid succession/ for real-time results/ records processed as they happen/ event streams can be loaded to storage
   - e.g., watching streaming services, social media feeds, fraud detection..
<br/>

3. lambda architecture
   - combines batch and streaming data pipeline methods<br/>
     ![image](https://github.com/youngmin-jin/exercise/assets/135728064/0e18bf55-f5df-413a-8c59-0a1250f78d00)

   - historical data -> delivered in batches/ real-time data -> speed layer => these are integrated in the serving layer
   - when data window is needed but speed is critical/ accuracy and speed are both important
<br/>

- tools
  - open sources
    - pandas: usually works on a single machine with small data/ but can be used with spark by using API
      > import pyspark.pandas as ps<br/>
      *https://sparkbyexamples.com/pyspark/pandas-api-on-apache-spark-pyspark/
    - Apache Airflow
  - enterprise
    - AWS Glue: fully managed ETL service that simplifies data prep for analytics/ crawls your data sources and discovers data formats/ suggests schemas for storing the data/ create ETL jobs from the AWS console
    - Panoply: ELT-specific platform/ no-code integration/ SQL-based view
<br/>


# Apache Airflow 
  ![image](https://github.com/youngmin-jin/exercise/assets/135728064/844dab74-0015-430b-8336-2a4277ae7017)
  - primarily a workflow manager
  - allows users to programmatically author, schedule, and monitor big data workflow/ but not for streaming solution
  - makes data pipelines more maintanable, testable, and collaborative/ e.g., version management
  - architecture<br/>
    ![image](https://github.com/youngmin-jin/exercise/assets/135728064/f6863c58-90ce-421e-bc78-9999e3f8522d)<br/><br/>
  
  - DAG
    - represents workflows or pipelines/ define what tasks should run
    - nodes are tasks/ edges define the order in which the two tasks should run
    - configuration
      - tasks are written in pyhthon
      - tasks implement operators e.g., python, sql, or bash operator
      - sensor operators poll for a certain time or condition (e.g., check every 30s whether a file exists)/ other operators such as email or HTTP request can be used
      - library imports-> DAG arguments-> DAG definition-> task definitions-> task pipeline
        ![image](https://github.com/youngmin-jin/exercise/assets/135728064/a1983533-3ef7-4c8b-bcde-a31b6c9650cc) 
        ![image](https://github.com/youngmin-jin/exercise/assets/135728064/bd50bbf1-1e7f-4877-8d7b-bb8018a11781)<br/><br/>
    
    *dashboard of Airflow
    ![image](https://github.com/youngmin-jin/exercise/assets/135728064/5c7dc5e2-afbb-48cb-aae7-fe9f42286d6f)<br/><br/>
    *tree view of DAG
    ![image](https://github.com/youngmin-jin/exercise/assets/135728064/ba174be2-3cc5-4bbd-9862-055098c0ab32)<br/><br/>
    *graph view of DAG
    ![image](https://github.com/youngmin-jin/exercise/assets/135728064/491d6bd5-f108-47ea-99e0-34971cc6e64b)<br/><br/>
        
  - Airflow scheduler
    - schedules and deployes your DAGs
    - deploys on worker array-> follows your DAG-> set the first DAG run-> subsequent run 
      

















