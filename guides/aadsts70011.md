# AADSTS70011: InvalidScope - The scope requested by the app is invalid.


## Troubleshooting Steps
Certainly! The error code **AADSTS70011** occurs when the application requests a scope that is not valid for the Azure Active Directory (AAD) resource. Below is a detailed troubleshooting guide to address and resolve this error.

### **Troubleshooting Guide for AADSTS70011**

#### **1. Initial Diagnostic Steps**
- **Review the Error Message**: Ensure that the error message accompanies the error code to provide context. The message typically indicates the specific scope that is considered invalid.
- **Check Application Registration**: Verify that the application is properly registered in the Azure portal and that the configuration matches the required scopes.
- **Review the API Permissions**: Navigate to the Azure AD app registration and ensure the requested scopes are listed among the API permissions for the application.

#### **2. Common Issues that Cause This Error**
- **Non-Existent Scope**: The scope specified does not exist in the Azure AD or is not part of the application’s declared permissions.
- **Misspelled Scope**: There may be a typographical error in the scope name.
- **Low Permission Levels**: The application may not have the necessary permission granted by an administrator to access a specific scope.
- **Consents Not Granted**: If using scopes that require user consent or admin consent, these may not have been granted.

#### **3. Step-by-Step Resolution Strategies**
1. **Identify the Requested Scope**:
   - Look at the login request and identify the exact scope being requested that triggered the error.

2. **Verify Scope in Azure Portal**:
   - Go to the **Azure Portal**.
   - Navigate to **Azure Active Directory** > **App registrations** > [Your App].
   - Under **API Permissions**, check that the requested scope is included in the list.

3. **Correct Any Typos**:
   - Ensure that the scope is spelled correctly and matches the format required by the resource.

4. **Grant Necessary Permissions**:
   - Check if additional permissions are needed.
   - If new scopes were added, ensure they are marked for admin consent and have been approved as necessary.

5. **Consent to Permissions**:
   - Use options within Azure AD to grant user or admin consent for the required permissions. If required, you may need to re-authenticate to obtain the necessary tokens.

6. **Update the Application Configuration**:
   - If scopes are changed in Azure AD, ensure those updates are reflected in your application’s authentication code/configuration.

7. **Re-Test the Application**:
   - After making any necessary changes, re-test the app authentication to confirm that the error has been resolved.

#### **4. Additional Notes or Considerations**
- Ensure that the scopes are consistent with the permissions required for the specific API you are trying to access.
- If integrating with Microsoft Graph or other Microsoft services, confirm the latest list of scopes in the official documentation.
- If you’re using OAuth2 flows, ensure that the requested scopes align with the authorization flow being used (Authorization Code, Delegated Permissions, etc.).

#### **5. Documentation for Guidance**
- [Azure Active Directory Documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/)
- [API Permissions documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-app-permissions-and-admin-consent)
- [Microsoft identity platform and OAuth 2.0 scopes](https://docs.microsoft.com/en-us/azure/active-directory/develop/scopes)
- [Understanding Azure AD authentication errors](https://docs.microsoft.com/en-us/azure/active-directory/develop/scenario-desktop-authentication)

#### **6. Advice for Data Collection & Logging**
- **Event Viewer Logs**: Check the application log in the Event Viewer for additional errors or warnings that may provide more context about the failure.
- **Network Tracing**: Use **Fiddler** or similar tools to capture network traffic during the authentication process. Look for the request to the token endpoint and inspect the payload to see the exact scopes being sent.
- **Azure AD Logs**: Review the sign-in logs in the Azure AD portal to trace any authentication issues that could be related to the error.

By following these steps, you should be able to diagnose and resolve the error associated with AADSTS70011 effectively. If issues persist, consider reaching out to Azure support for more specialized assistance.