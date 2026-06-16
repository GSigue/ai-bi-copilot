from app.ai.response_formatter import format_response
from openai import OpenAI
from app.ai.sql_guard import is_safe_sql
from app.ai.prompt_templates import build_prompt
from app.core.db import run_query
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

sql = generate_sql_llm(question)

if not is_safe_sql(sql):
    return {
        "error": "Unsafe SQL detected",
        "sql": sql
    }


def generate_sql_llm(question: str) -> str:
    prompt = build_prompt(question)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a SQL expert."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    sql = response.choices[0].message.content.strip()

    return sql


    }
    
 def ask_ai(question: str):
    sql = generate_sql_llm(question)
    result = run_query(sql)

    return format_response(question, sql, result)