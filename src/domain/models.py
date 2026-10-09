"""Core domain entities for Sash with Pydantic validation."""

import uuid
from datetime import datetime
from enum import Enum
from typing import Any

try:
    from pydantic import BaseModel, Field, field_validator

    PYDANTIC_AVAILABLE = True
except ImportError:
    PYDANTIC_AVAILABLE = False
    # Fallback to dataclasses if pydantic not available
    from dataclasses import dataclass, field

    BaseModel = object
    Field = lambda *args, **kwargs: None

from src.domain.clock import now


class ChannelType(str, Enum):
    """Supported communication channels."""

    SMS = "sms"
    WHATSAPP = "whatsapp"
    EMAIL = "email"
    VOICE = "voice"


class EventStatus(str, Enum):
    """Status of a workflow event."""

    PENDING = "pending"
    SENT = "sent"
    DELIVERED = "delivered"
    FAILED = "failed"
    BOUNCED = "bounced"


class WorkflowStatus(str, Enum):
    """Status of a workflow execution."""

    DRAFT = "draft"
    ACTIVE = "active"
    PAUSED = "paused"
    COMPLETED = "completed"
    FAILED = "failed"


class QualificationDecision(str, Enum):
    """Qualification decision for an engagement."""

    PROCEED = "proceed"
    PROCEED_WITH_CONDITIONS = "proceed_with_conditions"
    DECLINE = "decline"


if PYDANTIC_AVAILABLE:

    class Customer(BaseModel):
        """Customer entity representing an end-user in a workflow."""

        id: str = Field(default_factory=lambda: str(uuid.uuid4()))
        phone_number: str
        email: str | None = None
        external_id: str | None = None
        metadata: dict[str, Any] = Field(default_factory=dict)
        correlation_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
        created_at: datetime = Field(default_factory=now)
        updated_at: datetime = Field(default_factory=now)

        @field_validator("phone_number")
        @classmethod
        def validate_phone(cls, v: str) -> str:
            if not v or len(v) < 10:
                raise ValueError("Phone number must be at least 10 digits")
            return v

        class Config:
            use_enum_values = True

    class Workflow(BaseModel):
        """Workflow definition with steps and configuration."""

        id: str = Field(default_factory=lambda: str(uuid.uuid4()))
        name: str
        description: str
        steps: list[dict[str, Any]] = Field(default_factory=list)
        status: WorkflowStatus = WorkflowStatus.DRAFT
        metadata: dict[str, Any] = Field(default_factory=dict)
        correlation_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
        created_at: datetime = Field(default_factory=now)
        updated_at: datetime = Field(default_factory=now)

        def add_step(self, step: dict):
            """Add a step to the workflow."""
            self.steps.append(step)
            self.updated_at = now()

        class Config:
            use_enum_values = True

    class WorkflowExecution(BaseModel):
        """Runtime execution of a workflow for a specific customer."""

        id: str = Field(default_factory=lambda: str(uuid.uuid4()))
        workflow_id: str
        customer_id: str
        status: WorkflowStatus = WorkflowStatus.ACTIVE
        current_step: int = 0
        metadata: dict[str, Any] = Field(default_factory=dict)
        correlation_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
        started_at: datetime = Field(default_factory=now)
        completed_at: datetime | None = None

        def complete(self):
            """Mark execution as completed."""
            self.status = WorkflowStatus.COMPLETED
            self.completed_at = now()

        def fail(self, reason: str):
            """Mark execution as failed."""
            self.status = WorkflowStatus.FAILED
            self.metadata["failure_reason"] = reason
            self.completed_at = now()

        class Config:
            use_enum_values = True

    class Event(BaseModel):
        """Single event in a workflow execution (e.g., message sent)."""

        id: str = Field(default_factory=lambda: str(uuid.uuid4()))
        execution_id: str
        step_index: int
        channel: ChannelType
        status: EventStatus = EventStatus.PENDING
        content: dict[str, Any] = Field(default_factory=dict)
        metadata: dict[str, Any] = Field(default_factory=dict)
        correlation_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
        created_at: datetime = Field(default_factory=now)
        updated_at: datetime = Field(default_factory=now)

        def mark_sent(self):
            """Mark event as sent."""
            self.status = EventStatus.SENT
            self.updated_at = now()

        def mark_delivered(self):
            """Mark event as delivered."""
            self.status = EventStatus.DELIVERED
            self.updated_at = now()

        def mark_failed(self, reason: str):
            """Mark event as failed."""
            self.status = EventStatus.FAILED
            self.metadata["failure_reason"] = reason
            self.updated_at = now()

        class Config:
            use_enum_values = True

    class Engagement(BaseModel):
        """Customer engagement record for qualification and tracking."""

        id: str = Field(default_factory=lambda: str(uuid.uuid4()))
        customer_name: str
        company: str
        use_case: str
        priority: str = "medium"
        status: str = "qualified"
        notes: str = ""
        channels: list[str] = Field(default_factory=list)
        expected_volume: int = 0
        timeline_days: int = 30
        correlation_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
        created_at: datetime = Field(default_factory=now)
        updated_at: datetime = Field(default_factory=now)

        class Config:
            use_enum_values = True

    class AuditRecord(BaseModel):
        """Audit trail record for tracking state changes."""

        id: str = Field(default_factory=lambda: str(uuid.uuid4()))
        entity_type: str
        entity_id: str
        action: str
        old_state: dict[str, Any] | None = None
        new_state: dict[str, Any] | None = None
        actor: str = "system"
        correlation_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
        timestamp: datetime = Field(default_factory=now)

        class Config:
            use_enum_values = True

