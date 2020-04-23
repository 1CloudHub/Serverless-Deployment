import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame
from awsglue.job import Job

args = getResolvedOptions(sys.argv, [
    'JOB_NAME',
    'TempDir',
    'username',
    'password',
    'driver',
    'url',
    'database_name',
    'table_name',
    'bucket_name',
    'partition_Keys'
])

print('Args collected')
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
url = args['url']
table_name = args['table_name']
database_name = args['database_name']
driver = args['driver']
username = args['username']
password = args['password']
bucket_name = args['bucket_name']
partition_Keys = args['partition_Keys'].split(',')
db_table_name = database_name + str('.') + table_name

print('url is: ', url)
print('table_name is: ', table_name)
print('database_name is: ', database_name)
print('driver is: ', driver)
print('username is: ', username)
print('password is: ', password)
print('bucket_name is: ', bucket_name)
print('partition_Keys is: ', partition_Keys)


path = 's3://' + str(bucket_name) + "/" + str(database_name) + "/" + str(table_name)
print('Path is: ', path)

# Read Data from database using JDBC driver in to DataFrame
source_df = spark.read.format("jdbc").option("url", url).option("dbtable", db_table_name).option("driver",
                                                                                                 driver).option("user",
                                                                                                                username).option(
    "password", password).load()

job.init(args['JOB_NAME'], args)

# Convert DataFrames to AWS Glue's DynamicFrames Object
dynamic_dframe = DynamicFrame.fromDF(source_df, glueContext, "dynamic_df")

glueContext.write_dynamic_frame.from_options(
    frame=dynamic_dframe,
    connection_type="s3",
    connection_options={"path": path,
                        "partitionKeys": partition_Keys},
    format="parquet")
job.commit()