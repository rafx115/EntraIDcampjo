
# AADSTS90056: BadResourceRequest - To redeem the code for an access token, the app should send a POST request to the/tokenendpoint. Also, prior to this, you should provide an authorization code and send it in the POST request to the/tokenendpoint. Refer to this article for an overview ofOAuth 2.0 authorization code flow. Direct the user to the/authorizeendpoint, which will return an authorization_code. By posting a request to the/tokenendpoint, the user gets the access token. CheckApp registrations > Endpointsto confirm that the two endpoints were configured correctly.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS90056: BadResourceRequest

The AADSTS90056 error usually occurs when the application attempts to redeem an authorization code for an access token without properly following the OAuth 2.0 authorization code flow. This guide will help you troubleshoot this error systematically.

---

### Initial Diagnostic Steps

1. **Check the Error Description**: Carefully read the error message associated with AADSTS90056. It usually suggests that there is a problem with the POST request to the `/token` endpoint.

2. **Review Code/Request Flow**:
   - Verify that you have obtained an authorization code before sending a request to the `/token` endpoint.
   - Confirm you are using the correct endpoint for both authorization (`/authorize`) and token (`/token`).

3. **Inspect Application Logs**: Check your application's logs to see the specific requests you made and the response errors returned by the Azure Active Directory (AAD).

---

### Common Issues that Cause this Error

1. **Missing Authorization Code**: You might be trying to request an access token without obtaining a valid authorization code first.

2. **Incorrect Endpoint URLs**: The application might be configured incorrectly, leading to wrong URLs for authorization or token exchanges.

3. **Incorrect Client Credentials**: Ensure that the Client ID and Client Secret used in the request to the `/token` endpoint are correct.

4. **Scope Parameter Issues**: Ensure that the correct scopes are requested and included in the authorization flow.

5. **Authorization Code Expiry**: The authorization code might have expired. Authorization codes typically have a short lifespan.

6. **Request Method**: Make sure the request to the `/token` endpoint is correctly formatted as a POST request.

---

### Step-by-Step Resolution Strategies

1. **Check App Registrations**:
   - Go to Azure Portal > Azure Active Directory > App registrations.
   - Select your application and check the **Endpoints** section for the correct `/authorize` and `/token` endpoints.

2. **Acquire Authorization Code**:
   - Direct the user to the `/authorize` endpoint with the correct parameters:
     - `client_id`
     - `response_type=code`
     - `redirect_uri`
     - `scope`
   - Ensure that it successfully returns an authorization code.

3. **Send POST Request to `/token`**:
   - Structure the POST request to the `/token` endpoint:
     - URL: (from the Endpoint)
     - Headers:
       - `Content-Type: application/x-www-form-urlencoded`
     - Body (example parameters):
       - `grant_type=authorization_code`
       - `code=<authorization_code>`
       - `redirect_uri=<redirect_uri>`
       - `client_id=<client_id>`
       - `client_secret=<client_secret>`

4. **Verify Scopes**:
   - Ensure that your request includes all necessary scopes that the application needs.

5. **Handle Authorization Code Expiry**:
   - If an authorization code is invalid, prompt the user to login again to get a fresh authorization code.

6. **Debugging Tools**:
   - Use tools like Postman or curl to manually verify your requests to the `/authorize` and `/token` endpoints.

---

### Additional Notes or Considerations

- The authorization code is a one-time-use code, so it must be redeemed immediately after it is obtained.
- Be mindful of the OAuth 2.0 state parameter to prevent CSRF attacks.
- Always check the permissions given to your application in the Azure Portal to ensure they are sufficient for your needs.

---

### Documentation for Guidance

- [OAuth 2.0 Authorization Framework](https://oauth.net/2/)
- [How to secure your app with Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-v2-aspnet)
- [Microsoft Identity Platform - Authorization Code Flow](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow)

**Note**: To check if the documentation is reachable, please access the links provided above to ensure they load without issues.

---

### Advice for Data Collection

- Gather the following data if errors persist:
  - Full HTTP request and response logs.
  - The URL used for authorization and token requests.
  - The authorization code received and any related parameters.
  - The exact error messages returned by AAD.

This information is vital for deeper analysis or when seeking assistance from support or community forums.