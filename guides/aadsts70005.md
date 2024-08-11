
# AADSTS70005: UnsupportedResponseType - The app returned an unsupported response type due to the following reasons:response type 'token' isn't enabled for the appresponse type 'id_token' requires the 'OpenID' scope -contains an unsupported OAuth parameter value in the encoded wctx


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS70005

Error code AADSTS70005 may occur when an application attempts to acquire tokens but returns an unsupported response type or improperly formatted request parameters. This guide provides structured steps for diagnosing and resolving the issue.

---

#### Initial Diagnostic Steps

1. **Identify the Application**: Determine which application is generating the error. Ensure you have permissions to access the necessary configuration settings of the application within Azure AD.

2. **Check Error Logs**: Review the logs and capture the full error message including the response body. Look for error details that may provide insight into the request and response.

3. **Reproduce the Error**: If possible, attempt to reproduce the error under a controlled environment, and take note of the request parameters used.

---

#### Common Issues That Cause This Error

1. **Unsupported Response Type**:
   - The application is configured with an unsupported response type (e.g., 'token' or 'id_token').
  
2. **Lack of Required Scopes**:
   - The application requests an 'id_token' but does not include the 'openid' scope, which is required.

3. **Embedded State/Wctx Parameters**:
   - The response may contain unsupported values or an improperly encoded `wctx` parameter.

4. **Application Registration Misconfiguration**:
   - Incorrect settings in the Azure AD application registration can lead to unsupported response types or missing required scopes.

---

#### Step-by-Step Resolution Strategies

1. **Verify Application Registration**:
   - Navigate to the Azure portal.
   - Go to **Azure Active Directory** > **App registrations**.
   - Select the application in question.
   - Review the **Authentication** section to ensure the correct **Redirect URIs** are specified.
   
2. **Check Response Type Settings**:
   - Under the Authentication blade, verify allowed response types.
   - For implicit grant flows (if applicable), ensure ‘Access tokens’ and ‘ID tokens’ are enabled.

3. **Update Scopes**:
   - Confirm that upon requesting tokens, you include the required scopes. If requesting an `id_token`, ensure to include the `openid` scope.
   - Example scope request: `openid profile email`.

4. **Inspect the OAuth Parameters**:
   - Review your request for any encoded parameters such as `wctx`.
   - Ensure that all parameters are properly encoded, and no unsupported values are present. 

5. **Update Client Application Code**:
   - Check the code where the authentication request is constructed. Ensure that it specifies supported response types and includes necessary scopes.

6. **Re-authenticate and Retry**:
   - After making necessary changes, re-authenticate using the application and monitor if the issue persists.

---

#### Additional Notes or Considerations

- **Permissions**: Ensure that the application has necessary permissions granted from Azure AD after configuration changes. 

- **Token Configuration**: Be mindful that combinations of grant types (authorization code, implicit, etc.) can affect what response types are permissible.

- **Testing Environment**: If you are using a test environment, ensure it's properly in sync with production settings.

---

#### Documentation and Resources for Guidance

- [Azure AD App Registration Overview](https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)
- [Use the OAuth 2.0 Authorization Code Authorization Flow](https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-Oauth2-auth-code-flow)
- [Microsoft identity platform and OAuth 2.0](https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-protocols-oidc)
- [Azure AD response type options](https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow#response-types)

#### Test Documentation Reachability

- Verify that the links provided above lead to the Microsoft documentation by attempting to access them in a browser.

---

#### Advice for Data Collection

- Collect details of the requests and responses surrounding the error, which may include HTTP request URLs, headers, and body content.
- Include the specific tenant settings, application registration IDs, and the environment (development, staging, production).
- Record any previous changes made to the application or Azure AD settings before the issue began.

Maintaining this information will aid in troubleshooting and possibly escalate the issue more effectively if needing to involve Microsoft's support.