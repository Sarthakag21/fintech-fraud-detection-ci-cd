# Databricks notebook source
import spark
from IPython import display

silver_path = "abfss://silver@storagefintechfraud.dfs.core.windows.net/transactions"

# COMMAND ----------

silver_stream_df = (
    spark.readStream
    .format("delta")
    .load(silver_path)
)

# COMMAND ----------

from pyspark.sql.functions import *

# COMMAND ----------

gold_df = (
    silver_stream_df
    .withColumn(
        "fraud_score",

        when(col("amount") > col("avg_spend") * 3, 40).otherwise(0)
        +

        when(col("risk_score") > 80, 30).otherwise(0)
        +

        when(col("risk_segment") == "High", 20).otherwise(0)
        +

        when(col("transaction_city") != col("home_city"), 10).otherwise(0)
    )
)

# COMMAND ----------

gold_df = gold_df.withColumn(
    "fraud_status",
    when(col("fraud_score") > 60, "HIGH RISK")
    .when(col("fraud_score") >= 30, "MEDIUM RISK")
    .otherwise("LOW RISK")
)

# COMMAND ----------

gold_df = gold_df.withColumn(
    "fraud_reason",
    when(
        (col("amount") > col("avg_spend") * 3) &
        (col("risk_score") > 80),
        "High Amount + High Risk Customer"
    )
    .when(
        col("amount") > col("avg_spend") * 3,
        "Amount Much Higher Than Average"
    )
    .when(
        col("risk_score") > 80,
        "Customer Risk Score Above Threshold"
    )
    .when(
        col("transaction_city") != col("home_city"),
        "Transaction From Different City"
    )
    .otherwise("Normal Transaction")
)

# COMMAND ----------

dbutils.fs.rm(
    "abfss://landing@storagefintechfraud.dfs.core.windows.net/checkpoints/display_gold_v2/commits",
    True
),
dbutils.fs.rm(
    "abfss://landing@storagefintechfraud.dfs.core.windows.net/checkpoints/display_gold_v2/offsets",
    True
)

# COMMAND ----------

gold_query = (
    gold_df.writeStream
    .outputMode("append")
    .option(
        "checkpointLocation",
        "abfss://landing@storagefintechfraud.dfs.core.windows.net/checkpoints/gold_v2"
    )
    .toTable("databricksfintechfraud.default.fraud_transactions")
)

# COMMAND ----------

gold_stream = (
    spark.readStream
    .table("databricksfintechfraud.default.fraud_transactions")
)

display(
    gold_stream,
    checkpointLocation="abfss://landing@storagefintechfraud.dfs.core.windows.net/checkpoints/display_gold_v2"
)

# COMMAND ----------

