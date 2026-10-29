#matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy. It provides an object-oriented API for embedding plots into applications using general-purpose GUI toolkits like Tkinter, wxPython, Qt, or GTK.    
# import matplotlib.pyplot as plt
# fig, ax = plt.subplots(figsize=(6, 3))
# ax.plot([1, 2, 3, 4], [1, 4, 2, 3],marker='o')
# ax.set_title('Simple Plot')
# ax.set_xlabel('Weekly Data')
# ax.set_ylabel('Units')
# ax.grid(True,alpha=0.3)
# fig.tight_layout()
# plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# 1. Create sample sales dataset
data = {
    "Product": [
        "Laptop", "Mobile", "Headphones", "Laptop",
        "Mobile", "Tablet", "Headphones", "Tablet",
        "Laptop", "Mobile"
    ],
    "Month": [
        "Jan", "Jan", "Jan", "Feb", "Feb",
        "Feb", "Mar", "Mar", "Mar", "Mar"
    ],
    "Sales": [
        50000, 20000, 5000, 60000, 25000,
        15000, 7000, 18000, 55000, 30000
    ],
    "Quantity": [2, 4, 5, 2, 5, 3, 7, 4, 2, 6]
}

df = pd.DataFrame(data)

# 2. Display dataset
print("SALES DATA")
print(df)

# 3. Basic analytics
print("\nTotal Revenue:", df["Sales"].sum())
print("Total Quantity Sold:", df["Quantity"].sum())
print("Average Sale:", df["Sales"].mean())

# 4. Revenue by product
product_sales = df.groupby("Product")["Sales"].sum()
print("\nRevenue by Product:")
print(product_sales)

# 5. Monthly revenue
monthly_sales = (
    df.groupby("Month")["Sales"]
    .sum()
    .reindex(["Jan", "Feb", "Mar"])
)

print("\nMonthly Revenue:")
print(monthly_sales)

# 6. Create dashboard with 4 charts
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Bar chart
product_sales.plot(
    kind="bar", ax=axes[0, 0], color="skyblue"
)
axes[0, 0].set_title("Revenue by Product")
axes[0, 0].set_ylabel("Revenue")
axes[0, 0].tick_params(axis="x", rotation=30)

# Line chart
monthly_sales.plot(
    kind="line", marker="o", ax=axes[0, 1],
    color="green"
)
axes[0, 1].set_title("Monthly Revenue Trend")
axes[0, 1].set_ylabel("Revenue")
axes[0, 1].grid(True)

# Pie chart
product_sales.plot(
    kind="pie", autopct="%1.1f%%",
    ax=axes[1, 0]
)
axes[1, 0].set_title("Revenue Share by Product")
axes[1, 0].set_ylabel("")

# Histogram
df["Sales"].plot(
    kind="hist", bins=5, ax=axes[1, 1],
    color="orange", edgecolor="black"
)
axes[1, 1].set_title("Sales Distribution")
axes[1, 1].set_xlabel("Sales Amount")

plt.suptitle("Sales Data Analytics Dashboard",
             fontsize=16)
plt.tight_layout()
plt.savefig("sales_dashboard.png", dpi=300)
plt.show()