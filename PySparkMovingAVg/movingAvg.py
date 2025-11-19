#pip install pyspark

from pyspark.sql import SparkSession
from pyspark.sql.window import Window
import pyspark.sql.functions as F

# Create Spark session
spark = SparkSession.builder \
    .appName("MovingAverageExample") \
    .getOrCreate()

# Load CSV file
df = spark.read.csv("stocks.csv", header=True, inferSchema=True)

# Define Window (previous 2 rows + current row)
windowSpec = Window.partitionBy("stock") \
                   .orderBy("date") \
                   .rowsBetween(-2, 0)

# Moving average of price (window size = 3)
result = df.withColumn(
    "moving_avg_price",
    F.avg("price").over(windowSpec)
)

# Show top 10 rows
result.show(10, truncate=False)
