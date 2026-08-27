import pandas as pd
import sqlalchemy as sa


# Connecting to the lesson database

engine = sa.create_engine(
    "sqlite:///../db/lesson.db"
)

# Reading joined data into a DataFrame

query = """
    SELECT
        line_items.line_item_id,
        line_items.quantity,
        line_items.product_id,
        products.product_name,
        products.price
    FROM line_items
    JOIN products
        ON line_items.product_id = products.product_id;
"""

df = pd.read_sql(query, engine)


print("First 5 rows from the database:")
print(df.head())


# Adding total price column

df["total"] = df["quantity"] * df["price"]


print("\nFirst 5 rows with total:")
print(df.head())


# Grouping by product_id and aggregate

order_summary = (
    df.groupby("product_id")
    .agg({
        "line_item_id": "count",
        "total": "sum",
        "product_name": "first"
    })
    .reset_index()
)


print("\nGrouped product summary:")
print(order_summary.head())


# Sorting by product name

order_summary = order_summary.sort_values(
    by="product_name"
)


# Writing summary to CSV

order_summary.to_csv(
    "order_summary.csv",
    index=False
)


print("\norder_summary.csv created successfully.")