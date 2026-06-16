from sqlalchemy import create_engine, text
import os

# ----------------------------
# DATABASE CONFIG
# ----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DB_PATH = os.path.join(BASE_DIR, "data", "sales.db")

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    f"sqlite:///{DB_PATH}"
)

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # needed for SQLite
)

# ----------------------------
# CORE QUERY EXECUTOR
# ----------------------------
def run_query(sql: str):
    """
    Executes SQL safely and returns results.
    This is the ONLY function LLM will use to access DB.
    """

    try:
        with engine.connect() as conn:
            result = conn.execute(text(sql))

            # Convert result to list of dicts
            rows = result.fetchall()

            if rows:
                columns = result.keys()
                return [dict(zip(columns, row)) for row in rows]

            return []

    except Exception as e:
        return {"error": str(e)}