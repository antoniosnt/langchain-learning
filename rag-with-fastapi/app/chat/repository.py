import re
from typing import Any

from app.core.database.connection import connection


class ChatRepository:
    def fetch_report_data(self, sql: str, limit: int = 100) -> list[dict[str, Any]]:
        query = sql.strip().rstrip(";").strip()
        if not re.match(r"(?is)^(select|with)\b", query) or ";" in query:
            raise ValueError("The generated query must be a single SELECT statement.")

        with connection() as db:
            # The report connection also should use a PostgreSQL role with
            # SELECT permission only for the tables used by reports.
            db.execute("SET TRANSACTION READ ONLY")
            db.execute("SET LOCAL statement_timeout = '10s'")
            cursor = db.execute(query)
            rows = cursor.fetchmany(limit + 1)
            return [dict(row) for row in rows[:limit]]
