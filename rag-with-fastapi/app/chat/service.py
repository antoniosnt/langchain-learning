from pathlib import Path

from app.chat.repository import ChatRepository
from app.core.llm.ollama_llm import OllamaLLMFactory

APP_ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = APP_ROOT / "core" / "database" / "schemas.sql"


class ChatService:
    def __init__(self):
        self.llm = OllamaLLMFactory()
        self.repository = ChatRepository()

    def create_report(self, question: str) -> dict:
        schema = SCHEMA_PATH.read_text(encoding="utf-8")

        sql = self.llm.generate_sql(question=question, schema=schema)

        rows = self.repository.fetch_report_data(sql=sql)

        message = self.llm.generate_report_message(question=question, rows=rows)

        return {"message": message, "data": rows}
