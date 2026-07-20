# Databricks notebook source
gold_df = spark.read.table(
    "databricksfintechfraud.default.fraud_transactions"
)

# COMMAND ----------

(
    gold_df
    .coalesce(1)                     # single CSV file
    .write
    .mode("overwrite")
    .option("header", "true")
    .csv("abfss://dashboard@storagefintechfraud.dfs.core.windows.net/gold_latest")
)

# COMMAND ----------

