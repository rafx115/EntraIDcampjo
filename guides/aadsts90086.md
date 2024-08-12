
# AADSTS90086: OrgIdWsTrustDaTokenExpired - The user DA token is expired.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS90086 - "OrgIdWsTrustDaTokenExpired"

#### Initial Diagnostic Steps
1. **Verify User Identity**: Ensure you are attempting to log in with the correct user credentials. Check if the account is still active and not disabled.
2. **Check Token Expiry**: Understand the duration for which the security token is valid. If the token has expired, you need to renew it.
3. **Account Status**: Confirm that the user account is not locked, deleted, or otherwise inactive in Azure Active Directory (Azure AD).
4. **Network Conditions**: Assess network connectivity to Azure AD services. Poor network conditions can lead to authentication timeouts.
5. **Policy Settings**: Investigate if there are any newly applied Conditional Access policies or MFA requirements that may affect user logins.

#### Common Issues that Cause this Error
- **Expired Security Token**: The issued token for the user has expired before the authentication request was made.
- **Misconfigured Authentication Settings**: Incorrect settings in the identity provider or application can lead to token issues.
- **Old Client Applications**: Using an outdated version of an application that does not properly handle token renewal.
- **User Session Timeouts**: Prolonged inactivity can cause a session timeout leading to expired tokens.
- **Clock Skew Issues**: A significant difference in system time between the client and server can cause the token to be seen as expired.

#### Step-by-Step Resolution Strategies
1. **Renew Token**:
   - Guide the user to re-authenticate to obtain a new token.
   - If using an application that uses refresh tokens, validate that it correctly requests a new token when the current one expires.

2. **Check Authentication Policies**:
   - Review any recent updates to authentication policies in Azure AD that may affect user sign-ins.
   - Ensure that the Conditional Access policies are well configured to accommodate users needing access.

3. **Update Applications**:
   - Ensure that any client applications are updated to the latest version, which would include better handling of token lifecycles and renewals.

4. **Review Session Settings**:
   - In Azure AD, check the session control settings. Consider adjusting the session timeout settings based on organizational needs.

5. **System Clocks**:
   - Verify that the system clocks for both the client device and Azure AD are in sync. Adjust if necessary.

6. **Monitor for Issues**:
   - Enable logging on the application if possible to diagnose if additional errors occur after user attempts to log in.

7. **Contact Support**:
   - If none of the above strategies resolve the issue, consider contacting Microsoft support with detailed information about the account and the authentication attempt.

#### Additional Notes or Considerations
- **User Awareness**: It may help to inform users about best practices for managing their sessions, including logging off when not in use.
- **Multi-factor Authentication**: If MFA is in place, ensure the user understands the steps necessary to authenticate properly through all required factors.
- **Service Health**: Check the Azure service health dashboard to determine if there are any ongoing issues with Azure Active Directory services.

#### Documentation for Guidance
- [Microsoft Authentication Library (MSAL)](https://docs.microsoft.com/en-us/azure/active-directory/develop/msal-overview)
- [Azure Active Directory Authentication](https://docs.microsoft.com/en-us/azure/active-directory/develop/authentication-scenarios)
- [Token Lifetime Policies](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-configurable-token-lifetimes)

#### Advice for Data Collection
- **Event Viewer Logs**: Check for any relevant logs in the Event Viewer under Windows Logs > Application. Look for warnings or errors related to the authentication process.
- **Network Traces**:
   - Use **Nettrace** or **Fiddler** to capture the HTTP requests during the login attempt. Analyze the requests to operational endpoints for any anomalies or error codes.
- Look for specific logs around the time a user attempts to sign in and note any errors or messages relating to AADSTS or tokens.

By following these guidelines, you should be able to effectively diagnose and resolve the AADSTS90086 error regarding expired DA tokens.