# Databricks notebook source
# MAGIC %md
# MAGIC 1. Read the data from value and then store into the Bronze layer

# COMMAND ----------

filepath=("/Volumes/databricks_practical/practical-schema/storagefiles/CSV/employees.csv")
df=spark.read.format("csv")\
.option("header","true")\
.option("inferSchema","true")\
.load(filepath)\
.write.mode("overwrite")\
.saveAsTable("databricks_practical.bronze.Emplyees")
display(df)

# COMMAND ----------

filepath=("/Volumes/databricks_practical/practical-schema/storagefiles/CSV/departments.csv")
df=spark.read.format("csv")\
.option("header","true")\
.option("inferSchema","true")\
.load(filepath)\
.write.mode("overwrite")\
.saveAsTable("databricks_practical.bronze.Departments")
display(df)