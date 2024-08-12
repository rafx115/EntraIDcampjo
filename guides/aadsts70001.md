
# AADSTS70001: UnauthorizedClient - The application is disabled. To learn more, see the troubleshooting article for errorAADSTS70001.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS70001 Error Code

**Error Description**: `AADSTS70001` indicates that the application attempting to authenticate is disabled or deactivated in Azure Active Directory (AAD). 

### Initial Diagnostic Steps
1. **Check the Application Registration**:
   - Go to the Azure portal.
   - Navigate to **Azure Active Directory** > **App registrations**.
   - Look for the application that is encountering the issue and confirm that it exists.

2. **Check Application Status**:
   - Verify if the application is set to "Enabled" in the Application's properties.
   - Ensure you are using the correct application ID and redirect URI.

3. **Review User Permissions**:
   - Check if the user attempting to authenticate has the necessary permissions to access the application. 

4. **Examine the Authentication Code**:
   - Review the authentication flows in the code to ensure you are using the proper parameters in your authentication request.

### Common Issues Causing AADSTS70001
1. **Application Disabled**:
   - The most common cause is that the application is disabled either accidentally or intentionally.

2. **Misconfigured App Registration**:
   - App registration may have missing or incorrect settings such as Reply URLs or Permissions.

3. **User Restrictions**:
   - The user account attempting authentication may not have access to the application.

4. **Tenant Issues**:
   - Issues within specific Azure AD tenants can also lead to authentication problems.

### Step-by-Step Resolution Strategies
1. **Enable the Application**:
   - If you identified the application is disabled:
     - Navigate to the Azure portal.
     - Go to **Azure Active Directory** > **App registrations**.
     - Select the application and ensure its status is set to **Enabled**. If not, enable it.

2. **Verify Application Configuration**:
   - In the **App registrations** section, check the **Authentication** settings:
     - Ensure the Reply URLs and other settings (like the API permissions) are correctly configured.

3. **Check API Permissions**:
   - Go back to the application registration.
   - Under **API permissions**, make sure the required permissions are granted and without any pending approval.

4. **Assign Users or Groups**:
   - Make sure that the users or groups that need to use the application are assigned to it:
     - Go to **Enterprise applications** > select your application > **Users and groups** and assign the necessary users.

5. **Consult Logs for Additional Information**:
   - If the issue persists, collecting more information from various logs may be beneficial:
     - Enable Azure AD Sign-in logs to see detailed error messages.
     - Check application logs for additional context on the authentication failed events.
     
### Additional Notes or Considerations
- **Service Principal**: Ensure that if you are using a service principal for the application, it is not disabled.
- **Licensing**: Verify if any specific licensing is required for the application or user to function correctly.
- **Tenant-Specific Behavior**: Some errors may be related to configurations specific to your Azure tenant.
  
### Documentation for Guidance
- [Azure AD App Registration Overview](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)
- [Troubleshoot the AADSTS70001 Error](https://docs.microsoft.com/en-us/azure/active-directory/develop/references/aadsts-errors#aadsts70001)

### Advice for Data Collection
1. **Event Viewer Logs**: Review logs on the machine running the application. Specifically check for any application-specific logs about authentication events.
2. **Network Traces**:
   - **Nettrace**: Use this tool to capture network packets that may help identify transport-level issues.
   - **Fiddler**: Use it to capture HTTP/HTTPS traffic to see the authentication requests and responses, including headers and payload information that might be causing issues.
  
Make sure to act in accordance with compliance requirements when using any data collection tools, especially in a production environment.