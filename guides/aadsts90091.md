# AADSTS90091: GraphServiceUnreachable


## Troubleshooting Steps
## Troubleshooting Guide for AADSTS90091: "GraphServiceUnreachable"

### Overview
AADSTS90091 is an error code returned by Azure Active Directory (Azure AD) indicating that the service responsible for handling Graph API requests is temporarily unreachable. This can often be related to network issues, service outages, or misconfigurations within Azure AD or the application that is requesting the Graph API.

---

### Initial Diagnostic Steps
1. **Check Azure Service Health**:
   - Visit the [Azure Status page](https://status.azure.com/) to see if there are any reported outages or issues with Azure AD or Microsoft Graph services.

2. **Verify Network Connectivity**:
   - Ensure the user’s system has an active internet connection.
   - Confirm that there are no network firewalls or proxies blocking access to the required Microsoft Graph endpoints.

3. **Review Configuration**:
   - Check the application registration in the Azure portal.
   - Verify API permissions for Microsoft Graph and ensure they are correctly set.

4. **Check for Token Expiry**:
   - Ensure that access tokens used in requests are not expired and are being refreshed as necessary.

---

### Common Issues that Cause This Error
1. **Service Outage**:
   - Temporary outages of Azure services or Microsoft Graph.

2. **Network Issues**:
   - VPN or firewall configurations might hinder access to Microsoft's Graph API.

3. **DNS Resolution Failures**:
   - The client may be unable to resolve the Graph API URLs due to DNS issues.

4. **Misconfigured Application**:
   - Incorrect application permissions or client IDs in the Azure portal.

5. **Regional Restrictions**:
   - The service might have limited availability in specific regions.

---

### Step-by-Step Resolution Strategies
1. **Monitor Azure Service Status**:
   - Regularly check the status page for ongoing incidents. If there is a service disruption, it's best to wait until Azure resolves the issue.

2. **Network Troubleshooting**:
   - Test access to the Graph API using tools like Postman or curl:
     ```bash
     curl -X GET "https://graph.microsoft.com/v1.0/" -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
     ```
   - If you receive connectivity errors, trace network routes and check firewall settings.

3. **Update Network DNS Settings**:
   - Configure DNS settings to use public DNS servers (like Google’s 8.8.8.8) and test if the issue persists.

4. **Validate Application Configuration**:
   - Go to the Azure Portal:
     - Navigate to "Azure Active Directory" > "App registrations" > <Your app>
     - Ensure all API permissions for Microsoft Graph are granted.
     - Check if the necessary **redirect URIs** are configured correctly.

5. **Re-authenticate**:
   - If applicable, request a fresh token. Ensure that your method for retrieving tokens complies with OAuth 2.0 standards.

6. **Contact Microsoft Support**:
   - If the issue continues, open a support ticket with Microsoft Azure support for further investigation.

---

### Additional Notes or Considerations
- Ensure that the user has the necessary roles assigned in Azure AD for the application to function correctly.
- If you encounter frequent timeouts or latency, consider retuning your application’s retry policies for resilience.

---

### Documentation for Reference
- [Azure Active Directory Error Codes](https://docs.microsoft.com/en-us/azure/active-directory/develop/reference-aadsts-error-codes)
- [Microsoft Graph API Documentation](https://docs.microsoft.com/en-us/graph/overview)
- [Troubleshoot Microsoft Graph authorization errors](https://docs.microsoft.com/en-us/graph/auth/authentication-scenarios)

---

### Advice for Data Collection
If issues persist and you need to collect diagnostic data:

1. **Event Viewer Logs**:
   - On the client machine, open Event Viewer (eventvwr.msc) and look under:
     - Windows Logs -> Application
     - Windows Logs -> System
   - Look for any errors related to network connections or Microsoft APIs.

2. **Network Tracing**:
   - Use `nettrace` to capture network traffic:
     - Open Command Prompt as Administrator.
     - Run `netsh trace start capture=yes report=activity`.
     - Reproduce the issue and then stop the trace by running `netsh trace stop`.
     - Review the report generated.

3. **Fiddler**:
   - Use Fiddler to inspect outgoing requests to the Graph API.
   - Look for any alerts or failed responses that indicate connectivity or authorization problems.

Ensure the collected logs are analyzed before escalating for support, as they may give insights into latency issues or misconfigurations.

By following the above guide, you should be able to troubleshoot the AADSTS90091 error effectively. If problems continue to occur, don’t hesitate to reach out for further assistance.