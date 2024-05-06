import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("MyPySparkApp").getOrCreate()

#read file csv
df = spark.read.csv("username.csv", header=True, inferSchema=True)

#read file json
df = spark.read.json("zipcodes.json", inferSchema=True)

#read find parquet
df = spark.read.parquet("MT cars.parquet")

from pyspark.sql.functions import col

df = spark.range(10).repartition(5)  # Repartition into 5 partitions
df = df.repartition(col("id"))  # Partition by the "id" column

df = spark.range(10).repartition(5).coalesce(2)  # Reduce to 2 partitions

df = spark.createDataFrame([("A", 1), ("B", 2), ("A", 3)], ["category", "value"])
df = df.partitionBy("category") 

stations.write.format("delta").saveAsTable("default.table_name")

data.writeTo("mdm.table_name")\
          .tableProperty("location", "s3://path/to/location/") \
          .create()