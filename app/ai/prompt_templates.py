SCHEMA_CONTEXT = """
You are a senior data analyst writing SQL for a SQLite database.

DATABASE SCHEMA:

customers(customer_id, name, region)
products(product_id, product_name, category, price)
orders(order_id, customer_id, order_date, total_amount)
order_items(order_item_id, order_id, product_id, quantity, subtotal)

RULES:
- Only write valid SQLite SQL
- Always use correct table joins
- Do not hallucinate tables or columns
- Return ONLY SQL, no explanation
"""


def build_prompt(question: str) -> str:
    return f"""
{SCHEMA_CONTEXT}

User Question:
{question}

Return only SQL query:
"""