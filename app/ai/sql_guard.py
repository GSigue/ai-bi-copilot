def is_safe_sql(sql: str) -> bool:
    blocked = ["DROP", "DELETE", "UPDATE", "INSERT", "ALTER"]

    upper_sql = sql.upper()

    for word in blocked:
        if word in upper_sql:
            return False

    return True