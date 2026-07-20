# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql.types import *
import random

# COMMAND ----------

merchant_categories = ["Electronics", "Shopping", "Food", "Travel", "Finance", "Healthcare"]
cities = ["Delhi", "Mumbai", "Bangalore", "Pune", "Chennai", "Hyderabad", "Jaipur", "Chandigarh", "Kolkata", "Patna"]
countries = ["India"]

merchant_data = []

for i in range(10000):
    merchant_data.append((
        f"MER{i+1}",
        f"Merchant_{i+1}",
        random.choice(merchant_categories),
        random.randint(1, 100),
        random.choice(cities),
        random.choice(countries)
    ))

# COMMAND ----------

merchant_schema = [
    "merchant_id",
    "merchant_name",
    "merchant_category",
    "risk_score",
    "city",
    "country"
]

merchant_df = spark.createDataFrame(merchant_data, merchant_schema)

# COMMAND ----------

merchant_df = merchant_df.withColumn("created_date", current_timestamp())

# COMMAND ----------

merchant_df.count()

# COMMAND ----------

display(merchant_df.limit(20))

# COMMAND ----------

merchant_df.write.mode("overwrite").parquet(
    "abfss://landing@storagefintechfraud.dfs.core.windows.net/reference-data/merchant_master"
)

# COMMAND ----------

dbutils.fs.ls("abfss://landing@storagefintechfraud.dfs.core.windows.net/reference-data/merchant_master")

# COMMAND ----------

