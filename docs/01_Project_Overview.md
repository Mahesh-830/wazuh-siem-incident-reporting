# Wazuh SIEM Alert Enrichment & Incident Reporting

**Version:** 1.0

**Project Type:** Cybersecurity Portfolio Project

**Author:** Mahesh Tilot

---

# Document Information

| Field | Details |
|--------|---------|
| Project Name | Wazuh SIEM Alert Enrichment & Incident Reporting |
| Version | 1.0 |
| Language | Python |
| Platform | Ubuntu Server |
| SIEM | Wazuh |
| Documentation Version | 1.0 |

---

# Executive Summary

Modern Security Operations Centers (SOCs) continuously monitor endpoints, servers, and network infrastructure to detect malicious activity. As organizations generate thousands of security events every day, analysts require efficient methods to prioritize alerts, investigate incidents, and produce accurate reports.

This project demonstrates a practical SOC workflow by integrating Wazuh SIEM with Python-based automation. The solution processes Wazuh security alerts, enriches them with additional investigation context, maps alerts to the MITRE ATT&CK framework, extracts File Integrity Monitoring (FIM) information, calculates risk scores, and automatically generates incident reports.

Rather than replacing Wazuh, this project extends its alert analysis capabilities by reducing manual investigation effort and presenting structured information that supports faster incident response.

---

# Purpose of this Document

This document provides an overview of the project, explains its objectives, describes the technologies used, and introduces the overall workflow implemented throughout the solution.

It serves as the starting point for understanding the architecture, implementation, testing, and documentation contained within this repository.

---

# Introduction

Security Information and Event Management (SIEM) platforms are widely used to collect, correlate, and analyze security events generated across enterprise environments. These platforms enable analysts to detect suspicious behavior, investigate incidents, and maintain visibility into organizational security.

Although SIEM solutions provide extensive event information, analysts often need additional context before an alert becomes actionable. Manual enrichment increases investigation time and may delay incident response.

This project addresses that challenge by automating alert enrichment using Python. Security alerts collected by Wazuh are processed to extract investigation-relevant information and transformed into structured outputs that support Security Operations Center (SOC) investigations.

---

# Background

Wazuh is an open-source SIEM and XDR platform capable of monitoring endpoints, detecting security events, performing File Integrity Monitoring (FIM), log analysis, vulnerability detection, and compliance monitoring.

During this project, Wazuh was configured to monitor security events generated within the laboratory environment. Custom dashboards were developed to visualize alert trends, MITRE ATT&CK mappings, custom detections, and event statistics.

To extend the investigation process beyond the default Wazuh capabilities, Python automation was developed to enrich alerts and generate investigation-ready incident reports.

### Figure 1: Wazuh Login Page 
![Wazuh Login Page](../screenshots/01_Wazuh_Login.png)
### Figure 2: Wazuh Dashboard 
![Wazuh Dashboard](../screenshots/02_Wazuh_Overview.png)
### Figure 3A: Wazuh Nexus SOC Dashbaord
![Nexus Dashboard](../screenshots/03_A_Nexus_SOC_Dashboard.png)
### Figure 3B: Wazuh Nexus SOC Dashboard
![Nexus Dashboard](../screenshots/03_B_Nexus_SOC_Dashboard.png)

---

# Problem Statement

SOC analysts often receive large numbers of alerts containing technical information but limited investigative context.

Manual investigation introduces several challenges:

- High alert volume
- Manual alert prioritization
- Time-consuming incident reporting
- Repetitive analysis tasks
- Delayed incident response

This project demonstrates how Python automation can reduce manual effort by automatically enriching alerts with additional contextual information.

---

# Project Objectives

The primary objectives of this project are:

- Deploy and configure a Wazuh SIEM environment.
- Generate and monitor security events.
- Configure File Integrity Monitoring (FIM).
- Develop Python-based alert enrichment.
- Calculate alert risk scores.
- Map alerts to the MITRE ATT&CK framework.
- Extract cryptographic hash values (MD5, SHA1, SHA256).
- Generate automated incident reports.
- Demonstrate a practical SOC investigation workflow.

---

# Project Scope

The project focuses on the following areas:

- Security Event Monitoring
- Alert Analysis
- File Integrity Monitoring (FIM)
- Python Automation
- Alert Enrichment
- MITRE ATT&CK Mapping
- Risk Scoring
- Incident Reporting

The implementation is designed as a laboratory demonstration intended to showcase SIEM automation concepts and SOC investigation workflows.

---

# Key Features

The project provides the following functionality:

- Security monitoring using Wazuh SIEM
- Custom SOC dashboard
- Security event collection
- File Integrity Monitoring (FIM)
- Python-based alert enrichment
- Risk score calculation
- MITRE ATT&CK mapping
- Hash extraction (MD5, SHA1, SHA256)
- Enriched JSON generation
- Automated incident report generation

---

# Technologies Used

| Technology | Purpose |
|------------|---------|
| Wazuh SIEM | Security Monitoring |
| Python 3 | Alert Enrichment |
| Ubuntu Server | Wazuh Server |
| VS Code | Development |
| JSON | Alert Processing |
| MITRE ATT&CK | Threat Classification |
| File Integrity Monitoring | File Change Detection |

---

# Project Directory Structure

```text
wazuh-enrichment/
│
├── diagrams/
├── docs/
├── reports/
├── screenshots/
├── source_logs/
│
├── enrich_alerts.py
├── incident_report.py
├── enriched_alerts.json
└── README.md
```

---

# High-Level Workflow

The overall workflow implemented by this project is shown below.

```text
Security Event
       │
       ▼
Wazuh SIEM Detection
       │
       ▼
Security Alert
       │
       ▼
Python Alert Enrichment
       │
 ┌─────┼─────────────┐
 │     │             │
 ▼     ▼             ▼
Risk  MITRE      FIM Details
Score Mapping   Hash Extraction
       │
       ▼
Enriched Alert (JSON)
       │
       ▼
Incident Report Generation
       │
       ▼
SOC Investigation
```

---

# Expected Outcomes

After completing this project, the following outcomes are achieved:

- Successful deployment of a Wazuh SIEM laboratory.
- Detection of security events.
- Automated alert enrichment.
- Structured incident reports.
- Improved alert investigation workflow.
- Practical demonstration of SOC automation concepts.

---

# Conclusion

This project demonstrates how Wazuh SIEM and Python can be combined to improve security alert analysis through automation. By enriching alerts with contextual information, calculating risk scores, mapping MITRE ATT&CK techniques, extracting File Integrity Monitoring data, and generating incident reports, the solution provides a structured workflow suitable for educational SOC environments and cybersecurity portfolio demonstrations.

The following documents describe the architecture, implementation, installation, testing methodology, troubleshooting procedures, and future enhancements in greater technical detail.

## GitHub Repository

Repository: https://github.com/Mahesh-830/wazuh-siem-incident-reporting