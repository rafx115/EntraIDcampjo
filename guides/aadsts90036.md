# AADSTS90036: MsodsServiceUnretryableFailure - An unexpected, non-retryable error from the WCF service hosted by MSODS has occurred.Open a support ticketto get more details on the error.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS90036 Error

The AADSTS90036 error indicates a non-retryable failure associated with the Microsoft Online Data Services (MSODS) service. This problem typically requires a more in-depth analysis, often leading to support involvement. However, the following guide provides steps for initial diagnostics and common resolutions.

#### Initial Diagnostic Steps

1. **Check User Status:**
   - Ensure the user experiencing the error has an active account with the right permissions.
   - Verify if there are any ongoing issues regarding account suspension or deactivation.

2. **Examine Service Health:**
   - Go to the Microsoft Azure Service Health dashboard to check for any ongoing outages or incidents related to Azure Active Directory (AAD) or MSODS.

3. **Review Rate Limits:**
   - Verify whether the application is hitting any API rate limits set by Azure AD or MSODS.

4. **Analyze Error Details:**
   - Collect detailed error messages, including timestamps and user context, for further analysis.

5. **Reproduce the Error:**
   - Try to reproduce the error in a controlled environment where you can observe the behavior reliably.

#### Common Issues That Cause This Error

1. **Configuration Errors:**
   - Incorrect app registrations or misconfigured redirect URIs in Azure AD.

2. **Network Issues:**
   - Network connectivity problems between your application and the MSODS endpoints.

3. **Permission Issues:**
   - Lack of required permissions for the application trying to access the MSODS services.

4. **Service Interruption:**
   - Temporary interruptions or maintenance periods affecting MSODS services.

5. **Token Issuance Problems:**
   - Issues with the issuance or validation of access tokens by Azure AD.

#### Step-by-Step Resolution Strategies

1. **Verify App Registration:**
   - Log into the Azure portal and navigate to Azure Active Directory > App registrations.
   - Confirm that the application is registered and that the redirect URIs are correctly set up.

2. **Validate API Permissions:**
   - Under the app registration, check "API permissions" to ensure necessary permissions are granted.
   - Make sure to grant admin consent for those permissions if required.

3. **Check Authentication Flows:**
   - Verify that the authentication flow being used is supported by your app.
   - If necessary, test different authentication flows (e.g., authorization code, implicit).

4. **Inspect Conditional Access Policies:**
   - Review any conditional access policies that might be affecting user access to the MSODS services.

5. **Implement Network Monitoring:**
   - Use tools such as Fiddler or Network Tracing (nettrace) to observe the network calls made by your application.

6. **Examine Logs:**
   - Check Event Viewer logs on the relevant servers for .NET or WCF application logs that might provide more context.

7. **Open a Support Ticket:**
   - If the above steps do not resolve the issue, escalate by opening a support ticket with Microsoft, providing all gathered diagnostics.

#### Additional Notes or Considerations

- **Environment Isolate:** If you're running applications in multiple environments (test, production), validate whether this error occurs across all or is isolated to one environment.
- **Recent Changes:** Reflect on any recent changes (code deployments, configuration changes) that might have inadvertently caused the error.

#### Documentation for Guidance

- [Azure Active Directory Documentation](https://docs.microsoft.com/en-us/azure/active-directory/) – Resource for configuring Azure AD features.
- [MSODS and Azure AD Troubleshooting Guide](https://docs.microsoft.com/en-us/azure/active-directory/develop/troubleshoot-authentication) – Specific troubleshooting tips related to Azure AD.
- [Fiddler Documentation](https://www.telerik.com/fiddler) – Information on how to use Fiddler for debugging HTTP requests.
- [Event Viewer Documentation](https://docs.microsoft.com/en-us/windows/win32/sysinternals/event-viewer) – Guide on how to utilize the Event Viewer in Windows for logging.

#### Data Collection for Diagnostics

When reporting the issue or troubleshooting, collect the following logs:

1. **Event Viewer Logs:**
   - Collect relevant logs from the Application and System branches.

2. **Network Tracing with nettrace:**
   - Use this tool to capture network calls and response states.

3. **Fiddler Logs:**
   - Monitor and log HTTP/HTTPS traffic to capture the error message and additional information.

4. **Detailed Error Messages:**
   - Highlight all the details around when and where the error occurred, including timestamps and involved endpoints.

By following this detailed guide, you should be able to diagnose and potentially resolve the AADSTS90036 error or at least collect enough information to assist Microsoft support in addressing the underlying issue.