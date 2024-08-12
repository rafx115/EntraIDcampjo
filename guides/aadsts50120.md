
# AADSTS50120: ThresholdJwtInvalidJwtFormat - Issue with JWT header. Contact the tenant admin.


## Troubleshooting Steps
Certainly! The error code AADSTS50120, along with the description "ThresholdJwtInvalidJwtFormat - Issue with JWT header. Contact the tenant admin." is indicative of a problem with the JWT (JSON Web Token) format being used in authentication requests to Azure Active Directory (AAD). Below is a comprehensive troubleshooting guide to address this issue.

### Troubleshooting Guide for AADSTS50120

#### Initial Diagnostic Steps

1. **Understand the Context**:
   - Gather information on when and how the error occurs (e.g., during login, API requests, etc.).
   - Confirm whether this is a consistent issue or intermittent.

2. **Check User Credentials**:
   - Ensure the user credentials being tested are valid and active.
   - Verify the user's permissions and roles within Azure AD.

3. **Examine the JWT Structure**:
   - If you have access to the JWT, review its structure to confirm it adheres to the standard format (three base64URL-encoded parts: header, payload, and signature).

4. **Access Azure Portal**: 
   - If you have tenant admin access, log into the Azure Portal to check tenant settings or consult logs.

#### Common Issues That Cause This Error

1. **Malformed JWT Header**: 
   - The header might be incorrectly formatted or contain invalid characters.

2. **Incorrect Token Type**: 
   - Using a token format that isn't expected by the Azure service (e.g., using an ID token instead of an access token).

3. **Expired or Invalid Tokens**: 
   - The token used may have expired or been revoked.

4. **Misconfigured Applications**: 
   - The application registration in Azure AD might be configured incorrectly, causing it to generate invalid tokens.

5. **Custom Claims Issues**: 
   - If you are using custom claims, they might be incorrectly defined or not mandated by the service.

#### Step-by-Step Resolution Strategies

1. **Review and Correct the JWT**:
   - Use a JWT decoder (e.g., [jwt.io](https://jwt.io/)) to inspect the token's header and payload.
   - Ensure that the `alg` (algorithm) in the header aligns with Azure’s requirements (e.g., RS256).

2. **Testing JWT Generation**:
   - If you control the JWT creation process, review the code generating the token.
   - Ensure you're using the correct signing keys and payload claims.

3. **Check Application Registration**:
   - In Azure Portal, navigate to "Azure Active Directory" > "App registrations" and validate the settings of the application:
     - Confirm the Redirect URIs are set correctly.
     - Check permissions and scopes granted.

4. **Monitor Token Validity**:
   - Implement logging to capture token validity checks and identify if tokens are being revoked.

5. **Engage with Tenant Admin**:
   - If you’re not the tenant admin, contact the administrator for further access or assistance.
   - The admin may need to review sign-in logs in Azure AD to identify issues.

6. **Look at Error Logs**:
   - Azure AD logs can be found in the Azure Portal under "Azure Active Directory" > "Sign-ins".
   - Analyze the logs for related errors and additional context.

#### Additional Notes or Considerations

- **Security Token Configuration**: Make sure the signing certificates are regularly updated.
- **Check for Policy Requirements**: Ensure there are no conditional access policies interfering with JWT issuance.
  
#### Documentation for Guidance

- [Understanding JSON Web Tokens](https://jwt.io/introduction)
- [Azure Active Directory Authentication Overview](https://docs.microsoft.com/en-us/azure/active-directory/develop/authentication-scenarios)
- [Working with App Registrations](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)

#### Advice for Data Collection

- **Event Viewer Logs**: Check the application's event logs for any issues during JWT processing.
- **Network Tracing**: Utilize tools like Nettrace or similar tools to capture HTTP traffic if needed to inspect the JWT being sent.
- **Fiddler or Postman**:
  - If possible, make authentication attempts in tools like Postman and inspect the request and response for any anomalies.
  - Use Fiddler to see the outbound requests and responses, helpful in verifying the full authentication flow.

By following this guide, you should be able to diagnose and resolve the AADSTS50120 error effectively. If the issue persists after going through these steps, consider reaching out to Microsoft Support for advanced troubleshooting.