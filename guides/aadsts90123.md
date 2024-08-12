
# AADSTS90123: IdentityProviderAccessDenied - The token can't be issued because the identity or claim issuance provider denied the request.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS90123 Error Code

**Error Overview:**
- **Error Code:** AADSTS90123
- **Description:** IdentityProviderAccessDenied - The token can't be issued because the identity or claim issuance provider denied the request.

### Initial Diagnostic Steps

1. **Review User Credentials:**
   - Ensure that the user is using the correct credentials (username/password).
   - Verify if the user's account is active and not locked out.

2. **Check Tenant Configuration:**
   - Review the Azure AD tenant settings to ensure the identity providers are correctly configured.
   - Confirm that the identity provider (like ADFS, social logins, etc.) is active.

3. **User Permissions:**
   - Ensure that the user has the necessary permissions to access the application.
   - Verify group memberships assigned to the user.

4. **Inspect Claim Sets:**
   - Check the claims being requested in the authentication process and ensure they align with what the identity provider is expecting.

### Common Issues that Cause This Error

1. **Access Policy Denial:**
   - The identity provider may have policies that deny access based on conditions like user group membership or location.

2. **Misconfigured Identity Provider:**
   - Incorrect configuration in the identity provider settings may lead to request denial.

3. **Claims Transformation Issues:**
   - Misconfiguration in claims mappings can result in unexpected denial from the identity provider.

4. **Multi-factor Authentication (MFA):**
   - If MFA is required but not completed by the user, access will be denied.

5. **Service Principal Issues:**
   - The service principal associated with the application might not have the required permissions to access the identity provider.

### Step-by-Step Resolution Strategies

1. **Verify User Details:**
   - Confirm that the user's account is active and meets any specific access policies.
   - If the user is part of a Conditional Access group, verify that the group has necessary conditions fulfilled.

2. **Review Identity Provider Configuration:**
   - Go to Azure AD -> External Identities -> Identity providers, and check the status and configuration of the identity provider.
   - Check for any detailed logs or messages that indicate why the request was denied.

3. **Audit Access Policies:**
   - Navigate to Azure AD -> Security -> Conditional Access and review policies that might affect the user or identity provider.
   - Disable or modify the policies temporarily for testing.

4. **Inspect Logs:**
   - Review sign-in logs under Azure AD -> Sign-ins for detailed error messages related to the failed token request.
   - Look for the specific request in the logs to gather additional context about the failure.

5. **Claims Configuration Check:**
   - If using claims mapping, navigate to the application registration and review the 'Token configuration' section to ensure claims are correctly set up.

6. **Testing with Different Accounts:**
   - Attempt to log in with a different user account that is known to work successfully. This can help isolate whether the issue is user-specific.

7. **Testing Identity Provider Response:**
   - Conduct tests using tools like Postman to simulate requests to the identity provider to see if the same issue occurs outside of your application.

### Additional Notes or Considerations

- Ensure that the user is not located in a region or device that's specifically blocked by the identity provider's policies.
- Temporary changes to identity provider settings to allow wide access can be useful for identifying the root cause, but should be reverted once testing is complete.

### Documentation for Guidance

- [Microsoft Azure AD Error Codes](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-error-codes)
- [Managing Identity Providers in Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/external-identities/identity-providers)
- [Conditional Access in Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/conditional-access/overview)

### Advice for Data Collection

1. **Event Viewer Logs:**
   - Check logs related to authentication events, focusing on any application or service logs that might indicate issues during the authentication process.
   - Look for related Application, Security, or System logs that coincide with the time of the authentication failure.

2. **Network Tracing Tools:**
   - Use `NetTrace` or a similar utility to capture network traffic during the authentication process to analyze any potential request/response issues.
   - If using Fiddler, ensure HTTPS traffic is decrypted, as it can provide insights into the headers and responses from the identity provider.

3. **Fiddler Usage:**
   - Set up Fiddler to capture traffic and inspect the request/response details for insights into why the identity provider denied the token.
   - Look specifically for error messages in the HTTP response body that may give further guidance on the failure.

By following this guide, you should be able to diagnose and resolve the AADSTS90123 error effectively.