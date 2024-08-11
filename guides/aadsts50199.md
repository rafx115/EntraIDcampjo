
# AADSTS50199: CmsiInterrupt - For security reasons, user confirmation is required for this request. Interrupt is shown for all scheme redirects in mobile browsers.No action required. The user was asked to confirm that this app is the application they intended to sign into.This is a security feature that helps prevent spoofing attacks. This occurs because a system webview has been used to request a token for a native application.To avoid this prompt, the redirect URI should be part of the following safe list:http://https://chrome-extension:// (desktop Chrome browser only)


## Troubleshooting Steps
### Detailed Troubleshooting Guide for Error Code AADSTS50199: CmsiInterrupt

#### Initial Diagnostic Steps:
1. **Identify the Context**: Understand when and where the error occurs. Note if it's during sign-in, authentication, or token request processes.
2. **Check Redirect URI**: Ensure the redirect URI being used is correct and matches the configuration settings in your app's identity provider.
3. **Verify Browser Settings**: Confirm the browser settings for the user/device experiencing the issue.
4. **Review Logs**: Look for any specific error messages or warnings in application logs or identity provider logs that might provide more context.

#### Common Issues that Cause this Error:
- Incorrect or mismatched redirect URI settings.
- Using a system webview for token requests instead of a browser for a native application.
- Missing or incorrect configuration settings in the identity provider or app.

#### Step-by-Step Resolution Strategies:
1. **Review Redirect URI**: Ensure that the redirect URI used in your application matches the authorized redirect URIs in your app settings.
2. **Update App Configuration**: Modify the app configuration settings to correctly handle the authentication and authorization flows.
3. **Use Browser for Token Requests**: For native applications, make sure to use a browser for token requests instead of a system webview.
4. **Add Redirect URI to Safe List**: Add the necessary redirect URI to the safe list as mentioned in the error message to prevent the interrupt prompt.
5. **Clear Browser Cache**: Clear the cache and cookies on the browser to ensure that no stored data is causing conflicts.

#### Additional Notes or Considerations:
- **Security Feature**: The CmsiInterrupt is a security feature to prevent spoofing attacks, so it's important not to bypass it without proper verification.
- **User Confirmation**: User confirmation is required as part of the security protocols, and no immediate action may be needed from your end.

#### Documentation for Guidance:
- Microsoft Azure Active Directory documentation on handling authentication interruptions: [Azure AD Authentication Interruption Documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/authentication-interrupt).

By following these steps and considerations, you should be able to troubleshoot and resolve the error code AADSTS50199 related to the CmsiInterrupt successfully.