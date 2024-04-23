# Basics
## BigQuery 
- partitioning
  - divide a large table into smaller partitions
  - improve query performance and control costs by reducing the number of bytes read by a query <br><br>
    <img src="https://github.com/youngmin-jin/practice/assets/135728064/0bbe09fb-449a-401f-bca7-c830140230b2" width="500"><br><br>
    <img src="https://github.com/youngmin-jin/practice/assets/135728064/149a6853-6973-4fe1-8eff-830bb9b9dc7f" width="500"><br><br>

<img src="https://github.com/youngmin-jin/practice/assets/135728064/8172cd61-17bb-410e-90d4-3c40092f3cad" width="500"><br><br>
<img src="https://github.com/youngmin-jin/practice/assets/135728064/38d593c5-1ddc-4b88-a6ed-8fb06419919b" width="500"><br><br>
<img src="https://github.com/youngmin-jin/practice/assets/135728064/b35f6954-30b2-4629-b859-22f27bd6f621" width="500"><br><br>
<img src="https://github.com/youngmin-jin/practice/assets/135728064/b51150b1-f679-43a5-80e4-8f574a1c559b" width="500"><br><br>


<br><br>
## Cloud Spanner
- globally distributed relational database with strong consistency and scalability features
- good option when you plan to use large amounts of data (more than 10TB) <br><br>
<img src="https://github.com/youngmin-jin/practice/assets/135728064/f1e84a87-123f-4128-a639-daacdb7a4791" width="500"><br><br>
<img src="https://github.com/youngmin-jin/practice/assets/135728064/1c114062-f8c2-4c7f-a0dd-b62f57981dbd" width="500"><br><br>
<img src="https://github.com/youngmin-jin/practice/assets/135728064/3221437f-8ef0-467e-bc9b-4e4a38d51dd1" width="500"><br><br>


<br><br>
## Cloud SQL
- Cloud SQL is a good option when you need relational database capabilities but don’t need storage capacity over 10TB or more than 4000 concurrent connections. You also need to be skilled at on-premise management.
<img src="https://github.com/youngmin-jin/practice/assets/135728064/000f08b4-fc1c-4124-8f39-eb5d4b9d46f5" width="500"><br><br>
<img src="https://github.com/youngmin-jin/practice/assets/135728064/7000c6b9-1a69-4949-b142-f8bcafa3f67c" width="500"><br><br>
<img src="https://github.com/youngmin-jin/practice/assets/135728064/64eff376-6c11-45f4-aa12-84ccb01701e6" width="500"><br><br>


<br><br>
## Bigtable
<img src="https://github.com/youngmin-jin/practice/assets/135728064/8cab1c68-9066-4db2-8200-3dcbf8acf8bc" width="500"><br><br>
<img src="https://github.com/youngmin-jin/practice/assets/135728064/6dce4760-1fcf-429d-8a0d-d1a40a6e9b95" width="500"><br><br>


<br><br>
## Dataproc
<img src="https://github.com/youngmin-jin/practice/assets/135728064/51d887ea-f708-47ed-b940-dcc75b85498c" width="500"><br><br>
<img src="https://github.com/youngmin-jin/practice/assets/135728064/9241b437-1b47-4436-a01d-62520d6250ac" width="500"><br><br>
<img src="https://github.com/youngmin-jin/practice/assets/135728064/4e043732-1341-4d5a-860c-0da3b8d3956e" width="500"><br><br>


<br><br>
## Dataflow
<img src="https://github.com/youngmin-jin/practice/assets/135728064/a731f49a-9ddf-4606-ba51-7828b98d438c" width="500"><br><br>
<img src="https://github.com/youngmin-jin/practice/assets/135728064/1cb2af8e-018c-4165-98dd-be8b5391d704" width="500"><br><br>


<br><br>
## Pub/sub
- snapshot
  - durable record of the acknowledgement state of a subscription at a specific point in time
  - captures info on whether msg published to a topic have been successfully processed by the subscriber
  - crucial for recovery
    ```
    {
      "name": string,
      "topic": string,
      "expireTime": string,
      "labels": {
        string: string,
        ...
      }
    }
    ```
  <img src="https://github.com/youngmin-jin/practice/assets/135728064/4213c85f-0fcf-4685-919f-d81d105e4d37" width="500"><br><br>
<img src="https://github.com/youngmin-jin/practice/assets/135728064/a80949ac-2059-4c7b-9293-31afc02cb759" width="500"><br><br>

