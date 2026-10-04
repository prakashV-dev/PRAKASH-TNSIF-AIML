import pandas as pd

data = {
    "Product Name": ["Laptop","Mouse","Keyboard","Monitor","Headphones","Webcam",],
    "Category": ["Electronics","Accessories","Accessories","Electronics","Accessories","Accessories",],
    "Price": [1000, 25, 50, 300, 80, 60],
    "Quantity Sold": [15, 120, 85, 40, 65, 30],
}

df = pd.DataFrame(data)

df["Total Sales"] = df["Price"] * df["Quantity Sold"]
print("--- Full Dataset with Total Sales ---")
print(df)

highest_sales = df.loc[df["Total Sales"].idxmax()]
print("\n--- Product with Highest Sales ---")
print(f"{highest_sales['Product Name']} (${highest_sales['Total Sales']:,})")

avg_price = df["Price"].mean()
print(f"\nAverage Product Price: ${avg_price:.2f}")

print("\n--- Products with Quantity Sold > 50 ---")
print(df[df["Quantity Sold"] > 50])

print("\n--- Products Sorted by Total Sales ---")
print(df.sort_values(by="Total Sales", ascending=False))
