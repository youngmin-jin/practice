# Concepts
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
  
- Data pipelines 
  - Batch
    - Apache Airflow: represents your batch workflow as a directed acyclic graph (DAG)
      ![image](https://github.com/youngmin-jin/exercise/assets/135728064/844dab74-0015-430b-8336-2a4277ae7017)

  - Streaming
    - Apache Kafka

# ETL shell script using cron
- touch file.sh : create a shell script file
- gedit file.sh : open the file
- chmod +x file.sh : set permissions to make the shell script executable
- crontab -e : open crontab editor
- 1****path/file.sh : enter schedule
