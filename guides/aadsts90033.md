
# AADSTS90033: MsodsServiceUnavailable - The Microsoft Online Directory Service (MSODS) isn't available.


## Troubleshooting Steps
Certainly! The error code AADSTS90033, with the description "MsodsServiceUnavailable - The Microsoft Online Directory Service (MSODS) isn’t available," indicates that there is an issue with the Microsoft Online Directory Service (MSODS) that is preventing it from processing requests. Below is a troubleshooting guide to help you diagnose and resolve this issue.

### Troubleshooting Guide for AADSTS90033

#### Initial Diagnostic Steps

1. **Check Service Health:**
   - Visit the Microsoft 365 service health dashboard: [Microsoft 365 Service Health Status](https://portal.office.com/adminportal/home#/servicehealth). Check if there are any reported outages or issues with the Azure Active Directory or Microsoft Online Directory Service.

2. **Verify the Error Context:**
   - Try to understand the context in which the error occurs. Is it during a specific operation (like login, token acquisition, etc.) or for specific applications? 

3. **Review Recent Changes:**
   - Determine if any changes were recently made to the Azure AD configuration, application registrations, or user accounts that might correlate with the onset of this error.

#### Common Issues that Cause This Error

1. **Service Outage:**
   - Temporary outages or degradation of the Azure Active Directory service.

2. **Network Issues:**
   - Problems with network connectivity that might affect your ability to reach MSODS.

3. **Incorrect Configuration:**
   - Issues related to application configuration, such as invalid redirect URIs or misconfigured permissions.

4. **Account Issues:**
   - Issues related to specific user accounts or permissions that may prevent access or lead to the failure of directory services.

#### Step-by-Step Resolution Strategies

1. **Check Service Status:**
   - If a service outage is identified, retry the operation after some time once Microsoft confirms the resolution of service issues.

2. **Test Network Connectivity:**
   - Verify that your network connection is stable. You can use tools like `ping`, `tracert`, or network monitoring software to check connectivity to Azure services.

3. **Review Application Configuration:**
   - Ensure that your application registration in Azure AD is set up correctly:
     - Validate the redirect URIs.
     - Verify that API permissions are properly configured and granted.
     - Ensure that the app is not disabled in the Azure portal.

4. **Review Logs for Errors:**
   - Look for logs that could give more insight:
     - Azure AD audit logs: [Azure AD Sign-ins logs](https://portal.azure.com/#blade/Microsoft_AAD_RegisteredApps/ApplicationsListBlade).
     - Application logs in your application’s monitoring solution.

5. **Contact Support:**
   - If the issue persists and internal resolution is unsuccessful, consider reaching out to Microsoft support for further assistance. Provide them with relevant details about the issue context and any logs collected.

#### Additional Notes or Considerations

- **Time-Limited Issues:**
  - Sometimes, these services may have transient issues that resolve themselves. If the error is intermittent, monitor it for a while before taking drastic measures.

- **Require Updates:**
  - Ensure that any SDK, libraries, or tools used to access the Azure AD are updated to their latest versions.

- **Rate Limits:**
  - Be aware of the possibility of rate limits being hit if your application is making an excessive number of requests in a short period.

### Documentation for Guidance

- [Microsoft Azure Active Directory Documentation](https://docs.microsoft.com/en-us/azure/active-directory/)
- [Understanding Azure AD error codes](https://docs.microsoft.com/en-us/azure/active-directory/develop/reference-aad-error-codes)
- [Azure AD Service Health Monitoring](https://docs.microsoft.com/en-us/azure/active-directory/reports-monitoring/monitor-health)

### Advice for Data Collection (Event Viewer, NetTrace, Fiddler)

- **Event Viewer:**
  - Check the Windows Event Viewer for application-specific errors in the logs that might indicate problems during authentication or service calls. Path: `Windows Logs > Application`.

- **NetTrace:**
  - If applicable, collect network traces using tools like Wireshark or the built-in Windows `netsh trace` command while reproducing the error to see if any network communication issues are evident.

- **Fiddler/Browser Developer Tools:**
  - Use Fiddler or browser developer tools (like Chrome DevTools) to view HTTP request and response headers while the error occurs. Look for ASP.NET HTTP response codes or additional error message details that can provide insight.

By following this guide, you can systematically address the error AADSTS90033 and work toward a resolution.