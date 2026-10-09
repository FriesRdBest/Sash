"""Unit tests for the AI engineering review module."""

from src.ai_review.engine import (
    FindingSource,
    Severity,
    run_ai_review,
    run_deterministic_checks,
    sanitize_code_snippet,
)


def test_secret_detection():
    source = """
api_key = "sk_live_1234567890abcdef"
def foo():
    pass
"""
    findings = run_deterministic_checks("test.py", source)
    assert any("API key" in f.title for f in findings)
    assert any(f.severity == Severity.CRITICAL for f in findings)


def test_unsafe_import_detection():
    source = """
import pickle

def load(data):
    return pickle.loads(data)
"""
    findings = run_deterministic_checks("test.py", source)
    assert any("pickle" in f.title for f in findings)
    assert any(f.severity == Severity.MEDIUM for f in findings)


def test_long_function_detection():
    lines = ["def long():"] + ["    pass"] * 50
    source = "\n".join(lines)
    findings = run_deterministic_checks("test.py", source)
    assert any("Long function" in f.title for f in findings)


def test_sanitize_removes_secrets():
    source = 'API_KEY = "sk_live_1234567890abcdef"'
    sanitized = sanitize_code_snippet(source)
    assert "sk_live" not in sanitized
    assert "API_KEY" in sanitized


def test_ai_review_aggregates_findings():
    files = [
        (
            "a.py",
            """
import subprocess
SECRET = "verysecretvalue123"
""",
        ),
        (
            "b.py",
            """
def ok():
    return 1
""",
        ),
    ]
    result = run_ai_review(files, enable_ai_explanations=False)
    assert len(result.findings) >= 2
    assert all(f.source == FindingSource.DETERMINISTIC for f in result.findings)
    assert result.metadata["enable_ai_explanations"] is False


def test_ai_log_entries_are_sanitized():
    files = [
        (
            "c.py",
            """
TOKEN = "ghp_xxxxxxxxxxxxxxxxxxxx"
""",
        ),
    ]
    result = run_ai_review(files, enable_ai_explanations=True, model_hint="demo-model")
    assert len(result.ai_log) > 0
    for entry in result.ai_log:
        assert entry.sanitized is True
        assert "ghp_" not in entry.prompt_snippet
