# AADSTS50013: InvalidAssertion - Assertion is invalid because of various reasons - The token issuer doesn't match the API version within its valid time range -expired -malformed - Refresh token in the assertion isn't a primary refresh token. Contact the app developer.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS50013

**Error Description:**
AADSTS50013 ("InvalidAssertion") indicates that a token assertion is invalid for various reasons, which can include issues related to the token issuer, API version validity, token expiration, or malformed tokens. Additionally, it may indicate that the refresh token provided is not a primary refresh token.

#### 1. Initial Diagnostic Steps

1. **Verify Context**: Determine the application scenario in which the error occurs.
   - Is it during user authentication or token refresh?
   - Which identity provider is being used?

2. **Gather Token Details**: Collect information about the token received.
   - Inspect the token's structure (JWT format, claims, etc.).
   - Identify the issuer and audience claims.

3. **Check Time Settings**: Confirm that the server time is synchronized correctly (with NTP services if possible). Time skew can lead to invalid tokens.

4. **Review API Version**: Identify the expected API version that your application supports and compare it with the token issuer's capabilities.

#### 2. Common Issues that Cause AADSTS50013

1. **Token Expiration**: The token might be expired or not valid for the requested operation.
2. **Malformed Tokens**: The structure of the token may not adhere to expected formats.
3. **Issuer Mismatch**: The issuer of the token does not match the expected issuer for the specific API version.
4. **Refresh Token Issues**: The refresh token provided might not be a primary refresh token or not linked correctly to the user account.
5. **Scope or Consent Issues**: Misconfigured scopes or lack of user consent might also lead to this error.

#### 3. Step-by-Step Resolution Strategies

1. **Verify Token Validity**:
   - Decode the JWT token to inspect its claims (online JWT decoder or use libraries).
   - Check expiration claim (`exp`) and/or issued-at claim (`iat`).

2. **Correct API Version**:
   - Ensure that the application is calling the correct end-point that matches the token issuer's API version.
   - Consult the API documentation for compatibility details.

3. **Confirm Token Issuer**:
   - Ensure that the issuer in the token matches the issuer URL that your application is configured to trust.
   - Look for discrepancies in tenant IDs or other identifiers.

4. **Refresh Token Check**:
   - If a refresh token is being sent, confirm it is a primary refresh token that corresponds with the user authentication process.
   - Review refresh token management in your application's backend or identity provider’s dashboard.

5. **Implement Error Handling**:
   - If the error persists, implement comprehensive logging of authentication and token requests to trace the causes effectively.

6. **User Consent Scenarios**:
   - Verify if user consent is effectively implemented and that the scopes are correctly requested during the initial sign-in.

#### 4. Additional Notes or Considerations

- Ensure that the OAuth application settings in the Azure portal or corresponding provider are correctly configured.
- Temporarily enable verbose logging/tracing in your application to capture more detailed information regarding the authentication attempts.
- If applicable, review your application's configuration against any recent updates to the Azure AD (e.g., changes in authentication policies).

#### 5. Documentation

- [Microsoft Identity Platform documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/)
- [Token Lifetime Policies](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-configurable-token-lifetimes)
- [OAuth 2.0 Authorization framework](https://oauth.net/2/)

#### 6. Advice for Data Collection

- **Event Viewer Logs**: Check the Application and System logs in Windows Event Viewer for any errors related to authentication issues.
  
- **Network Trace**: Use `nettrace` to monitor network requests and analyze the payload and headers being sent and received, specifically around the moment of the error.

- **Fiddler**: Use Fiddler to inspect HTTP(s) requests and responses, capturing the full interaction between your app and the token issuer.

- **Log User Actions**: Implement logging around user login attempts, including timestamps and outcome, to better analyze trends or recurrent issues.

This troubleshooting guide should help in diagnosing and resolving the AADSTS50013 error. Make sure to involve relevant stakeholders and communicate effectively throughout the troubleshooting process.