<br><br>
## Transfer Appliance & Transfer Service
<img src="https://github.com/youngmin-jin/practice/assets/135728064/239dac5e-4129-4685-a1cc-3ef2c8bf8b98" width="500"><br><br>
<img src="https://github.com/youngmin-jin/practice/assets/135728064/f769c057-16a4-4b3a-aa17-c37bc9a06d8f" width="500"><br><br>
<img src="https://github.com/youngmin-jin/practice/assets/135728064/12b3d78c-9bc5-4036-b613-5324b74bf2b9" width="500"><br><br>

## Cloud Logging 
<img src="https://github.com/youngmin-jin/practice/assets/135728064/359fb71c-af2d-48d8-836b-e4e141f8ccac" width="500"><br><br>

## Encryption
<img src="https://github.com/youngmin-jin/practice/assets/135728064/bba30855-5d73-4cbe-a56f-76c823529411" width="500"><br><br>
  
## Stackdriver (Cloud Monitoring)
<img src="https://github.com/youngmin-jin/practice/assets/135728064/602365db-9bd6-4297-96ce-75c16b5a83f2" width="500"><br><br>

## Personally Identifiable information (PII)/ Cloud Data loss Prevention (DLP)
<img src="https://github.com/youngmin-jin/practice/assets/135728064/74fbbf4a-d1aa-4829-b240-069f911bee42" width="500"><br><br>
<img src="https://github.com/youngmin-jin/practice/assets/135728064/035af368-f9cd-49a8-88ab-d632762462e5" width="500"><br><br>

## Dialogflow/ Speech-to-Text API 
<img src="https://github.com/youngmin-jin/practice/assets/135728064/e76ce049-7f23-43af-9b2d-ab74a82d7437" width="500"><br><br>
<img src="https://github.com/youngmin-jin/practice/assets/135728064/466dbb8d-821a-47de-bd26-c06b9dab75fd" width="500"><br>

## Others
<br><br>
<img src="https://github.com/youngmin-jin/practice/assets/135728064/34486a99-635b-48ce-86f8-f52c0308936c" width="500"> <br>
<img src="https://github.com/youngmin-jin/practice/assets/135728064/7f89e722-42fd-40f0-bbc3-fbe769b2ba2c" width="500"> <br>
<img src="https://github.com/youngmin-jin/practice/assets/135728064/6e7b913e-0090-4f2e-85ca-896b8acc5ed7" width="500"> <br>
<img src="https://github.com/youngmin-jin/practice/assets/135728064/fcd20aef-ca21-42fb-a2c6-e5e2b686b44a" width="500"> <br>
<img src="https://github.com/youngmin-jin/practice/assets/135728064/14a5c45d-1be3-4a20-be43-c2d475ea1c44" width="500"> <br>
<img src="https://github.com/youngmin-jin/practice/assets/135728064/e1cdda05-a2b7-4b72-8c6c-5033d13f0c5c" width="500"> <br>
<img src="https://github.com/youngmin-jin/practice/assets/135728064/86b9489a-3363-44fc-8c16-c7b7dcf0978e" width="500"> <br>
 

<br><br>
# Concept
<img src="https://github.com/youngmin-jin/practice/assets/135728064/beb6aeab-db6c-4e16-ac54-d05cda1917f5" width="500"> <br><br>
<img src="https://github.com/youngmin-jin/practice/assets/135728064/0232645c-df12-47eb-ba84-af25d2bfe6f3" width="600"> <br><br>
<img src="https://github.com/youngmin-jin/practice/assets/135728064/0848ecbc-0827-44e4-8dde-e7e915ee74ee" width="600"> <br>
*Cloud Bigtable requires minimum 1tb data to be stored <br><br>

<img src="https://github.com/youngmin-jin/practice/assets/135728064/c082214f-4ec0-49fb-a0c9-6f8e730cd2cb" width="600"> <br>
*Cloud Dataflow and Dataprep are fully managed by google/ Dataproc might need to be managed by you <br><br>

<img src="https://github.com/youngmin-jin/practice/assets/135728064/0cb06b75-3eac-4cb0-af08-209a0dba4ba5" width="600"> <br>
<img src="https://github.com/youngmin-jin/practice/assets/135728064/21ad3c0b-a4e9-4820-9c19-aa209108b058" width="600"> <br>
<img src="https://github.com/youngmin-jin/practice/assets/135728064/a0e5c826-4570-464b-b3b3-ed077d5759bf" width="600"> <br>











