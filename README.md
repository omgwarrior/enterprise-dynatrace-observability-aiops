# Enterprise Dynatrace Observability & AIOps — Architecture Portfolio

**Author:** Alvin Cly | Chief Architect / Enterprise Observability / SRE / DevOps  
**Status:** v0.1 educational proof of concept — synthetic data, no live integrations

## Why this project exists

Illustrates the architectural approach to a multi-phase observability transformation after an initial Dynatrace platform deployment. It emphasizes infrastructure and application discovery, collection-pattern decisions, migration waves, SOW governance, validation, and human-approved change controls. It is not a claim of a production Dynatrace implementation.

## Quickstart (Python 3.10+; no dependencies)

```bash
python -m src.migration
python -m unittest discover -s tests -v
```

The assessment prints coverage metrics and creates `reports/migration-assessment.json`.

## Example expected results

For the five synthetic assets: **2 validated, 3 gaps, 40% coverage**. These are synthetic example values, not customer measurements.

## Project layout

- `data/inventory.json` — synthetic mixed-technology inventory
- `src/migration.py` — collector mapping and coverage gap assessment
- `src/approval.py` — simulated human-approval gate
- `tests/` — standard-library unit tests
- `docs/ARCHITECTURE.md` — target architecture, sizing and future roadmap
- `docs/SOW-DELIVERY.md` — delivery phases, acceptance and support boundaries
- `.github/workflows/ci.yml` — automated test workflow
- `SECURITY.md` — public portfolio security constraints

## Demo walkthrough

1. Review source assets and owners in `data/inventory.json`.
2. Run the assessment and inspect the coverage gaps.
3. Review collection-pattern suggestions for Linux, Kubernetes, networks, databases and legacy UNIX.
4. Inspect the approval gate: unapproved changes are blocked, high-risk approved changes require further review.
5. Review SOW acceptance criteria and architecture expansion plan.

## What is and isn't implemented

**Implemented:** local inventory assessment, basic mapping, coverage calculation, approval-gate simulation, automated unit tests.  
**Not implemented:** live Dynatrace API calls, agent deployments, ActiveGate installation, actual ServiceNow changes, LLM/agentic-AI inference, real telemetry ingestion, production validation or throughput benchmarks. These are planned extensions, not current capabilities.

## Official technical references

- [Dynatrace ActiveGate capabilities](https://docs.dynatrace.com/docs/ingest-from/dynatrace-activegate/capabilities)
- [Dynatrace Extensions](https://docs.dynatrace.com/docs/ingest-from/extensions/concepts)
- [Dynatrace OTLP ingestion](https://docs.dynatrace.com/docs/ingest-from/opentelemetry-classic/otlp-api)

## Publish to GitHub

After extracting the zip, from the project folder:

```bash
git init
git add .
git commit -m "Initial enterprise observability architecture demo"
gh auth login
gh repo create omgwarrior/enterprise-dynatrace-observability-aiops --public --source=. --remote=origin --push
```

Requires Git and GitHub CLI, with authorization to publish to `omgwarrior`. Confirm repository name is available before creating. Do not include any private customer materials.
