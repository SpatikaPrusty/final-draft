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
mongo_users_ip = f"mongodb+srv://{mongo_username}:{mongo_password}@{mongo_cluster}.bprftog.mongodb.net/{mongo_database}.users?retryWrites=true&w=majority"
mongo_policies_ip = f"mongodb+srv://{mongo_username}:{mongo_password}@{mongo_cluster}.bprftog.mongodb.net/{mongo_database}.policies?retryWrites=true&w=majority"
mongo_policyholders_ip = f"mongodb+srv://{mongo_username}:{mongo_password}@{mongo_cluster}.bprftog.mongodb.net/{mongo_database}.policyholders?retryWrites=true&w=majority"

# Load data from MongoDB with the specified collection name
users = sqlC.read.format("com.mongodb.spark.sql.DefaultSource").option("uri", mongo_users_ip).load()
policies = sqlC.read.format("com.mongodb.spark.sql.DefaultSource").option("uri", mongo_policies_ip).load()

# Create a temporary view
users.createOrReplaceTempView("users")
policies.createOrReplaceTempView("policies")

created_timestamp="2024-02-21 12:00:00"
updated_timestamp="2024-03-03 12:00:00"

# Query to select users whose createdAt timestamp is more recent than the provided timestamp
users_df = sqlC.sql(f"SELECT * FROM users")
policies_df = sqlC.sql(f"SELECT * FROM policies")

users_pandas_df = users_df.toPandas()
from pyspark.sql.functions import col

from pyspark.sql.functions import col

# Check-1 for missing values in 'gender' column
missing_age_count = users_df.filter(col('gender').isNull()).count()
if missing_age_count > 0:
    print(f"Missing values found in 'gender' column: {missing_age_count}")
else:
    print("No missing values found in 'gender' column")

# Check-2 for negative values in age column
invalid_age_count = users_df.filter(col('age') < 0).count()
if invalid_age_count > 0:
    print(f"Invalid values found in 'age' column: {invalid_age_count}")
else:
    print("No invalid values found in 'age' column")

# Check-3 for duplicate entries based on mail
duplicate_entries_count = users_df.groupBy('mail').count().filter('count > 1').count()
if duplicate_entries_count > 0:
    print(f"Duplicate entries found based on 'mail' column: {duplicate_entries_count}")
else:
    print("No duplicate entries found based on 'mail' column")

# Check-4 for outliers in numerical columns (e.g., incomePerAnnum)
outliers_count = users_df.filter(col('incomePerAnnum') < 0).count()
if outliers_count > 0:
    print(f"Outliers found in 'incomePerAnnum' column: {outliers_count}")
else:
    print("No duplicate entries found based on 'mail' column")

# Check-5 for incorrect names with numbers
incorrect_names_count = users_df.filter(col('name').rlike('\\d+')).count()
if incorrect_names_count > 0:
    print(f"Incorrect names found containing numbers in the 'name' column: {incorrect_names_count}")
else:
    print("No incorrect names")