# Research and domain model

This directory contains research notes, domain definitions, and architectural decisions that inform the Sash application design.

## Contents

- `sinch_product_surface.md` — Overview of Sinch API capabilities relevant to the flagship scenario
- `workflow_states.md` — State machine for the Aurora Marketplace verification workflow
- `event_model.md` — Normalized communication event schema
- `assumptions_register.md` — Documented assumptions and their validation status
- `provider_capability_matrix.md` — Comparison of SMS, WhatsApp, and email channel characteristics
- `customer_journey.md` — Aurora Marketplace user verification journey map
- `lifecycle_diagram.md` — Event lifecycle from send request to final delivery status

## Purpose

These documents convert the job description and Sinch product surface into an explicit, bounded domain model before implementation begins. This ensures:

- Every workflow state is defined
- Event transitions are documented
- Duplicate and out-of-order events are addressed
- Unsupported assumptions are marked
- Source links are recorded for future reference

## Usage

Reference these documents when:

- Designing new features
- Resolving ambiguities in event handling
- Explaining why certain edge cases are handled a specific way
- Onboarding new contributors to the domain

## Status

Phase 2 in progress. Documents will be populated as research is completed.
