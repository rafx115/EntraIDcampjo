# AADSTS90056: BadResourceRequest - To redeem the code for an access token, the app should send a POST request to the/tokenendpoint. Also, prior to this, you should provide an authorization code and send it in the POST request to the/tokenendpoint. Refer to this article for an overview ofOAuth 2.0 authorization code flow. Direct the user to the/authorizeendpoint, which will return an authorization_code. By posting a request to the/tokenendpoint, the user gets the access token. CheckApp registrations > Endpointsto confirm that the two endpoints were configured correctly.


## Troubleshooting Steps
# Troubleshooting Guide for Error Code AADSTS90056 - BadResourceRequest

## Overview
The error code AADSTS90056 indicates a bad resource request in the context of obtaining an access token from Azure Active Directory (Azure AD). This typically occurs when the OAuth 2.0 authorization code flow is not followed correctly.

---

## Initial Diagnostic Steps

1. **Verify the Error Message**: Ensure that the error is indeed AADSTS90056. Check the full error message for context.
2. **Check the Flow**: Confirm that you are implementing the OAuth 2.0 authorization code flow correctly, as it involves precise steps.
3. **Review OAuth 2.0 Endpoints**: Ensure that you have the correct /authorize and /token endpoints from Azure AD.
4. **Review Application Registration**: Check the App registrations in the Azure portal and confirm that the application is properly configured.

---

## Common Issues

1. **Incorrect Endpoint Used**:
   - Ensure that you are using the correct URL paths for the /authorize and /token endpoints as provided in your Azure app registration.

2. **Missing Authorization Code**:
   - Ensure that an authorization code was successfully obtained before attempting to exchange it for an access token. This is often overlooked.

3. **Invalid or Expired Authorization Code**:
   - An authorization code can only be used once and has a limited lifespan, usually a few minutes.

4. **Misconfigured App Registration**:
   - The app registration might not have the correct API permissions or redirect URIs set up.

5. **Redirect URI Mismatch**:
   - Ensure that the redirect URI used in the authorization request matches the one configured in the application registration.

---

## Step-by-Step Resolution Strategies

1. **Ensure Correct OAuth Flow**:
   - Begin by directing the user to the /authorize endpoint to obtain an authorization code.
   - Example Request:
     ```
     GET https://login.microsoftonline.com/{tenant}/oauth2/v2.0/authorize?
         client_id={client_id}&
         response_type=code&
         redirect_uri={redirect_uri}&
         response_mode=query&
         scope={scopes}
     ```

2. **Exchange Authorization Code for Access Token**:
   - Once you have the authorization code, make a POST request to the /token endpoint to exchange it for an access token.
   - Example POST Request:
     ```
     POST https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token
     Content-Type: application/x-www-form-urlencoded

     client_id={client_id}&
     client_secret={client_secret}&
     grant_type=authorization_code&
     code={authorization_code}&
     redirect_uri={redirect_uri}
     ```

3. **Check Endpoint Configuration**:
   - Navigate to **Azure Portal > Azure Active Directory > App registrations > Your App > Endpoints**. Ensure the URL endpoints you are using match those listed.

4. **Confirm Redirect URI**:
   - Under your app registration settings, check the **Authentication** section and confirm that the redirect URI specified matches the one used in your requests.
   
5. **Check Application Permissions**:
   - Ensure that your app has the necessary API permissions set correctly in the Azure portal.

---

## Additional Notes or Considerations

- Each authorization code is valid for only one exchange. Attempting to use the same code multiple times will result in errors.
- Make sure to adhere to the scopes your app is requesting. Insufficient permissions can also lead to access token errors.
- The app must be registered in the Azure portal with the necessary permissions granted by an administrator if required.

---

## Documentation for Guidance

- [Microsoft OAuth 2.0 Authorization Code Flow](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code)
- [Azure AD App Registration Overview](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)
- [Azure AD Tokens Overview](https://docs.microsoft.com/en-us/azure/active-directory/develop/access-tokens)

---

## Advice for Data Collection

If you encounter issues, consider collecting the following data:

- **Event Viewer Logs**: Look for any related logs in the Windows Event Viewer that may give insights into application errors.
- **Network Trace**: Use `nettrace` or `Wireshark` to capture network traffic and ensure that requests are being sent and received correctly.
- **Fiddler**: Utilize Fiddler to log HTTP(s) requests. This can help verify the exact requests that are being sent and any responses received from the Azure endpoint.

By following these detailed troubleshooting steps, you should be able to resolve the AADSTS90056 error effectively.