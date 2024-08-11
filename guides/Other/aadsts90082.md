# AADSTS90082: OrgIdWsFederationNotSupported - The selected authentication policy for the request isn't currently supported.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS90082 Error

AADSTS90082, with the description “OrgIdWsFederationNotSupported - The selected authentication policy for the request isn't currently supported”, typically occurs in scenarios involving Microsoft Azure Active Directory (Azure AD) when there is a misconfiguration related to authentication policies, particularly when using Windows Federation Authentication. Here’s a detailed guide to troubleshoot and resolve this error.

#### Initial Diagnostic Steps

1. **Identify the Context**: 
   - Determine when the error occurs (e.g., during sign-in, when accessing a specific application).
   - Note the specific application and the type of authentication being used.

2. **Check Logs**:
   - Review the logs in Azure AD, Application Insights, or the application itself to gather additional context around the error.
   - Look for patterns or additional error messages that could provide more insight.

3. **User Context**:
   - Confirm if this is affecting all users in the organization or just specific users or groups.

#### Common Issues that Cause this Error

1. **Unsupported Authentication Method**: 
   - The application or request is configured to use a federation authentication method not supported by Azure AD for the given policy.

2. **Incorrect Configuration**:
   - Misconfigured authentication policies in the Azure AD settings or in the application’s settings.

3. **Federation Metadata Issues**:
   - Problems with the federation metadata document being incorrectly configured, inaccessible, or outdated.

4. **Policy Changes**:
   - Recent changes in authentication policies or settings that haven’t propagated properly.

5. **Service Interruption**: 
   - Temporary issues with Azure services or network connections that may impact authentication.

#### Step-by-Step Resolution Strategies

1. **Review and Update Authentication Policies**:
   - Sign into the Azure portal and navigate to “Azure Active Directory” -> “Enterprise applications”.
   - Locate the application that is generating the error and review its authentication settings.
   - Ensure the authentication methods and policies align with what the application requires.

2. **Verify Federation Settings**:
   - Check the configuration of your federation service (e.g., ADFS) to ensure it is properly integrated with Azure AD.
   - Look for any discrepancies or errors in the federation metadata URL.

3. **Disable Unsupported Authentication**:
   - If the application is set to use a federation authentication method that isn't supported, consider switching to a supported method (e.g., OAuth or SAML).
   - Update the application settings accordingly to use a different authentication mechanism if necessary.

4. **Testing Configuration Changes**:
   - After making changes, attempt to reproduce the issue to verify if the error persists.
   - Conduct tests with different users or groups to ensure that changes apply universally.

5. **Fallback Plan**:
   - Maintain and implement a fallback to original settings until a solution is verified to avoid disruptions.

#### Additional Notes or Considerations

- Ensure all changes done in Azure AD are properly documented and restored if necessary.
- Consider cross-checking with Azure AD service health for any reported issues during the time of error occurrence.
- Understand user consent and permissions, especially if modifications were performed on application permissions.

#### Documentation and Resources

1. **Azure AD Overview**:
   - [Overview of Azure Active Directory](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-overview)

2. **Configure Authentication**:
   - [Configure sign-in options for your app in Azure AD](https://learn.microsoft.com/en-us/azure/active-directory/develop/active-directory-how-to-configure-authentication)

3. **Troubleshoot Sign-in Errors**:
   - [Troubleshoot sign-in errors in Azure AD](https://learn.microsoft.com/en-us/azure/active-directory/user-help/user-help-troubleshoot-sign-in)

#### Test Documentation Reachability

Please verify that the following links to Microsoft documentation are reachable:
- [Overview of Azure Active Directory](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-overview)
- [Configure sign-in options for your app in Azure AD](https://learn.microsoft.com/en-us/azure/active-directory/develop/active-directory-how-to-configure-authentication)
- [Troubleshoot sign-in errors in Azure AD](https://learn.microsoft.com/en-us/azure/active-directory/user-help/user-help-troubleshoot-sign-in)

#### Advice for Data Collection

- When troubleshooting issues in Azure AD, it’s crucial to collect and log the following data:
    - Exact error messages and codes.
    - User details (e.g., usernames and sign-in attempts).
    - Timestamps when the errors occurred.
    - Configuration settings of the application and Azure AD relevant to authentication.
    - Any specific changes made recently in Azure or the application.

This information can be pivotal when engaging Microsoft Support if the issue persists or becomes complex.

Category: Other