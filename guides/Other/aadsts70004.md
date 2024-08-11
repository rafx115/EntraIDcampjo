# AADSTS70004: InvalidRedirectUri - The app returned an invalid redirect URI. The redirect address specified by the client does not match any configured addresses or any addresses on the OIDC approve list.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS70004: InvalidRedirectUri

The error code AADSTS70004 is commonly encountered when the redirect URI specified by the application during the authentication process does not match any of the redirect URIs configured in the Azure Active Directory (AAD) for that application. Here’s a detailed guide to troubleshoot and resolve this error.

#### Initial Diagnostic Steps

1. **Understand the Architecture**:
   - Identify the application type (e.g., web app, native application, etc.) using Azure AD for authentication.
   - Confirm the framework and technology used (e.g., .NET, Node.js).

2. **Capture the Error**:
   - Note the complete error message.
   - Check logs or output where the error occurred to gather context about the request being made when the error was returned.

3. **Review the Authentication Flow**:
   - Understand the OAuth2 or OIDC flow being used. Confirm that the redirect URI is intended as part of the authentication process.

#### Common Issues That Cause This Error

1. **Mismatch of Redirect URIs**:
   - The redirect URI used in the application does not match any URI registered in the Azure AD application registration.

2. **Usage of HTTP vs. HTTPS**:
   - The registered redirect URI in Azure may be specified as HTTPS, but the application tries to use HTTP.

3. **Trailing Slashes**:
   - A trailing slash in the redirect URI may cause a mismatch (e.g., `/callback` vs. `/callback/`).

4. **Typographical Errors**:
   - Typos in the URI can lead to a failure to match registered URIs.

5. **Change in Hosting Environment**:
   - If the application is moved to a different environment (e.g., from local development to production), ensure that the redirect URI matches the new environment.

6. **Dynamic Redirect URIs**:
   - Some applications may generate redirect URIs dynamically; ensure that those are registered in Azure.

#### Step-by-Step Resolution Strategies

1. **Check Registered Redirect URIs**:
   - Go to the Azure portal.
   - Navigate to **Azure Active Directory** > **App registrations**.
   - Find and select your application.
   - Under **Authentication**, check the list of redirect URIs.

2. **Update Redirect URIs**:
   - If the needed URI is not listed, add it by clicking on **Add a platform** and then configuring the redirect URI for the appropriate platform (e.g., Web).
   - Save the changes.

3. **Verify the Redirect URI in Code**:
   - Open the source code for the application and check the configuration for the redirect URI during the OAuth flow.
   - Ensure this matches exactly with one listed in Azure.

4. **Test the Authentication Flow**:
   - After confirming or updating the redirect URI, perform a test login to verify that the error does not occur.

5. **Consider Null or Empty Redirect URIs**:
   - Ensure that your application does not send an empty redirect URI when making the authorization request.

6. **Debugging**:
   - Use tools like Fiddler or browser developer tools to inspect the network traffic during the authentication request to see the exact request and response.

#### Additional Notes and Considerations

- **Multiple Redirect URIs**: 
   - If the application is intended to have multiple redirect URIs, ensure they are all registered correctly.

- **Redirect URI Formatting**:
   - Make sure to use the correct format (case sensitivity, including protocol, and encoding) for the redirect URI.

- **In Development vs. Production**: 
   - Maintain separate redirect URIs for development and production environments and ensure you switch them accordingly.

#### Documentation for Guidance

- **Azure AD App Registration Documentation**:
  - [Quickstart: Register an application with the Microsoft identity platform](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)

- **Understanding Redirect URIs**:
  - [Redirect URIs in Azure AD B2C](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-app-types#redirect-uris)
  
- **Conditional Access Policies**:
  - [Conditional Access in Azure Active Directory](https://docs.microsoft.com/en-us/azure/active-directory/conditional-access/overview)

### Testing Documentation Reachability

- To test that the documentation is reachable, ensure that you can open the provided links in a web browser. If any links are not reachable, verify the URLs or check your internet connection.

### Advice for Data Collection

- **Log Requests and Responses**: 
   - Log all requests to the identity platform including request parameters, especially the redirect_uri.
  
- **Capture Errors**: 
   - Capture error messages and codes in your application's logging system to assist with troubleshooting.

- **User Context**: 
   - Gather user session context if applicable, to identify if the issue is happening in a specific environment or due to user-specific configurations.

By following this guide, you should be able to effectively diagnose and resolve the AADSTS70004 error related to invalid redirect URIs in an Azure AD authentication flow.

Category: Other