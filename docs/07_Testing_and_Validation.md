# Testing and Validation

**Version:** 1.0

**Author:** Mahesh Tilot

---

# Purpose

This document describes the testing methodology used to verify the functionality of the Wazuh SIEM Alert Enrichment & Incident Reporting project. The objective of testing was to confirm that each component operated correctly and that the complete workflow functioned as expected.

---

# Testing Objectives

The project was tested to verify:

- Wazuh successfully detected security events.
- Alerts were generated correctly.
- Python enrichment executed without errors.
- Risk scores were assigned.
- MITRE ATT&CK mappings were preserved.
- File Integrity Monitoring (FIM) details were extracted.
- MD5, SHA1, and SHA256 hashes were captured.
- Incident reports were generated successfully.

---

# Test Environment

| Component | Description |
|-----------|-------------|
| Host OS | Windows 11 |
| Guest OS | Ubuntu Server |
| SIEM | Wazuh |
| Development Tool | Visual Studio Code |
| Language | Python 3 |

---

# Test Cases

| Test ID | Test Description | Expected Result | Status |
|----------|------------------|-----------------|--------|
| TC-01 | Generate security event | Wazuh detects the event | PASS |
| TC-02 | Create security alert | Alert appears in dashboard | PASS |
| TC-03 | Run enrich_alerts.py | Enriched JSON generated | PASS |
| TC-04 | Risk score calculation | Risk score assigned | PASS |
| TC-05 | MITRE mapping | Technique retained | PASS |
| TC-06 | FIM extraction | File details extracted | PASS |
| TC-07 | Hash extraction | MD5, SHA1, SHA256 extracted | PASS |
| TC-08 | Run incident_report.py | Report generated | PASS |

---

# Validation Results

The completed tests confirmed that:

- Security events were collected successfully.
- Wazuh detection rules generated alerts.
- Dashboards displayed security activity.
- Python enrichment completed successfully.
- JSON output contained additional investigation context.
- Incident reports summarized alerts in a structured format.

---

# Output Verification

The following outputs were verified during testing:

- `enriched_alerts.json`
- `reports/incident_report.txt`

Verification included:

- Risk score accuracy
- MITRE ATT&CK mapping
- File Integrity Monitoring details
- Hash extraction
- Report formatting

### Figure:7.1 - Custom Rule 100500 – Notepad Detection

Objective: To verify that the custom Wazuh rule (Rule ID: 100500) successfully detects the execution of the Notepad application.

Test Procedure: The Notepad application was launched on the monitored Windows endpoint, and a sample text was entered. Wazuh monitored the activity and generated an alert based on the custom detection rule.

Result: The custom rule successfully detected the Notepad execution. The event was recorded in the Wazuh dashboard with Rule ID 100500, and the corresponding alert and JSON event details were generated successfully.

### 7.1-A NOTEPAD COMMAND EXECUTION
![Notepad Detection](../screenshots/Notepad-Detection_1.png)
### 7.1-B WAZUH SECURITY EVENT
![Notepad Detection](../screenshots/Notepad-Detection_2.png)
### 7.1-C WAZUH ALERT DETAILS
![Notepad Detection](../screenshots/Notepad-Detection_3.png)
### 7.1-D JSON EVENT DETAILS - I
![Notepad Detection](../screenshots/Notepad-Detection_4.png)
### 7.1-E JSON EVENT DETAILS - II
![Notepad Detection](../screenshots/Notepad-Detection_5.png)


### Figure:7.2 - Custom Rule 100501 – PowerShell Detection

Objective: To validate that the custom Wazuh rule (Rule ID: 100501) detects PowerShell execution.

Test Procedure: PowerShell was executed on the monitored Windows endpoint. Wazuh analysed the generated system event and triggered the corresponding custom detection rule.

Result: PowerShell execution was successfully detected. Wazuh generated an alert with Rule ID 100501, and the event information was available in both the alert and JSON views.

### 7.2-A POWERSHELL COMMAND EXECUTION
![Powershell Detection](../screenshots/Powershell-process_1.png)
### 7.2-B WAZUH SECURITY EVENT
![Powershell Detection](../screenshots/Powershell-process_2.png)
### 7.2-C WAZUH ALERT DETAILS
![Powershell Detection](../screenshots/Powershell-process_3.png)
### 7.2-D JSON EVENT DETAILS - I
![Powershell Detection](../screenshots/Powershell-process_4.png)
### 7.2-E JSON EVENT DETAILS - II
![Powershell Detection](../screenshots/Powershell-process_5.png)


