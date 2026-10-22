# Reference architecture

Synthetic sources (Zabbix, Prometheus, SNMP, Splunk, AppDynamics) -> discovery and mapping -> appropriate Dynatrace collection pattern (OneAgent, ActiveGate extension, Dynatrace Operator, OTLP) -> telemetry validation -> service ownership and operational acceptance.

This repo currently implements **inventory assessment only**. Collector names are recommendations, not deployed integrations. Verify supported OS, product edition, connectivity, token scopes, data residency, license and ingest economics before production use.

## Capacity and throughput

Estimate signal rates (events/sec, spans/sec, logs/sec, metric cardinality), peak bursts, network egress, ActiveGate CPU/memory and scaling, buffering, retry behavior, retention, and ingestion cost. Benchmark a representative pilot; do not assume additional hardware is always required.

## Change controls

Discovery -> change proposal -> security review -> CAB approval where required -> planned window -> dry run -> deployment -> dual-run validation -> acceptance -> rollback or handover. The approval example is local simulation only.

## Future milestones

1. Add read-only Dynatrace inventory API client with mocked tests.
2. Add OpenTelemetry Collector example with environment-variable secrets.
3. Add Terraform and Ansible dry-run samples.
4. Add a human-approved agentic-AI recommendation adapter with prompt-injection defenses and audit logs.
5. Add optional ServiceNow integration with mock provider and real credentials only via secure secrets.
6. Add dashboards and acceptance report artifacts.
