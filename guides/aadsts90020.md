# AADSTS90020: The SAML 1.1 Assertion is missing ImmutableID of the user. Developer error - the app is attempting to sign in without the necessary or correct authentication parameters.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS90020

**Error Description:**  
The error code AADSTS90020 indicates that the SAML 1.1 Assertion is missing the ImmutableID of the user. This issue arises when there are incorrect or missing authentication parameters during the sign-in process. The system cannot match the user to their Azure AD identity, causing the authentication to fail.

### Initial Diagnostic Steps

1. **Review the Error Message:**
   - Analyze the full error message in the context of the application attempting the authentication. Look for any additional details provided that may point to the source of the issue.

2. **Check the Application Configuration:**
   - Verify that the application is properly configured in Azure Active Directory (Azure AD).
   - Confirm that the SAML settings (including the Assertion Consumer Service URL, Entity ID, etc.) are correctly defined.

3. **Inspect the AAD Logs:**
   - Navigate to Azure Active Directory Admin Center and check the sign-in logs for any related entries that may provide further context on why the authentication failed.

### Common Issues that Cause This Error

1. **Missing ImmutableID:**
   - The SAML assertion does not include the ImmutableID claim, which is used to uniquely identify the user in Azure AD.

2. **Incorrect Claim Mapping:**
   - The application may be misconfigured to expect a different claim or not correctly mapping the claims from the Identity Provider.

3. **Wrong Authentication Parameters:**
   - Ensure that the application is attempting to sign in with the correct parameters. This could include incorrect username or any other parameter required for authentication. 

4. **User Not Federated:**
   - The user attempting to sign in might not be federated or may not exist in the Azure AD tenant.

### Step-by-Step Resolution Strategies

1. **Check SAML Assertion Claims:**
   - Use tools like Fiddler, Postman, or browser developer tools to capture the SAML assertion being sent to Azure AD during the sign-in process.
   - Ensure the assertion contains the ImmutableID claim. If it's missing, investigate why the Identity Provider does not send it.

2. **Update Identity Provider Configuration:**
   - If the ImmutableID claim is not being sent, review and modify the Identity Provider configuration to ensure it is set to include this claim in the assertion.

3. **Correct Application Settings:**
   - In Azure AD:
     - Go to **Enterprise applications** > Select your application > **Single sign-on** > **SAML-based Sign-on**.
     - Check the **User attributes and claims** section to ensure the claim for ImmutableID is mapped correctly.

4. **Testing with Another User:**
   - If feasible, try to authenticate using a different user account that is known to be correctly set up in the Azure AD. This can help determine if the issue is user-specific.

5. **Review and Assign Correct User Roles:**
   - Ensure the user has the necessary roles assigned in Azure AD that allow them to sign in to the application.

### Additional Notes or Considerations

- **User Permissions:** Ensure that the user attempting to sign in has the necessary permissions and is part of the correct Azure AD groups.
  
- **Update Documentation:** Familiarize yourself with proper SAML assertion structures and claims used in Azure AD to avoid misconfigurations.

### Documentation for Further Guidance

- [Microsoft Azure AD SAML authentication documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/identity-provider-saml-sso)
- [Troubleshooting SAML authentication issues](https://docs.microsoft.com/en-us/azure/active-directory/develop/troubleshoot-saml-protocol)
- [Configuring SAML claims mapping](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-claims-mapping)

### Advice for Data Collection (Event Viewer Logs, Nettrace, Fiddler)

- **Fiddler or Postman:**
  - Use Fiddler to capture the requests/responses.
  - Look for SAML assertions in HTTP responses and check them for missing claims.
  
- **Event Viewer Logs:**
  - Check the application event logs on the server running the app for any relevant logs that coincide with the failed authentication attempts.
  
- **Network Tracing (Nettrace):**
  - Use tools like `netsh trace` for capturing network packets if there are suspicions of network-level issues.

- **Log Analysis:**
  - Analyze the captured logs to look for HTTP status codes, errors, and unexpected behavior during the authentication flow.

Following this guide should help in diagnosing and resolving the error code AADSTS90020 and ensuring proper configuration for SAML authentication with Azure AD.