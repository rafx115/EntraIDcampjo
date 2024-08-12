# AADSTS50058: UserInformationNotProvided - Session information isn't sufficient for single-sign-on. This means that a user isn't signed in. This is a common error that's expected when a user is unauthenticated and hasn't yet signed in.If this error is encountered in an SSO context where the user has previously signed in, this means that the SSO session was either not found or invalid.This error might be returned to the application if prompt=none is specified.


## Troubleshooting Steps
## Troubleshooting Guide for AADSTS50058 Error

### Overview of AADSTS50058
The AADSTS50058 error indicates that a user session is not established or is not in a state sufficient for Single Sign-On (SSO) to occur. It often arises when a user has not signed in or an expected SSO session is unavailable or invalid. This error can be returned when the `prompt=none` parameter is specified, meaning that the application is attempting to sign in the user without prompting them for credentials.

### Initial Diagnostic Steps
1. **Identify the Context**: Determine whether the user is authenticated at the time the error occurs.
2. **Check User Account Status**: Ensure that the user account is active and has the necessary permissions in Azure Active Directory (AAD).
3. **Review Application Configuration**: Verify that the application is correctly configured for SSO and that the right redirect URIs are set up in AAD.
4. **Analyze User Environment**: Inspect user settings and browser configurations that could affect authentication.

### Common Issues that Cause AADSTS50058
- **Session Timeout**: The user session has expired due to inactivity.
- **Invalid or Missing Cookies**: Cookies required for SSO may not have been set or have been deleted.
- **Incorrect Application Registration**: Misconfiguration in Azure AD concerning the application settings.
- **Network Issues**: Problems with network connectivity that would prevent the application from communicating with AAD.
- **Browser Settings**: Strict cookie settings or third-party browser extensions might be interfering with the authentication process.

### Step-by-Step Resolution Strategies
1. **Check User Authentication**:
   - Ask the user to confirm if they are signed in to their account in another tab or application.
   - If not, direct the user to sign in properly before attempting to execute the action that leads to the error.

2. **Clear Browser Cache and Cookies**:
   - Advise the user to clear their browser's cache and cookies, which can resolve issues related to invalid session data.

3. **Ensure Proper Application Registration**:
   - Log in to the Azure portal and navigate to Azure Active Directory.
   - Check the application’s registration and verify that the redirect URIs are correct.
   - Ensure the application permissions required for SSO are granted.

4. **Review SSO Configuration**:
   - Ensure the SSO settings for the application are correctly configured by revisiting the SSO settings in Azure AD.
   - Validate that the `prompt=none` parameter is used correctly and aligns with the application's behavior.

5. **Investigate Session Size/Timeout Configuration**:
   - Adjust session timeout policy settings in Azure AD if necessary, ensuring they align with user's needs.

6. **Test with Different Browsers or Clear Extensions**:
   - Ask the user to attempt logging in from a different browser or incognito mode.
   - Disable any browser extensions that may be interfering with authentication.

7. **Examine User Role and Permissions**:
   - Ensure that the user has the appropriate role assigned in Azure AD to access the application.

### Additional Notes or Considerations
- If the problem persists after following the above steps, explore potential back-end issues or connection settings between the application and AAD.
- Test the functionality in different environments (e.g., production vs. non-production).
  
### Documentation for Guidance
- [Azure AD Error Codes Documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/reference-aad-error-codes)
- [Implementing Azure AD SSO](https://docs.microsoft.com/en-us/azure/active-directory/develop/scenario-web-app-sign-user-overview)

### Data Collection for Further Troubleshooting
- **Event Viewer Logs**:
   - Look into the Application and Security logs for any authentication errors or warnings related to Azure AD.
- **Network Tracing (NetTrace)**:
   - Capture the network requests made during authentication. This includes headers and payload for visibility into the authentication flow.
- **Fiddler**:
   - Use Fiddler to monitor HTTP requests between the application and Azure AD. Check the responses and any error messages that can provide insight.

### Conclusion
Following this guide will help diagnose and resolve the AADSTS50058 error systematically. Documenting each step taken and the context surrounding the issue will enable further assistance if necessary. Always ensure that the user environment is checked first, as it often contributes to authentication issues.