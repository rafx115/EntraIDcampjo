# AADSTS90086: OrgIdWsTrustDaTokenExpired - The user DA token is expired.


## Troubleshooting Steps
Certainly! The error code AADSTS90086, along with the message "OrgIdWsTrustDaTokenExpired - The user DA token is expired," indicates that a user's security token used in Azure Active Directory (AAD) has expired. Below is a detailed troubleshooting guide for this issue.

### Detailed Troubleshooting Guide for AADSTS90086

#### 1. Initial Diagnostic Steps
   - **Check the Error Context**: Note where and when the error occurred (e.g., during application access or API calls).
   - **Verify User Identity and Properties**: Confirm the user's identity and permissions; check if they are part of the expected security groups.
   - **Review the Expiration Timestamp**: If possible, capture the expiration time of the token to ascertain if it has truly expired.

#### 2. Common Issues that Cause this Error
   - Expired tokens: The user's DA (Delegated Access) token has likely reached its expiration limit.
   - Session management: Token refresh policies may not be configured correctly.
   - User inactivity: If a user has not accessed the application for an extended period, their session may have expired.
   - Misconfigured authentication settings: There might be issues in the application’s configuration with Azure AD.
   - Client-side cache: The user's device may be cached with old credentials or tokens.

#### 3. Step-by-Step Resolution Strategies
   1. **Token Acquisition**:
      - Encourage the user to sign out of the application and then sign back in. This will typically request a new token.
      
   2. **Review Token Lifetimes**:
      - Check the token lifetime settings in the Azure AD portal (under `Azure Active Directory` > `App registrations` > `Your application` > `Token configuration`).

   3. **Reconfigure Application Permissions**:
      - Ensure that the application has the requisite permissions to request the new tokens. Under `API permissions`, adjust as necessary.

   4. **Adjust Token Lifetimes** (if applicable):
      - If users regularly encounter expired tokens, consider extending the token lifetime settings. This can usually be done under `Azure Active Directory` > `Enterprise applications` > `Your application` > `Properties`.

   5. **Implement Refresh Tokens**:
      - If your application is expected to maintain a session for long periods, check that it is correctly requesting refresh tokens and refreshing them as needed.
      
   6. **Check for User Account Lockouts**:
      - Ensure the user account is not locked or disabled, which can prevent successful authentication and token issuance.

   7. **Monitor Logs**:
      - Use Azure AD Sign-ins logs to track user sign-in events and identify patterns or frequent failures.

#### 4. Additional Notes or Considerations
   - If the users regularly experience expired tokens, it’s advisable to investigate the user experience design. Consider adding prompts for regular re-authentication.
   - Educate users about how tokens work and the need for periodic reauthentication.

#### 5. Documentation Where Steps Can Be Found for Guidance
   - **Azure AD Authentication Documentation**: [Overview of Azure Active Directory authentication](https://docs.microsoft.com/en-us/azure/active-directory/develop/authentication-scenarios)
   - **Token Lifetime Management**: [Configure the token lifetime](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-configurable-token-lifetimes)
   - **Azure AD Sign-ins Logs**: [Sign-in logs in Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/reports-monitoring/concept-sign-ins)

#### 6. Test the Documentation Can Be Reachable
   - Check the provided links in a browser to ensure they are active and accessible. The pages should load without errors, demonstrating availability.

#### 7. Advice for Data Collection
   - Collect logs from the Azure portal for sign-ins and token requests.
   - Gather exact timestamps of when the error occurred for correlating with Azure logs.
   - Capture any error messages and screenshots that detail the issue.
   - Document user feedback on their experience leading up to the error.

By following these steps and gathering relevant information, you can effectively troubleshoot the AADSTS90086 error and help users regain access to their applications. If the issue persists, consider escalating to Microsoft support for deeper investigation.

Category: Other