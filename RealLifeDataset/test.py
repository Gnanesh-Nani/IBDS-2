"""
Big Data Analysis Project
Complete Python Script
Dataset used: Online Retail Dataset (UCI Machine Learning Repository)
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
url = "dataset.xlsx"
df = pd.read_excel(url)

# --- Data Cleaning ---
df_clean = df.dropna(subset=["CustomerID"])        # Remove rows with missing CustomerID
df_clean = df_clean[df_clean["Quantity"] > 0]      # Remove negative or zero quantities
df_clean["InvoiceDate"] = pd.to_datetime(df_clean["InvoiceDate"])  # Convert to datetime
df_clean["TotalAmount"] = df_clean["Quantity"] * df_clean["UnitPrice"]

# --- Business Insights ---
# Insight 1: Top 10 highest revenue products
top_products = (
    df_clean.groupby("Description")["TotalAmount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

# Insight 2: Monthly sales trend
monthly_sales = (
    df_clean.set_index("InvoiceDate")
    .resample("ME")["TotalAmount"]
    .sum()
)

# Insight 3: Top 5 customers by revenue
top_customers = (
    df_clean.groupby("CustomerID")["TotalAmount"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

# --- Visualizations ---

# Top Products Bar Chart (Save as Image)
plt.figure(figsize=(10, 5))
top_products.plot(kind="bar")
plt.title("Top 10 Products by Revenue")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("top_10_products.png")
plt.close()

# Monthly Sales Trend Line Chart (Save as Image)
plt.figure(figsize=(10, 5))
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Revenue")
plt.tight_layout()
plt.savefig("monthly_sales_trend.png")
plt.close()

# Top Customers Bar Chart (Save as Image)
plt.figure(figsize=(8, 5))
top_customers.plot(kind="bar", color='orange')
plt.title("Top 5 Customers by Revenue")
plt.xlabel("CustomerID")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("top_5_customers.png")
plt.close()

# --- Print Insights ---
print("=== Key Insights ===\n")
print("1️⃣ Top 10 Products by Revenue:")
print(top_products)
print("\n2️⃣ Monthly Sales Trend (Total Revenue by Month):")
print(monthly_sales.head(12))  # print first 12 months
print("\n3️⃣ Top 5 Customers by Revenue:")
print(top_customers)

# --- Summary ---
summary = """
Summary:
- A small group of top-selling products generates the majority of revenue.
- Monthly sales trends highlight demand fluctuations and seasonality.
- Top customers contribute significantly to total revenue.

How Big Data Helps:
- Identifies hidden patterns for better decision-making.
- Predicts customer behavior and improves forecasting.
- Boosts profitability by focusing on best-performing products.
"""

print(summary)
