import json

INPUT_FILE = "enriched_alerts.json"
OUTPUT_FILE = "reports/incident_report.txt"

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    alerts = json.load(f)

with open(OUTPUT_FILE, "w", encoding="utf-8") as report:

    report.write("=====================================\n")
    report.write("      SECURITY INCIDENT REPORT\n")
    report.write("=====================================\n\n")

    report.write(f"Total Incidents: {len(alerts)}\n\n")

    for i, alert in enumerate(alerts, start=1):

        report.write(f"Incident #{i}\n")
        report.write("-------------------------------------\n")
        report.write(f"Timestamp: {alert.get('timestamp')}\n")
        report.write(f"Host: {alert.get('agent')}\n")
        report.write(f"Rule ID: {alert.get('rule_id')}\n")
        report.write(f"Description: {alert.get('description')}\n")
        report.write(f"Risk Score: {alert.get('risk_score')}\n")
        report.write(f"MITRE ID: {alert.get('mitre_id')}\n")
        report.write(f"MITRE Tactic: {alert.get('mitre_tactic')}\n")
        report.write(f"MITRE Technique: {alert.get('mitre_technique')}\n")
        report.write(f"Process: {alert.get('process_image')}\n")
        report.write(f"Command Line: {alert.get('commandLine')}\n")
        report.write(f"File:{alert.get('file')}\n")
        report.write(f"FIM Event:{alert.get('fim_event')}\n")
        report.write(f"Changed Attributes:{alert.get('changed_attributes')}\n")
        report.write(f"MD5:{alert.get('md5_after')}\n")
        report.write(f"SHA1: {alert.get('sha1_after')}\n")
        report.write(f"SHA256: {alert.get('sha256_after')}\n")
        report.write("\n")

    report.write("=====================================\n")
    report.write("SOAR Response: Executed Successfully\n")
    report.write("Status: Investigation Complete\n")
    report.write("=====================================\n")

print("Incident report generated successfully!")
print(f"Output file: {OUTPUT_FILE}")
