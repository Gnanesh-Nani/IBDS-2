# PySpark MLlib Classification Example
# Predicting Customer Churn (Categorical Outcome)

from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.ml.feature import StringIndexer, VectorAssembler
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

# -------------------------------
# 1. Create Spark Session
# -------------------------------
spark = SparkSession.builder.appName("CustomerChurnPrediction").getOrCreate()

# -------------------------------
# -------------------------------
# 2. Load Dataset from CSV
# -------------------------------
# Make sure customer_data.csv contains columns:
# CustomerID, Age, Subscribed, Balance, Label

data = spark.read.csv("customer_data.csv", header=True, inferSchema=True)

# -------------------------------
# data = spark.createDataFrame([
#     (1, 34, "Yes", 20000, "Churn"),
#     (2, 25, "No", 30000, "Stay"),
#     (3, 45, "Yes", 15000, "Churn"),
#     (4, 30, "No", 28000, "Stay"),
#     (5, 41, "No", 12000, "Churn"),
# ], ["CustomerID", "Age", "Subscribed", "Balance", "Label"])

# -------------------------------
# 3. Preprocessing
# -------------------------------
# Convert categorical columns to numeric
indexer1 = StringIndexer(inputCol="Subscribed", outputCol="SubscribedIndexed")
indexer2 = StringIndexer(inputCol="Label", outputCol="LabelIndexed")

data_indexed = indexer1.fit(data).transform(data)
data_indexed = indexer2.fit(data_indexed).transform(data_indexed)

# Assemble features
assembler = VectorAssembler(
    inputCols=["Age", "SubscribedIndexed", "Balance"],
    outputCol="features"
)
final_data = assembler.transform(data_indexed).select("features", "LabelIndexed")

# -------------------------------
# 4. Train-Test Split
# -------------------------------
train, test = final_data.randomSplit([0.8, 0.2], seed=42)

# -------------------------------
# 5. Train MLlib Classification Model
# -------------------------------
lr = LogisticRegression(featuresCol="features", labelCol="LabelIndexed")
model = lr.fit(train)

# -------------------------------
# 6. Make Predictions
# -------------------------------
predictions = model.transform(test)

# -------------------------------
# 7. Evaluate Model
# -------------------------------
evaluator = MulticlassClassificationEvaluator(
    labelCol="LabelIndexed", predictionCol="prediction", metricName="accuracy"
)
accuracy = evaluator.evaluate(predictions)

print("Model Accuracy:", accuracy)

# Show prediction output
predictions.select("features", "prediction", "LabelIndexed").show()

# -------------------------------
# 8. Explanation
# -------------------------------
# MLlib simplifies large-scale ML workflows by:
# - Automatically distributing data and computation across clusters
# - Providing built-in tools for preprocessing, feature engineering, and evaluation
# - Supporting pipelines for reproducible workflows
# - Scaling to large datasets without memory limitations

spark.stop()
