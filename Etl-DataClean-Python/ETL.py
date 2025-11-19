import pandas as pd

# -------------------------
# 1. EXTRACT
# -------------------------
df = pd.read_csv("input.csv")
print("Raw Data:")
print(df)

# -------------------------
# 2. TRANSFORM
# -------------------------

# Rule 1: Remove rows where customer_id is NULL
df = df.dropna(subset=["customer_id"])

# Rule 2: Standardize date format from YYYY/MM/DD → YYYY-MM-DD
df["join_date"] = pd.to_datetime(df["join_date"], errors="coerce").dt.strftime("%Y-%m-%d")

# Rule 3: Replace missing purchase amounts with 0
df["purchase_amount"] = df["purchase_amount"].fillna(0)

print("\nCleaned Data:")
print(df)

# -------------------------
# 3. LOAD
# -------------------------
df.to_csv("cleaned_output.csv", index=False)

print("\nData successfully loaded into cleaned_output.csv")
