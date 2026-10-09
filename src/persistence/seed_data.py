"""Seed data loader for reproducible demo data."""

from src.persistence.sqlite_repo import (
    customer_repo, workflow_repo, execution_repo, 
    event_repo, engagement_repo, reset_database
)
from src.domain.models import ChannelType, WorkflowStatus, EventStatus
from src.domain.clock import now


def load_seed_data():
    """Load reproducible seed data into the database."""
    reset_database()
    
    # Seed customers
    customers = [
        {
            "id": "cust_001",
            "phone_number": "+1234567890",
            "email": "alice@example.com",
            "external_id": "EXT-001",
            "metadata": {"segment": "premium"},
            "correlation_id": "corr_001",
            "created_at": now().isoformat(),
            "updated_at": now().isoformat(),
        },
        {
            "id": "cust_002",
            "phone_number": "+0987654321",
            "email": "bob@example.com",
            "external_id": "EXT-002",
            "metadata": {"segment": "standard"},
            "correlation_id": "corr_002",
            "created_at": now().isoformat(),
            "updated_at": now().isoformat(),
        },
    ]
    
    for cust in customers:
        customer_repo.save(cust["id"], cust)
    
    # Seed workflows
    workflows = [
        {
            "id": "wf_001",
            "name": "User Verification",
            "description": "SMS verification with email fallback",
            "steps": [
                {"type": "sms", "template": "Your code is {{code}}"},
                {"type": "email", "template": "Verify: {{code}}", "condition": "sms_failed"},
            ],
            "status": "active",
            "metadata": {"version": "1.0"},
            "correlation_id": "corr_wf_001",
            "created_at": now().isoformat(),
            "updated_at": now().isoformat(),
        },
    ]
    
    for wf in workflows:
        workflow_repo.save(wf["id"], wf)
    
    # Seed engagements
    engagements = [
        {
            "id": "eng_001",
            "customer_name": "Alice Johnson",
            "company": "Acme Corp",
            "use_case": "User verification for marketplace",
            "priority": "high",
            "status": "qualified",
            "notes": "High-volume use case, needs SMS + WhatsApp",
            "channels": ["sms", "whatsapp"],
            "expected_volume": 10000,
            "timeline_days": 14,
            "correlation_id": "corr_eng_001",
            "created_at": now().isoformat(),
            "updated_at": now().isoformat(),
        },
        {
            "id": "eng_002",
            "customer_name": "Bob Smith",
            "company": "StartupXYZ",
            "use_case": "Order notifications",
            "priority": "medium",
            "status": "new",
            "notes": "Small volume, email only",
            "channels": ["email"],
            "expected_volume": 500,
            "timeline_days": 30,
            "correlation_id": "corr_eng_002",
            "created_at": now().isoformat(),
            "updated_at": now().isoformat(),
        },
    ]
    
    for eng in engagements:
        engagement_repo.save(eng["id"], eng)
    
    return {
        "customers": len(customers),
        "workflows": len(workflows),
        "engagements": len(engagements),
    }


if __name__ == "__main__":
    result = load_seed_data()
    print(f"Loaded seed data: {result}")
