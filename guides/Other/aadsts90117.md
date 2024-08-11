# AADSTS90117: InvalidRequestInput


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS90117 - InvalidRequestInput

Error code AADSTS90117 typically indicates that the request sent to Azure Active Directory (AAD) was malformed or that some expected fields were missing or invalid. Here's a structured approach to troubleshoot this error.

---

#### 1. Initial Diagnostic Steps

- **Identify Context**: Determine what specific action triggered the error. Was it during authentication, token refresh, or another operation? 
- **Check Request Logs**: If possible, capture the logs of the request that led to the error. This includes headers, body content, and any related diagnostics.
- **Review User Information**: Who was affected by the error? Ensure that the user account is active and properly configured in AAD.

---

#### 2. Common Issues that Cause This Error

- **Malformed Request**: The request URL may be incorrect, such as missing parameters or an invalid response type.
- **Incorrect Application ID**: Ensure that the Application ID (Client ID) used in the request is correct and registered in the Azure portal.
- **Improperly Configured Redirect URIs**: A mismatch between the redirect URI configured in Azure AD and the one used in the request can cause this error.
- **Missing Required Parameters**: Some parameters must be included in specific requests, such as `client_id`, `redirect_uri`, `response_type`, etc.
- **Invalid Scopes**: The scopes provided in the request may not match with the application's permissions or may be formatted incorrectly.
- **Entity Not Found**: For users or applications, ensure that they exist in Azure AD.

---

#### 3. Step-by-Step Resolution Strategies

1. **Review Request Syntax**:
   - Verify the URI, headers, and body of the request for incorrect or missing parameters.

2. **Validate App Registration**:
   - Go to the Azure Portal:
     - Navigate to `Azure Active Directory` > `App registrations`.
     - Find the corresponding application.
     - Check the `Application (client) ID`, and ensure it's the one being used in the request.

3. **Check Redirect URIs**:
   - Still in the App registration:
     - Go to `Authentication`.
     - Ensure the `Redirect URIs` list includes the one used in your application.

4. **Test Required Parameters**:
   - Confirm all required parameters are present. Typical parameters include:
     - `client_id`
     - `redirect_uri`
     - `grant_type` (if applicable)
     - `scope`

5. **Validate Scopes**:
   - Ensure the requested scopes in your authentication request are proper. They should match those configured for your app in Azure AD.

6. **Inspect for Typos**:
   - Address any potential typos in the application, user information, or even in the request URIs.

7. **Consult Azure Sign-In Logs**:
   - In the Azure portal, navigate to `Azure Active Directory` > `Sign-ins`.
   - Look for failures to gather more specific information about the request that caused the failure.

8. **Re-test**: 
   - Make adjustments based on findings and re-test the request to see if the issue persists.

---

#### 4. Additional Notes or Considerations

- **HTTP Method**: Ensure you’re using the correct HTTP method (GET, POST, etc.) as required by the authentication flow.
- **Service Health**: Check Azure status for any ongoing issues that may be impacting your requests.
- **Network Conditions**: Sometimes, network-related issues can also cause malformed requests if requests are being mishandled.

---

#### 5. Documentation Where Steps Can Be Found

- Microsoft Documentation for [Azure Active Directory Authentication Scenarios](https://docs.microsoft.com/en-us/azure/active-directory/develop/authentication-scenarios)
- [Azure AD App Registration Overview](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)
- [Troubleshoot Azure AD sign-in issues](https://docs.microsoft.com/en-us/azure/active-directory/reports-monitoring/troubleshoot-sign-in-issues)

---

#### 6. Test Documentation Reachability

- Verify the links to the documentation are reachable directly in your browser.
    - [Authentication Scenarios](https://docs.microsoft.com/en-us/azure/active-directory/develop/authentication-scenarios)
    - [App Registration Overview](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)
    - [Troubleshooting Sign-in Issues](https://docs.microsoft.com/en-us/azure/active-directory/reports-monitoring/troubleshoot-sign-in-issues)

---

#### 7. Advice for Data Collection

- **Prepare Logs**: Capture network logs from the client-side, especially for the authentication request and response.
- **Include Environment Details**: Note the platform, language, and library versions you are using.
- **Document Error Messages**: Take detailed notes on any error messages or codes returned by the Azure AD service.

---

By following this guide, you should be able to effectively diagnose and resolve the AADSTS90117 error.

Category: Other