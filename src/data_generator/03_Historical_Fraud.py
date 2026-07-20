# Databricks notebook source
from pyspark.sql.functions import *

# COMMAND ----------

fraud_df = spark.range(1, 500001)

# COMMAND ----------

fraud_df = fraud_df.select(
    concat(lit("FRAUD"), col("id")).alias("fraud_case_id"),
    concat(lit("TXN"), (rand()*1000000).cast("int")).alias("transaction_id"),

    when(rand() < 0.2, "High Amount Fraud")
    .when(rand() < 0.4, "Suspicious Merchant")
    .when(rand() < 0.6, "Multiple Failed Attempts")
    .when(rand() < 0.8, "Impossible Travel")
    .otherwise("Night Transaction").alias("fraud_type"),

    (rand()*100 + 1).cast("int").alias("fraud_score"),

    when(rand() < 0.5, "Closed")
    .when(rand() < 0.8, "Open")
    .otherwise("Pending").alias("investigation_status"),

    (rand()*150000 + 5000).cast("int").alias("fraud_amount"),

    when(rand() < 0.1, "Hyderabad")
    .when(rand() < 0.2, "Delhi")
    .when(rand() < 0.3, "Jaipur")
    .when(rand() < 0.4, "Mumbai")
    .when(rand() < 0.5, "Chandigarh")
    .when(rand() < 0.6, "Bangalore")
    .when(rand() < 0.7, "Kolkata")
    .when(rand() < 0.8, "Pune")
    .when(rand() < 0.9, "Patna")
    .otherwise("Chennai").alias("city"),

    current_timestamp().alias("detected_at")
)

# COMMAND ----------

fraud_df.count()

# COMMAND ----------

display(fraud_df.limit(20))

# COMMAND ----------

fraud_df = fraud_df.repartition(4)

# COMMAND ----------

fraud_df.write.mode("overwrite").parquet(
    "abfss://landing@storagefintechfraud.dfs.core.windows.net/reference-data/historical_fraud"
)

# COMMAND ----------

