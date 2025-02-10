#!/usr/bin/env python
# coding: utf-8

# # Setup & Data Loading

# In[3]:


pip install pandas openpyxl


# In[6]:


import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Setting for a clean and professional look
sns.set_style("whitegrid")
plt.rcParams.update({'font.size': 12})


# In[7]:


import pandas as pd

file_path = r"C:\Users\yungs\OneDrive\Documents\SQL Portfolio\Onyx Data -DataDNA Dataset Challenge - Merchandise Sales Dataset - January 2025\Onyx Data -DataDNA Dataset Challenge - Merchandise Sales Dataset - January 2025.xlsx"
xls = pd.ExcelFile(file_path)

print(xls.sheet_names)  # Check if the file loads


# In[8]:


df = pd.read_excel(xls, sheet_name="Data")
print(df.head())
print(df.info())


# # Data Cleaning & Processing

# In[9]:


print(df.isnull().sum()) # Count missing values per column


# In[10]:


print(df.duplicated().sum()) # Count of duplicate rows
#df = df.drop_duplicates() If there are duplicates


# In[11]:


df.columns = df.columns.str.lower().str.replace(" ", "_")
print(df.columns) #Verify Changes


# In[12]:


print(df.dtypes)


# In[13]:


print(df.isnull().sum())


# # Exploratory Data Analysis (EDA)

# print(df["buyer_gender"].unique())
# print(df["international_shipping"].unique())

# In[14]:


print(df["rating"].unique())


# # Sales Trend Analysis

# In[15]:


df["year_month"] = df["order_date"].dt.to_period("M") # Creates YYYY-MM format
monthly_sales = df.groupby("year_month")["total_sales"].sum().reset_index()

print(monthly_sales.head()) # Preview Monthly Sales


# In[41]:


# Monthly Sales Trend
plt.figure(figsize = (10, 5))
sns.lineplot(data = df, x = 'order_date', y = 'total_sales', marker = 'o', color = '#007acc', linewidth = 2)
plt.xlabel("Order Date")
plt.ylabel("Total Sales")
plt.title("Monthly Sales Trend")
plt.xticks(rotation = 45)
plt.savefig("monthly_sales_trend.png")
plt.show()


# # Product Performance Analysis

# In[17]:


category_sales = df.groupby("product_category")["total_sales"].sum().reset_index()
category_sales = category_sales.sort_values(by = "total_sales", ascending = False)

print(category_sales.head())


# In[42]:


# Best-Selling Product by Category
plt.figure(figsize = (8, 5))
ax = sns.barplot(data = df.groupby("product_category")["total_sales"].sum().reset_index(),
                x = "product_category", y = "total_sales", palette = "coolwarm")
ax.bar_label(ax.containers[0])
plt.xlabel("Product Category")
plt.ylabel("Total Sales")
plt.title("Best-Selling Product Categories")
plt.savefig("best_selling_product_categories.png")
plt.show()


# In[19]:


product_sales = df.groupby("product_id")["total_sales"].sum().reset_index()
product_sales = product_sales.sort_values(by = "total_sales", ascending = False)

print("Top 5 Best-Selling Products:")
print(product_sales.head())

print("\nBottom 5 Least-Selling Products:")
print(product_sales.tail())


# In[43]:


plt.figure(figsize = (12, 6))

# Top 10 Best_Selling Products
sns.barplot(data = product_sales.head(10), x = "total_sales", y = "product_id", palette = "Blues_r")
plt.xlabel("Total Quantity Sold")
plt.ylabel("Product ID")
plt.title("Top 10 Best-Selling Products")
plt.savefig("top10_best_selling_products.png")
plt.show()

# Bottom 10 Least-Selling Products
plt.figure(figsize = (12, 6))
sns.barplot(data = product_sales.tail(10), x = "total_sales", y = "product_id", palette = "Reds_r")
plt.xlabel("Total Quantity Sold")
plt.ylabel("Product ID")
plt.title("Top 10 Least-Selling Products")
plt.savefig("top10_least_selling_products.png")
plt.show()


# # Geographical Sales Analysis

# In[21]:


location_sales = df.groupby("order_location")["total_sales"].sum().reset_index()
location_sales = location_sales.sort_values(by = "total_sales", ascending = False)

print("Top 5 Location by Sales:")
print(location_sales.head())


# In[44]:


# Top 10 Location by Sales
top_locations = df.groupby("order_location")["total_sales"].sum().reset_index()
plt.figure(figsize = (10, 5))
sns.barplot(data = top_locations, x = "total_sales", y = "order_location", palette = "Blues_r")
plt.xlabel("Total Sales")
plt.ylabel("Order Location")
plt.title("Top 10 Location by Sales")
plt.savefig("top10_locations_by_sales.png")
plt.show()


# # Shipping Impact on Sales

# In[23]:


shipping_sales = df.groupby("international_shipping")["total_sales"].sum().reset_index()
print(shipping_sales)


# In[45]:


# Sales Comparison: Domestic vs. International Shipping
plt.figure(figsize = (8, 5))
ax = sns.barplot(data = df.groupby("international_shipping")["total_sales"].sum().reset_index(),
                 x = "international_shipping", y = "total_sales", palette = "Set2")
