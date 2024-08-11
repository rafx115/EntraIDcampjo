
# AADSTS50013: InvalidAssertion - Assertion is invalid because of various reasons - The token issuer doesn't match the API version within its valid time range -expired -malformed - Refresh token in the assertion isn't a primary refresh token. Contact the app developer.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS50013 - Invalid Assertion Error

The AADSTS50013 error indicates an invalid assertion, which means there is an issue with the token being used for authentication. Here is a detailed guide to help troubleshoot this error.

#### Initial Diagnostic Steps
1. **Confirm Error Context**: Determine when the error occurs. Is it during authentication in an application, a specific API call, or when refreshing tokens?
2. **Check User Details**: Identify which user reported the error and verify if their credentials or permissions are correctly configured.
3. **Inspect Logs**: If available, check related logs for additional context around the error. Look for any preceding events or errors.

#### Common Issues That Cause AADSTS50013
- **Token Issuer Mismatch**: The token may not be issued from the correct issuer or tenant.
- **Expired Tokens**: The token may have expired, making it invalid.
- **Malformed Tokens**: Tokens could be improperly formatted or constructed.
- **Refresh Token Issues**: The refresh token might not be a primary refresh token or invalid.
- **API Versioning Issues**: Tokens issued might not match the API's expected version.
- **Clock Skew**: Time discrepancies between the client and server could lead to assertions being considered invalid.

#### Step-by-Step Resolution Strategies
1. **Check Token Validity**:
    - Use JWT.io or any suitable JWT (JSON Web Token) decoder tool.
    - Verify:
        - Issuer (`iss`) matches the expected issuer.
        - Expiration (`exp`) and Not Before (`nbf`) claims are within valid time boundaries.
        - Token signature is valid (requires your app's public key).

2. **Review Application Configuration**:
    - Ensure that the app is correctly registered in Azure Active Directory (Azure AD).
    - Validate API permissions in the app registration.
    - Verify redirect URIs and scopes.

3. **Token Refresh Logic**:
    - If using refresh tokens, make sure you are using primary refresh tokens. Only the first refresh token issued will work for obtaining new access tokens.
    - Check your logic for refreshing tokens and ensure it follows Azure AD protocols.

4. **Check for API Version Compatibility**:
    - Make sure your application and the API being called support the same versioning scheme.
    - Review any API documentation for breaking changes.

5. **Check Clock Synchronization**:
    - Ensure your server/client's time is synced with NTP (Network Time Protocol) to avoid clock skew issues.

6. **Debugging Tools**:
    - Utilize Azure AD logs for audit and sign-in details. 
    - Use Azure Portal for real-time analysis of token issues.

7. **Consult Documentation**:
    - Refer to official Azure AD documentation for troubleshooting token issues:
      - [Azure Active Directory Token Reference](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-tokens)
      - [Troubleshooting common Azure Active Directory issues](https://docs.microsoft.com/en-us/azure/active-directory/develop/troubleshoot-common-aad-issues)

#### Additional Notes or Considerations
- If you are working in a corporate environment, ensure you comply with policies regarding user credentials and token management.
- Consider the usage of a single sign-on (SSO) solution that may reduce the frequency of token-related errors.
- In some cases, issues might also stem from OAuth2.0 flows; review the flow being used (authorization code, implicit, etc.).

#### Documentation Accessibility Test
To ensure the documentation is reachable:
1. Open a web browser.
2. Navigate to [Azure AD Token Reference](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-tokens).
3. Verify you can access and browse through the content without errors.

#### Advice for Data Collection
- Gather logs from the client application, Azure AD, and any intermediary components (e.g., proxies).
- Document the exact error message, time of occurrence, and actions taken at the time of the error.
- Record user details without sensitive information, noting roles and permissions associated with their accounts.

By following these procedures, you should be able to quickly diagnose and remediate the AADSTS50013 error. If issues persist, consider reaching out to Microsoft Support for further assistance.