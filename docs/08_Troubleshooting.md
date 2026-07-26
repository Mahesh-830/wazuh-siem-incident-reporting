# Troubleshooting

**Version:** 1.0

**Author:** Mahesh Tilot

---

# Purpose

This document provides solutions to common issues that may occur during the installation, configuration, execution, and testing of the Wazuh SIEM Alert Enrichment & Incident Reporting project.

The goal is to assist users in identifying problems quickly and applying appropriate corrective actions.

---

# Common Issues

## Issue 1 – Wazuh Dashboard Not Accessible

### Symptoms

- Dashboard fails to load.
- Browser displays connection errors.
- Login page does not appear.

### Possible Causes

- Wazuh Dashboard service is not running.
- Incorrect IP address.
- Network connectivity issues.

### Resolution

- Verify the Wazuh Dashboard service status.
- Confirm the server IP address.
- Ensure the required ports are accessible.
- Restart the dashboard service if necessary.

---

## Issue 2 – Wazuh Manager Not Receiving Events

### Symptoms

- No new alerts appear.
- Dashboard remains unchanged.
- Event count does not increase.

### Possible Causes

- Wazuh Agent disconnected.
- Network communication failure.
- Manager service unavailable.

### Resolution

- Verify agent connectivity.
- Confirm manager service is running.
- Review Wazuh logs for errors.

---

## Issue 3 – File Integrity Monitoring (FIM) Events Missing

### Symptoms

- File modifications are not detected.
- No FIM alerts generated.

### Possible Causes

- FIM monitoring not configured.
- File path excluded.
- Monitoring service not active.

### Resolution

- Verify FIM configuration.
- Confirm monitored directories.
- Restart Wazuh services.
- Generate a new file modification event.

---

## Issue 4 – Python Script Execution Failure

### Symptoms

- Script terminates unexpectedly.
- Python displays execution errors.

### Possible Causes

- Incorrect file path.
- Missing input file.
- Invalid JSON format.

### Resolution

- Verify project directory.
- Confirm alerts.json exists.
- Validate JSON syntax.
- Execute scripts from the project root.

---

## Issue 5 – Incident Report Not Generated

### Symptoms

- incident_report.txt not created.

### Possible Causes

- Enrichment step failed.
- Missing enriched_alerts.json.
- File permission issues.

### Resolution

- Run enrich_alerts.py successfully.
- Verify enriched_alerts.json generation.
- Check write permissions.

---

## Issue 6 – Missing Hash Values

### Symptoms

- MD5, SHA1 or SHA256 fields are empty.

### Possible Causes

- Alert is not related to File Integrity Monitoring.
- Hash values unavailable in the original alert.

### Resolution

- Generate a valid FIM alert.
- Verify Wazuh alert contains hash information.

---

# Best Practices

To ensure reliable operation:

- Keep Wazuh services running.
- Verify agent connectivity regularly.
- Validate JSON input before processing.
- Execute scripts from the project directory.
- Review generated reports after each execution.
- Maintain backups of important project files.

---

# Key Takeaways

- Most issues can be resolved through service verification and configuration checks.
- Proper validation of JSON input prevents enrichment failures.
- File Integrity Monitoring should be verified before testing.
- Reviewing generated outputs helps identify issues early.

---

# Conclusion

The troubleshooting procedures described in this document provide practical guidance for diagnosing and resolving common issues encountered during the development and execution of the project. Following these recommendations helps maintain a stable and reproducible laboratory environment.

---

# References

1. Wazuh Documentation
2. Python Documentation
3. Ubuntu Documentation