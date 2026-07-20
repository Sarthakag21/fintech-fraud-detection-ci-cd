# Databricks notebook source
from pyspark.sql.types import *

import spark

txn_schema = StructType([
    StructField("transaction_id", StringType(), True),
    StructField("user_id", StringType(), True),
    StructField("merchant_id", StringType(), True),
    StructField("amount", IntegerType(), True),
    StructField("transaction_city", StringType(), True),
    StructField("payment_mode", StringType(), True),
    StructField("transaction_time", StringType(), True)
])

# COMMAND ----------

landing_path = "abfss://landing@storagefintechfraud.dfs.core.windows.net/transactions"

schema_path = "abfss://checkpoint@storagefintechfraud.dfs.core.windows.net/schema/transactions"

# COMMAND ----------

stream_df = (
    spark.readStream
    .format("cloudFiles")
    .option("cloudFiles.format", "json")
    .option("cloudFiles.schemaLocation", schema_path)
    .schema(txn_schema)
    .load(landing_path)
)

# COMMAND ----------

bronze_query = (
    stream_df.writeStream
    .format("delta")
    .outputMode("append")
    .option(
        "checkpointLocation",
        "abfss://landing@storagefintechfraud.dfs.core.windows.net/checkpoints/bronze"
    )
    .start("abfss://bronze@storagefintechfraud.dfs.core.windows.net/transactions")
)

# COMMAND ----------

