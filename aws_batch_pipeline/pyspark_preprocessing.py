# libraries
from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame
from pyspark.context import SparkContext
import pyspark.sql.functions as f

# create a GlueContext
sc = SparkContext()
glueContext = GlueContext(sc)

# read data from db
datasource = glueContext.create_dynamic_frame.from_catalog(
    database="nyc-db"
    , table_name="2014raw"
)

# convert to PySpark df
df = datasource.toDF()

# transform the data
# column name change
transformed_df = df.select(
    f.col("BOROUGH NAME").alias("BOROUGH_NAME")
    , f.col("BOROUGH")
    , f.rtrim(f.col("NEIGHBORHOOD")).alias("NEIGHBORHOOD")
    , f.rtrim(f.col("BUILDING CLASS CATEGORY")).alias("BUILDING_CLASS_CATEGORY")
    , f.col("TAX CLASS AT PRESENT").alias("TAX_CLASS_AT_PRESENT")
    , f.col("BLOCK")
    , f.col("LOT")
    , f.col("EASE-MENT")
    , f.col("BUILDING CLASS AT PRESENT").alias("BUILDING_CLASS_AT_PRESENT")
    # , f.trim(f.col("ADDRESS"))
    , f.trim(f.col("APARTMENT NUMBER")).alias("APARTMENT_NUMBER")
    , f.col("ZIP CODE").alias("ZIP_CODE")
    # , f.col("RESIDENTIAL UNITS").alias("RESIDENTIAL_UNITS")
    # , f.col("COMMERCIAL UNITS").alias("COMMERCIAL_UNITS")
    # , f.col("TOTAL UNITS").alias("TOTAL_UNITS")
    , f.col("LAND SQUARE FEET").alias("LAND_SQUARE_FEET")
    , f.col("GROSS SQUARE FEET").alias("GROSS_SQUARE_FEET")
    , f.col("YEAR BUILT").alias("YEAR_BUILT")
    , f.trim(f.col("TAX CLASS AT TIME OF SALE")).alias('TAX_CLASS_AT_TIME_OF_SALE')
    , f.trim(f.col("BUILDING CLASS AT TIME OF SALE")).alias('BUILDING_CLASS_AT_TIME_OF_SALE')
    , f.col("SALE PRICE").alias("SALE_PRICE")
    , f.col("SALE DATE").alias("SALE_DATE")
)

# value and value type change
transformed_df = transformed_df.withColumn("NEIGHBORHOOD", f.regexp_replace(f.col("NEIGHBORHOOD"), r"\"", ""))\
                    .withColumn("BUILDING_CLASS_CATEGORY", f.regexp_replace(f.col("BUILDING_CLASS_CATEGORY"), r"\"", ""))\
                    .withColumn("EASE-MENT", f.regexp_replace(f.col("EASE-MENT"), r"\"", ""))\
                    .withColumn("LAND_SQUARE_FEET", f.regexp_extract(f.col("LAND_SQUARE_FEET"), r"[-+]?\d+(,\d{3})*", 0))\
                    .withColumn("LAND_SQUARE_FEET", f.regexp_replace("LAND_SQUARE_FEET", ",", ""))\
                    .withColumn("LAND_SQUARE_FEET", f.col("LAND_SQUARE_FEET").cast("int"))\
                    .withColumn("GROSS_SQUARE_FEET", f.regexp_extract(f.col("GROSS_SQUARE_FEET"), r"[-+]?\d+(,\d{3})*", 0))\
                    .withColumn("GROSS_SQUARE_FEET", f.regexp_replace("GROSS_SQUARE_FEET", ",", ""))\
                    .withColumn("GROSS_SQUARE_FEET", f.col("GROSS_SQUARE_FEET").cast("int"))\
                    .withColumn("SALE_PRICE", f.regexp_extract(f.col("SALE_PRICE"), r"[-+]?\d+(,\d{3})*", 0))\
                    .withColumn("SALE_PRICE", f.regexp_replace("SALE_PRICE", ",", ""))\
                    .withColumn("SALE_PRICE", f.col("SALE_PRICE").cast("int"))

# convert to dynamic frame
transformed_df_dy = DynamicFrame.fromDF(transformed_df, glueContext, "transformed_df")

# write the transformed data to the target data store
glueContext.write_dynamic_frame.from_options(
    frame=transformed_df_dy
    , connection_type="s3"
    , connection_options={"path":"s3://5254-test-0214/transformed/"}
    , format="csv"
)
