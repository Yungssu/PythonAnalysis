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

2️⃣ Sales Performance Analysis
``` python
# Monthly Sales Trend
plt.figure(figsize=(10, 5))
df.groupby(df["order_date"].dt.to_period("M"))["revenue"].sum().plot(kind="line", marker="o", color="#4C72B0")

plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.title("Monthly Sales Trend")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
```
![Sales Performace](https://github.com/Yungssu/PythonAnalysis/blob/main/Python_Analysis/monthly_sales_trend.png)

3️⃣ Product Performance Analysis
- **Top 10 Best Selling Products**
``` python
# Top 10 Best-Selling Products
top_products = df.groupby("product_name")["revenue"].sum().nlargest(10)

plt.figure(figsize=(10, 5))
sns.barplot(x=top_products.values, y=top_products.index, palette="Blues_r")
plt.xlabel("Total Revenue")
plt.ylabel("Product")
plt.title("Top 10 Best-Selling Products")
plt.show()

```
![Top 10 Best Selling Products](https://github.com/Yungssu/PythonAnalysis/blob/main/Python_Analysis/top10_best_selling_products.png)
- **Top 10 Least Selling Products**
``` python
# Top 10 Least Selling Products
low_products = df.groupby("product_name")["revenue"].sum().nsmallest(10)

plt.figure(figsize=(10, 5))
sns.barplot(x=low_products.values, y=low_products.index, palette="Reds_r")
plt.xlabel("Total Revenue")
plt.ylabel("Product")
plt.title("Top 10 Lowest-Selling Products")
plt.show()
```
![Top 10 Least Selling Products](https://github.com/Yungssu/PythonAnalysis/blob/main/Python_Analysis/top10_least_selling_products.png)

4️⃣ Customer Insights & Buying Behavior
- **Sales by Gender**
``` python
# Sales by Gender
plt.figure(figsize=(6, 4))
sns.barplot(x=df["gender"], y=df["revenue"], palette={"Male": "#FF6F61", "Female": "#6B5B95"})
plt.xlabel("Gender")
plt.ylabel("Total Sales")
plt.title("Sales Breakdown by Buyer Gender")
plt.show()
```
![Sales by Gender](https://github.com/Yungssu/PythonAnalysis/blob/main/Python_Analysis/sales_by_buyer_gender.png)

- **Sales Distribution by Age Group**
``` python
# Sales Distribution by Age Group
plt.figure(figsize = (8, 5))
ax = sns.barplot(data = age_sales, x = "age_group", y = "total_sales", palette = "cool")
ax.bar_label(ax.containers[0])
plt.xlabel("Age Group")
plt.ylabel("Total Sales")
plt.title("Sales Distribution by Age Group")
# plt.savefig("sales_distribution_by_age_group.png")
plt.show()
```
![Sales Distribution by Age Group](https://github.com/Yungssu/PythonAnalysis/blob/main/Python_Analysis/sales_distribution_by_age_group.png)

5️⃣ Discounts & Pricing Impact
- **Effect of Discount on Sales**
``` python
# Effect of Discount on Sales
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df["discount_percentage"], y=df["revenue"], alpha=0.5, color="#FFA07A")
plt.xlabel("Discount Percentage")
plt.ylabel("Total Sales")
plt.title("Effect of Discounts on Sales")
plt.show()
```
![Effect of Discount on Sales](https://github.com/Yungssu/PythonAnalysis/blob/main/Python_Analysis/effect_discount_on_sales.png)

- **Impact of Ratings on Sales**
``` python
# Impact of Ratings on Sales
plt.figure(figsize = (8, 5))
ax = sns.barplot(data = rating_sales, x = "rating", y = "total_sales", palette = "viridis")
ax.bar_label(ax.containers[0])
plt.xlabel("Product Rating")
plt.ylabel("Average Sales")
plt.title("Impact of Rating on Sales")
plt.savefig("impact_rating_on_sales.png")
plt.show()
```
![Impact of Rating on Sales](https://github.com/Yungssu/PythonAnalysis/blob/main/Python_Analysis/impact_rating_on_sales.png)


- **Impact of Shipping Charges on Sales**
``` python
# Impact of Shipping Charges on Sales
plt.figure(figsize = (8, 5))
sns.scatterplot(data = df, x = "shipping_charges", y = "total_sales", alpha = 0.6, color = "#ff4c4c")
plt.xlabel("Shipping Charges")
plt.ylabel("Total Sales")
plt.title("Impact of Shipping Charges on Sales")
plt.savefig("impact_shipping_charges_on_sales.png")
plt.show()
```
![Impact of Shipping Charges on Sales](https://github.com/Yungssu/PythonAnalysis/blob/main/Python_Analysis/impact_shipping_charges_on_sales.png)

6️⃣ Shipping & Market Analysis
- **Sales Comparison: Domestic vs. International**
``` python
# Sales Comparison: Domestic vs. International Shipping
plt.figure(figsize=(8, 5))
sns.barplot(x=df["shipping_type"], y=df["revenue"], palette="viridis")
plt.xlabel("Shipping Type")
plt.ylabel("Total Revenue")
plt.title("Sales Comparison: Domestic vs. International Shipping")
plt.show()
```
![Domestic vs. International](https://github.com/Yungssu/PythonAnalysis/blob/main/Python_Analysis/domestic_vs_internationalshipping.png)

---
## 📌 Recommendations  

Based on the **Merchandise Sales Analysis**, here are key recommendations to optimize sales, improve inventory management, and enhance profitability:  

### 🔥 **1. Focus on Best-Selling Products**  
- Increase stock levels for **top-performing products** to meet demand.  
- Prioritize marketing and promotional efforts for **high-revenue items**.  

### 🛒 **2. Optimize Inventory for Seasonal Demand**  
- Align stock replenishment with **seasonal trends** to avoid overstocking or stockouts.  
- Offer **seasonal discounts** to clear out low-performing inventory.  

### 💰 **3. Adjust Pricing Strategies**  
- Implement **dynamic pricing** for products with fluctuating demand.  
- Consider **bundle discounts** to encourage bulk purchases.  

### 📈 **4. Enhance Customer Targeting**  
- Use **customer segmentation** to personalize promotions.  
- Leverage insights from **purchase patterns** to recommend relevant products.  

### 🚀 **5. Improve Data-Driven Decision Making**  
- Regularly analyze **sales trends** to adjust strategies.  
- Integrate **real-time analytics** to monitor performance dynamically.  

By implementing these strategies, businesses can **boost revenue, optimize inventory, and improve customer satisfaction**. 🚀  

---
## 🔗 Portfolio Link  
[Back to My Portfolio][(https://github.com/Yungssu/kennethHuyong.github.io)
