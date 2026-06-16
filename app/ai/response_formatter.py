def format_response(question, sql, result):
    return {
        "question": question,
        "generated_sql": sql,
        "row_count": len(result) if result else 0,
        "data": result
    }