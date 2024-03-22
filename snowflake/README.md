# Concepts

# Roles

# Cost Management
- Child account's (e.g., ACME) cost is managed by the main organization

# Get data from an external storage
### Structured data
#### 1. Create a stage connecting an external storage (e.g., s3) in a schema
> ![image](https://github.com/youngmin-jin/practice/assets/135728064/c3b60801-fb92-4f92-b95b-bc61d1629fc3)

#### 2. View data using the stage
> SELECT $1 FROM @DATABASE.SCHEMA.STAGE;

#### 3. Create a file format to load data
> CREATE OR REPLACE FILE FORMAT ZENAS_ATHLEISURE_DB.PRODUCTS.zmd_file_format_2 <br/>
> &nbsp;&nbsp;&nbsp;FIELD_DELIMITER = '|' <br/>
> &nbsp;&nbsp;&nbsp;RECORD_DELIMITER = ';' <br/>
> &nbsp;&nbsp;&nbsp;TRIM_SPACE = TRUE; <br/>

#### 4. Create a view or table using the file format
> CREATE OR REPLACE VIEW zenas_athleisure_db.products.SWEATBAND_PRODUCT_LINE AS <br/>
> &nbsp;&nbsp;SELECT REPLACE($1, chr(13)||chr(10)) AS PRODUCT_CODE <br/>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;, $2 AS HEADBAND_DESCRIPTION <br/>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;, $3 AS WRISTBAND_DESCRIPTION <br/>
> &nbsp;&nbsp;FROM @ZENAS_ATHLEISURE_DB.PRODUCTS.UNI_KLAUS_ZMD/swt_product_line.txt <br/>
> &nbsp;&nbsp;(file_format => ZENAS_ATHLEISURE_DB.PRODUCTS.zmd_file_format_2); 

#### Result
- Before <br/>
![image](https://github.com/youngmin-jin/practice/assets/135728064/29bda676-82a4-4857-b6ba-ee8eb4e010b0) <br/>

- After <br/>
![image](https://github.com/youngmin-jin/practice/assets/135728064/0bb6f84b-ef89-4420-910e-9674a59ed7a4)
<br/><br/>

### Unstructured data
#### 1. View metadata of unstructured data using "Directory"
> SELECT * <br/>
> FROM DIRECTORY(@DATABASE.SCHEMA.STAGE);

#### 2. Enable directory in the stage
> ALTER STAGE ZENAS_ATHLEISURE_DB.PRODUCTS.UNI_KLAUS_CLOTHING <br/>
> SET DIRECTORY = (ENABLE = TRUE); <br/>
> <br/>
> ALTER STAGE ZENAS_ATHLEISURE_DB.PRODUCTS.UNI_KLAUS_CLOTHING REFRESH;<br/>

#### Result
![image](https://github.com/youngmin-jin/practice/assets/135728064/d0398574-acfe-4c63-90fc-d9804725a79f)
<br/><br/>


# Geospatial Functions
- [Open Street Map (WKT Playground)](https://clydedacruz.github.io/openstreetmap-wkt-playground/)
- [Geojson.io](https://geojson.io/#map=2/0/20) (map using json)
- [Snowflake: Geospatial Functions](https://docs.snowflake.com/en/sql-reference/functions-geospatial)
<br/><br/>

## Example
> CREATE OR REPLACE VIEW DENVER_AREA_TRAILS AS <br/>
> &nbsp;&nbsp;SELECT $1:features[0]:properties:Name::STRING AS FEATURE_NAME <br/>
> &nbsp;&nbsp;&nbsp;&nbsp;, $1:features[0]:geometry:coordinates::STRING AS FEATURE_COORDINATES <br/>
> &nbsp;&nbsp;&nbsp;&nbsp;, $1:features[0]:geometry::STRING AS GEOMETRY <br/>
> &nbsp;&nbsp;&nbsp;&nbsp;, ST_LENGTH(TO_GEOGRAPHY(GEOMETRY)) AS TRAIL_LENGTH <br/>
> &nbsp;&nbsp;&nbsp;&nbsp;, $1:features[0]:properties::STRING AS FEATURE_PROPERTIES <br/>
> &nbsp;&nbsp;&nbsp;&nbsp;, $1:crs:properties:name::STRING AS SPECS <br/>
> &nbsp;&nbsp;&nbsp;&nbsp;, $1 AS WHOLE_OBJECT <br/>
> &nbsp;&nbsp;FROM @TRAILS_GEOJSON <br/>
> &nbsp;&nbsp;(FILE_FORMAT => FF_JSON);
<br/><br/>
  - ST_LENGTH() : to calculate the length of geospatial data <br/>
  - TO_GEOGRAPHY() : to convert STRING or ARRAY to geospatial data <br/>