ax.bar_label(ax.containers[0])
plt.xlabel("Shipping Type")
plt.ylabel("Total Sales")
plt.title("Sales Comparison: Domestic vs. International Shipping")
plt.savefig("domestic_vs_internationalshipping.png")
plt.show()


# # Customer Demographics & Behavior

# In[25]:


gender_sales = df.groupby("buyer_gender")["total_sales"].sum().reset_index()
print(gender_sales)


# In[46]:


# Sales Breakdown by Gender
plt.figure(figsize = (8, 5))
ax = sns.barplot(data = gender_sales, x = "buyer_gender", y = "total_sales", palette = "pastel")
ax.bar_label(ax.containers[0])
plt.xlabel("Gender")
plt.ylabel("Total Sales")
plt.title("Sales Breakdown by Buyer Gender")
plt.savefig("sales_by_buyer_gender.png")
plt.show()


# In[27]:


bins = (0, 18, 25, 35, 45, 55, 65, 100) # Age Ranges
labels = ["<18", "18-24", "25-34", "35-44", "45-54", "55-64", "65+"]
df["age_group"] = pd.cut(df["buyer_age"], bins = bins, labels = labels, right = False)

age_sales = df.groupby("age_group")["total_sales"].sum().reset_index()
print(age_sales)


# In[47]:


# Sales Distribution by Age Group
plt.figure(figsize = (8, 5))
ax = sns.barplot(data = age_sales, x = "age_group", y = "total_sales", palette = "cool")
ax.bar_label(ax.containers[0])
plt.xlabel("Age Group")
plt.ylabel("Total Sales")
plt.title("Sales Distribution by Age Group")
plt.savefig("sales_distribution_by_age_group.png")
plt.show()


# # Impact of Ratings and Discounts on Sales

# In[29]:


rating_sales = df.groupby("rating")["total_sales"].mean().reset_index()
print(rating_sales)


# In[48]:


# Impact of Rating on Sales
plt.figure(figsize = (8, 5))
ax = sns.barplot(data = rating_sales, x = "rating", y = "total_sales", palette = "viridis")
ax.bar_label(ax.containers[0])
plt.xlabel("Product Rating")
plt.ylabel("Average Sales")
plt.title("Impact of Rating on Sales")
plt.savefig("impact_rating_on_sales.png")
plt.show()


# In[31]:


shipping_analysis = df.groupby("shipping_charges")["total_sales"].mean().reset_index()
print(shipping_analysis)


# In[49]:


# Impact of Shipping Charges on Sales
plt.figure(figsize = (8, 5))
sns.scatterplot(data = df, x = "shipping_charges", y = "total_sales", alpha = 0.6, color = "#ff4c4c")
plt.xlabel("Shipping Charges")
plt.ylabel("Total Sales")
plt.title("Impact of Shipping Charges on Sales")
plt.savefig("impact_shipping_charges_on_sales.png")
plt.show()


# In[33]:


df["discount"] = ((df["sales_price"] - df["total_sales"]) / df["sales_price"]) * 100
df["discount"] = df["discount"].round(2) # Round to 2 decimals


# In[34]:


discount_sales = df.groupby("discount")["total_sales"].mean().reset_index()
print(discount_sales)


# In[50]:


# Effect of Discounts on Sales
plt.figure(figsize = (8, 5))
sns.scatterplot(data = df, x = "discount", y = "total_sales", alpha = 0.5, color = "#cc6600")
plt.xlabel("Discount Percentage")
plt.ylabel("Total Sales")
plt.title("Effect of Discounts on Sales")
plt.savefig("effect_discount_on_sales.png")
plt.show()


# In[36]:


repeat_customers = df.groupby(["order_location", "buyer_gender", "buyer_age"])["order_id"].count().reset_index()
repeat_customers.columns = ["order_location", "buyer_gender", "buyer_age", "purchase_count"]

print(repeat_customers["purchase_count"].value_counts()) # Check distribution purchase


# In[37]:


loyal_customers = repeat_customers[repeat_customers["purchase_count"] > 1]
print("Number of Repeat Customers:", len(loyal_customers))


# In[51]:


# Distribution of Repeat Purchases
plt.figure(figsize = (8,5))
sns.histplot(repeat_customers["purchase_count"], bins = 15, kde = True, color = "#5a9e6f")
plt.xlabel("Number of Purchases")
plt.ylabel("Number of Customers")
plt.title("Distribution of Repeat Purchases")
plt.savefig("distribution_repeat_purchases.png")
plt.show()


# # Word Cloud for Customer Reviews 

# In[39]:


pip install wordcloud


# In[40]:


from wordcloud  import WordCloud 

# Combine all reviews intro single Text
text = " ".join(df["review"].dropna())

# Generate word cloud
wordcloud = WordCloud(width = 800, height = 400, background_color = "white").generate(text)

# Display word cloud
plt.figure(figsize = (10, 5))
plt.imshow(wordcloud, interpolation = "bilinear")
plt.axis("off")
plt.title("Common Words in Reviews")
plt.show()


# In[ ]:




