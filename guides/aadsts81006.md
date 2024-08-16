# AADSTS81006: DesktopSsoNoAuthorizationHeader - No authorization header was found.


## Troubleshooting Steps
# Troubleshooting Guide for AADSTS81006 Error Code: "DesktopSsoNoAuthorizationHeader"

## Description
The error code **AADSTS81006**, indicating "DesktopSsoNoAuthorizationHeader - No authorization header was found," typically occurs during authentication processes using Azure Active Directory (AAD), particularly when attempting to obtain tokens for accessing protected resources.

## Initial Diagnostic Steps
1. **Identify the Context**: Understand the application or service that is trying to authenticate with AAD. Is it a desktop application? A web app? A mobile app?
2. **Examine the Authentication Flow**: Determine how the authentication is being initiated. Is it using OAuth, OpenID Connect? Are you acquiring tokens silently or interactively?
3. **Review Application Registration**: Verify that the application is registered correctly in Azure AD and has the necessary API permissions.
4. **Check Connectivity**: Ensure the device can reach Azure AD endpoints. Look for any network restrictions (like corporate firewalls).

## Common Issues That Cause This Error
1. **Missing Authorization Header**: The most direct cause of this error is that the application failed to send an authorization header when attempting to access a resource.
2. **Expired Tokens**: If tokens are cached, they may have expired, causing failures when attempts are made to use them without refreshing or acquiring new ones.
3. **Incorrect Client Configuration**: The client application might not be correctly configured, leading to improper request formation.
4. **Network Interruption**: Problems with the network can lead to incomplete requests and cause failures in obtaining the required token.
5. **Token Cache Issues**: Problems with token cache invalidation or retrieval from the cache can lead to a missing authorization header.

## Step-by-Step Resolution Strategies
1. **Check the Authentication Request**:
   - Inspect the request being sent from the application to AAD. Ensure that an authorization header is being included.
   - If using libraries (like MSAL), make sure you're correctly following the recommended practices to obtain tokens.

2. **Acquiring a Token**:
   - If you're trying to perform a silent token acquisition, make sure that the user has previously authenticated, and valid tokens exist in the cache.
   - If necessary, trigger an interactive sign-in to ensure that valid tokens are acquired.

3. **Review Application Permissions**:
   - Go to the Azure portal, navigate to "Azure Active Directory" > "App registrations".
   - Check the "API permissions" of your application. Ensure necessary permissions are granted and properly consented.

4. **Check Token Cache**:
   - Inspect the implementation of your token cache, ensuring that valid tokens are being stored and retrieved.
   - If you're in a testing phase, consider clearing the token cache and re-acquiring tokens.

5. **Inspect Network Conditions**:
   - Make sure that there is no firewall or proxy interfering with the requests made to Azure AD endpoints.

6. **Update SDKs**:
   - If you are using libraries (like MSAL), ensure they are updated to the latest version, as updates may fix bugs related to token handling.

## Additional Notes or Considerations
- **Single-Sign-On (SSO)**: If your application is attempting to use SSO, make sure the SSO features are properly set up and that your application's configuration aligns with Azure AD's requirements for SSO.
- **Debugging Tools**: Utilize tools like Fiddler or browser developer tools to inspect HTTP requests/responses for missing or malformed headers.
  
## Documentation for Guidance
- [Microsoft Identity Platform documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/)
- [Azure Active Directory Authentication Library (ADAL)](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-authentication-libraries)
- [Microsoft Authentication Library (MSAL)](https://docs.microsoft.com/en-us/azure/active-directory/develop/msal-overview)

## Advice for Data Collection
To aid in diagnosing issues further, consider collecting the following logs:
1. **Event Viewer Logs**:
   - Check the Windows Event Viewer, focusing on the application logs for any relevant errors that may indicate authentication issues.

2. **Network Tracing**:
   - Use **NetTrace** to capture network traffic to see any dropped headers or requests.
   - This will help confirm if the authorization header is missing before reaching Azure AD.

3. **Fiddler / Postman**:
   - Use Fiddler to intercept traffic and analyze the HTTP requests and responses.
   - If API calls can be replicated, consider using Postman for testing the authentication flow and inspect the headers being sent.

By following these steps and checks, you should be able to troubleshoot and resolve the `AADSTS81006` error effectively.