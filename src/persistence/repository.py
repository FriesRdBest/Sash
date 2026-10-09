"""In-memory persistence for demo purposes."""

import json
from datetime import datetime
from typing import Generic, TypeVar

T = TypeVar("T")


class InMemoryRepository(Generic[T]):
    """Generic in-memory repository for demo persistence."""

    def __init__(self):
        self._store: dict[str, T] = {}

    def save(self, entity: T) -> str:
        """Save an entity and return its ID."""
        entity_id = getattr(entity, "id", str(len(self._store)))
        self._store[entity_id] = entity
        return entity_id

    def get(self, entity_id: str) -> T | None:
        """Get an entity by ID."""
        return self._store.get(entity_id)

    def get_all(self) -> list[T]:
        """Get all entities."""
        return list(self._store.values())

    def delete(self, entity_id: str) -> bool:
        """Delete an entity by ID."""
        if entity_id in self._store:
            del self._store[entity_id]
            return True
        return False

    def count(self) -> int:
        """Get count of entities."""
        return len(self._store)

    def clear(self):
        """Clear all entities."""
        self._store.clear()

    def find_by(self, **kwargs) -> list[T]:
        """Find entities by attribute values."""
        results = []
        for entity in self._store.values():
            match = True
            for key, value in kwargs.items():
                if not hasattr(entity, key) or getattr(entity, key) != value:
                    match = False
                    break
            if match:
                results.append(entity)
        return results


class JsonSerializer:
    """Serialize entities to/from JSON for export."""

    @staticmethod
    def serialize(entity) -> dict:
        """Serialize an entity to a dictionary."""
        result = {}
        for key, value in entity.__dict__.items():
            if isinstance(value, datetime):
                result[key] = value.isoformat()
            elif hasattr(value, "value"):  # Enum
                result[key] = value.value
            elif isinstance(value, dict):
                result[key] = value
            else:
                result[key] = str(value)
        return result

    @staticmethod
    def to_json(entity) -> str:
        """Serialize an entity to JSON string."""
        return json.dumps(JsonSerializer.serialize(entity), indent=2)


# Singleton repositories for demo
from src.domain.models import Customer, Engagement, Event, Workflow, WorkflowExecution

customer_repo = InMemoryRepository[Customer]()
workflow_repo = InMemoryRepository[Workflow]()
execution_repo = InMemoryRepository[WorkflowExecution]()
event_repo = InMemoryRepository[Event]()
engagement_repo = InMemoryRepository[Engagement]()


def get_all_repos():
    """Return all repositories for inspection."""
    return {
        "customers": customer_repo,
        "workflows": workflow_repo,
        "executions": execution_repo,
        "events": event_repo,
        "engagements": engagement_repo,
    }
