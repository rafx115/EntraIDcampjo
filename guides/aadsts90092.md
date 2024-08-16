# AADSTS90092: GraphNonRetryableError


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS90092 (GraphNonRetryableError)

**Description:**  
The error code AADSTS90092 indicates a non-retryable error related to Microsoft Graph API calls, often due to authorization issues, permissions, or request-related problems. This error suggests that the request could not be processed for a reason that isn't expected to be resolved by retrying.

---

### 1. Initial Diagnostic Steps

1. **Identify Context**: Determine the context in which the error occurs. Is it during application authentication, API calls, or user sign-ins?
   
2. **HTTP Response Analysis**: Capture the HTTP response body. This often contains additional details about the error that can help in diagnosing the specific issue.

3. **Reproduce the Error**: Try to reproduce the error with the same parameters to understand better the cause.

4. **Check Application Permissions**: Verify that the application has the correct permissions set up in the Azure portal.

5. **User Context**: Confirm the user account causing the issue is active and doesn't have any conditional access policies that might prevent access.

---

### 2. Common Issues That Cause This Error

- **Insufficient Permissions**: The application lacks the necessary Graph API permissions.
  
- **Invalid or Expired Access Token**: The access token used is either invalid or expired, leading to authentication failure.

- **Misconfigured Application Registration**: Issues in the Azure application registration such as incorrect reply URLs or missing permissions.

- **API Limitations**: The request being made could exceed the rate limits set by Microsoft Graph.

- **User Licenses and Entitlements**: The user may be lacking appropriate licenses or entitlements required to access the requested resources.

---

### 3. Step-by-Step Resolution Strategies

1. **Review API Permissions**:
   - Go to Azure Portal > Azure Active Directory > App registrations > Your application > API permissions.
   - Ensure that all required permissions are granted and consented.

2. **Re-Authenticate**:
   - Make sure the token is refreshed if you have existing access tokens.
   - Use the latest Microsoft Authentication Library (MSAL) to acquire tokens.

3. **Check Application Configuration**:
   - Verify the application registration in Azure:
     - Ensure that the Redirect URI is correctly set.
     - Check for any platform-specific configurations (Web, Mobile, etc.).

4. **Check for User Activation Issues**:
   - Ensure the user account is active and doesn’t have any restrictions.
   - Review user licenses in Azure Active Directory.

5. **Handle Rate Limits**:
   - If applicable, implement throttling to respect Microsoft Graph rate limits.
   - Monitor the number of calls made to the API to avoid 429 errors.

6. **Test with Graph Explorer**:
   - Use the Microsoft Graph Explorer to test the API calls and see if they succeed under the same permissions.

7. **Implementation of Error Handling**:
   - Implement proper error handling logic to manage different types of error responses gracefully.

---

### 4. Additional Notes or Considerations

- Ensure that you are making API calls from a context (application/user) that has permission to do so.
- Regularly review and audit API permissions as your application evolves.
- Be aware of any recent changes in Microsoft Graph API that might affect your application's functionality.

---

### 5. Documentation for Guidance

- [Microsoft Graph Permissions Reference](https://docs.microsoft.com/en-us/graph/permissions-reference)
- [Microsoft Identity Platform and OAuth 2.0 Authorization Code Flow](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow)
- [Troubleshoot Azure AD Authentication](https://docs.microsoft.com/en-us/azure/active-directory/develop/troubleshoot-authentication)
- [Graph API Rate Limits](https://docs.microsoft.com/en-us/graph/throttling)

---

### 6. Advice for Data Collection (Event Viewer Logs, Nettrace, Fiddler)

- **Event Viewer Logs**: Check for any relevant application logs under "Applications and Services Logs" pertaining to Azure AD or the application’s own logs if available.

- **Nettrace Logs**: 
  - Consider using .NET Tracing (if applicable) to gather detailed execution logs.
  - Use tools like the Windows Performance Recorder to capture comprehensive trace logs.

- **Fiddler**:
  - Use Fiddler to capture the HTTP traffic during API calls. Look for the headers and body of requests and responses to identify issues with authentication or permissions.

- **Log All Attempts**: Ensure you log all attempts, including request URLs and error responses, to have a clearer picture of the context in which failures occur.

By following these guidelines, you should be able to diagnose and resolve the AADSTS90092 error effectively.