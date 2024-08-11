
# AADSTS50194: Application '{appId}'({appName}) isn't configured as a multitenant application. Usage of the /common endpoint isn't supported for such applications created after '{time}'. Use a tenant-specific endpoint or configure the application to be multitenant.


## Troubleshooting Steps
**Troubleshooting Guide for AADSTS50194 Error:**

**Initial Diagnostic Steps:**
1. Ensure that you have the correct Application ID ('{appId}') and Application Name ('{appName}').
2. Verify the date when the application was created ('{time}').
3. Check if the application is configured as a multi-tenant application.

**Common Issues That Cause This Error:**
1. The application was not configured as a multi-tenant application during creation.
2. Usage of the /common endpoint for non-multi-tenant applications.
3. Incorrect configuration settings within the Azure Active Directory application.

**Step-by-Step Resolution Strategies:**
1. **Update the Application Configuration:**
    - Go to the Azure Portal and navigate to the Azure Active Directory section.
    - Locate your application by searching for the Application ID or Application Name.
    - Update the application to be multi-tenant. This setting allows the application to be used by accounts in any Azure AD tenant.
  
2. **Switch to Tenant-Specific Endpoint:**
    - Replace the '/common' endpoint with a tenant-specific endpoint in your application code or configuration.
    - Modify the authentication endpoint to use a tenant-specific URL instead of using the '/common' endpoint.

3. **Check Permissions and Consent:**
    - Ensure that the necessary permissions are properly configured for the application in the Azure Portal.
    - Check if users have consented to the required permissions when logging in for the first time.

**Additional Notes or Considerations:**
- Make sure to communicate with the Azure AD administrators or developers responsible for the application to coordinate any changes.
- Regularly review and update application configurations to align with best practices and security requirements.

**Documentation and Guidance:**
- Microsoft Azure Active Directory documentation provides detailed guidance on configuring multi-tenant applications and resolving related errors like AADSTS50194.
- Refer to the Azure Active Directory documentation on multi-tenant applications: [Azure AD Multi-Tenant Applications](https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-convert-app-to-be-multi-tenant).

By following these steps and considering the additional notes provided, you should be able to troubleshoot and resolve the AADSTS50194 error related to multi-tenant application configuration in Azure Active Directory.