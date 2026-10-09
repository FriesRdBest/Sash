"""Workflow designer: configuration, validation, versioning, JSON export/import."""

import json
import uuid
from datetime import datetime, timezone
from typing import Any

from pydantic import BaseModel, Field, field_validator

SUPPORTED_CHANNELS = {"sms", "whatsapp", "email", "voice"}


class RetryPolicy(BaseModel):
    """Retry configuration for a workflow step."""

    max_attempts: int = Field(default=3, ge=1, le=10)
    backoff_seconds: list[int] = Field(default_factory=lambda: [5, 30, 120])

    @field_validator("backoff_seconds")
    @classmethod
    def validate_backoff(cls, v: list[int]) -> list[int]:
        if len(v) == 0:
            raise ValueError("backoff_seconds must have at least one value")
        if any(x < 0 for x in v):
            raise ValueError("backoff_seconds values must be non-negative")
        return v


class WorkflowStep(BaseModel):
    """A single step in a communication workflow."""

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    channel: str
    template: str
    timeout_seconds: int = Field(default=90, ge=1)
    retry_policy: RetryPolicy = Field(default_factory=RetryPolicy)
    fallback_to: str | None = None  # id of fallback step

    @field_validator("channel")
    @classmethod
    def validate_channel(cls, v: str) -> str:
        if v not in SUPPORTED_CHANNELS:
            raise ValueError(f"Unsupported channel: {v}")
        return v


class WorkflowConfig(BaseModel):
    """Complete workflow configuration."""

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    description: str = ""
    version: int = Field(default=1, ge=1)
    owner: str = ""
    consent_required: bool = True
    steps: list[WorkflowStep] = Field(default_factory=list)
    created_at: str = Field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    updated_at: str = Field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    @field_validator("steps")
    @classmethod
    def validate_steps(cls, v: list[WorkflowStep]) -> list[WorkflowStep]:
        if len(v) == 0:
            raise ValueError("Workflow must have at least one step")
        step_ids = {step.id for step in v}
        for step in v:
            if step.fallback_to and step.fallback_to not in step_ids:
                raise ValueError(f"Fallback target {step.fallback_to} not found in steps")
        return v

    def bump_version(self):
        """Increment version and update timestamp."""
        self.version += 1
        self.updated_at = datetime.now(timezone.utc).isoformat()

    def to_json(self, indent: int = 2) -> str:
        """Export workflow as JSON."""
        return self.model_dump_json(indent=indent)

    @classmethod
    def from_json(cls, json_str: str) -> "WorkflowConfig":
        """Import workflow from JSON."""
        data = json.loads(json_str)
        return cls(**data)


class WorkflowValidationError(Exception):
    """Raised when workflow validation fails."""

    pass


def validate_workflow(config: WorkflowConfig) -> list[str]:
    """Validate workflow and return list of error messages."""
    errors = []

    if not config.name or len(config.name) < 3:
        errors.append("Workflow name must be at least 3 characters")

    if len(config.steps) == 0:
        errors.append("Workflow must have at least one step")

    channel_set = {step.channel for step in config.steps}
    if "sms" not in channel_set and "email" not in channel_set:
        errors.append("Workflow must include SMS or Email as a channel")

    for i, step in enumerate(config.steps):
        if not step.template or len(step.template) < 5:
            errors.append(f"Step {i + 1} template must be at least 5 characters")
        if step.timeout_seconds > 300:
            errors.append(f"Step {i + 1} timeout exceeds 300 seconds")

    return errors


def create_sample_workflow() -> WorkflowConfig:
    """Create a sample Aurora Marketplace verification workflow."""
    step1 = WorkflowStep(
        name="Send SMS verification",
        channel="sms",
        template="Your verification code is {{code}}. Valid for 10 minutes.",
        timeout_seconds=90,
    )
    step2 = WorkflowStep(
        name="Fallback to email",
        channel="email",
        template="Verify your account: {{code}}",
        timeout_seconds=120,
        fallback_to=None,
    )
    step1.fallback_to = step2.id

    return WorkflowConfig(
        name="Aurora Marketplace Verification",
        description="Resilient account verification with SMS primary and email fallback",
        owner="Sash Demo",
        consent_required=True,
        steps=[step1, step2],
        version=1,
    )
