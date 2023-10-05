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
   - _Apache Airflow_
   - usually run periodically like hours, days, weeks..
   - when latest data is not needed/ accuracy is critical
   - data cleaning improves quality but increases latency
   - e.g., data backups, transaction history loading, long-range forecasting..
<br/>

2. Streaming
   - _Apache Kafka_
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
  - primarily a workflow manager/ defines and organizes machine learning pipeline dependencies
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
    
    *dashboard of Airflow<br/>
    ![image](https://github.com/youngmin-jin/exercise/assets/135728064/5c7dc5e2-afbb-48cb-aae7-fe9f42286d6f)<br/><br/>
    *tree view of DAG<br/>
    ![image](https://github.com/youngmin-jin/exercise/assets/135728064/ba174be2-3cc5-4bbd-9862-055098c0ab32)<br/><br/>
    *graph view of DAG<br/>
    ![image](https://github.com/youngmin-jin/exercise/assets/135728064/491d6bd5-f108-47ea-99e0-34971cc6e64b)<br/><br/>
        
  - Airflow scheduler
    - schedules and deployes your DAGs
    - deploys on worker array-> follows your DAG-> set the first DAG run-> subsequent run <br/><br/><br/>


# Apache Kafka
  - One of ESP solutions (Event Streaming Platform) <br/><br/>
    *ESP: manage event streaming from various event sources (e.g., sensors, devices..) to destinations 
    > ![image](https://github.com/youngmin-jin/practice/assets/135728064/479717fa-3769-4efa-8462-8e82f49128ac)
    > ![image](https://github.com/youngmin-jin/practice/assets/135728064/97acf642-6fed-447d-b5ab-a87f0a3f41bc) <br/>
    > e.g., Apache Kafka, Amazon Kinesis, Apache Storm.. <br/><br/>

  - distribution system-> able to handle high data throughput and concurrency in parallel/ scalable/ permanent persistency/ open source
  - originally used to track user activities (e.g., keyboard strokes, click, page view..) but now used for all kinds of metric-streaming (e.g., sensor reading, GPS, hardward or software monitoring, log..)
  - all events are ingested in Kafka, and become available for destinations (e.g., further data storage, online or offline databases, real-time analytics such as dashboard, ML..)

  - architecture
    > ![image](https://github.com/youngmin-jin/practice/assets/135728064/e1d2947f-db2c-4eb4-ab41-4aa98ffc727f) <br/><br/>
    > *core components
    > ![image](https://github.com/youngmin-jin/practice/assets/135728064/1618c721-e923-40ce-8880-2246bba8f282) <br/><br/>
    > *brokers are dedicated server to receive, store, process and distribute events/ synchronized and managed by another dedicated server called ZooKeeper <br/>
    > *different types of clients, such as Kafka CLI or API using Java, Python, are available <br/>

    - Kafka producer
      > ![image](https://github.com/youngmin-jin/practice/assets/135728064/f9d5fc0d-05a6-4383-ae63-f1fccd4500ab)<br/>
        - e.g., create kafka producers to publish e.g., log/ user-activities events to log/ user-activities topic partitions (optinally with associated events, like user id)
          > *kafka producer creation CLI <br/>
          > ![image](https://github.com/youngmin-jin/practice/assets/135728064/3b74c209-a824-4f75-b206-3ad5b4dfad38) <br/>

    - Kafka consumer
      > ![image](https://github.com/youngmin-jin/practice/assets/135728064/cf6bae5b-1aae-497a-a660-02dd6b53a81b) <br/>
      - e.g., make kafka consumers-> make them subscribe corresponding topics-> kafka push the events to the subscribed consumers-> consumers send to event destinations
        > *kafka consumer creation CLI <br/>
        > ![image](https://github.com/youngmin-jin/practice/assets/135728064/04f3789d-971b-4b1e-87ad-bf85f664df35) <br/>

  - example of streaming processing using kafka (with other data processors)
    > ![image](https://github.com/youngmin-jin/practice/assets/135728064/3fcc1097-9743-4b6b-aaf0-39cc5c7fa51e) <br/>
    1) request raw weather json data from a weather API
    2) start a weather producer to publish the raw data to a raw weather topic
    3) start a consumer to read the raw weather data from the weather topic
    4) create an ad hoc data processor to filter the raw weather data to only filter extreme events (e.g., extremely high or low temp) -> **Kafka Streams API** can replace
    5) the processor sends the processed data to another producer, and publishes to a processed weather topic
    6) the processed weather data is consumed by dedicated consumer and sent to a dashboard for visu <br/><br/>

    - Kafka Streams API
      - simple client library supporting users with data processing in event streaming pipelines
      - processes and analyzes data stored in kafka topics
      - example of streaming processing using kafka (with Kafka Streams API)
        > ![image](https://github.com/youngmin-jin/practice/assets/135728064/b6225172-7cfc-4250-b5a1-cec75f24d60f) <br/>
        > *iv. step can be replaced by kafka streams api






    
      

















