# Concepts

# Roles

# Cost Management
- Child account's (e.g., ACME) cost is managed by the main organization
<br/><br/><br/>

# Others
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




