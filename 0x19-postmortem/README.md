# POSTMORTEM PROJECT ALX

## NGINX OUTAGE INCIDENT POSTMORTEM

### Issue Summary:

Duration: The outage occurred from 08:30 AM to 10:15 AM (UTC) on April 5th.
Impact: Users experienced a complete unavailability of the web service. Approximately 30% of users were affected during the outage.
Root Cause: The outage was caused by a conflict in Nginx configuration files, leading to the web server's inability to serve user requests.

### Timeline:

08:45 AM: Initial assumption pointed towards a potential DDoS attack due to the unusual spike in traffic.

09:00 AM: Further investigation revealed conflicting configuration settings in Nginx.

09:30 AM: Misleading paths, including examining network issues and database problems, were explored before narrowing down to Nginx configuration conflicts.

Root Cause and Resolution:

Root Cause: A recent configuration update led to a conflict in Nginx settings, causing the server to stop serving user requests.

Resolution: The conflicting configuration files were identified, and the system was reverted to a stable state by restoring a backup of the Nginx settings.

### Corrective and Preventative Measures:

Improvements/Fixes:

Strengthen the change management process to include thorough testing before deploying configurations.
Implement automated monitoring for configuration changes and potential conflicts.

Tasks to Address the Issue:

Conduct a comprehensive review of Nginx configurations to identify and eliminate potential conflicts.
Enhance documentation for configuration changes to ensure clarity and prevent future misunderstandings.

