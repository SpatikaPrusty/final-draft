from pyspark import SparkContext, SQLContext
import pyspark
from datetime import datetime, timedelta
import pytz

# Spark configuration
conf = pyspark.SparkConf().set("spark.jars.packages",
                               "org.mongodb.spark:mongo-spark-connector_2.12:3.0.1") \
                           .setMaster("local") \
                           .setAppName("MyApp") \
                           .setAll([("spark.driver.memory", "40g"), ("spark.executor.memory", "50g")])

# Entry point to PySpark
sc = SparkContext(conf=conf)
sqlC = SQLContext(sc)

# MongoDB Atlas credentials and cluster details
mongo_username = "spatikaprusty"
mongo_password = "xEiSjulggyRHE3MU"
mongo_cluster = "cluster0"
mongo_database = "Bootcamp"
mongo_collection = "users"  

# Construct MongoDB URI
mongo_ip = f"mongodb+srv://{mongo_username}:{mongo_password}@{mongo_cluster}.bprftog.mongodb.net/{mongo_database}.{mongo_collection}?retryWrites=true&w=majority"
print(mongo_ip)

# Load data from MongoDB with the specified collection name
users = sqlC.read.format("com.mongodb.spark.sql.DefaultSource").option("uri", mongo_ip).load()

# Create a temporary view
users.createOrReplaceTempView("users")

users=users.drop("_id")
users=users.drop("__v")
users=users.drop("updatedAt")

created_timestamp="2024-03-21 12:00:00"
updated_timestamp="2024-03-03 12:00:00"

# Query to select users whose createdAt timestamp is more recent than the provided timestamp
created_users = sqlC.sql(f"SELECT * FROM users WHERE createdAt < '{created_timestamp}'")
updated_users = sqlC.sql(f"SELECT * FROM users WHERE updatedAt > '{updated_timestamp}'")

# csv and parquet format
created_users.toPandas().to_csv('latest_c_output_file.csv', index=False)
created_users.toPandas().to_parquet('p_output_file.parquet', engine='pyarrow')

# Display the user details
print(f"User details created in last 24hrs : '{created_timestamp}'")
created_users.show()

print(f"User details Updated in last 24hrs : '{updated_timestamp}'")
updated_users.show()