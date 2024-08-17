# ALX

## Postmortem


### Postmortem Report: Unauthorized Access Due to Misconfigured Nginx User Privileges

**Issue Summary:**
- **Duration of Outage:** 2024-08-15, 14:00 - 16:30 UTC (2 hours 30 minutes)
- **Impact:** A critical web application experienced unauthorized access, resulting in potential data exposure for approximately 40% of the users. Users reported seeing other users' private data on the web interface, raising concerns about privacy breaches.
- **Root Cause:** The web server was mistakenly running under the root user instead of the less-privileged `nginx` user, allowing an attacker to exploit a vulnerability and gain unauthorized access to sensitive information.

### Timeline:
- **14:00 UTC** - Issue detected by a monitoring alert indicating unusual traffic spikes and errors in the application logs.
- **14:05 UTC** - Initial investigation began. Engineers assumed a temporary network issue due to traffic spikes.
- **14:15 UTC** - Application logs were reviewed, revealing unauthorized access to private data.
- **14:20 UTC** - Incident escalated to the security team. Security engineers started investigating potential breaches.
- **14:30 UTC** - Misleading path: Assumed a SQL injection attack due to abnormal database queries. Security rules were temporarily tightened.
- **14:45 UTC** - Further investigation showed that the web server was running under the root user, which contradicted security best practices.
- **15:00 UTC** - Misconfiguration in the Nginx service was identified as the root cause.
- **15:30 UTC** - The Nginx service was reconfigured to run under the `nginx` user. Additional security patches were applied.
- **16:00 UTC** - Incident resolution confirmed. Affected users were logged out and forced to reset their credentials.
- **16:30 UTC** - Post-incident monitoring showed no further unauthorized access, and the incident was declared resolved.

### Root Cause and Resolution:
The root cause of the incident was a misconfiguration in the Nginx web server, which was running under the root user rather than the `nginx` user. This configuration exposed the server to significant security risks, as the root user has full administrative privileges on the system. An attacker exploited a vulnerability within the application to gain unauthorized access to sensitive user data.

The issue was resolved by reconfiguring the Nginx service to run under the `nginx` user, which has limited privileges. This change significantly reduced the potential impact of any future vulnerabilities. In addition, security patches were applied to the web application to close the exploited vulnerability.

### Corrective and Preventative Measures:
**Improvements and Fixes:**
1. **Review and Audit Security Configurations:** Conduct a comprehensive audit of all server configurations to ensure that no critical services are running with root privileges.
2. **Implement Role-Based Access Controls:** Enforce stricter role-based access controls to limit the impact of any potential security breach.
3. **Enhanced Monitoring and Alerts:** Upgrade monitoring systems to detect and alert on any unauthorized privilege escalation attempts.

**Tasks:**
- **Patch Nginx Server:** Ensure all Nginx servers are patched and configured to run under the `nginx` user.
- **Add Monitoring on Server Privileges:** Implement monitoring for privilege escalation on all servers.
- **Security Review of Web Applications:** Conduct a thorough security review of all web applications to identify and mitigate potential vulnerabilities.
- **User Credential Reset:** Force a credential reset for all affected users to prevent unauthorized access.

By taking these steps, we aim to prevent similar incidents from occurring in the future and to strengthen our overall security posture.
