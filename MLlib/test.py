# ML Classification Example without Spark
# Predicting Customer Churn using scikit-learn

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# -------------------------------------
# 1. Load Dataset from CSV
# -------------------------------------
df = pd.read_csv("customer_data.csv")

# Encode categorical columns
le_sub = LabelEncoder()
le_label = LabelEncoder()

df["SubscribedIndexed"] = le_sub.fit_transform(df["Subscribed"])
df["LabelIndexed"] = le_label.fit_transform(df["Label"])

# -------------------------------------
# 2. Prepare Features
# -------------------------------------
X = df[["Age", "SubscribedIndexed", "Balance"]]
y = df["LabelIndexed"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# -------------------------------------
# 3. Train Logistic Regression Model
# -------------------------------------
model = LogisticRegression()
model.fit(X_train, y_train)

# -------------------------------------
# 4. Predictions & Accuracy
# -------------------------------------
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)

# Show sample predictions
output = pd.DataFrame({
    "Features": X_test.values.tolist(),
    "Prediction": y_pred,
    "Actual": y_test
})
print(output)