### Figure:7.3 - Custom Rule 100502 – Command Prompt Detection

Objective: To verify that the custom Wazuh rule (Rule ID: 100502) detects Command Prompt execution.

Test Procedure: The Command Prompt application was launched on the monitored endpoint. Wazuh monitored the process creation event and generated the corresponding security alert.

Result: The custom rule successfully detected Command Prompt execution. The generated alert included Rule ID 100502 and the complete event details.

### 7.3-A COMMAND PROMPT EXECUTION 
![CMD Detection](../screenshots/CMD_1.png)
### 7.3-B WAZUH SECURITY EVENT
![CMD Detection](../screenshots/CMD_2.png)
### 7.3-C WAZUH ALERT DETAILS
![CMD Detection](../screenshots/CMD_3.png)
### 7.3-D JSON EVENT DETAILS - I
![CMD Detection](../screenshots/CMD_4.png)
### 7.3-E JSON EVENT DETAILS - II
![CMD Detection](../screenshots/CMD_5.png)


### Figure:7.4 - Custom Rule 100503 – Whoami Enumeration Detection

Objective: To validate that the custom Wazuh rule (Rule ID: 100503) detects execution of the whoami command.

Test Procedure: The whoami command was executed from the Command Prompt to simulate user enumeration activity. Wazuh analysed the command execution and triggered the corresponding detection rule.

Result: The execution of the whoami command was successfully detected. Wazuh generated an alert with Rule ID 100503, confirming successful detection of the enumeration activity.

### 7.4-A WHOAMI COMMAND EXECUTION
![Whoami Detection](../screenshots/Whoami_1.png)
### 7.4-B WAZUH SECURITY EVENT
![Whoami Detection](../screenshots/Whoami_2.png)
### 7.4-C WAZUH ALERT DETAILS
![Whoami Detection](../screenshots/Whoami_3.png)
### 7.4-D JSON EVENT DETAILS - I
![Whoami Detection](../screenshots/Whoami_4.png)
### 7.4-E JSON EVENT DETAILS - II
![Whoami Detection](../screenshots/Whoami_5.png)


### Figure:7.5 - Custom Rule 100504 – Net User Enumeration Detection

Objective: To verify that the custom Wazuh rule (Rule ID: 100504) detects execution of the net user command.

Test Procedure: The net user command was executed to enumerate user accounts on the Windows system. Wazuh monitored the command execution and generated the corresponding alert.

Result: The enumeration activity was successfully detected. Wazuh generated an alert with Rule ID 100504, and the event details were successfully recorded.

### 7.5-A NETUSER COMMAND EXECUTION
![NetUser Detection](../screenshots/NetUser_1.png)
### 7.5-B WAZUH SECURITY EVENT
![NetUser Detection](../screenshots/NetUser_2.png)
### 7.5-C WAZUH ALERT DETAILS
![NetUser Detection](../screenshots/NetUser_3.png)
### 7.5-D JSON EVENT DETAILS - I
![NetUser Detection](../screenshots/NetUser_4.png)
### 7.5-E JSON EVENT DETAILS - II
![NetUser Detection](../screenshots/NetUser_5.png)


### Figure:7.6 - Custom Rule 100505 – Suspicious PowerShell Download Activity

Objective: To validate that the custom Wazuh rule (Rule ID: 100505) detects suspicious PowerShell download activity.

Test Procedure: A PowerShell command containing a download operation was executed to simulate suspicious behaviour. Wazuh analysed the command and generated an alert based on the custom detection rule.

Result: The suspicious PowerShell download activity was successfully detected. Wazuh generated an alert with Rule ID 100505, demonstrating successful identification of potentially malicious behaviour.

