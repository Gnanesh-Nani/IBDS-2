Below is a **complete mini–data warehouse example** with:

 2 Dimension tables → **Customer**, **Product**
 1 Fact table → **Sales**
 Sample data (with valid foreign keys)
 SQL queries to calculate:

* **Total Sales by Product Category**
* **Total Sales by Customer Region**
   Explanation of why a warehouse is better than raw OLTP tables

You can run this in **MySQL, PostgreSQL, SQL Server**, etc. (syntax is generic).

---

#  1. **Create Dimension Tables**

## **Customer Dimension**

```sql
CREATE TABLE dim_customer (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(50),
    region VARCHAR(50)
);
```

## **Product Dimension**

```sql
CREATE TABLE dim_product (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    category VARCHAR(50)
);
```

---

#  2. **Create Fact Table (Sales)**

```sql
CREATE TABLE fact_sales (
    sales_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    quantity INT,
    price DECIMAL(10,2),
    sales_date DATE,
    FOREIGN KEY (customer_id) REFERENCES dim_customer(customer_id),
    FOREIGN KEY (product_id) REFERENCES dim_product(product_id)
);
```

---

#  3. **Insert Sample Data**

## **Insert Customer Data**

```sql
INSERT INTO dim_customer VALUES
(1, 'Ravi', 'South'),
(2, 'Megha', 'North'),
(3, 'John', 'West'),
(4, 'Aditi', 'East');
```

## **Insert Product Data**

```sql
INSERT INTO dim_product VALUES
(101, 'Laptop', 'Electronics'),
(102, 'Mouse', 'Electronics'),
(103, 'Chair', 'Furniture'),
(104, 'Table', 'Furniture');
```

## **Insert Fact Sales Data**

```sql
INSERT INTO fact_sales VALUES
(1, 1, 101, 1, 50000, '2025-01-10'),
(2, 2, 102, 2, 700,   '2025-01-11'),
(3, 3, 103, 1, 2500,  '2025-01-12'),
(4, 4, 104, 1, 4500,  '2025-01-12'),
(5, 1, 102, 3, 700,   '2025-01-13'),
(6, 2, 103, 2, 2500,  '2025-01-14');
```

---

#  4. **Queries**

---

##  **A. Total Sales by Product Category**

We must calculate **quantity × price**, grouped by category.

```sql
SELECT 
    p.category,
    SUM(s.quantity * s.price) AS total_sales
FROM fact_sales s
JOIN dim_product p 
    ON s.product_id = p.product_id
GROUP BY p.category;
```

### ✔ Example Output

| category    | total_sales |
| ----------- | ----------- |
| Electronics | 52100       |
| Furniture   | 9500        |

---

##  **B. Total Sales by Customer Region**

```sql
SELECT 
    c.region,
    SUM(s.quantity * s.price) AS total_sales
FROM fact_sales s
JOIN dim_customer c
    ON s.customer_id = c.customer_id
GROUP BY c.region;
```

### ✔ Example Output

| region | total_sales |
| ------ | ----------- |
| South  | 52100       |
| North  | 5700        |
| West   | 2500        |
| East   | 4500        |

---

#  5. **Why Data Warehousing Improves Analysis**

###  **1. Optimized for Analytics, not transactions**

Transactional databases (OLTP) store many small operations (sales, updates, deletes).
Warehouses (OLAP) store summarized, historical data ideal for reporting.

###  **2. Faster Query Performance**

Warehouse tables are denormalized or star-schema-based → fewer joins → faster reporting.

###  **3. Cleaner Business Logic**

Dimensions (Customer, Product) hold descriptive attributes.
Fact tables store measurable data.
Queries become simpler and standardized.

###  **4. Consistency**

Everyone sees the same version of:

* Product categories
* Regions
* Customer master data

###  **5. Historical Storage**

Warehouses store many years of data, unlike transactional systems that purge old records.

---

#  Summary

You built a **complete mini data warehouse** with:

* Two dimension tables (Customer, Product)
* One fact table (Sales)
* Working sample data
* Aggregation queries for product and region

And learned why data warehouses make business analytics faster and more reliable.

---

Just tell me!
