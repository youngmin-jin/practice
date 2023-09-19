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
- latency and thoughput are kig design considerations for data pipelines/ therefore, parallelization and I/O buffers can help mitigate bottlenecks
  ![image](https://github.com/youngmin-jin/exercise/assets/135728064/0ab9e89e-34c5-40ac-b34c-7370dd4240e0)

<br/>

- types
1. Batch
   - Apache Airflow:
    ![image](https://github.com/youngmin-jin/exercise/assets/135728064/844dab74-0015-430b-8336-2a4277ae7017)
      - versatile 'configuration' as code data pipeline platform
      - allows users to programmatically author, schedule, and monitor big data workflow
      - represents your batch workflow as a directed acyclic graph (DAG) <br/>
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
   - combines batch and streaming data pipeline methods
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

