else:
    # Fallback to dataclasses
    from dataclasses import dataclass, field

    @dataclass
    class Customer:
        id: str = field(default_factory=lambda: str(uuid.uuid4()))
        phone_number: str = ""
        email: str | None = None
        external_id: str | None = None
        metadata: dict[str, Any] = field(default_factory=dict)
        correlation_id: str = field(default_factory=lambda: str(uuid.uuid4()))
        created_at: datetime = field(default_factory=now)
        updated_at: datetime = field(default_factory=now)

    @dataclass
    class Workflow:
        id: str = field(default_factory=lambda: str(uuid.uuid4()))
        name: str = ""
        description: str = ""
        steps: list[dict[str, Any]] = field(default_factory=list)
        status: WorkflowStatus = WorkflowStatus.DRAFT
        metadata: dict[str, Any] = field(default_factory=dict)
        correlation_id: str = field(default_factory=lambda: str(uuid.uuid4()))
        created_at: datetime = field(default_factory=now)
        updated_at: datetime = field(default_factory=now)

        def add_step(self, step: dict):
            self.steps.append(step)
            self.updated_at = now()

    @dataclass
    class WorkflowExecution:
        id: str = field(default_factory=lambda: str(uuid.uuid4()))
        workflow_id: str = ""
        customer_id: str = ""
        status: WorkflowStatus = WorkflowStatus.ACTIVE
        current_step: int = 0
        metadata: dict[str, Any] = field(default_factory=dict)
        correlation_id: str = field(default_factory=lambda: str(uuid.uuid4()))
        started_at: datetime = field(default_factory=now)
        completed_at: datetime | None = None

        def complete(self):
            self.status = WorkflowStatus.COMPLETED
            self.completed_at = now()

        def fail(self, reason: str):
            self.status = WorkflowStatus.FAILED
            self.metadata["failure_reason"] = reason
            self.completed_at = now()

    @dataclass
    class Event:
        id: str = field(default_factory=lambda: str(uuid.uuid4()))
        execution_id: str = ""
        step_index: int = 0
        channel: ChannelType = ChannelType.SMS
        status: EventStatus = EventStatus.PENDING
        content: dict[str, Any] = field(default_factory=dict)
        metadata: dict[str, Any] = field(default_factory=dict)
        correlation_id: str = field(default_factory=lambda: str(uuid.uuid4()))
        created_at: datetime = field(default_factory=now)
        updated_at: datetime = field(default_factory=now)

        def mark_sent(self):
            self.status = EventStatus.SENT
            self.updated_at = now()

        def mark_delivered(self):
            self.status = EventStatus.DELIVERED
            self.updated_at = now()

        def mark_failed(self, reason: str):
            self.status = EventStatus.FAILED
            self.metadata["failure_reason"] = reason
            self.updated_at = now()

    @dataclass
    class Engagement:
        id: str = field(default_factory=lambda: str(uuid.uuid4()))
        customer_name: str = ""
        company: str = ""
        use_case: str = ""
        priority: str = "medium"
        status: str = "qualified"
        notes: str = ""
        channels: list[str] = field(default_factory=list)
        expected_volume: int = 0
        timeline_days: int = 30
        correlation_id: str = field(default_factory=lambda: str(uuid.uuid4()))
        created_at: datetime = field(default_factory=now)
        updated_at: datetime = field(default_factory=now)

    @dataclass
    class AuditRecord:
        id: str = field(default_factory=lambda: str(uuid.uuid4()))
        entity_type: str = ""
        entity_id: str = ""
        action: str = ""
        old_state: dict[str, Any] | None = None
        new_state: dict[str, Any] | None = None
        actor: str = "system"
        correlation_id: str = field(default_factory=lambda: str(uuid.uuid4()))
        timestamp: datetime = field(default_factory=now)
