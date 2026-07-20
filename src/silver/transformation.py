# Databricks notebook source
import spark
from IPython import display

bronze_path = "abfss://bronze@storagefintechfraud.dfs.core.windows.net/transactions"

# COMMAND ----------

bronze_stream_df = (
    spark.readStream
    .format("delta")
    .load(bronze_path)
)

# COMMAND ----------

from pyspark.sql.functions import *

# COMMAND ----------

clean_df = (
    bronze_stream_df
    .withColumn("amount", col("amount").cast("int"))
    .withColumn("transaction_timestamp", to_timestamp("transaction_time"))
    .drop("transaction_time")
    .dropDuplicates(["transaction_id"])
)

# COMMAND ----------

user_df = spark.read.parquet(
    "abfss://silver@storagefintechfraud.dfs.core.windows.net/reference-data/user_profile"
)

# COMMAND ----------

merchant_df = spark.read.parquet(
    "abfss://silver@storagefintechfraud.dfs.core.windows.net/reference-data/merchant_master"
)

# COMMAND ----------

silver_df = (
    clean_df
    .join(user_df, "user_id", "left")
    .join(merchant_df, "merchant_id", "left")
)

# COMMAND ----------

dbutils.fs.rm(
    "abfss://landing@storagefintechfraud.dfs.core.windows.net/checkpoints/display_silver/commits",
    True
),
dbutils.fs.rm(
    "abfss://landing@storagefintechfraud.dfs.core.windows.net/checkpoints/display_silver/offsets",
    True
)

# COMMAND ----------

silver_query = (
    silver_df.writeStream
    .format("delta")
    .outputMode("append")
    .option("checkpointLocation", "abfss://landing@storagefintechfraud.dfs.core.windows.net/checkpoints/silver")
    .start("abfss://silver@storagefintechfraud.dfs.core.windows.net/transactions")
)

# COMMAND ----------

silver_stream = (
    spark.readStream
    .format("delta")
    .load("abfss://silver@storagefintechfraud.dfs.core.windows.net/transactions")
)

display(
    silver_stream,
    checkpointLocation="abfss://landing@storagefintechfraud.dfs.core.windows.net/checkpoints/display_silver"
)

# COMMAND ----------

