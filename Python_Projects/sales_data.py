import pandas as pd

df = pd.read_csv('sales_data.csv')

# display the first five row
print("First 5 rows of the sales data:")
print(df.head())

# Calculate the total sale 
total_sales = df['Sales'].sum()
print("\nTotal Sales Amount:", total_sales)

# Calculate and display the average sales per region
avg_sales_per_region = df.groupby('Region')['Sales'].mean()
print("\nAverage Sales per Region:")
print(avg_sales_per_region)

# region with the highest average sale
top_region = avg_sales_per_region.idxmax()
top_avg_sales = avg_sales_per_region.max()
print(f"\nRegion with the highest average sales: {top_region} (₹{top_avg_sales:.2f})")
