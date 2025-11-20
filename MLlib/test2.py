from pyspark.sql import SparkSession
from pyspark.ml.feature import StringIndexer, VectorAssembler
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

spark = SparkSession.builder \
    .appName("CustomerChurnMLlib") \
    .getOrCreate()


df = spark.read.csv("customer_data.csv", header=True, inferSchema=True)


sub_indexer = StringIndexer(inputCol="Subscribed", outputCol="SubscribedIndexed")
df = sub_indexer.fit(df).transform(df)

label_indexer = StringIndexer(inputCol="Label", outputCol="LabelIndexed")
df = label_indexer.fit(df).transform(df)

feature_cols = ["Age", "SubscribedIndexed", "Balance"]
assembler = VectorAssembler(inputCols=feature_cols, outputCol="features")
df = assembler.transform(df)

train_df, test_df = df.randomSplit([0.8, 0.2], seed=42)

lr = LogisticRegression(featuresCol="features", labelCol="LabelIndexed")
model = lr.fit(train_df)


predictions = model.transform(test_df)

evaluator = MulticlassClassificationEvaluator(
    labelCol="LabelIndexed",
    predictionCol="prediction",
    metricName="accuracy"
)

accuracy = evaluator.evaluate(predictions)
print("Model Accuracy:", accuracy)

predictions.select("features", "prediction", "LabelIndexed").show(10, truncate=False)

spark.stop()
