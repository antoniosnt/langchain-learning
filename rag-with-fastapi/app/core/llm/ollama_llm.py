import json

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

SQL_TEMPLATE = """
Generate one read-only PostgreSQL SELECT query for the user's request.
Use only the tables and columns in the supplied schema. Do not include a
Markdown code fence or explanatory text. Limit the result to at most 100 rows.

Schema:
{schema}

User request:
{question}
"""

REPORT_TEMPLATE = """
Write a brief, clear, respectful message introducing the report results.
Use only facts in the supplied results. Do not invent values or claim results
that are not present. If there are no rows, say that no matching records were
found. Do not include JSON or Markdown tables; the application returns the data
separately.

User request:
{question}

Report results:
{data}
"""


class OllamaLLMFactory:
    def __init__(self):
        self.model = ChatOllama(model="qwen2.5", temperature=0)
        self.sql_prompt = ChatPromptTemplate.from_template(SQL_TEMPLATE)
        self.report_prompt = ChatPromptTemplate.from_template(REPORT_TEMPLATE)
        self.sql_chain = self.sql_prompt | self.model | StrOutputParser()
        self.report_chain = self.report_prompt | self.model | StrOutputParser()

    def generate_sql(self, question: str, schema: str) -> str:
        return self.sql_chain.invoke({"question": question, "schema": schema})

    def generate_report_message(self, question: str, rows: list[dict]) -> str:
        return self.report_chain.invoke(
            {
                "question": question,
                "data": json.dumps(rows, default=str, ensure_ascii=False),
            }
        )
