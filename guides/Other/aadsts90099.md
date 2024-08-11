# AADSTS90099: The application '{appId}' ({appName}) has not been authorized in the tenant '{tenant}'. Applications must be authorized to access the external tenant before partner delegated administrators can use them. Provide pre-consent or execute the appropriate Partner Center API to authorize the application.


## Troubleshooting Steps
The error code AADSTS90099 indicates that the application in question has not been authorized to access the tenant specified. This commonly occurs in a multi-tenant application scenario, where the application needs explicit permission from the tenant administrator before it can access tenant resources.

### Troubleshooting Guide for AADSTS90099

#### Initial Diagnostic Steps
1. **Identify the Application**: Note the `{appId}` and `{appName}` from the error message. This identifies the application that is experiencing the authorization issue.
2. **Check Tenant ID**: Verify the `{tenant}` identifier to ensure you are working within the correct tenant context.
3. **Review Roles and Permissions**: Ensure that the user attempting to authenticate has the proper permissions and roles assigned relevant to the application.

#### Common Issues that Cause this Error
- The application has not been registered in the tenant.
- The application has not been granted permission by the tenant administrator.
- The application is designed to work as a multi-tenant, but no authorization has taken place in the external tenant.
- The tenant administrators are unaware of the necessity for pre-consent for partner applications.

#### Step-by-Step Resolution Strategies

1. **Check Application Registration**:
   - Log in to the Azure portal.
   - Navigate to Azure Active Directory > App registrations.
   - Search for your application using the `{appId}` or `{appName}` to ensure it is registered in the tenant.

2. **Grant Admin Consent**:
   - In the Azure portal, go to Azure Active Directory > Enterprise applications.
   - Find your application and click on it.
   - Navigate to Permissions, and verify if the required API permissions are correctly listed.
   - If not, click on “Grant admin consent for {tenant}”.

3. **Use Partner Center API for Authorization**:
   - If the application needs specific permissions that require explicit consent, you may need to call the relevant APIs to automatically authorize the application. Use the Partner Center SDK or REST API to execute the necessary authorization.
   - Refer to the [Microsoft Partner Center API documentation](https://docs.microsoft.com/en-us/partner-center/develop/overview) for details on how to authorize applications.

4. **Pre-Consent for Partner Applications**:
   - Talk to the tenant administrator and explain the process for granting consent to applications. They will need to be involved in providing the necessary consent.
   - Use the following URL format to guide admins through the consent process: 
     ```
     https://login.microsoftonline.com/{tenant}/adminconsent?client_id={appId}
     ```
   - Replace `{tenant}` and `{appId}` with the appropriate values. 

5. **Verify Tenant Configurations**:
   - Ensure that conditional access policies and any security settings applied in the tenant are not preventing the application from being authorized.

#### Additional Notes or Considerations
- If the application requires sensitive permissions, it is subject to stricter approval processes, which might delay authorization.
- Multi-tenant applications must handle user consent to permissions carefully, as the process can differ significantly between tenants.

#### Documentation for Guidance
- [Microsoft Azure Active Directory - Register an application](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)
- [Admin consent for Azure AD apps](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-admin-consent)
- [Partner Center API Overview](https://docs.microsoft.com/en-us/partner-center/develop/overview)

#### Test Document Reachability
You can test the documentation links provided above by visiting them in your web browser to ensure that they are accessible and up-to-date.

#### Advice for Data Collection
- **Collect Logs**: Gather logs from your application that recorded the authentication attempt. Logs should include timestamps, the error message, and any relevant identifiers (like user ID, tenant ID, app ID).
- **Audit Azure AD Sign-In Logs**: Go to Azure Active Directory > Sign-ins to view the authentication logs to gather insights on the requests and errors encountered.
- **Gather Feedback from Administrators**: Document any feedback or issues reported by tenant admins related to application consent or permissions.

By following this troubleshooting guide, you should be able to resolve the AADSTS90099 error efficiently and ensure that your application has been authorized properly in the tenant.

Category: Other