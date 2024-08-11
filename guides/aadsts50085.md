
# AADSTS50085: Refresh token needs social IDP login. Have user try signing-in again with username -password


## Troubleshooting Steps
### Error Code: AADSTS50085 - Refresh Token Needs Social IDP Login

#### Initial Diagnostic Steps:
1. **Confirm the Error**: Verify that the user is indeed receiving the error message AADSTS50085 stating that the refresh token requires social IDP login.
2. **Check User Credentials**: Ensure that the username and password being used are correct and valid for the associated social identity provider.

#### Common Issues:
- Expired Refresh Token: The refresh token may have expired, which requires the user to log in again using social IDP login.
- Incorrect or Outdated Credentials: Users may be entering incorrect login credentials or using outdated information.
- Identity Provider Configuration: Issues with the social identity provider's settings can also lead to this error.

#### Step-by-Step Resolution Strategies:
1. **Have User Try Signing In Again**:
   - Instruct the user to sign in again with the appropriate username and password linked to the social identity provider.
2. **Retrieve New Tokens**:
   - If the refresh token has expired, guide the user to authenticate again to obtain a new refresh token.
3. **Update Credentials**:
   - Ensure the user enters the correct and up-to-date login credentials to avoid authentication errors.
4. **Identity Provider Check**:
   - Verify the configuration settings of the social identity provider for any issues affecting the token refresh process.

#### Additional Notes or Considerations:
- **User Awareness**: Educate users on the importance of using the correct credentials and regularly updating them to prevent authentication issues.
- **Time Sensitivity**: Refresh tokens have an expiration period, so prompt action is necessary to avoid disruptions in the authentication process.

#### Documentation:
For further guidance, refer to the Microsoft documentation on error AADSTS50085 and related troubleshooting steps:
[Microsoft Azure AD Error Codes](https://docs.microsoft.com/en-us/azure/active-directory/develop/reference-aadsts-error-codes)

By following the provided steps and ensuring the user performs the necessary actions, you can address the error code AADSTS50085 effectively and assist the user in resolving their authentication issue.