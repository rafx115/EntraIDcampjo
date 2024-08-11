
# AADSTS90090: GraphRetryableError - The service is temporarily unavailable.


## Troubleshooting Steps
**Troubleshooting Guide for AADSTS90090: GraphRetryableError - The service is temporarily unavailable**

### Overview
The error code AADSTS90090 indicates that the Microsoft Azure Active Directory (AAD) Graph API is currently experiencing a temporary service issue. This can disrupt interactions with the API, such as user authentication or token retrieval.

### Initial Diagnostic Steps
1. **Check Service Health:**
   - Visit the [Azure Status page](https://status.azure.com/en-us/status) to see if there are any ongoing outages or service issues affecting Azure services, particularly AAD.
  
2. **Verify Error Occurrence:**
   - Confirm that the error consistently occurs and not just sporadically. Note the frequency and timing of the errors.

3. **Review Application Id and Permissions:**
   - Ensure that the application requesting access has the proper permissions and that the relevant API permissions have been granted.

### Common Issues that Cause this Error
- Temporary outages or high traffic on the Azure service.
- Misconfigured application settings or permissions in Azure AD.
- Rate limiting due to excessive requests in a short time frame.
- Insufficient permissions to access certain API resources.
- Network-related issues on the client's side preventing connectivity to Azure services.

### Step-by-Step Resolution Strategies
#### Step 1: Temporary Workaround
- Wait and retry the operation after a few minutes. The error is temporary and may resolve itself as the service becomes available again.

#### Step 2: Check for Rate Limiting
- Monitor API calls made in a short period. If the application is making too many requests, consider implementing exponential backoff in request attempts to handle rate limits gracefully.

#### Step 3: Ensure Configuration is Correct
1. **Review Azure AD App Registration:**
   - Navigate to the Azure portal, and select your app registration.
   - Ensure API permissions are configured correctly. If necessary, grant admin consent for the permissions.

2. **Check Redirect URIs:**
   - Ensure that the redirect URIs specified match those used in your application.

3. **Clear Azure AD Tokens:**
   - Sometimes stale tokens can cause issues. Clear existing tokens associated with your application and attempt to sign in again.

#### Step 4: Monitor Service Updates
- Keep an eye on the Azure Status page and monitor your application to see if the issue resolves itself over time.

### Additional Notes or Considerations
- If the error persists beyond a reasonable time, it may be beneficial to open a support request with Azure Support.
- If your application is critical, consider implementing failover logic or service redundancy to mitigate the impact of such errors.

### Documentation for Guidance
- Azure AD Graph API Documentation: [Microsoft Graph API Overview](https://docs.microsoft.com/en-us/graph/overview)
- Azure Status: [Azure Service Health Dashboard](https://status.azure.com/en-us/status)
- Implementing Exponential Backoff for Retry Logic: [Best Practices for Azure API Management](https://docs.microsoft.com/en-us/azure/api-management/api-management-best-practices#retry-policies)

### Test Documentation Reachability
- The links provided in the documentation section should be accessible. 
  - For example, visit the [Microsoft Graph API Overview](https://docs.microsoft.com/en-us/graph/overview) and ensure the page loads without issues.

### Advice for Data Collection
- Collect logs from your application that include:
  - Timestamp of the error occurrence.
  - Request and response details when the error was faced (excluding sensitive information).
  - Frequency of the requests made leading up to the error.
- If the error persists, consider running a network trace to see if requests to the Azure service are being blocked or failing.

By following this guide, you can effectively troubleshoot the AADSTS90090 error, minimize downtime, and potentially improve the resilience of your application.