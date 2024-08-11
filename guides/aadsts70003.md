# AADSTS70003: UnsupportedGrantType - The app returned an unsupported grant type.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS70003 Error Code - UnsupportedGrantType

When encountering the AADSTS70003 error with the description "UnsupportedGrantType - The app returned an unsupported grant type," it typically indicates an issue with the grant type being used by the application during authentication. Follow the steps below to help diagnose and resolve this error:

#### Initial Diagnostic Steps:
1. **Verify Grant Type:** Confirm the grant type specified in the authentication request or settings of the application.
2. **Check Application Configuration:** Ensure that the application is configured to use a supported grant type according to the identity provider's specifications.
3. **Review Logs:** Check application logs, identity provider logs, and Azure Active Directory logs for more detailed error messages or clues.

#### Common Issues:
- **Incorrect Grant Type:** The application is using a grant type that is not supported by Azure Active Directory.
- **Misconfigured Application:** The application is not properly configured to use the correct grant type.
- **Token Request Mismatch:** The grant type specified during the token request does not match the allowed grant types for the application.

#### Step-by-Step Resolution Strategies:
1. **Verify Grant Type Compatibility:**
   - Refer to the Azure Active Directory documentation to identify the supported grant types.
2. **Update Application Configuration:**
   - Adjust the application's settings to use a supported grant type if needed.
3. **Check Token Request:**
   - Ensure that the grant type in the token request matches the supported grant types for the application.
4. **Test Authentication:**
   - Test the application's authentication flow to see if the issue persists after making changes.

#### Additional Notes or Considerations:
- Azure Active Directory supports standard grant types like Authorization Code Grant, Implicit Grant, Client Credentials Grant, Resource Owner Password Credentials Grant, etc.
- Ensure that the application is using the correct client ID and client secret while requesting tokens.
- Consider the security implications of the grant types being used and choose the appropriate one based on your application's requirements.

#### Documentation:
- [Azure Active Directory Grant Types](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-implicit-grant-flow)
- [Azure AD Supported Token Issuance Policies](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-configurable-token-lifetimes)
- [Troubleshooting Azure AD Authentication Errors](https://docs.microsoft.com/en-us/troubleshoot/azure/active-directory/error-codes-authentication-endpoint)

By following these steps and considerations, you should be able to diagnose and resolve the AADSTS70003 error related to UnsupportedGrantType effectively.