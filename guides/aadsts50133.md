
# AADSTS50133: SsoArtifactRevoked - The session isn't valid due to password expiration or recent password change.


## Troubleshooting Steps
Certainly! The error code AADSTS50133 indicates that the user's session isn't valid either due to password expiration or a recent password change. Below is a comprehensive troubleshooting guide to assist in resolving this issue.

### Troubleshooting Guide for AADSTS50133

#### Initial Diagnostic Steps
1. **Verify the User's Account Status:**
   - Check if the account is active or has been disabled.
   - Confirm that the user can log in through a different application or directly via the Azure Portal.

2. **Check for Password Expiration:**
   - Inquire whether the user has received any notifications about their password expiring.
   - Confirm the password expiration policy applied to the user’s account (e.g., in Azure AD).

3. **Identify Recent Password Changes:**
   - Determine if the user has changed their password recently and whether they are attempting to access the service with the old password.

#### Common Issues that Cause AADSTS50133
1. **Expired Password:**
   - The user’s password has expired, and they have not updated it.
   
2. **Recent Password Change:**
   - The user changed their password during a session, leading to session invalidation.

3. **Session Cookies:**
   - Old session information may still be stored in the browser or application, leading to conflicts.

4. **Multi-Factor Authentication (MFA) Issues:**
   - MFA may prevent the users from re-establishing their session after a password change.

5. **Token Issuance:**
   - If tokens are being cached or not updated post-password change, the user may get errors when trying to authenticate.

#### Step-by-Step Resolution Strategies
1. **Reset Password:**
   - If the password has expired, advise the user to reset their password from the Azure portal or through a self-service password reset (SSPR) mechanism, if enabled.

2. **Clear Cache and Cookies:**
   - Have the user clear their browser cookies and cache or restart the application they are using to remove old session tokens.

3. **Logout and Re-login:**
   - Instruct the user to fully log out of the application and then log back in to establish a new session with the updated credentials.

4. **MFA Re-authentication:**
   - Ensure that MFA prompts are being completed during the sign-in process, especially after password changes.

5. **Check Application Configuration:**
   - Review the application settings to ensure that it properly handles session management post-password changes.

6. **Contact Admin:**
   - If the problem persists after verifying password status and clearing sessions, escalate the issue to your IT administrator for investigation in Azure AD or the relevant identity provider settings.

#### Additional Notes and Considerations
- Encourage users to set up notifications for password expiration to avoid session interruption.
- Depending on organizational password policies, consider implementing or promoting the use of adaptive authentication measures.

#### Documentation for Guidance
- **Azure AD Password Policies:** [Password policies in Azure Active Directory](https://docs.microsoft.com/en-us/azure/active-directory/authentication/howto-password-policy)
- **Azure AD Sign-In Error Codes:** [Microsoft Azure Active Directory - Common error codes](https://docs.microsoft.com/en-us/azure/active-directory/develop/reference-aadsts-error-codes)
- **Azure AD Conditional Access:** [Overview of Conditional Access](https://docs.microsoft.com/en-us/azure/active-directory/conditional-access/overview)

#### Advice for Data Collection
- **Event Viewer Logs:**
  - Capture relevant logs under Windows Logs → Applications and Services Logs for Azure AD and other related services.
  
- **Network Tracing:**
  - Use `nettrace` or similar tools to log network traffic to identify any anomalies during the request process to the Azure services.
  
- **Fiddler:**
  - Set up Fiddler to monitor and debug HTTP traffic between the client and the server. Pay attention to 401 unauthorized responses or any indication of session issues.

By following the above guide and suggestions, you should be able to effectively resolve the AADSTS50133 error and help users regain access to their services.