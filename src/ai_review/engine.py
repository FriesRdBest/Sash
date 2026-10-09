"""AI engineering review: responsible AI-assisted development with deterministic checks."""

import ast
import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any
from uuid import uuid4


class Severity(str, Enum):
    INFO = "info"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class FindingSource(str, Enum):
    DETERMINISTIC = "deterministic"
    AI_ASSISTED = "ai_assisted"


@dataclass
class Finding:
    id: str
    title: str
    description: str
    severity: Severity
    source: FindingSource
    file_path: str
    line: int | None = None
    evidence: str = ""
    remediation: str = ""


@dataclass
class AIUseLogEntry:
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    purpose: str = ""
    model_hint: str = ""
    prompt_snippet: str = ""  # sanitized, no secrets/PII
    artifacts_summary: str = ""  # e.g. "explanation for finding F123"
    sanitized: bool = True


@dataclass
class AIReviewResult:
    run_id: str
    generated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    findings: list[Finding] = field(default_factory=list)
    ai_log: list[AIUseLogEntry] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "run_id": self.run_id,
            "generated_at": self.generated_at.isoformat(),
            "findings": [
                {
                    "id": f.id,
                    "title": f.title,
                    "description": f.description,
                    "severity": f.severity.value,
                    "source": f.source.value,
                    "file_path": f.file_path,
                    "line": f.line,
                    "evidence": f.evidence,
                    "remediation": f.remediation,
                }
                for f in self.findings
            ],
            "ai_log": [
                {
                    "timestamp": e.timestamp.isoformat(),
                    "purpose": e.purpose,
                    "model_hint": e.model_hint,
                    "prompt_snippet": e.prompt_snippet,
                    "artifacts_summary": e.artifacts_summary,
                    "sanitized": e.sanitized,
                }
                for e in self.ai_log
            ],
            "metadata": self.metadata,
        }

    def to_markdown(self) -> str:
        lines = [
            "# AI Engineering Review",
            "",
            f"**Run ID:** `{self.run_id}`",
            f"**Generated:** {self.generated_at.isoformat()}",
            "",
        ]

        if self.findings:
            lines.append("## Findings")
            lines.append("")
            for f in self.findings:
                icon = {
                    "info": "ℹ️",
                    "low": "🟢",
                    "medium": "🟠",
                    "high": "🔴",
                    "critical": "🚫",
                }.get(f.severity.value, "❓")
                loc = f" (line {f.line})" if f.line else ""
                lines.append(
                    f"- {icon} **{f.title}** `{f.id}`{loc}: {f.description} "
                    f"(source: {f.source.value}, severity: {f.severity.value})"
                )
                if f.evidence:
                    lines.append(f"  - Evidence: `{f.evidence}`")
                if f.remediation:
                    lines.append(f"  - Remediation: {f.remediation}")
            lines.append("")

        if self.ai_log:
            lines.append("## AI use log")
            lines.append("")
            for e in self.ai_log:
                lines.append(
                    f"- {e.timestamp.isoformat()} — {e.purpose} "
                    f"(model: {e.model_hint or 'N/A'}, sanitized: {e.sanitized})"
                )
                if e.prompt_snippet:
                    lines.append(f"  - Prompt snippet: {e.prompt_snippet}")
            lines.append("")

        return "\n".join(lines)


def sanitize_code_snippet(code: str) -> str:
    """Return a sanitized code snippet safe for AI prompts (no secrets/PII)."""
    # Very conservative: remove string literals and obvious secrets patterns.
    # This is a demo; in production, use a proper scanner.
    code = re.sub(r'"""[\s\S]*?"""', '"""..."""', code)
    code = re.sub(r"'''[\s\S]*?'''", "'''...'''", code)
    code = re.sub(r'"[^"\n]{8,}"', '"..."', code)
    code = re.sub(r"'[^'\n]{8,}'", "'...'", code)
    code = re.sub(r"(?i)(api_key|secret|password|token)\s*=\s*[^\n]+", r"\1 = REDACTED", code)
    return code


