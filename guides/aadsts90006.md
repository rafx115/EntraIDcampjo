# AADSTS90006: ExternalServerRetryableError - The service is temporarily unavailable.


## Troubleshooting Steps
## Troubleshooting Guide for AADSTS90006: ExternalServerRetryableError - The Service is Temporarily Unavailable

### Understanding AADSTS90006:

The error code AADSTS90006 signifies that there is an external server issue causing temporary unavailability in connecting with Azure Active Directory (Azure AD). It is a retryable error, indicating that the request should be tried again after a brief pause.

<<<<<<< HEAD
### Initial Diagnostic Steps:
=======
3. **Resolution Strategies**:
   - **Step 1**: Confirm that the issue is not specific to your environment by checking with other users or contacting the identity provider's support.
   - **Step 2**: If the issue is widespread, wait for some time and try again later as it might be a temporary service outage.
   - **Step 3**: Check your network connection to ensure there are no issues preventing communication with the authentication service.
   - **Step 4**: Clear browser cache and cookies or try using a different browser to rule out any local issues.
   - **Step 5**: If the issue persists, contact the identity provider�s support for further assistance.
>>>>>>> 44a6fd6d2b08a07d1c083c6d7db8bca24b23c735

1. **Check Azure Status:**
   - Go to the [Azure Status Page](https://status.azure.com) to see if there are any ongoing service interruptions or outages affecting Azure AD services.

2. **Confirm the Time of Occurrence:**
   - Note the exact time when the error occurred. Temporary service issues may resolve quickly.

3. **Review Logs:**
   - Examine application and system logs to find related error metrics or patterns leading to the AADSTS90006 error.

4. **Reproduce the Error:**
   - Attempt to reproduce the error to establish its consistency. This can help in understanding if it's a systemic issue or not.

5. **Test Connectivity:**
   - Run network diagnostics to confirm that connectivity to Azure AD service endpoints is operational. Tools like `ping` or `tracert` may help check the network path.

### Common Issues That Cause this Error:

1. **Temporary Service Outages:**
   - Azure AD service experiencing temporary outages, which can affect application authentication requests.

2. **Service Throttling:**
   - Hitting the Azure AD API rate limits may lead to temporary failures.

3. **DNS Issues:**
   - DNS resolution problems may prevent proper communication with the Azure AD service.

4. **Network Configuration Issues:**
   - Firewalls, proxies, or network security groups that might block access to Azure services.

5. **Application Configuration Errors:**
   - Misconfigured Azure AD applications or invalid credentials might trigger error responses.

### Step-by-Step Resolution Strategies:

1. **Retry the Request:**
   - Since this is a retryable error, wait a few seconds to a minute and then retry the authentication request.

2. **Monitor Azure Status:**
   - If the Azure Status Page indicates an ongoing issue, wait for Microsoft to resolve the service outage before attempting again.

3. **Check for Configuration Issues:**
   - Ensure your application settings, such as redirect URIs, application secrets, and permissions are correctly configured in the Azure & its portal.

4. **Investigate Rate Limits:**
   - Review your application's use of Azure AD APIs and modify it to reduce the load if necessary.

5. **Examine Network Configuration:**
   - Verify that no outbound connections are being blocked to Azure AD endpoints. Test by accessing common Azure URLs and ensure they resolve correctly.

6. **DNS Resolution Tests:**
   - Flush your DNS cache and verify that DNS can resolve Azure AD services. Test by accessing Azure endpoints directly via the browser or using command-line tools (e.g., `nslookup`).

### Additional Notes or Considerations:

- Monitor for patterns when the issue occurs. If it's frequent but intermittent, additional logging and alerting in your application may be required.
- Be aware that retrying too quickly or too frequently can lead to throttling, further complicating the issue.

### Documentation for Additional Guidance:

For more information on troubleshooting Azure AD errors, you can find documentation here:
- [Azure Active Directory Error Code Reference](https://docs.microsoft.com/en-us/azure/active-directory/develop/reference-aad-error-codes)

### Test Documentation Reachability:

To test if the documentation is reachable, verify by visiting:
- [Azure Active Directory Error Code Reference](https://docs.microsoft.com/en-us/azure/active-directory/develop/reference-aad-error-codes)

**(Please check the documentation link to ensure it works for your access environment or system configuration.)**

### Advice for Data Collection:

When encountering the AADSTS90006 error, gather the following data for better troubleshooting:

1. **Error Message Details:**
   - Capture the full error message, including any stack traces or additional information provided by the system.

2. **Logs:**
   - Collect application logs, Azure AD sign-in logs, and any related debug information.

3. **Network Diagnostics:**
   - Document results from any network diagnostics, such as `ping`, `tracert`, or DNS tests.

4. **Request Hyperparameters:**
   - Document headers, payload, and API endpoints being requested when the error occurred.

5. **User Context:**
   - Note if the error is occurring for specific users or all users.

By following this structured guide, you should be able to troubleshoot and resolve the AADSTS90006 error effectively.