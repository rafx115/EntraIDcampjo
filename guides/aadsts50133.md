# AADSTS50133: SsoArtifactRevoked - The session isn't valid due to password expiration or recent password change.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS50133 - SsoArtifactRevoked

#### Initial Diagnostic Steps:
1. **Confirm the Error**: Ensure the error code is indeed AADSTS50133 SsoArtifactRevoked.
2. **Check User Activity**: Verify if the user recently changed their password or if their password has expired.

#### Common Issues causing this error:
1. **Password Expiration**: User's password has expired.
2. **Recent Password Change**: User has recently changed their password.
3. **Single Sign-On Configuration**: Issues with the Single Sign-On configuration.
4. **Token Revocation**: User session revoked due to security reasons.

#### Step-by-Step Resolution Strategies:

1. **Password Expiration / Recent Password Change**:
    - Advise the user to update their password if it has expired or was recently changed.
    - Instruct the user to log out of all sessions and log in again with the new password.

2. **Single Sign-On Configuration**:
    - Check the Single Sign-On configuration settings.
    - Reset the configuration if necessary and have the user attempt to log in again.

3. **Token Revocation**:
    - If the token is revoked for security reasons, the user may need to undergo a re-authentication process.
    - Advise the user to try logging in again after the security issue is resolved.

#### Additional Notes or Considerations:
- Encourage users to keep track of their password expiration dates and change passwords promptly.
- Ensure that Single Sign-On configurations are up-to-date and aligned with the organization's security policies.

#### Documentation for Guidance:
- [Microsoft Azure Active Directory Error Codes](https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-error-codes)

By following these troubleshooting steps, you should be able to address the AADSTS50133 SsoArtifactRevoked error effectively. If the issue persists, consider reaching out to the IT support team for further assistance.