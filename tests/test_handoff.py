"""Unit tests for the handoff package generator."""

import pytest

from src.handoff.generator import generate_handoff_package


@pytest.fixture
def handoff():
    return generate_handoff_package()


def test_package_has_all_sections(handoff):
    assert handoff.architecture_md
    assert handoff.workflow_definition
    assert handoff.configuration_guide_md
    assert handoff.deployment_instructions_md
    assert handoff.runbook_md
    assert handoff.test_evidence_md
    assert handoff.alert_guide_md
    assert handoff.ownership_matrix_md
    assert handoff.rollback_plan_md
    assert handoff.training_checklist_md
    assert handoff.open_risk_register_md


def test_workflow_definition_is_structured(handoff):
    wf = handoff.workflow_definition
    assert "name" in wf
    assert "steps" in wf
    assert isinstance(wf["steps"], list)
    assert len(wf["steps"]) > 0


def test_ownership_matrix_has_table(handoff):
    assert "|" in handoff.ownership_matrix_md
    assert "Owner" in handoff.ownership_matrix_md


def test_rollback_plan_has_steps(handoff):
    assert (
        "Steps" in handoff.rollback_plan_md
        or "step" in handoff.rollback_plan_md.lower()
    )


def test_metadata_is_present(handoff):
    assert handoff.metadata["version"]
    assert handoff.metadata["phase"]
    assert handoff.metadata["project"]
