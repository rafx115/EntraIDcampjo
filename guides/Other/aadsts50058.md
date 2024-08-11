# AADSTS50058: UserInformationNotProvided - Session information isn't sufficient for single-sign-on. This means that a user isn't signed in. This is a common error that's expected when a user is unauthenticated and hasn't yet signed in.If this error is encountered in an SSO context where the user has previously signed in, this means that the SSO session was either not found or invalid.This error might be returned to the application if prompt=none is specified.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS50058 Error Code

**Error Code**: AADSTS50058  
**Description**: UserInformationNotProvided - Session information isn't sufficient for single-sign-on. This indicates that a user isn't signed in, leading to the error, particularly in scenarios where prompt=none is used.

---

### 1. Initial Diagnostic Steps

1. **Check the Error Message**:
   - Verify the full error message and context where it occurred. AADSTS50058 indicates a lack of user session.

2. **User Authentication Status**:
   - Confirm whether the user was indeed signed in previously. Lack of a valid session will trigger this error.

3. **Examine Application Logs**:
   - Review the application logs to find any prior authentication requests or SSO attempts that may provide insight into the session state.

4. **Check for Redirects**:
   - Determine if the authentication flow was interrupted with an unexpected redirect or a network issue.

5. **Reproduce the Error**:
   - Attempt to replicate the error in the same environment to understand the scenarios that lead to this issue.

---

### 2. Common Issues that Cause This Error

1. **Expired or Invalid SSO Session**:
<<<<<<< HEAD:guides/Other/aadsts50058.md
   - The users session may have expired. SSO sessions can have specific lifetimes after which they require re-authentication.
=======
   - The user�s session may have expired. SSO sessions can have specific lifetimes after which they require re-authentication.
>>>>>>> 8ca1440664e61dbdf9b1aa83f352634474c59c2f:guides/aadsts50058.md

2. **Cookies or Local Storage Issues**:
   - The SSO cookies or local storage data used for authentication may be missing, corrupted, or blocked by browser settings.

3. **Inconsistent Application Configurations**:
   - Mismatched configurations between the application and Azure AD could lead to failure in establishing a SSO session.

4. **Multiple Accounts**:
   - If the user has multiple Azure AD accounts, there can be confusion about which account to use for SSO.

5. **Network or Firewall Restrictions**: 
   - Network policies or firewalls may block necessary communications to Azure AD.

---

### 3. Step-by-Step Resolution Strategies

1. **Verify User Authentication**:
   - Ensure the user is authenticated by checking direct login or using different authentication flows.

2. **Clear Browser Cache and Cookies**:
<<<<<<< HEAD:guides/Other/aadsts50058.md
   - Clear the browsers cookies and cache to remove any corrupted SSO data. Instruct users to do this and try signing in again.
=======
   - Clear the browser�s cookies and cache to remove any corrupted SSO data. Instruct users to do this and try signing in again.
>>>>>>> 8ca1440664e61dbdf9b1aa83f352634474c59c2f:guides/aadsts50058.md

3. **Check Application and Azure AD Configuration**:
   - Confirm that the application is correctly registered in Azure AD:
     - Check Reply URLs.
     - Ensure proper permissions are set.
     - Validate that the client ID and secret are correctly implemented in the application.

4. **Examine Session Lifetime Settings**:
   - Review Azure AD session settings (like SSO token lifetime) to check whether they are appropriately set for your application's needs. Update settings if required.

5. **Prompt for Authentication**:
   - If using `prompt=none` in your request, consider removing it for debugging and to ensure authentication prompts are shown.

6. **Test Across Different Browsers**:
   - Check if the issue persists across various browsers or devices, which could indicate a local configuration issue.

7. **Network Troubleshooting**:
   - Ensure there are no network restrictions preventing access to Azure AD authentication endpoints.

8. **User Experience Evaluation**:
   - Encourage users to log out from all sessions and re-login to reset their session state.

---

### 4. Additional Notes or Considerations

- **SSO Policies**: Be aware of how SSO implementation supports different authentication flows (like legacy vs. modern) that may impact session management.
- **Session Tokens**: Understand the lifecycle of session tokens and ensure that your application handles renewals appropriately.
- **User Education**: Educate users regarding managing multiple accounts and avoiding confusion between them.

---

### 5. Documentation and Guidance

For further details and guidance, refer to:

- [Microsoft Azure Active Directory Documentation](https://docs.microsoft.com/en-us/azure/active-directory/)
- [Troubleshooting Single Sign-On](https://docs.microsoft.com/en-us/azure/active-directory/develop/troubleshoot-sso)
- [Understanding Azure AD Error Codes](https://docs.microsoft.com/en-us/azure/active-directory/develop/reference-aadsts-error-codes)

**Test URL Access**: 
- Confirm that these links are reachable from your network or application environment to ensure users can follow guidance:
  - [AAD Documentation](https://docs.microsoft.com/en-us/azure/active-directory/)
  - [Troubleshooting Guide](https://docs.microsoft.com/en-us/azure/active-directory/develop/troubleshoot-sso)

---

### 6. Advice for Data Collection

To effectively troubleshoot, gather the following data:

- **User Details**: Time, user account, and role involved at the time of the error.
- **Session Information**: Details on session tokens and authentication attempts.
- **Logs**: Collect logs from both the application and Azure AD.
- **Browser Console Output**: Capture JavaScript console and network requests made during the SSO process to identify failures.
- **Configuration Snapshots**: Save or document any settings related to session and SSO configurations in Azure AD.

By following the above steps in this troubleshooting guide, you can efficiently diagnose and resolve the AADSTS50058 error.

Category: Other