### 7.6-A POWERSHELL SUSPICIOUS DOWNLOAD COMMAND EXECUTION
![Suspicious Powershell Download](../screenshots/SPD_1.png)
### 7.6-B WAZUH SECURITY EVENT
![Suspicious Powershell Download](../screenshots/SPD_2.png)
### 7.6-C WAZUH ALERT DETAILS
![Suspicious Powershell Download](../screenshots/SPD_3.png)
### 7.6-D JSON EVENT DETAILS - I
![Suspicious Powershell Download](../screenshots/SPD_4.png)
### 7.6-E JSON EVENT DETAILS - II
![Suspicious Powershell Download](../screenshots/SPD_5.png)


### Figure:7.7 - Custom Rule 100506 – Encoded PowerShell Command Detection

Objective: To verify that the custom Wazuh rule (Rule ID: 100506) detects encoded PowerShell commands.

Test Procedure: A PowerShell command using the encoded command option was executed on the monitored endpoint. Wazuh analysed the command-line arguments and triggered the corresponding detection rule.

Result: The encoded PowerShell command was successfully detected. Wazuh generated an alert with Rule ID 100506, confirming successful detection of obfuscated PowerShell execution.

### 7.7-A ENCODED POWERSHELL COMMAND EXECUTION
![Encoded Powershell Detection](../screenshots/Encoded_PS_Command_1.png)
### 7.7-B WAZUH SECURITY EVENT
![Encoded Powershell Detection](../screenshots/Encoded_PS_Command_2.png)
### 7.7-C WAZUH ALERT DETAILS
![Encoded Powershell Detection](../screenshots/Encoded_PS_Command_3.png)
### 7.7-D JSON EVENT DETAILS
![Encoded Powershell Detection](../screenshots/Encoded_PS_Command_4.png)


### Figure:7.8 - Custom Rule 100507 – Nmap Port Scan Detection

Objective: To validate that the custom Wazuh rule (Rule ID: 100507) detects Nmap port scanning activity.

Test Procedure: An Nmap port scan was performed against the monitored system to simulate reconnaissance activity. Wazuh analysed the generated events and triggered the custom detection rule.

Result: The Nmap scan was successfully detected. Wazuh generated an alert with Rule ID 100507, demonstrating successful detection of network reconnaissance activity.

### 7.8-A NMAP COMMAND EXECUTION
![Nmap Detection](../screenshots/Nmap_1.png)
### 7.8-B WAZUH SECURITY EVENT
![Nmap Detection](../screenshots/Nmap_2.png)
### 7.8-C WAZUH  ALERT DETAILS
![Nmap Detection](../screenshots/Nmap_3.png)
### 7.8-D JSON EVENT DETAILS - I
![Nmap Detection](../screenshots/Nmap_4.png)
### 7.8-E JSON EVENT DETAILS - II
![Nmap Detection](../screenshots/Nmap_5.png)


### Figure:7.9 - Alert Enrichment and Incident Report Generation

Objective: To validate that the custom Python scripts successfully enrich Wazuh alerts and generate a structured incident report.

Test Procedure: After validating all custom detection rules, the enrich_alerts.py script was executed to process the collected Wazuh alerts and generate an enriched JSON output. The incident_report.py script was then executed to analyse the enriched alerts and produce a structured incident report summarizing the detected security events.

Result: The enrichment and reporting process completed successfully. The generated incident report included key information such as alert details, host information, risk scores, MITRE ATT&CK mappings, and file integrity monitoring data, confirming the successful end-to-end workflow from detection to automated incident reporting.

### 7.9-A PYTHON SCRIPT EXECUTION
![Python Script Execution](../screenshots/10_Python_Execution.png)
### 7.9-B ENRICHED ALERTS OUTPUT
![Enriched Alerts JSON](../screenshots/07_Enriched_Alert.png)
### 7.9-C GENERATED INCIDENT REPORT
![Generated Incident Report](../screenshots/08_Incident_Report.png)

---


# Key Takeaways

- End-to-end workflow operated successfully.
- Alert enrichment completed without errors.
- Incident reports were generated correctly.
- Testing confirmed the functionality of all major project components.

---

# Conclusion

Testing confirmed that the Wazuh SIEM Alert Enrichment & Incident Reporting project functioned as designed. The integration of Wazuh and Python automation successfully demonstrated an end-to-end SOC workflow, from event detection through alert enrichment to automated incident reporting.

---

# References

1. Wazuh Documentation
2. MITRE ATT&CK Framework
3. Python Documentation