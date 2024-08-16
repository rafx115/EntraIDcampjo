# AADSTS70005: UnsupportedResponseType - The app returned an unsupported response type due to the following reasons:response type 'token' isn't enabled for the appresponse type 'id_token' requires the 'OpenID' scope -contains an unsupported OAuth parameter value in the encoded wctx


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS70005 Error

The AADSTS70005 error indicates an issue with the response type requested during an OAuth authentication flow in Azure Active Directory (Azure AD). This guide will help you diagnose and resolve this error.

---

### Initial Diagnostic Steps

1. **Check the App Registration**: Verify that your application is registered correctly in Azure AD and that you have the correct configurations in place.
  
2. **Review the Authentication Request**: Capture the exact authentication request being sent when the error occurs. This includes the response types, scopes, and other parameters.

3. **Inspect Logs**: Check the Azure AD sign-in logs for any additional details related to the error. You can find this in the Azure portal under Azure Active Directory > Sign-ins.

---

### Common Issues that Cause This Error

1. **Invalid Response Type**:
   - The application is trying to use `response_type=token`, which is not enabled for the app.
  
2. **Missing Scopes**:
   - If using `response_type=id_token`, the 'OpenID' scope is required.

3. **Incorrect Client Configuration**:
   - Application permissions are not configured properly in Azure AD.

4. **Unsupported URL Encoding**:
   - Invalid or unsupported parameters (such as `encoded wctx`) may be causing the issue in requests.

---

### Step-by-Step Resolution Strategies

#### Step 1: Verify Response Types
- Go to Azure Portal > Azure Active Directory > App Registrations > Your App > Authentication.
- Ensure that the **Implicit grant and hybrid flows** settings allow for the response types you're trying to use:
  - If expecting ID tokens, ensure that "ID tokens" is checked.
  - If you require access tokens, ensure you have checked "Access tokens".

#### Step 2: Review Required Scopes
- Confirm that your request includes the OpenID scope when you're using `response_type=id_token`.
- Example of a valid scope query string:
  ```
  scope=openid
  ```

#### Step 3: Check API Permissions
- Navigate to Azure AD > App Registrations > Your App > API permissions.
- Ensure that required permissions are granted, and check for any permissions that require admin consent.

#### Step 4: Inspect the Authentication Request
- Review the request parameters to ensure they conform to the expected OAuth 2.0/OIDC standards.
- An example request might look like:
  ```
  GET https://login.microsoftonline.com/{TenantID}/oauth2/v2.0/authorize?
  client_id={ClientID}&response_type=id_token
  &scope=openid
  ```

#### Step 5: Test in a Controlled Environment
- If possible, test the authentication flow using a tool like Postman or Insomnia where you can manually set the request parameters.

---

### Additional Notes or Considerations

- Ensure that the app is not running in a local environment with truncated URLs or malformed requests.
- If you're using a framework or library to perform authentication (e.g., MSAL), ensure it is configured properly and up-to-date.
- Be aware of the differences between response types in the Implicit and Authorization Code grant flows.

---

### Documentation for Guidance

- [Quickstart: Configure an app to access web APIs](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-v2-webapp-dotnet)
- [Azure Active Directory OpenID Connect Protocol](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-protocols-oidc)
- [Authentication Library for JavaScript (MSAL.js)](https://docs.microsoft.com/en-us/azure/active-directory/develop/msal-overview)

---

### Advice for Data Collection

1. **Event Viewer Logs**:
   - Check the application logs to see if there are any additional error messages or stack traces related to the authentication process.

2. **Use of Network Tracing Tools**:
   - Utilize tools like Fiddler or Fiddler Everywhere to capture network requests and analyze the headers, parameters, and responses involved in the OAuth flow.
   - Make sure to look for HTTP status codes, and the body of each request and response for relevant error messages.

3. **Browser Developer Tools**:
   - If you're running in a browser environment, use Developer Tools (F12) to inspect network activity around the authentication flow.

Using these steps, you should be able to diagnose the AADSTS70005 error and implement the necessary changes to resolve it.