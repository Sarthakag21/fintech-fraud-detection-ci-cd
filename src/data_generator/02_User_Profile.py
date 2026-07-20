# Databricks notebook source
from pyspark.sql.functions import *
import random

# COMMAND ----------

cities = ["Delhi", "Mumbai", "Bangalore", "Pune", "Chennai", "Hyderabad", "Jaipur", "Chandigarh", "Kolkata", "Patna"]
kyc_statuses = ["Verified", "Pending", "Rejected"]
risk_segments = ["Low", "Medium", "High"]

user_data = []

for i in range(100000):
    user_data.append((
        f"USER{i+1}",
        f"User_{i+1}",
        random.choice(cities),
        random.randint(1000, 50000),
        random.randint(1, 10),
        random.choice(kyc_statuses),
        random.choice(risk_segments)
    ))

# COMMAND ----------

user_schema = [
    "user_id",
    "name",
    "home_city",
    "avg_spend",
    "account_age",
    "kyc_status",
    "risk_segment"
]

user_df = spark.createDataFrame(user_data, user_schema)

# COMMAND ----------

user_df.count()

# COMMAND ----------

user_df.write.mode("overwrite").parquet(
    "abfss://landing@storagefintechfraud.dfs.core.windows.net/reference-data/user_profile"
)

# COMMAND ----------

