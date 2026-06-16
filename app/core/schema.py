from sqlalchemy import Table, Column, Integer, String, Float, ForeignKey, MetaData, Boolean, Date

metadata = MetaData()

# -----------------------
# CUSTOMERS
# -----------------------
customers = Table(
    "customers",
    metadata,
    Column("customer_id", Integer, primary_key=True),
    Column("name", String),
    Column("email", String),
    Column("region", String),
)

# -----------------------
# PRODUCTS
# -----------------------
products = Table(
    "products",
    metadata,
    Column("product_id", Integer, primary_key=True),
    Column("product_name", String),
    Column("category", String),
    Column("price", Float),
)

# -----------------------
# ORDERS (FACT TABLE)
# -----------------------
orders = Table(
    "orders",
    metadata,
    Column("order_id", Integer, primary_key=True),
    Column("customer_id", Integer, ForeignKey("customers.customer_id")),
    Column("order_date", String),
    Column("total_amount", Float),
)

# -----------------------
# ORDER ITEMS
# -----------------------
order_items = Table(
    "order_items",
    metadata,
    Column("order_item_id", Integer, primary_key=True),
    Column("order_id", Integer, ForeignKey("orders.order_id")),
    Column("product_id", Integer, ForeignKey("products.product_id")),
    Column("quantity", Integer),
    Column("subtotal", Float),
)

# -----------------------
# PRODUCT ENRICHMENT (EXTERNAL DATA LAYER)
# -----------------------
product_enrichment = Table(
    "product_enrichment",
    metadata,
    Column("product_id", Integer, ForeignKey("products.product_id")),
    Column("similar_products", String),
    Column("market_trend", String),
    Column("demand_score", Integer),
)

# -----------------------
# SALES ENRICHED VIEW (LOGICAL LAYER)
# -----------------------
sales_enriched = Table(
    "sales_enriched",
    metadata,
    Column("order_id", Integer),
    Column("date", String),
    Column("sales", Float),
    Column("region", String),
    Column("temp_max", Float),
    Column("precipitation", Float),
    Column("is_holiday", Boolean),
    Column("holiday_name", String),
    Column("is_weekend", Boolean),
    Column("day_of_week", Integer),
)