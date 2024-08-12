
# AADSTS90099: The application '{appId}' ({appName}) has not been authorized in the tenant '{tenant}'. Applications must be authorized to access the external tenant before partner delegated administrators can use them. Provide pre-consent or execute the appropriate Partner Center API to authorize the application.


## Troubleshooting Steps
## Troubleshooting Guide for Error Code AADSTS90099

**Error Description:**  
The application '{appId}' ({appName}) has not been authorized in the tenant '{tenant}'. Applications must be authorized to access the external tenant before partner delegated administrators can use them. Provide pre-consent or execute the appropriate Partner Center API to authorize the application.

### Initial Diagnostic Steps

1. **Understand the Error**: AADSTS90099 indicates that the application in question has not been authorized by the tenant that is being accessed. This usually happens when an application attempts to perform operations in a tenant that has not explicitly consented to the application’s permissions.

2. **Identify Key Components**:
   - **App ID ({appId})**: The unique identifier for the application.
   - **App Name ({appName})**: The name of the application that is trying to access resources.
   - **Tenant ID or Domain**: The identifier for the Azure Active Directory tenant that is being accessed.

3. **Check User Permissions**: Verify that the user or the delegated admin trying to access the application has the correct roles and permissions in the Azure AD tenant.

4. **Verify Application Registration**: 
   - Ensure that the application is correctly registered in the Azure AD tenant.
   - Check whether the app registration includes the necessary API permissions.

### Common Issues That Cause This Error

1. **Lack of Pre-Consent**: The application has not received pre-consent from the tenant administrators.

2. **Missing Application Registration**: The application may not be registered in the target tenant.

3. **Role and Permissions Issues**: The delegated administrator role might not have enough permissions to authorize the application.

4. **API Permissions Not Granted**: The required API permissions for the app might not be granted, or admin consent may not have been provided.

5. **Conflicting Consent Parameters**: The parameters being passed when initiating the authorization flow might conflict with what is expected from the Azure AD tenant.

### Step-by-Step Resolution Strategies

1. **Authenticate the Delegated Administrator**:
   - Ensure that the user account attempting to access the resource is a delegated administrator with sufficient privileges.

2. **Pre-Consent the Application**:
   - As an admin in the Azure AD tenant, navigate to Azure Portal.
   - Go to **Azure Active Directory** -> **Enterprise applications**.
   - Search for the application using the App ID or App Name.
   - Grant admin consent for the necessary permissions if consent has not been provided.

3. **Using Partner Center API**:
   - If programmatic authorization is needed, consider executing the relevant Partner Center API to authorize the application directly.
   - Documentation for Partner Center APIs can be found in the official Microsoft Partners documentation.

4. **Review Application Registration**:
   - Confirm that the application is registered within the tenant.
   - Go to the **Azure AD** section in the portal, and check under **App registrations**.

5. **Check Required API Permissions**:
   - In the app registration, go to **API permissions**.
   - Ensure that the application has permissions correctly set up and that admin consent has been granted for those permissions.

6. **Testing**:
   - After making the changes, attempt to access the application again to confirm whether the issue has been resolved.

### Additional Notes or Considerations

- Make sure to account for the possibility of multiple tenants and check if the application is attempting to access a tenant where it has not been authorized.
- For any multi-tenant applications, ensure that they follow best practices for security and authentication.
- Regularly review application permissions and consent settings to avoid such issues.

### Documentation for Guidance

- [Get Started with Azure AD](https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-v2-netcore)
- [Azure AD Application Registration](https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-apps)
- [Admin consent in Azure AD](https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-admin-consent)
- [Partner Center API Reference](https://learn.microsoft.com/en-us/partner-center/developers/partner-center-api-reference)

### Advice for Data Collection

If the problem persists or additional troubleshooting is needed:

1. **Event Viewer Logs**: 
   - Check Event Viewer on the client machine or server for any related logs that could indicate authentication issues or errors.

2. **Network Tracing**: 
   - Use tools like **NetTrace** or **Fiddler** to capture network traffic when the issue occurs. This will help identify if proper API requests are being made or if any unexpected errors occur during communication.

3. **Error Codes**: 
   - Look for specific error codes or descriptions in the traces that may provide further insight into what is failing in the authorization process.

By following these steps, you should be able to diagnose and resolve the AADSTS90099 error effectively.