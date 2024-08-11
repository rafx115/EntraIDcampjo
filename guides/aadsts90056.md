# AADSTS90056: BadResourceRequest - To redeem the code for an access token, the app should send a POST request to the/tokenendpoint. Also, prior to this, you should provide an authorization code and send it in the POST request to the/tokenendpoint. Refer to this article for an overview ofOAuth 2.0 authorization code flow. Direct the user to the/authorizeendpoint, which will return an authorization_code. By posting a request to the/tokenendpoint, the user gets the access token. CheckApp registrations > Endpointsto confirm that the two endpoints were configured correctly.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS90056: BadResourceRequest

#### Initial Diagnostic Steps:
1. Verify that the application has the necessary permissions and configurations set up within Azure AD.
2. Ensure that the endpoints (/authorize and /token) are correctly configured in the app registration.
3. Check if the authorization code is being properly obtained and sent in the POST request to the /token endpoint.
4. Review the OAuth 2.0 authorization code flow for a better understanding of the process.

#### Common Issues That Cause This Error:
1. Incorrectly configured endpoints in the Azure AD app registration.
2. Missing or expired authorization code when making the request to the /token endpoint.
3. Lack of proper permissions for the app registration to obtain an access token.
4. Network connectivity issues preventing successful communication with the endpoints.

#### Step-by-Step Resolution Strategies:
1. **Verify Endpoints Configuration**:
   - Go to Azure Portal > Azure Active Directory > App registrations > Select the app.
   - Check the "Endpoints" section to ensure that the /authorize and /token endpoints are correctly configured.

2. **Obtain Authorization Code**:
   - Direct the user to the /authorize endpoint to obtain the authorization_code.

3. **Send Authorization Code in POST Request**:
   - Ensure that the obtained authorization_code is included in the POST request to the /token endpoint.

4. **Check App Permissions**:
   - Review the required permissions for the app registration to redeem the code for an access token.

5. **Troubleshoot Network Connectivity**:
   - Ensure that there are no network issues preventing communication with the endpoints.

#### Additional Notes or Considerations:
- It's important to follow the OAuth 2.0 authorization code flow correctly to avoid errors.
- Double-check all configurations, permissions, and endpoints to ensure a seamless process.

#### Documentation for Guidance:
- Microsoft Documentation: [OAuth 2.0 Authorization Code Flow Overview](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow)

By following these troubleshooting steps and considering the common issues, you should be able to address the AADSTS90056 error code related to BadResourceRequest effectively.