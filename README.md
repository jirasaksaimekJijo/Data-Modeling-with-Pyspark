# Week4: Data-Modeling-with-Pyspark

## Description
- PySpark:  A Python interface for working with Apache Spark. It lets you use the power of Spark's distributed computing framework with the ease and familiarity of the Python programming language. apache spark A fast, powerful, and versatile engine for large-scale data processing. It uses in-memory computations and works with a variety of data sources.

- RDD (Resilient Distributed Dataset): The fundamental data structure in Spark. RDDs are collections of data elements spread across a cluster that can be operated on in parallel. Think of them as big chunks of data cleverly split for efficient processing.

- Data Wrangling: The process of transforming and cleaning raw data into a form that's suitable and ready for further analysis.

- CSV (Comma-Separated Values):  A very common file format for storing data. Think of it like a simple spreadsheet where values are separated by commas.

- JSON (JavaScript Object Notation): A popular format for exchanging data between different systems. It uses a human-readable structure of key-value pairs.

## Prosesc
## 1.install pyspark 

### 1.1 pyspark is ?

PySpark is an incredible asset for working with big data. By harnessing the power of Apache Spark from within Python, you can efficiently read, process, and analyze massive datasets. This makes tasks like data exploration, transformation, and even machine learning much more manageable on large-scale data.

### 1.2 set up on Docker
#### Why Docker for PySpark?
- Portability: Build a self-contained PySpark environment that runs consistently across different machines.
- Isolation: Manage dependencies without conflicts on your host system.
- Scalability: Easily replicate your PySpark setup for larger datasets or distributed computing.

1.install Docker
Get Docker Desktop from the official website
```bash
https://www.docker.com/get-started
```

2.run commnad install pyspark-notebook
  Next, we need to install pyspark on Docker to make it easier to use.
```bash
docker pull jupyter/pyspark-notebook:x86_64-ubuntu-22.04
```

Once the image is created, you can command it to run the jupyter/pyspark  service.
```bash
docker run -it -p 8888:8888 my-pyspark-image
```
Once the run is complete, we will have a service that can run pyspark and is ready to use to use pyspark, Open a web browser and go to 
```bash
http://localhost:8888. 
```
You'll see the Jupyter Notebook interface.  

- server name run pyspark
![image](https://github.com/jirasaksaimekJijo/Week4-Data-Warehouse-with-Pyspark/assets/116647943/dfedfdce-9660-43fc-9449-0c1f7483b6fe)


## 2.pyspark example 
2.1 start pyspark
Always start SparkSession pyspark for startup.
```bash
import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("MyPySparkApp").getOrCreate()
```

2.2 read find (csv, json, parquet)
```bash
#read file csv
df = spark.read.csv("path/to/your/data.csv", header=True, inferSchema=True)

#read file json
df = spark.read.json("path/to/your/data.json", inferSchema=True)

#read find parquet
df = spark.read.parquet("path/to/your/data.parquet", inferSchema=True)
```
2.3 partition data for Increase reading speed

allows you to explicitly increase or decrease the number of partitions in a DataFrame.
```bash
from pyspark.sql.functions import col

df = spark.range(10).repartition(5)  # Repartition into 5 partitions
df = df.repartition(col("id"))  # Partition by the "id" column
```
Used to reduce the number of partitions. Useful for consolidating data into a smaller number of partitions without triggering a full shuffle.
```bash
df = spark.range(10).repartition(5).coalesce(2)  # Reduce to 2 partitions
```
Controls partitioning based on the values of specified columns. Data with the same values in the partitioning columns will end up in the same partition. Used for optimizing joins and saving data partitioned in a specific way.
```bash
df = spark.createDataFrame([("A", 1), ("B", 2), ("A", 3)], ["category", "value"])
df = df.partitionBy("category") 
```

2.4 writh data to table in Athena

You can process and prepare data in Databricks and then write it to S3 in a format Athena understands (e.g., CSV, Parquet).
Your Databricks example is correct if: 
'stations' is a Delta table in Databricks 'default.stations' is the Athena table you want to create/overwrite

#### save is Databricks
```bash
stations.write.format("delta").saveAsTable("default.stations")
```

#### save to athena
```bash
data.writeTo("mdm.table_name")\
          .tableProperty("location", "s3://path/to/location/") \
          .create()
```
