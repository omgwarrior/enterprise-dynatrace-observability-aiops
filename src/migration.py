"""Synthetic inventory assessment; no production changes or external API calls."""
import json
from pathlib import Path

COLLECTORS = {
    "linux": "OneAgent (subject to platform support)",
    "kubernetes": "Dynatrace Operator / OpenTelemetry",
    "network": "ActiveGate extension / supported SNMP integration",
    "database": "Supported database extension / application instrumentation",
    "unix": "Validate OS support; extension, API or OTel alternative",
}

def assess(items):
    results = []
    for item in items:
        status = "validated" if item["target_coverage"] else "gap"
        results.append({"id": item["id"], "owner": item["owner"],
                        "criticality": item["criticality"], "source": item["source"],
                        "collection_pattern": COLLECTORS.get(item["type"], "assess manually"),
                        "status": status,
                        "recommended_action": "retain and verify" if status == "validated" else "propose onboarding change"})
    return results

def summarize(results):
    total = len(results)
    passed = sum(x["status"] == "validated" for x in results)
    return {"total": total, "validated": passed, "gaps": total-passed,
            "coverage_pct": round(100*passed/total,1) if total else 100.0}

def main():
    root = Path(__file__).resolve().parents[1]
    items = json.loads((root/'data/inventory.json').read_text())
    results = assess(items)
    report = {"summary": summarize(results), "assets": results}
    out = root/'reports';out.mkdir(exist_ok=True)
    (out/'migration-assessment.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report["summary"],indent=2))
    print('Report: reports/migration-assessment.json')
if __name__ == '__main__': main()
