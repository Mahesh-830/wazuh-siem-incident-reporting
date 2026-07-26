import json
from datetime import datetime,UTC

INPUT_FILE = "/var/ossec/logs/alerts/alerts.json"
OUTPUT_FILE = "enriched_alerts.json"

def calculate_risk(level):
    if level >= 15:
        return "Critical"
    elif level >= 12:
        return "High"
    elif level >= 8:
        return "Medium"
    return "Low"

enriched = []

with open(INPUT_FILE, "r", encoding="utf-8", errors="ignore") as f:
    for line in f:
        try:
            alert = json.loads(line)
        except json.JSONDecodeError:
            continue

        rule = alert.get("rule", {})
        rule_id = str(rule.get("id", ""))

        level = int(rule.get("level", 0))
        mitre = rule.get("mitre", {})

        mitre_id = ",".join(mitre.get("id",["Unknown"]))
        mitre_tactic = ",".join(mitre.get("tactic",["Unknown"]))
        mitre_technique = ",".join(mitre.get("technique",["Unknown"]))

        data = alert.get("data", {})
        syscheck = alert.get("syscheck",{})

        if "win" in data:
            event_data = data["win"].get("eventdata", {})
        else:
             event_data = data

        enriched_alert = {
            "enriched_time": datetime.now(UTC).isoformat(),
            "timestamp": alert.get("timestamp"),
            "agent": alert.get("agent", {}).get("name"),
            "rule_id": rule_id,
            "description": rule.get("description"),
            "level": level,
            "risk_score": calculate_risk(level),
            "mitre_id": mitre_id,
            "mitre_tactic": mitre_tactic,
            "mitre_technique": mitre_technique,
            "process_image": event_data.get("image"),
            "command_line": event_data.get("commandLine"),
            "parent_process": event_data.get("parentImage"),
            "user": event_data.get("user"),
            "file": syscheck.get("path"),
            "fim_event": syscheck.get("event"),
            "changed_attributes": syscheck.get("changed_attributes"),
            "md5_after": syscheck.get("md5_after"),
            "sha1_after": syscheck.get("sha1_after"),
            "sha256_after": syscheck.get("sha256_after"),
        }

        enriched.append(enriched_alert)

with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
    json.dump(enriched, out, indent=2)

print(f"Enriched alerts saved: {len(enriched)}")
print(f"Output file: {OUTPUT_FILE}")
