
# AADSTS90086: OrgIdWsTrustDaTokenExpired - The user DA token is expired.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS90086: OrgIdWsTrustDaTokenExpired

#### Initial Diagnostic Steps:
1. **Confirm the Error:** Verify that the error code AADSTS90086 with the description OrgIdWsTrustDaTokenExpired is indeed being encountered.
2. **Check User Session:** Confirm if the user is actively using Azure Active Directory authentication services.

#### Common Issues Leading to the Error:
1. **Expired Token:** The error typically occurs when the user's DA token (Device Authentication Token) has expired.
2. **Inactive User Session:** The user may not have been active for an extended period, leading to token expiration.
  
#### Step-by-Step Resolution Strategies:
1. **Sign Out and Sign In:**
    - Instruct the user to sign out of their current session.
    - Prompt the user to sign back in using valid credentials to initiate the generation of a new DA token.

2. **Reauthenticate:**
    - If the issue persists, guide the user to reauthenticate their device for a fresh DA token.
  
3. **Check User Activity:**
    - Encourage users to remain active within the Azure AD environment to prevent token expiration.
  
4. **Reset User Token:**
    - Administrators could manually reset the DA token for the affected user following the proper Azure AD protocols.
  
#### Additional Notes or Considerations:
- **Token Lifespan:** Educate users on the lifespan of DA tokens and advise them to monitor expiration dates.
- **Admin Access:** If necessary, involve an Azure AD administrator to assist in troubleshooting and resolving the issue.
  
#### Documentation for Guidance:
- Detailed steps and best practices for handling Azure AD errors can be found in the official [Microsoft Azure AD documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/reference-aadsts-error-codes).

By following these steps and considerations, you can effectively troubleshoot and resolve the error code AADSTS90086 related to the expired DA token for a user in the Azure AD environment.