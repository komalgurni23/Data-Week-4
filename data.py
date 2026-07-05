import pandas as pd
import matplotlib.pyplot as plt
import os

# Create visualization folder
os.makedirs("visualizations", exist_ok=True)

# Load Dataset
try:
    df = pd.read_csv("sales_data.csv")
    print("Dataset Loaded Successfully!\n")
except FileNotFoundError:
    print("Error: sales_data.csv file not found!")
    exit()

# Display Data
print("First 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

# Data Cleaning
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

print("\nDataset after Cleaning:")
print(df.shape)

# Summary
print("\nSummary Statistics:")
print(df.describe())

# Analysis
total_sales = df["Total_Sales"].sum()
print("\nTotal Sales =", total_sales)

average_sales = df["Total_Sales"].mean()
print("Average Sales =", average_sales)

highest_sale = df["Total_Sales"].max()
print("Highest Sale =", highest_sale)

lowest_sale = df["Total_Sales"].min()
print("Lowest Sale =", lowest_sale)

# Product Wise Sales
product_sales = df.groupby("Product")["Total_Sales"].sum()

print("\nProduct Wise Sales")
print(product_sales)

# Region Wise Sales
region_sales = df.groupby("Region")["Total_Sales"].sum()

print("\nRegion Wise Sales")
print(region_sales)

# ---------------- Bar Chart ----------------
plt.figure(figsize=(8,5))
product_sales.plot(kind="bar")
plt.title("Product Wise Sales")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("visualizations/product_sales.png")
plt.show()

# ---------------- Pie Chart ----------------
plt.figure(figsize=(7,7))
region_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Region Wise Sales")
plt.ylabel("")
plt.tight_layout()
plt.savefig("visualizations/region_sales.png")
plt.show()

# ---------------- Line Chart ----------------
df["Date"] = pd.to_datetime(df["Date"])
daily_sales = df.groupby("Date")["Total_Sales"].sum()

plt.figure(figsize=(10,5))
daily_sales.plot(kind="line", marker="o")
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.grid(True)
plt.tight_layout()
plt.savefig("visualizations/daily_sales.png")
plt.show()

# Insights
print("\n========== PROJECT INSIGHTS ==========")

print("Total Sales :", total_sales)
print("Average Sales :", round(average_sales,2))
print("Highest Sale :", highest_sale)
print("Lowest Sale :", lowest_sale)

print("Best Selling Product :", product_sales.idxmax())
print("Lowest Selling Product :", product_sales.idxmin())

print("Best Region :", region_sales.idxmax())
print("Lowest Region :", region_sales.idxmin())

print("\nAnalysis Completed Successfully!")
print("Charts Saved in visualizations folder.")