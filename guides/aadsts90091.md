# AADSTS90091: GraphServiceUnreachable


## Troubleshooting Steps
**Troubleshooting Guide for Error Code AADSTS90091 (GraphServiceUnreachable)**

### Overview
Error code **AADSTS90091** indicates that Azure Active Directory (AAD) is unable to reach the Microsoft Graph service. This can affect applications that rely on Microsoft Graph for accessing AAD data and functionality.

### Initial Diagnostic Steps
1. **Check Service Status**: 
   - Visit the **Microsoft Service Health** dashboard to check if there are any ongoing issues with Azure Active Directory or Microsoft Graph.
   - Link: [Azure Service Health Status](https://status.azure.com/en-us/status)

2. **Identify Context**: 
   - Determine when and how often this error is occurring. Is it consistent or intermittent? Identify if it occurs at specific times or under certain load conditions.

3. **Environment Check**: 
   - Confirm the environment (e.g., production, development) where the error surfaced.
   - Review any changes that occurred around the time the error started appearing.

### Common Issues that Cause this Error
- **Network Issues**: Temporary network disruptions or latency between the application and Microsoft Graph.
- **API Throttling**: If requests exceed the allowed number of API calls, Microsoft Graph may reject subsequent calls.
- **Configuration Errors**: Issues in the registered application in Azure AD that could misconfigure permissions/scopes.
- **Service Outage**: Temporary issues on the Microsoft Graph side.

### Step-by-Step Resolution Strategies
1. **Network Connectivity**:
   - Run ping tests or traceroutes from the application server to the Microsoft Graph endpoints to check for connectivity issues.
   - Verify firewall settings to ensure they allow outbound traffic to Microsoft Graph.

2. **Review Application-Specific Limits**:
   - Check your application for throttling by reviewing the response headers when a request to the Graph API fails.
   - If throttling is suspected, implement retry logic with exponential backoff.

3. **Validate Application Permissions**:
   - Go to the Azure portal and review the permissions granted to your application.
   - Ensure that the necessary Microsoft Graph API permissions are consented and granted to your application.
   - Link: [API Permissions in Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/develop/permissions-reference)

4. **Examine Logs**:
   - Enable logging in your application to capture request and response details when accessing Microsoft Graph.
   - Look at any error messages or statuses returned by the Graph API.

5. **Utilize Graph Explorer**:
   - Test the Microsoft Graph API manually using the [Graph Explorer](https://developer.microsoft.com/en-us/graph/graph-explorer) to see if you encounter the same error.
   - This tool can help debug API availability independently of your application.

### Additional Notes or Considerations
- Ensure you are following best practices for managing API calls to avoid throttling.
- Implement robust error handling to gracefully manage temporary service unavailability.
- Monitor performance metrics and logs before and after implementing changes to help identify the impact of resolutions.

### Documentation for Guidance
- [Azure Active Directory Troubleshooting Azure AD Graph API](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-graph-api-troubleshooting)
- [Microsoft Graph API Documentation](https://docs.microsoft.com/en-us/graph/overview)
- [Managing Microsoft Graph API Permissions](https://docs.microsoft.com/en-us/graph/auth-v2-service#permissions)

**Test Reachability of Documentation:**
- Access the above links to ensure they are reachable and contain the necessary guidance. 

### Advice for Data Collection
- Gather the following data for easier troubleshooting:
  - Timestamps when the error occurs.
  - Full error messages returned from AAD or Graph API.
  - Application logs showing request and response details.
  - Network logs, including any potential connectivity issues or interruptions.
  - API call count near the time of the error.

If the problem persists after following these steps, consider reaching out to Microsoft Support with the gathered data for further assistance.