
# AADSTS50086: SasNonRetryableError


## Troubleshooting Steps
The error code AADSTS50086 with the description "SasNonRetryableError" typically occurs in scenarios involving Azure Active Directory (Azure AD) authentication failures. This guide will provide a comprehensive troubleshooting approach to resolve this error.

### Troubleshooting Guide for AADSTS50086 - SasNonRetryableError

#### Initial Diagnostic Steps
1. **Identify the Context of the Error**:
   - Determine when the error occurs (e.g., during sign-in, token acquisition, API calls).
   - Check if the user or service principal experiencing the error has previously signed in successfully.

2. **Check for Service Outages**:
   - Verify if there are any Azure service outages or incidents reported in the Azure Service Health dashboard.

3. **Review Logs**:
   - Collect relevant logs from Azure AD through Azure Portal or Azure Monitor.
   - Check if other users encounter the same error or if it’s isolated.

#### Common Issues that Cause this Error
- **Invalid Client Secrets or Certificates**: Ensure that the application’s client secrets or certificates used for authentication have not expired or been revoked.
- **Misconfigured Application Registrations**: Verify that the application registration in Azure AD is correctly configured, including redirect URIs and scopes.
- **Token Lifetime Policies**: Check if the token lifetime policies might be causing tokens to expire before they can be used.
- **Service Principal Permissions**: Ensure that the application/service principal has the necessary permissions granted in Azure AD.
- **MFA or Conditional Access Policies**: Conditions related to Multi-Factor Authentication (MFA) or other Conditional Access policies may be blocking access.

#### Step-by-Step Resolution Strategies
1. **Verify Application Registration**:
   - Go to Azure Portal > Azure Active Directory > App registrations.
   - Confirm the application exists and check its configuration settings, especially redirect URIs, scopes, and permissions.

2. **Check Client Secret**:
   - Under the app registration, navigate to Certificates & secrets.
   - If using a client secret, check if it’s expired and create a new one if necessary. Update your application with the new secret.

3. **Inspect Permissions**:
   - Still in the app registration, ensure the application has the necessary permissions. Review required API permissions and grant admin consent if necessary.

4. **Review Authentication Flow**:
   - Ensure that the application's authentication flow is correctly implemented, matching the defined implicit or authorization code flows.

5. **Examine Conditional Access Policies**:
   - Navigate to Azure Active Directory > Security > Conditional Access.
   - Identify any policies that might interfere with sign-in and adjust them as needed.

6. **Test with Another User**:
   - Check if the error persists with different user accounts. This helps identify if the issue is specific to a single user.

7. **Try Different Browsers or Devices**:
   - Sometimes, cached credentials or browser-specific issues can play a role. Test on multiple platforms to rule this out.

#### Additional Notes or Considerations
- **User Experience**: Make sure users know how to provide feedback if they experience this error, and document any additional details that they can provide (environment, device type, etc.).
- **Cutover Timing**: If your app recently changed configurations, allow time for propagation before testing.
- **Rate Limits**: Be aware of Azure AD rate limits that could affect the behavior of token requests.

#### Documentation for Further Guidance
- [Azure Active Directory documentation](https://docs.microsoft.com/en-us/azure/active-directory/)
- [Configure permission and consent](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-permissions-and-consent)
- [Authentication flow overview](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-overview)
- [Troubleshoot common Azure AD errors](https://docs.microsoft.com/en-us/azure/active-directory/develop/troubleshoot-authentication-azure-ad)

#### Advice for Data Collection
- **Event Viewer Logs**:
  - On Windows, check the Event Viewer under Applications and Services > Microsoft > Windows > AzureAD for relevant logs.
  
- **Network Tracing Tools**:
  - Capture network traffic using tools like **NetTrace** or **Fiddler** to see the actual requests being sent and the responses received from Azure AD.
  
- **Logging**:
  - Ensure that logging is enabled in your application to capture success/failure details during the authentication attempt, including timestamps, request IDs, and response codes.

#### Conclusion
The AADSTS50086 error often indicates a configuration issue or a problem with authentication parameters. Utilizing systematic troubleshooting steps will assist in identifying the root cause and implementing resolutions. Be proactive in checking Azure documentation and utilizing logging tools to help diagnose issues.