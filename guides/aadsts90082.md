# AADSTS90082: OrgIdWsFederationNotSupported - The selected authentication policy for the request isn't currently supported.


## Troubleshooting Steps
Certainly! The error code AADSTS90082 indicates that the authentication policy selected for the request isn't currently supported, often arising in federated authentication scenarios.

### Detailed Troubleshooting Guide for AADSTS90082

#### Initial Diagnostic Steps
1. **Understand the Context**: Determine what action the user was attempting to perform when the error occurred. Was it a sign-in attempt, accessing a resource, or using a specific application?
  
2. **Check Authentication Policies**: Identify and review the authentication policies configured for your tenant or organization. Different policies may apply based on the user’s profile or the application being accessed.

3. **Reproduce the Error**: Attempt to reproduce the error using the same credentials or access patterns. This will help isolate if the issue is user or application-specific.

4. **Review User Information**: Identify if the user experiencing the error has any particular attributes that may affect their authentication, such as being from an unsupported federation or using a specific application.

#### Common Issues That Cause This Error
1. **Unsupported Federation Type**: The organization may be configured to use a specific federation type that doesn't support the requested authentication flow.
2. **Misconfigured Identity Providers**: If using federated authentication, the identity provider may not be set up correctly or might not support the requested policy.
3. **Authentication Policies**: The authentication policy being applied to this user may not support the method or scenario being requested (e.g. some policies may enforce MFA while others may not).
4. **User Scope or Role Issues**: The user may not have permissions or attributes required for the request, causing the failure.

#### Step-by-Step Resolution Strategies
1. **Validate Authentication Method**:
   - Ensure that the authentication method being used is compatible with your organization’s policies.
   - Modify the application settings if necessary to match supported authentication protocols (e.g., OAuth 2.0, SAML).

2. **Review Federation Configuration**:
   - Check the federation settings in Azure AD for your organization.
   - Confirm that the identity provider settings (e.g., SSO) are correctly configured and that there are no known outages on their side.

3. **Examine Authentication Policies**:
   - Go to Azure AD and check the sign-in policies or conditional access policies.
   - Modify or create a policy that accommodates the authentication scenario you are trying to support.

4. **Test with Different Accounts**:
   - Try using a different user’s account to access the same resource. This can help determine if the issue is specific to one user’s settings or wider.

5. **Azure AD Support**: If basic troubleshooting fails, consider reaching out to Microsoft's support for specialized help.

6. **Logs and Diagnostics**:
   - Collect relevant logs from Azure AD and the application's sign-in logs.
   - Analyze any other logs that may provide information about the authentication requests.

#### Additional Notes or Considerations
- **Review Updates and Changes**: Confirm whether any recent changes were made to authentication policies or federated identity provider settings that could have introduced the issue.
- **Communication with Identity Provider**: If using third-party identity providers, ensure that any updates or changes on their side are compatible with Azure AD.

#### Documentation for Guidance
- [Understanding Conditional Access](https://docs.microsoft.com/en-us/azure/active-directory/conditional-access/overview)
- [Configuring a Federation Provider](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-federation-services)
- [Azure Active Directory Authentication](https://docs.microsoft.com/en-us/azure/active-directory/develop/authentication-scenarios)

#### Advice for Data Collection
- **Event Viewer Logs**: Check Windows Event Viewer logs for any authentication-related entries. Look under Applications and Services Logs for Azure AD logs.
- **Network Traces**:
  - Use **Nettrace** to capture network activity during the authentication process, which may help identify issues with network requests.
  - Use **Fiddler** to capture HTTP(S) traffic during sign in; this can give insights into headers or responses leading to the error.
- Ensure all logs/screenshots are anonymized to protect user data before sharing.

By following this troubleshooting guide, you should be able to identify and resolve the underlying issues causing the AADSTS90082 error in your organization.