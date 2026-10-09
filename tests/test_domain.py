"""Unit tests for domain models and transitions."""

import pytest
from datetime import datetime

from src.domain.models import (
    Customer, Workflow, WorkflowExecution, Event, Engagement,
    ChannelType, WorkflowStatus, EventStatus
)
from src.domain.clock import SystemClock, DeterministicClock, now


class TestCustomer:
    """Tests for Customer entity."""
    
    def test_create_customer(self):
        customer = Customer(
            phone_number="+1234567890",
            email="test@example.com"
        )
        
        assert customer.phone_number == "+1234567890"
        assert customer.email == "test@example.com"
        assert customer.id is not None
        assert isinstance(customer.created_at, datetime)
    
    def test_customer_has_correlation_id(self):
        customer = Customer(phone_number="+1234567890")
        assert customer.correlation_id is not None
        assert len(customer.correlation_id) > 0


class TestWorkflow:
    """Tests for Workflow entity."""
    
    def test_create_workflow(self):
        workflow = Workflow(
            name="Test Workflow",
            description="A test workflow"
        )
        
        assert workflow.name == "Test Workflow"
        assert workflow.status == WorkflowStatus.DRAFT
        assert len(workflow.steps) == 0
    
    def test_add_step(self):
        workflow = Workflow(name="Test", description="Test")
        workflow.add_step({"type": "sms", "template": "Hello"})
        
        assert len(workflow.steps) == 1
        assert workflow.steps[0]["type"] == "sms"
    
    def test_add_step_updates_timestamp(self):
        clock = DeterministicClock(datetime(2024, 1, 1, 12, 0, 0))
        workflow = Workflow(name="Test", description="Test")
        original_updated = workflow.updated_at
        
        workflow.add_step({"type": "sms"})
        
        assert workflow.updated_at >= original_updated


class TestWorkflowExecution:
    """Tests for WorkflowExecution entity."""
    
    def test_create_execution(self):
        execution = WorkflowExecution(
            workflow_id="wf_001",
            customer_id="cust_001"
        )
        
        assert execution.workflow_id == "wf_001"
        assert execution.customer_id == "cust_001"
        assert execution.status == WorkflowStatus.ACTIVE
        assert execution.current_step == 0
    
    def test_complete_execution(self):
        execution = WorkflowExecution(workflow_id="wf_001", customer_id="cust_001")
        execution.complete()
        
        assert execution.status == WorkflowStatus.COMPLETED
        assert execution.completed_at is not None
    
    def test_fail_execution(self):
        execution = WorkflowExecution(workflow_id="wf_001", customer_id="cust_001")
        execution.fail("Test failure")
        
        assert execution.status == WorkflowStatus.FAILED
        assert execution.metadata["failure_reason"] == "Test failure"


class TestEvent:
    """Tests for Event entity."""
    
    def test_create_event(self):
        event = Event(
            execution_id="exec_001",
            step_index=0,
            channel=ChannelType.SMS
        )
        
        assert event.execution_id == "exec_001"
        assert event.step_index == 0
        assert event.channel == ChannelType.SMS
        assert event.status == EventStatus.PENDING
    
    def test_mark_sent(self):
        event = Event(execution_id="exec_001", step_index=0, channel=ChannelType.SMS)
        event.mark_sent()
        
        assert event.status == EventStatus.SENT
    
    def test_mark_delivered(self):
        event = Event(execution_id="exec_001", step_index=0, channel=ChannelType.SMS)
        event.mark_delivered()
        
        assert event.status == EventStatus.DELIVERED
    
    def test_mark_failed(self):
        event = Event(execution_id="exec_001", step_index=0, channel=ChannelType.SMS)
        event.mark_failed("Delivery failed")
        
        assert event.status == EventStatus.FAILED
        assert event.metadata["failure_reason"] == "Delivery failed"


class TestDeterministicClock:
    """Tests for deterministic clock."""
    
    def test_fixed_time(self):
        fixed_time = datetime(2024, 1, 1, 12, 0, 0)
        clock = DeterministicClock(fixed_time)
        
        assert clock.now() == fixed_time
    
    def test_advance_time(self):
        clock = DeterministicClock(datetime(2024, 1, 1, 12, 0, 0))
        clock.advance(3600)  # 1 hour
        
        assert clock.now() == datetime(2024, 1, 1, 13, 0, 0)
