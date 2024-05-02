# Week... : Data-Modeling-with-Pyspark

## Description
To get started, I'll guide you through the installation of PySpark.  Then, we'll dive into some core PySpark commands covering the following:

- Importing data: Learn how to load common data formats like CSV, JSON, and more.
- Data Wrangling: Discover techniques to filter, select, and clean your data.

## Prosesc
1.install pyspark 
- pyspark is ?
- set up on Docker

2.pyspark example 
- read find (csv, json, parquet)
- partition data for Increase reading speed
- writh data to table in Athena

## 1.1 pyspark is ?

PySpark is an incredible asset for working with big data. By harnessing the power of Apache Spark from within Python, you can efficiently read, process, and analyze massive datasets. This makes tasks like data exploration, transformation, and even machine learning much more manageable on large-scale data.

## 1.2 set up on Docker
## Why Docker for PySpark?
- Portability: Build a self-contained PySpark environment that runs consistently across different machines.
- Isolation: Manage dependencies without conflicts on your host system.
- Scalability: Easily replicate your PySpark setup for larger datasets or distributed computing.

- 1. install Docker
```bash
https://www.docker.com/get-started
```
- 2.run commnad install pyspark-notebook
  
```bash
docker pull jupyter/pyspark-notebook:x86_64-ubuntu-22.04
```
start image jupyter/pyspark 
```bash
docker run -it -p 8888:8888 my-pyspark-image
```
- Open a web browser and go to http://localhost:8888. You'll see the Jupyter Notebook interface.

2.1
start pyspark 
```bash
import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("MyPySparkApp").getOrCreate()
```
example read file csv 
```bash
df = spark.read.csv("path/to/your/data.csv", header=True, inferSchema=True)
```

example read file json 
```bash
df = spark.read.json("path/to/your/data.json", inferSchema=True)
```

example read file parquet 
```bash
df = spark.read.parquet("path/to/your/data.parquet", inferSchema=True)
```

example write to table in databricks

```bash
stations.write.format("delta").saveAsTable("default.stations")
```

example write to table
```bash
data.writeTo("mdm.table_name")\
          .tableProperty("location", "s3://path/to/location/") \
          .create()
```
