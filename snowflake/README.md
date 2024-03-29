# Concepts

# Roles

# Cost Management
- Child account's (e.g., ACME) cost is managed by the main organization
<br/><br/><br/>

# Cases
<details>
  <summary>Data Sharing</summary>

# Data Sharing in Snowflake
## 1. Create a guest account, sign in to it, update the password, and create a new Warehouse
![image](https://github.com/youngmin-jin/practice/assets/135728064/8e807670-510c-43ae-8b3c-c91ea7e9b0a2)
![image](https://github.com/youngmin-jin/practice/assets/135728064/540ac660-7414-4817-89fc-f047dc781de4)
![image](https://github.com/youngmin-jin/practice/assets/135728064/8c7f1ce9-05e7-43a6-a400-11292f523e55)
![image](https://github.com/youngmin-jin/practice/assets/135728064/bebe6912-a398-4d51-ac59-129e1022c729)
![image](https://github.com/youngmin-jin/practice/assets/135728064/c5de03e2-6118-4def-9306-da95afeb9dbc)
<br/><br/><br/>

## 2. From the original account, do "Listing" to share data
![image](https://github.com/youngmin-jin/practice/assets/135728064/14a4e926-f3aa-47a7-a2a8-7dc1f7e888ec)
![image](https://github.com/youngmin-jin/practice/assets/135728064/866d55bb-a832-4be6-8979-03345665e21c)
![image](https://github.com/youngmin-jin/practice/assets/135728064/651088a3-25ac-45f3-98a6-1912cadda5fb)
![image](https://github.com/youngmin-jin/practice/assets/135728064/82e1bdd2-01f9-4da9-8e88-303e861706b7)
![image](https://github.com/youngmin-jin/practice/assets/135728064/0f74cd75-71ca-4b9f-9a8e-5a0814ae40f7)
<br/><br/><br/>

## 3. From the guest account, see the shared listing and download 
![image](https://github.com/youngmin-jin/practice/assets/135728064/1fa6abe5-7e78-4d6b-9a20-1fc5b6d30813) <br/><br/>

*from the original account, you can see a new DB with an add name.<br/>
![image](https://github.com/youngmin-jin/practice/assets/135728064/4a48827b-86f3-49cf-ba56-60a3660d8b81)
<br/><br/><br/>

## Option  
### - From the original account, add data dictionary to COUNTRY_CODE_TO_CURRENCY_CODE table
![image](https://github.com/youngmin-jin/practice/assets/135728064/0f8628b0-be04-4f0f-bf72-ebb9afd8696d)
![image](https://github.com/youngmin-jin/practice/assets/135728064/dbc451a6-ad2b-4af6-8edd-7f2dd8881331)
<br/><br/><br/>

### - From the original account, add sample queries
![image](https://github.com/youngmin-jin/practice/assets/135728064/93e21575-2f01-4832-8915-cbd0993001e3)
![image](https://github.com/youngmin-jin/practice/assets/135728064/b4d51f2f-5f9b-4ca7-9b4a-fc51f8937db7)
<br/><br/><br/>

### - From the guest account, see the change and "Get" it
![image](https://github.com/youngmin-jin/practice/assets/135728064/d3508cd5-4406-4a1c-a114-900cac3ff5f1)
<br/><br/><br/>

### - Not only data, but SQL functions are available to share
![image](https://github.com/youngmin-jin/practice/assets/135728064/0f1e7aad-5941-4bd6-b0ea-0e4be4c10e92)
<br/><br/>
*possible to share functions and necessary data without data exposure.

</details>



<details>
  <summary>Connecting External Storages</summary>
  
# Connecting External Storages
### Structured data
#### 1. Create a stage connecting an external storage (e.g., s3) in a schema
> ![image](https://github.com/youngmin-jin/practice/assets/135728064/c3b60801-fb92-4f92-b95b-bc61d1629fc3)

#### 2. View data using the stage
```
SELECT $1 FROM @DATABASE.SCHEMA.STAGE;
```

#### 3. Create a file format to load data
```
CREATE OR REPLACE FILE FORMAT ZENAS_ATHLEISURE_DB.PRODUCTS.zmd_file_format_2
  FIELD_DELIMITER = '|' 
  RECORD_DELIMITER = ';' 
  TRIM_SPACE = TRUE; 
```

#### 4. Create a view or table using the file format
```
CREATE OR REPLACE VIEW zenas_athleisure_db.products.SWEATBAND_PRODUCT_LINE AS
  SELECT REPLACE($1, chr(13)||chr(10)) AS PRODUCT_CODE
    , $2 AS HEADBAND_DESCRIPTION
    , $3 AS WRISTBAND_DESCRIPTION
  FROM @ZENAS_ATHLEISURE_DB.PRODUCTS.UNI_KLAUS_ZMD/swt_product_line.txt
  (file_format => ZENAS_ATHLEISURE_DB.PRODUCTS.zmd_file_format_2); 
```

#### Result
- Before <br/>
![image](https://github.com/youngmin-jin/practice/assets/135728064/29bda676-82a4-4857-b6ba-ee8eb4e010b0) <br/>

- After <br/>
![image](https://github.com/youngmin-jin/practice/assets/135728064/0bb6f84b-ef89-4420-910e-9674a59ed7a4)
<br/><br/>

### Unstructured data
#### 1. View metadata of unstructured data using "Directory"
```
SELECT *
FROM DIRECTORY(@DATABASE.SCHEMA.STAGE);
```

#### 2. Enable directory in the stage
```
ALTER STAGE ZENAS_ATHLEISURE_DB.PRODUCTS.UNI_KLAUS_CLOTHING
SET DIRECTORY = (ENABLE = TRUE); <br/><br/>

ALTER STAGE ZENAS_ATHLEISURE_DB.PRODUCTS.UNI_KLAUS_CLOTHING REFRESH;
```

#### Result
![image](https://github.com/youngmin-jin/practice/assets/135728064/d0398574-acfe-4c63-90fc-d9804725a79f)
<br/><br/>

</details>



<details>
  <summary>Geospatial Data</summary>
  
# Geospatial Data
- [Open Street Map (WKT Playground)](https://clydedacruz.github.io/openstreetmap-wkt-playground/)
- [Geojson.io](https://geojson.io/#map=2/0/20) (map using json)
- [Snowflake: Geospatial Functions](https://docs.snowflake.com/en/sql-reference/functions-geospatial)
<br/>

## Example
```
CREATE OR REPLACE VIEW DENVER_AREA_TRAILS AS
  SELECT $1:features[0]:properties:Name::STRING AS FEATURE_NAME
        , $1:features[0]:geometry:coordinates::STRING AS FEATURE_COORDINATES
        , $1:features[0]:geometry::STRING AS GEOMETRY
        , ST_LENGTH(TO_GEOGRAPHY(GEOMETRY)) AS TRAIL_LENGTH
        , $1:features[0]:properties::STRING AS FEATURE_PROPERTIES 
        , $1:crs:properties:name::STRING AS SPECS
        , $1 AS WHOLE_OBJECT 
  FROM @TRAILS_GEOJSON
  (FILE_FORMAT => FF_JSON);
```
  - ST_LENGTH() : to calculate the length of geospatial data <br/>
  - TO_GEOGRAPHY() : to convert STRING or ARRAY to geospatial data <br/>

</details>

<details>
  <summary>Handle Unstructured Data</summary>

# Handle Unstructured Data
## Use SQL to flatten unstructured data

## Table for unstructured data
### 1. Create a table using 'VARIANT' 
```
create or replace TABLE AGS_GAME_AUDIENCE.RAW.GAME_LOGS (
	RAW_LOG VARIANT
);
```

</details>



<details>
  <summary>Time-driven Data Pipeline (using TASK)</summary>
  
# Time-driven Data Pipeline (using TASK)
## Flow
![image](https://github.com/youngmin-jin/practice/assets/135728064/2d94bfe7-8bd7-474e-a193-549c7026c555)
<br/><br/>

## 1. Create GET_NEW_FILES (task) to get data from S3 to PIPELINE_LOGS (table)
```
CREATE OR REPLACE TABLE AGS_GAME_AUDIENCE.RAW.PIPELINE_LOGS (
    RAW_LOG VARIANT
);
```
```
CREATE OR REPLACE TASK AGS_GAME_AUDIENCE.RAW.GET_NEW_FILES
    WAREHOUSE = COMPUTE_WH
    SCHEDULE = '5 minute'
    AS  COPY INTO PIPELINE_LOGS
        FROM @uni_kishore_pipeline
        FILE_FORMAT = FF_JSON_LOGS;

-- execute the task
EXECUTE TASK AGS_GAME_AUDIENCE.RAW.GET_NEW_FILES;

-- suspend the task to avoid extra cost
ALTER TASK AGS_GAME_AUDIENCE.RAW.GET_NEW_FILES SUSPEND;
```

#### Result
```
SELECT *
FROM PIPELINE_LOGS;
```
![image](https://github.com/youngmin-jin/practice/assets/135728064/443f7074-730f-4d3d-9c23-e9db12a83b7d)
<br/><br/>


## 2. Create PL_LOGS (view) based on PIPELINE_LOGS (table)
```
CREATE OR REPLACE VIEW AGS_GAME_AUDIENCE.RAW.PL_LOGS AS 
    SELECT RAW_LOG:datetime_iso8601::TIMESTAMP_LTZ AS DATETIME_ISO8601
            , RAW_LOG:ip_address::TEXT AS IP_ADDRESS
            , RAW_LOG:user_event::TEXT AS USER_EVENT
            , RAW_LOG:user_login::TEXT AS USER_LOGIN
            , RAW_LOG
    FROM AGS_GAME_AUDIENCE.RAW.PIPELINE_LOGS;
```

#### Result
```
SELECT *
FROM PL_LOGS;
```
![image](https://github.com/youngmin-jin/practice/assets/135728064/30fc2271-d3da-4225-a316-99602cbe75f6)
<br/><br/>


## 3. Create LOGS_ENHANCED (table) and LOAD_LOGS_ENHANCED (task) to load the final data
```
CREATE OR REPLACE TABLE AGS_GAME_AUDIENCE.ENHANCED.LOGS_ENHANCED AS 
    SELECT LOGS.IP_ADDRESS 
        , LOGS.USER_LOGIN AS GAMER_NAME
        , LOGS.USER_EVENT AS GAME_EVENT_NAME
        , LOGS.DATETIME_ISO8601 AS GAME_EVENT_UTC
        , CITY
        , REGION
        , COUNTRY
        , TIMEZONE AS GAMER_LTZ_NAME
        , CONVERT_TIMEZONE('UTC', TIMEZONE, LOGS.DATETIME_ISO8601) AS GAME_EVENT_LTZ
        , DAYNAME(TO_DATE(GAME_EVENT_LTZ)) AS DOW_NAME
        , TOD_NAME
    FROM AGS_GAME_AUDIENCE.RAW.PL_LOGS LOGS
        JOIN IPINFO_GEOLOC.DEMO.LOCATION LOC 
        ON IPINFO_GEOLOC.PUBLIC.TO_JOIN_KEY(LOGS.IP_ADDRESS) = LOC.JOIN_KEY
            AND IPINFO_GEOLOC.PUBLIC.TO_INT(LOGS.IP_ADDRESS) 
            BETWEEN START_IP_INT AND END_IP_INT
        JOIN AGS_GAME_AUDIENCE.RAW.TIME_OF_DAY_LU AS TIME
        ON HOUR(GAME_EVENT_LTZ) = TIME.HOUR;
```
*IPINFO_GEOLOC.DEMO.LOCATION (table) <br/>
![image](https://github.com/youngmin-jin/practice/assets/135728064/3593cc0c-0b7a-4e51-877e-a32095615388)
<br/><br/>

*IPINFO_GEOLOC.PUBLIC.TO_JOIN_KEY (function) <br/>
-> convert ip address to ip4v
<br/><br/>

*IPINFO_GEOLOC.PUBLIC.TO_INT (function) <br/>
-> convert text to int
<br/><br/>

*AGS_GAME_AUDIENCE.RAW.TIME_OF_DAY_LU (table) <br/>
![image](https://github.com/youngmin-jin/practice/assets/135728064/df96e995-3bb2-4f8b-ac13-6c6f7960fad2)

#### Result
```
SELECT *
FROM AGS_GAME_AUDIENCE.ENHANCED.LOGS_ENHANCED;
```
![image](https://github.com/youngmin-jin/practice/assets/135728064/b9665290-f4fc-47c1-bb2a-c1f4a457b0f8)
<br/><br/>

```
CREATE OR REPLACE TASK AGS_GAME_AUDIENCE.RAW.LOAD_LOGS_ENHANCED
	WRAEHOUSE=COMPUTE_WH
	SCHEDULE='5 minute'
	AS MERGE INTO AGS_GAME_AUDIENCE.ENHANCED.LOGS_ENHANCED E
        USING (SELECT LOGS.IP_ADDRESS  
                    , LOGS.USER_LOGIN AS GAMER_NAME
                    , LOGS.USER_EVENT AS GAME_EVENT_NAME
                    , LOGS.DATETIME_ISO8601 AS GAME_EVENT_UTC
                    , CITY 
                    , REGION
                    , COUNTRY
                    , TIMEZONE AS GAMER_LTZ_NAME
                    , CONVERT_TIMEZONE('UTC', TIMEZONE, LOGS.DATETIME_ISO8601) AS GAME_EVENT_LTZ
                    , DAYNAME(GAME_EVENT_LTZ) AS DOW_NAME
                    , TOD_NAME
                FROM AGS_GAME_AUDIENCE.RAW.PL_LOGS LOGS
                    JOIN IPINFO_GEOLOC.DEMO.LOCATION LOC 
                    ON IPINFO_GEOLOC.PUBLIC.TO_JOIN_KEY(LOGS.IP_ADDRESS) = LOC.JOIN_KEY
                        AND IPINFO_GEOLOC.PUBLIC.TO_INT(LOGS.IP_ADDRESS) 
                        BETWEEN START_IP_INT AND END_IP_INT
                    JOIN AGS_GAME_AUDIENCE.RAW.TIME_OF_DAY_LU TOD
                    ON HOUR(GAME_EVENT_LTZ) = TOD.HOUR
                ) R
            ON E.GAMER_NAME = R.GAMER_NAME
            AND E.GAME_EVENT_UTC = R.GAME_EVENT_UTC
            AND E.GAME_EVENT_NAME = R.GAME_EVENT_NAME
        WHEN NOT MATCHED THEN
        INSERT (IP_ADDRESS
                , GAMER_NAME
                , GAME_EVENT_NAME
                , GAME_EVENT_UTC
                , CITY
                , REGION
                , COUNTRY
                , GAMER_LTZ_NAME
                , GAME_EVENT_LTZ
                , DOW_NAME
                , TOD_NAME
        ) VALUES (IP_ADDRESS
                , GAMER_NAME
                , GAME_EVENT_NAME
                , GAME_EVENT_UTC
                , CITY
                , REGION
                , COUNTRY
                , GAMER_LTZ_NAME
                , GAME_EVENT_LTZ
                , DOW_NAME
                , TOD_NAME
        );

-- execute the task
EXECUTE TASK AGS_GAME_AUDIENCE.RAW.LOAD_LOGS_ENHANCED;

-- suspend the task to avoid extra cost
ALTER TASK AGS_GAME_AUDIENCE.RAW.LOAD_LOGS_ENHANCED SUSPEND;
```

#### Result
```
SELECT *
FROM AGS_GAME_AUDIENCE.ENHANCED.LOGS_ENHANCED;
```
![image](https://github.com/youngmin-jin/practice/assets/135728064/e19be5a4-36be-460d-8186-a0395c729215)
<br/><br/>
-> updated upon 5 minutes
<br/><br/>

</details>



<details>
  <summary>Event-driven Data Pipeline (using PIPE, STREAM, pub/sub)</summary>
  
# Event-driven Data Pipeline (using PIPE, STREAM, pub/sub)
## Flow
![image](https://github.com/youngmin-jin/practice/assets/135728064/debdefd5-910b-4bba-a330-00826713132b)
<br/><br/>
*S3 already has a topic/ PIPE_GET_NEW_FILES subscripes
<br/><br/>

## 1. Create PIPE_GET_NEW_FILES (pipe) to get data from S3 to ED_PIPELINE_LOGS (table)
```
CREATE OR REPLACE PIPE PIPE_GET_NEW_FILES
    AUTO_INGEST=TRUE
    AWS_SNS_TOPIC='arn:aws:sns:us-west-2:321463406630:dngw_topic' AS 
COPY INTO ED_PIPELINE_LOGS
FROM (
    SELECT METADATA$FILENAME AS LOG_FILE_NAME 
          , METADATA$FILE_ROW_NUMBER AS LOG_FILE_ROW_ID 
          , CURRENT_TIMESTAMP(0) AS LOAD_LTZ 
          , GET($1,'datetime_iso8601')::TIMESTAMP_NTZ AS DATETIME_ISO8601
          , GET($1,'user_event')::TEXT AS USER_EVENT
          , GET($1,'user_login')::TEXT AS USER_LOGIN
          , GET($1,'ip_address')::TEXT AS IP_ADDRESS    
    FROM @AGS_GAME_AUDIENCE.RAW.UNI_KISHORE_PIPELINE
)
FILE_FORMAT = (FORMAT_NAME = FF_JSON_LOGS);
```

#### Result
```
SELECT *
FROM ED_PIPELINE_LOGS;
```
![image](https://github.com/youngmin-jin/practice/assets/135728064/1e12774e-d504-49a8-82b3-8ed0ef8c2992)
<br/><br/>


## 2. Create LOAD_LOGS_ENHANCED (task) to load the final data to LOGS_ENHANCED (table) based on ED_PIPELINE_LOGS (table)
```
CREATE OR REPLACE TASK AGS_GAME_AUDIENCE.RAW.LOAD_LOGS_ENHANCED
	WAREHOUSE=COMPUTE_WH
	SCHEDULE='5 minute'
	AS MERGE INTO AGS_GAME_AUDIENCE.ENHANCED.LOGS_ENHANCED E
        USING (SELECT LOGS.IP_ADDRESS 
                    , LOGS.USER_LOGIN AS GAMER_NAME
                    , LOGS.USER_EVENT AS GAME_EVENT_NAME
                    , LOGS.DATETIME_ISO8601 AS GAME_EVENT_UTC
                    , CITY
                    , REGION
                    , COUNTRY
                    , TIMEZONE AS GAMER_LTZ_NAME
                    , CONVERT_TIMEZONE('UTC', TIMEZONE, LOGS.DATETIME_ISO8601) AS GAME_EVENT_LTZ
                    , DAYNAME(GAME_EVENT_LTZ) AS DOW_NAME
                    , TOD_NAME
                FROM AGS_GAME_AUDIENCE.RAW.ED_PIPELINE_LOGS LOGS
                    JOIN IPINFO_GEOLOC.DEMO.LOCATION LOC 
                    ON IPINFO_GEOLOC.PUBLIC.TO_JOIN_KEY(LOGS.IP_ADDRESS) = LOC.JOIN_KEY
                        AND IPINFO_GEOLOC.PUBLIC.TO_INT(LOGS.IP_ADDRESS) 
                        BETWEEN START_IP_INT AND END_IP_INT
                    JOIN AGS_GAME_AUDIENCE.RAW.TIME_OF_DAY_LU TOD
                    ON HOUR(GAME_EVENT_LTZ) = TOD.HOUR
                ) R
            ON E.GAMER_NAME = R.GAMER_NAME
            AND E.GAME_EVENT_UTC = R.GAME_EVENT_UTC
            AND E.GAME_EVENT_NAME = R.GAME_EVENT_NAME
        WHEN NOT MATCHED THEN
        INSERT (IP_ADDRESS
                , GAMER_NAME
                , GAME_EVENT_NAME
                , GAME_EVENT_UTC
                , CITY
                , REGION
                , COUNTRY
                , GAMER_LTZ_NAME
                , GAME_EVENT_LTZ
                , DOW_NAME
                , TOD_NAME
        ) VALUES (IP_ADDRESS
                , GAMER_NAME
                , GAME_EVENT_NAME
                , GAME_EVENT_UTC
                , CITY
                , REGION
                , COUNTRY
                , GAMER_LTZ_NAME
                , GAME_EVENT_LTZ
                , DOW_NAME
                , TOD_NAME
        );

-- EXECUTE THE TASK
EXECUTE TASK AGS_GAME_AUDIENCE.RAW.LOAD_LOGS_ENHANCED;

-- SUSPEND THE TASK
ALTER TASK AGS_GAME_AUDIENCE.RAW.LOAD_LOGS_ENHANCED SUSPEND;
```

#### Result
```
SELECT *
FROM AGS_GAME_AUDIENCE.ENHANCED.LOGS_ENHANCED;
```
![image](https://github.com/youngmin-jin/practice/assets/135728064/d14ae7be-00eb-4808-8be9-e5f2f190e693)
<br/><br/>
*it is **both time-driven** and **event-drive** (updated every 5 minutes and every time new file added) <br/>
-> time-driven: by 5 minutes schedule <br/>
-> event-driven: by subscription of the topic
<br/><br/>
</details>







