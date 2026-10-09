"""SQLite persistence layer for Sash."""

import json
import os
import sqlite3
import tempfile
from datetime import datetime, timezone
from typing import Any, Generic, TypeVar

T = TypeVar("T")

# Use temp directory for SQLite database (writable in all environments)
_db_path = os.path.join(tempfile.gettempdir(), "sash.db")


class SQLiteRepository(Generic[T]):
    """SQLite-backed repository for persistent storage."""

    def __init__(self, table_name: str, db_path: str | None = None):
        self.table_name = table_name
        self.db_path = db_path or _db_path
        self._init_table()

    def _get_connection(self) -> sqlite3.Connection:
        """Get a database connection."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_table(self):
        """Initialize the table if it doesn't exist."""
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                id TEXT PRIMARY KEY,
                data TEXT NOT NULL,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
        """
        )
        conn.commit()
        conn.close()

    def save(self, entity_id: str, entity_data: dict[str, Any]) -> str:
        """Save an entity and return its ID."""
        conn = self._get_connection()
        cursor = conn.cursor()

        now = datetime.now(timezone.utc).isoformat()
        cursor.execute(
            f"""
            INSERT OR REPLACE INTO {self.table_name} (id, data, created_at, updated_at)
            VALUES (?, ?, ?, ?)
        """,
            (entity_id, json.dumps(entity_data), now, now),
        )

        conn.commit()
        conn.close()
        return entity_id

    def get(self, entity_id: str) -> dict[str, Any] | None:
        """Get an entity by ID."""
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(f"SELECT data FROM {self.table_name} WHERE id = ?", (entity_id,))
        row = cursor.fetchone()
        conn.close()

        if row:
            return json.loads(row["data"])
        return None

    def get_all(self) -> list[dict[str, Any]]:
        """Get all entities."""
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(f"SELECT data FROM {self.table_name}")
        rows = cursor.fetchall()
        conn.close()

        return [json.loads(row["data"]) for row in rows]

    def delete(self, entity_id: str) -> bool:
        """Delete an entity by ID."""
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {self.table_name} WHERE id = ?", (entity_id,))
        deleted = cursor.rowcount > 0
        conn.commit()
        conn.close()
        return deleted

    def count(self) -> int:
        """Get count of entities."""
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM {self.table_name}")
        count = cursor.fetchone()[0]
        conn.close()
        return count

    def clear(self):
        """Clear all entities."""
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {self.table_name}")
        conn.commit()
        conn.close()

    def find_by(self, **kwargs) -> list[dict[str, Any]]:
        """Find entities by attribute values."""
        all_entities = self.get_all()
        results = []

        for entity in all_entities:
            match = True
            for key, value in kwargs.items():
                if key not in entity or entity[key] != value:
                    match = False
                    break
            if match:
                results.append(entity)

        return results


class AuditRepository:
    """Specialized repository for audit records."""

    def __init__(self, db_path: str | None = None):
        self.db_path = db_path or _db_path
        self._init_table()

    def _get_connection(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_table(self):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS audit_log (
                id TEXT PRIMARY KEY,
                entity_type TEXT NOT NULL,
                entity_id TEXT NOT NULL,
                action TEXT NOT NULL,
                old_state TEXT,
                new_state TEXT,
                actor TEXT NOT NULL,
                correlation_id TEXT NOT NULL,
                timestamp TEXT NOT NULL
            )
        """
        )
        conn.commit()
        conn.close()

    def record(self, audit_data: dict[str, Any]) -> str:
        """Record an audit entry."""
        conn = self._get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO audit_log (id, entity_type, entity_id, action, old_state, new_state, actor, correlation_id, timestamp)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (
                audit_data.get("id"),
                audit_data.get("entity_type"),
                audit_data.get("entity_id"),
                audit_data.get("action"),
                (
                    json.dumps(audit_data.get("old_state"))
                    if audit_data.get("old_state")
                    else None
                ),
                (
                    json.dumps(audit_data.get("new_state"))
                    if audit_data.get("new_state")
                    else None
                ),
                audit_data.get("actor", "system"),
                audit_data.get("correlation_id"),
                audit_data.get("timestamp", datetime.now(timezone.utc).isoformat()),
            ),
        )

        conn.commit()
        conn.close()
        return audit_data["id"]

    def get_by_correlation(self, correlation_id: str) -> list[dict[str, Any]]:
        """Get all audit records for a correlation ID."""
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM audit_log WHERE correlation_id = ? ORDER BY timestamp",
            (correlation_id,),
        )
        rows = cursor.fetchall()
        conn.close()

        return [dict(row) for row in rows]

    def get_all(self) -> list[dict[str, Any]]:
        """Get all audit records."""
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM audit_log ORDER BY timestamp DESC")
        rows = cursor.fetchall()
        conn.close()

        return [dict(row) for row in rows]


# Singleton repositories
customer_repo = SQLiteRepository("customer")
workflow_repo = SQLiteRepository("workflow")
execution_repo = SQLiteRepository("execution")
event_repo = SQLiteRepository("event")
engagement_repo = SQLiteRepository("engagement")
audit_repo = AuditRepository()


def get_all_repos():
    """Return all repositories for inspection."""
    return {
        "customers": customer_repo,
        "workflows": workflow_repo,
        "executions": execution_repo,
        "events": event_repo,
        "engagements": engagement_repo,
        "audit": audit_repo,
    }


def reset_database():
    """Clear all data (for demo reset)."""
    customer_repo.clear()
    workflow_repo.clear()
    execution_repo.clear()
    event_repo.clear()
    engagement_repo.clear()
