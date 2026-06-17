mlflow.log_param("question", question)
mlflow.log_param("sql", sql)
mlflow.log_metric("row_count", len(result))