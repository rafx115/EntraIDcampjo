# AADSTS90043: NationalCloudAuthCodeRedirection - The feature is disabled.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS90043

**Error Code Description**: AADSTS90043 - NationalCloudAuthCodeRedirection: The feature is disabled.

#### Initial Diagnostic Steps

1. **Identify the Context**:
   - Determine under which circumstances the error occurs. Is it during user authentication, application access, or while redirecting after authentication?
   - Check if the error is affecting all users or just specific accounts.

2. **Check Azure Active Directory (AAD) Settings**:
   - Review the settings specifically related to cloud and national cloud configurations.
   - Confirm if the National Cloud features are enabled in your AAD setup.

3. **Review Error Message Details**:
   - Look for any additional error messages or codes that may accompany AADSTS90043 to gather more context about the failure.

#### Common Issues that Cause this Error

1. **Feature Disabled**:
   - The specific feature of National Cloud Auth Code Redirection might be disabled for your tenant, which results in the AADSTS90043 error.

2. **Incorrect Application Registration**:
   - The application may be incorrectly registered in Azure, or the redirect URIs may not be set up properly.

3. **User Permissions and Roles**:
   - Ensure users trying to authenticate have the right permissions and roles assigned to access the application.

4. **Conditional Access Policies**:
   - Check if there are conditional access policies that might block users based on location, device state, or other conditions.

#### Step-by-Step Resolution Strategies

1. **Enable the National Cloud Feature**:
   - If your organization requires National Cloud Auth Code Redirection, log into the Azure Portal:
     - Navigate to **Azure Active Directory**.
     - Check under **Enterprise applications** or **App registrations** to see if the National Cloud feature can be toggled on/off. Ensure that necessary settings are enabled.

2. **Review and Correct Application Registration**:
   - Go to **App registrations** in Azure AD:
     - Ensure that the redirect URIs set in the application match exactly with those defined in the application code.
     - Verify that the application is set up to use the correct national cloud (e.g., Azure Government, Azure China) if applicable.

3. **Check User Permissions**:
   - In the Azure Portal:
     - Navigate to **Azure Active Directory > Users**.
     - Check the roles assigned to the affected users, ensuring they have permission to access the application.

4. **Modify Conditional Access Policies**:
   - Go to **Security > Conditional Access**:
     - Review policies to identify any potential blocking rules. Modify or create exceptions based on your organization's requirements, ensuring that authentication flows are not blocked.

5. **Test the Changes**:
   - After making changes, test the application access to determine if the issue has been resolved. Clear browser cache or use an incognito window to eliminate cached states.

#### Additional Notes or Considerations

- Ensure that any changes made do not unintentionally create security vulnerabilities. Always follow your organization’s security policies.
- Communication with Azure support may be required if the feature settings appear correct but the error persists.

#### Documentation for Guidance

- [Azure AD Identity Protection documentation](https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview)
- [App registrations in Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)
- [Conditional Access in Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/conditional-access/overview)

**Testing Documentation Reachability**:
- To test if the documentation can be reached, click on the links provided or copy and paste them into your web browser. Ensure that you have proper permissions to view these documents.

#### Advice for Data Collection

- **Logs**: Enable and collect logs from Azure AD to track authentication events.
- **Error Reports**: Capture any error reports that users might see at the time of the failure.
- **User Feedback**: Collect input from affected users about their experiences, the time of occurrence, and the actions taken prior to encountering the error.
- **Network Information**: Gather information about the network conditions during the authentication attempt (VPN usage, geographic location).

Following this troubleshooting guide should help in diagnosing and resolving the AADSTS90043 error effectively.