## 🛒 Merchandise Sales Analysis 
---
## 🧠Project Overview
This project analyzes merchandise sales data to identify trends, assess product performance, and optimize business strategies. Using Python for data extraction, transformation, and visualization, this analysis provides actionable insights into sales, customer behavior, and pricing impacts.

---
## 📊Project Breakdown
This project follows a structured ETL (Extract, Transform, Load) approach:

- **Data Extraction**: Importing raw sales data from **Excel/CSV** files.
- **Data Transformation**: Cleaning and processing data using **pandas** and **NumPy**.
- **Data Visualization**: Creating insightful graphs with **matplotlib** and **seaborn** to interpret key findings.

## 🔍Key Features
- **Sales Trends**: Identify peak sales periods and seasonal demand.
- **Product Performance**: Determine the best and worst-selling products.
- **Customer Insights**: Analyze purchasing behavior by gender and age group.
- **Discount & Pricing Impact**: Assess how discounts influence total sales.
- **Shipping & Market Analysis**: Compare domestic vs. international sales performance.
---
1️⃣ Data Extraction & Preprocessing (ETL)
``` python
# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("merchandise_sales.csv")  # Update with actual filename

# Data Cleaning
df.dropna(inplace=True)  # Remove missing values
df["order_date"] = pd.to_datetime(df["order_date"])  # Convert date column
df["profit_margin"] = (df["revenue"] - df["cost"]) / df["revenue"]  # Calculate profit margin

# Preview dataset
print(df.head())
```

## 🔗 Portfolio Link  
[Back to My Portfolio][(https://github.com/Yungssu/kennethHuyong.github.io)
