# Project Workflow

**Version:** 1.0

**Author:** Mahesh Tilot

---

# Purpose

This document explains the complete operational workflow of the Wazuh SIEM Alert Enrichment & Incident Reporting project. It describes how security events are generated, detected, enriched, and transformed into investigation-ready incident reports.

The workflow demonstrates a practical Security Operations Center (SOC) process, showing how automation can improve the efficiency of security monitoring and incident response.

---

# Workflow Overview

The project follows a structured workflow consisting of event generation, detection, enrichment, analysis, and reporting.

Each stage builds upon the previous stage to provide meaningful context for SOC analysts during investigations.

---

# Complete Project Workflow

```text
┌─────────────────────────────┐
│  Security Event Generated   │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│   Wazuh Agent Collection    │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│    Wazuh Manager Analysis   │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│     Security Alert Created  │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│   Dashboard Visualization   │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│   Export Alert (JSON)       │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│ Python Alert Enrichment     │
└──────────────┬──────────────┘
               │
     ┌─────────┼───────────┐
     ▼         ▼           ▼
Risk Score  MITRE Map   FIM Analysis
     │         │           │
     └─────────┼───────────┘
               ▼
┌─────────────────────────────┐
│ Enriched JSON Alert         │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│ Incident Report Generation  │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│ SOC Investigation           │
└─────────────────────────────┘
```

---

# Workflow Stages

## Stage 1 – Security Event Generation

The workflow begins when a monitored system generates a security event.

Examples include:

- File modification
- Authentication activity
- Process execution
- User activity
- System events

These events represent the raw security information collected from the monitored endpoint.

---

## Stage 2 – Event Collection

The Wazuh Agent continuously monitors the endpoint and forwards collected events to the Wazuh Manager for analysis.

The agent acts as the primary data collection component within the monitoring architecture.

---

## Stage 3 – Detection and Analysis

The Wazuh Manager evaluates incoming events using predefined detection rules.

If suspicious or monitored activity is identified, a security alert is generated.

Each alert contains important information such as:

- Rule ID
- Severity
- Timestamp
- Agent
- Description

---

## Stage 4 – Dashboard Visualization

Generated alerts are displayed within the Wazuh Dashboard.

Analysts can use the dashboard to:

- Monitor active alerts
- View authentication events
- Analyze MITRE ATT&CK mappings
- Review File Integrity Monitoring (FIM) events
- Observe alert trends
- Investigate custom dashboards

---

## Stage 5 – Alert Export

Security alerts are exported in JSON format for additional processing.

The JSON structure contains all event information required by the Python enrichment engine.

---

## Stage 6 – Python Alert Enrichment

The enrichment engine processes every alert and extracts additional investigation data.

The enrichment process includes:

- Risk score calculation
- MITRE ATT&CK mapping
- File Integrity Monitoring analysis
- Hash extraction
- Structured JSON generation

---

## Stage 7 – Incident Report Generation

The enriched alerts are processed by the reporting module.

A structured incident report is generated containing:

- Alert information
- Risk assessment
- MITRE ATT&CK mapping
- FIM details
- Hash values
- Investigation summary

---

## Stage 8 – SOC Investigation

The final report provides analysts with investigation-ready information.

Instead of manually collecting data from multiple sources, analysts receive a structured report that supports faster analysis and incident response.

---

# Workflow Benefits

The implemented workflow provides several operational advantages:

- Automated alert enrichment
- Reduced manual analysis
- Faster investigations
- Consistent incident reporting
- Improved security visibility
- Better SOC efficiency

### Figure 4.1 - End-to-End Security Workflow

![Wazuh Workflow](../diagrams/02_Project_Workflow.svg)

---

# Key Takeaways

- Security events are automatically collected by Wazuh.
- Detection rules identify suspicious activity.
- Python enriches alerts with investigation context.
- Risk scores and MITRE mappings improve alert prioritization.
- Automated reports reduce manual SOC effort.
- The complete workflow demonstrates practical SIEM automation.

---

# Conclusion

This workflow demonstrates how Wazuh SIEM and Python automation work together to transform raw security events into structured, investigation-ready incident reports. By automating enrichment and reporting, the project improves analyst efficiency and provides a clear example of a modern SOC workflow.