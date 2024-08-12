
# AADSTS65005: MisconfiguredApplication - The app required resource access list doesn't contain apps discoverable by the resource, or the client app has requested access to resource, which wasn't specified in its required resource access list or Graph service returned bad request or resource not found. If the app supports SAML, you might have configured the app with the wrong Identifier (Entity). To learn more, see the troubleshooting article for errorAADSTS650056.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS65005 Error

#### Error Description
The error code AADSTS65005 indicates a misconfiguration in an application that is trying to access required resources but fails due to several potential issues. This can occur when the application’s required resource access list does not align with what is needed for the operations being requested.

### Initial Diagnostic Steps
1. **Review the Error Message**: Carefully read the detailed error message for clues as to what resource is causing the issue.
2. **Check Application Registration**:
   - Go to Azure Portal.
   - Select "Azure Active Directory" > "App registrations" and locate the application.
3. **Inspect Required Permissions**:
   - In the app registration, check "API permissions" to ensure the required permissions are listed.
4. **Validate Resource ID and Scopes**: Verify that the correct resource IDs and scopes are requested in the app.
5. **SAML Configuration**: If using SAML, ensure that the Identifier (Entity ID) is correctly configured.

### Common Issues that Cause This Error
1. **Misconfigured API Permissions**: Required permissions may not be granted to the application, or there may be a mismatch.
2. **Missing Resource in Required Access List**: The requested resource is not specified in the app's required resource access list.
3. **SAML Configuration Issues**: Incorrect Entity IDs or other SAML settings can cause this error.
4. **Graph API Issues**: If the application interacts with the Microsoft Graph API, confirm that the app is correctly configured to use it.
5. **User Consent Denied**: Users may lack permission or consent to access the application resources.
  
### Step-by-Step Resolution Strategies
1. **Check API Permissions**:
   - In Azure Active Directory, navigate to "App registrations".
   - Choose your application.
   - Verify under "API permissions" that the required permissions for the APIs your application accesses are listed and correctly configured.
   - If needed, click "Add a permission" to include any missing permissions.

2. **Review Manifest**:
   - Check the app's manifest to see if the "requiredResourceAccess" section correctly lists the required resources and their scopes.
   - Ensure that all required permissions are included in the manifest.

3. **Update SAML Configuration**:
   - If using SAML, double-check the Entity ID and endpoints (ACS URL) in the Azure portal against the configurations in your application.
   - Make sure the forward and backward relations are properly set up.

4. **User Consent**:
   - Visit the "Enterprise applications" panel in Azure AD.
   - Check for user consent and ensure that it has been granted.

5. **Testing and Validation**:
   - Use Postman or similar tools to test API calls to ensure that tokens can be retrieved and resources accessed.

6. **Consult Logs**:
   - Gather logs from Azure AD sign-in logs which can provide more context on repeated failures.

### Additional Notes or Considerations
- Always confirm that your application is using the correct endpoint URLs (both for OAuth and SAML).
- Be mindful of changes in resource permissions; updates may take a few moments to propagate.
- Ensure AD group membership aligns with required permissions.

### Documentation for Guidance
- [Microsoft Identity Platform Documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/)
- [Azure AD App Registration Overview](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)
- [Configuring API Permissions](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-permissions-and-consent)

### Advice for Data Collection
- **Event Viewer Logs**: Check the Application and System logs for errors related to authentication or application registration.
- **Nettrace**: Use Nettrace to monitor network activity. This can help identify potential misconfigurations in network requests.
- **Fiddler**: With Fiddler, inspect HTTP requests and responses to see if the intended permissions are being requested properly and if any errors are returned.

By following these steps, you should be able to effectively troubleshoot and resolve the AADSTS65005 error.