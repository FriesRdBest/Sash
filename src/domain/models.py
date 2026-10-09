"""Core domain entities for Sash."""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional
import uuid


class ChannelType(Enum):
    """Supported communication channels."""
    SMS = "sms"
    WHATSAPP = "whatsapp"
    EMAIL = "email"
    VOICE = "voice"


class EventStatus(Enum):
    """Status of a workflow event."""
    PENDING = "pending"
    SENT = "sent"
    DELIVERED = "delivered"
    FAILED = "failed"
    BOUNCED = "bounced"


class WorkflowStatus(Enum):
    """Status of a workflow execution."""
    DRAFT = "draft"
    ACTIVE = "active"
    PAUSED = "paused"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass
class Customer:
    """Customer entity representing an end-user in a workflow."""
    phone_number: str
    email: Optional[str] = None
    external_id: Optional[str] = None
    metadata: dict = field(default_factory=dict)
    
    def __post_init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()


@dataclass
class Workflow:
    """Workflow definition with steps and configuration."""
    name: str
    description: str
    steps: list = field(default_factory=list)
    status: WorkflowStatus = WorkflowStatus.DRAFT
    metadata: dict = field(default_factory=dict)
    
    def __post_init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
    
    def add_step(self, step: dict):
        """Add a step to the workflow."""
        self.steps.append(step)
        self.updated_at = datetime.utcnow()


@dataclass
class WorkflowExecution:
    """Runtime execution of a workflow for a specific customer."""
    workflow_id: str
    customer_id: str
    status: WorkflowStatus = WorkflowStatus.ACTIVE
    current_step: int = 0
    metadata: dict = field(default_factory=dict)
    
    def __post_init__(self):
        self.id = str(uuid.uuid4())
        self.started_at = datetime.utcnow()
        self.completed_at: Optional[datetime] = None
    
    def complete(self):
        """Mark execution as completed."""
        self.status = WorkflowStatus.COMPLETED
        self.completed_at = datetime.utcnow()
    
    def fail(self, reason: str):
        """Mark execution as failed."""
        self.status = WorkflowStatus.FAILED
        self.metadata["failure_reason"] = reason
        self.completed_at = datetime.utcnow()


@dataclass
class Event:
    """Single event in a workflow execution (e.g., message sent)."""
    execution_id: str
    step_index: int
    channel: ChannelType
    status: EventStatus = EventStatus.PENDING
    content: dict = field(default_factory=dict)
    metadata: dict = field(default_factory=dict)
    
    def __post_init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
    
    def mark_sent(self):
        """Mark event as sent."""
        self.status = EventStatus.SENT
        self.updated_at = datetime.utcnow()
    
    def mark_delivered(self):
        """Mark event as delivered."""
        self.status = EventStatus.DELIVERED
        self.updated_at = datetime.utcnow()
    
    def mark_failed(self, reason: str):
        """Mark event as failed."""
        self.status = EventStatus.FAILED
        self.metadata["failure_reason"] = reason
        self.updated_at = datetime.utcnow()


@dataclass
class Engagement:
    """Customer engagement record for qualification and tracking."""
    customer_name: str
    company: str
    use_case: str
    priority: str = "medium"  # low, medium, high, critical
    status: str = "qualified"  # new, qualified, active, completed, archived
    notes: str = ""
    
    def __post_init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
