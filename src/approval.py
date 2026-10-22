"""Deterministic approval-gate simulation; no AI model or ITSM API is called."""
from dataclasses import dataclass

@dataclass
class Change:
    asset_id: str
    action: str
    risk: str
    approved: bool = False

def evaluate(change):
    if not change.approved:
        return {"decision": "BLOCKED", "reason": "Human change approval required"}
    if change.risk == "high":
        return {"decision": "REVIEW", "reason": "High-risk change requires CAB and rollback validation"}
    return {"decision": "ELIGIBLE", "reason": "Simulation only; no deployment performed"}