def run_deterministic_checks(file_path: str, source: str) -> list[Finding]:
    """Run deterministic static checks on Python source."""
    findings: list[Finding] = []

    # 1. Secret patterns
    secret_patterns = [
        (r"(?i)(api_key|apikey)\s*=\s*[\'\"]?[A-Za-z0-9]{16,}", "Hard-coded API key"),
        (r"(?i)(secret|password|passwd)\s*=\s*[\'\"]?[A-Za-z0-9]{8,}", "Hard-coded secret/password"),
        (r"(?i)(token|auth_token)\s*=\s*[\'\"]?[A-Za-z0-9._-]{20,}", "Hard-coded token"),
    ]
    for pattern, title in secret_patterns:
        for i, line in enumerate(source.splitlines(), start=1):
            if re.search(pattern, line):
                findings.append(
                    Finding(
                        id=f"SEC_{len(findings)+1:03d}",
                        title=title,
                        description="Potential secret detected in source.",
                        severity=Severity.CRITICAL,
                        source=FindingSource.DETERMINISTIC,
                        file_path=file_path,
                        line=i,
                        evidence=line.strip()[:80],
                        remediation="Move secrets to environment variables or a secret manager.",
                    )
                )

    # 2. Unsafe imports
    unsafe_imports = {"pickle", "marshal", "subprocess"}
    try:
        tree = ast.parse(source)
    except SyntaxError:
        findings.append(
            Finding(
                id="SYN_001",
                title="Syntax error in source",
                description="File does not parse as valid Python.",
                severity=Severity.HIGH,
                source=FindingSource.DETERMINISTIC,
                file_path=file_path,
                line=None,
                evidence="Syntax error",
                remediation="Fix syntax before proceeding.",
            )
        )
        return findings

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name.split(".")[0] in unsafe_imports:
                    findings.append(
                        Finding(
                            id=f"IMP_{len(findings)+1:03d}",
                            title=f"Potentially unsafe import: {alias.name}",
                            description="This module can be dangerous if used with untrusted data.",
                            severity=Severity.MEDIUM,
                            source=FindingSource.DETERMINISTIC,
                            file_path=file_path,
                            line=node.lineno,
                            evidence=f"import {alias.name}",
                            remediation="Ensure strict input validation and least privilege.",
                        )
                    )
        elif isinstance(node, ast.ImportFrom):
            if node.module and node.module.split(".")[0] in unsafe_imports:
                findings.append(
                    Finding(
                        id=f"IMP_{len(findings)+1:03d}",
                        title=f"Potentially unsafe import: from {node.module}",
                        description="This module can be dangerous if used with untrusted data.",
                        severity=Severity.MEDIUM,
                        source=FindingSource.DETERMINISTIC,
                        file_path=file_path,
                        line=node.lineno,
                        evidence=f"from {node.module} import ...",
                        remediation="Ensure strict input validation and least privilege.",
                    )
                )

    # 3. Long functions (demo threshold)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            end_line = node.end_lineno or (node.lineno + 40)
            length = end_line - node.lineno
            if length > 40:
                findings.append(
                    Finding(
                        id=f"LEN_{len(findings)+1:03d}",
                        title=f"Long function: {node.name}",
                        description=f"Function length is {length} lines (threshold 40).",
                        severity=Severity.LOW,
                        source=FindingSource.DETERMINISTIC,
                        file_path=file_path,
                        line=node.lineno,
                        evidence=f"def {node.name}(...)",
                        remediation="Refactor into smaller, testable units.",
                    )
                )

    return findings


def ai_explain_finding(finding: Finding, model_hint: str = "") -> str:
    """
    Optional model-assisted explanation for a finding.

    This function is a placeholder for integration with an LLM.
    It must only receive sanitized code/explanations and must not be used
    to auto-approve or auto-fix code.
    """
    # Demo: no real model call; just a deterministic note.
    return (
        f"AI explanation (placeholder): {finding.title} at {finding.file_path} "
        f"is flagged as {finding.severity.value}. "
        f"Remediation: {finding.remediation}"
    )


def run_ai_review(
    files: list[tuple[str, str]],
    enable_ai_explanations: bool = False,
    model_hint: str = "",
) -> AIReviewResult:
    """
    Run AI engineering review over a list of (file_path, source) pairs.

    Deterministic checks are always authoritative.
    AI explanations are advisory only and logged.
    """
    all_findings: list[Finding] = []
    ai_log: list[AIUseLogEntry] = []

    for file_path, source in files:
        findings = run_deterministic_checks(file_path, source)
        all_findings.extend(findings)

        if enable_ai_explanations:
            for f in findings:
                sanitized_snippet = sanitize_code_snippet(source)
                prompt_snippet = f"Explain this finding: {f.title}\nFile: {file_path}\nCode snippet:\n{sanitized_snippet[:300]}"
                explanation = ai_explain_finding(f, model_hint=model_hint)
                ai_log.append(
                    AIUseLogEntry(
                        purpose=f"Explain finding {f.id}",
                        model_hint=model_hint,
                        prompt_snippet=prompt_snippet[:500],
                        artifacts_summary=f"Explanation for {f.id}",
                        sanitized=True,
                    )
                )

    return AIReviewResult(
        run_id=str(uuid4()),
        findings=all_findings,
        ai_log=ai_log,
        metadata={
            "files_scanned": len(files),
            "enable_ai_explanations": enable_ai_explanations,
            "model_hint": model_hint,
        },
    )
