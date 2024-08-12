
# AADSTS50085: Refresh token needs social IDP login. Have user try signing-in again with username -password


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS50085

Error code **AADSTS50085** indicates that the refresh token requires social Identity Provider (IDP) login. This typically occurs with applications that use Azure Active Directory (AAD) for authentication, especially when a user tries to refresh a token that was obtained through a social login (like Google or Facebook) but needs to re-authenticate with their credentials. Below is a detailed troubleshooting guide.

#### Initial Diagnostic Steps
1. **Verify User Account**: Confirm that the user account experiencing the issue is indeed associated with a social IDP.
2. **Check Token Expiration**: Understand whether the issue arises from an expired token without a valid refresh token.
3. **Review Application Logs**: Check the application logs for any related errors or warnings around the time of the user’s authentication attempt.
4. **Consent and Permissions**: Ensure that the user has granted the necessary permissions for the social IDP to access their account.

#### Common Issues That Cause This Error
1. **Expired Refresh Token**: The refresh token might be expired or invalid.
2. **Social IDP Changes**: The user might have changed their social IDP password or permissions.
3. **Unintended Session Logout**: The user might have logged out from the social IDP, invalidating the refresh token.
4. **Misconfiguration in Azure AD**: Configuration issues in Azure AD related to social logins can lead to this error.
5. **Incorrect Redirect URI**: The application may not be correctly set up to handle social IDP redirects.

#### Step-by-Step Resolution Strategies
1. **Prompt User to Re-authenticate**: 
   - Have the user log in again to the social IDP using their username and password. This will generate a new refresh token.
  
2. **Regenerate Tokens**:
   - After logging back in, issue a new authentication request to obtain new access and refresh tokens.

3. **Check Application Configuration**: 
   - Go to the Azure portal and ensure that all the settings for the application are correctly configured.
   - Verify that the correct social IDP is added and configured with the appropriate redirect URIs.

4. **Inspect Token Expiration Settings**: 
   - Review the token expiration settings in Azure AD and ensure they align with your application’s needs. 

5. **Monitor Permissions and Consent**:
   - Confirm that the user has provided the necessary permissions and consents for the application to access their social IDP information.

6. **Debugging with Logs**:
   - Review the application and server logs to identify any specific patterns or additional errors that correlate with the AADSTS50085 error.

#### Additional Notes or Considerations
- Ensure users understand the importance of maintaining their social IDP sessions and the impact of changing passwords or disabling accounts.
- Consider implementing a user-friendly error message that instructs users to sign in again when they encounter this error, instead of a technical error code.

#### Documentation for Guidance
- [Microsoft Identity Platform documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/)
- [Understanding Azure AD error codes](https://learn.microsoft.com/en-us/azure/active-directory/develop/reference-aad-error-codes)

#### Advice for Data Collection
- **Event Viewer Logs**: Check the application and system logs in Windows Event Viewer for relevant errors around authentication events.
- **Network Trace**: Utilize tools like Network Monitor or Fiddler to trace network requests during the authentication flow. Look for any failed requests related to token issuance.
  - In Fiddler, ensure HTTPS decryption is enabled to view the traffic.
- **Logging additional information**: Implement application-level logging to capture detailed information about the authentication process and any errors encountered.

By following these steps, you should be able to diagnose and resolve the AADSTS50085 error for your users effectively.