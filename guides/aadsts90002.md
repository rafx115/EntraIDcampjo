# AADSTS90002: InvalidTenantName - The tenant name wasn't found in the data store. Check to make sure you have the correct tenant ID. The application developer will receive this error if their app attempts to sign into a tenant that we cannot find. Often, this is because a cross-cloud app was used against the wrong cloud, or the developer attempted to sign in to a tenant derived from an email address, but the domain isn't registered.


## Troubleshooting Steps
## Troubleshooting Guide for Error Code AADSTS90002

### Overview
The error code AADSTS90002 ("InvalidTenantName") indicates that the tenant associated with the sign-in request could not be found in the Azure Active Directory (Azure AD) data store. This typically occurs when an application attempts to authenticate against a wrong or unregistered tenant.

### Initial Diagnostic Steps
1. **Check the Tenant ID or Name**: Confirm that the tenant ID (GUID) or the tenant name (domain) being used in the application or the sign-in process is correct.
2. **Verify the Application URL**: Ensure that the redirect URI or request URL for the app is properly configured and matches the registered application in Azure AD.
3. **Determine the Active Directory Location**: Ensure you are attempting to sign in to the correct Azure AD geographical region, especially if using region-specific URLs.
4. **Cross-Cloud Validation**: If applicable, verify whether you're trying to access an Azure service in a different cloud (e.g., Azure Government, Azure China, etc.) and ensure the correct environment is being targeted.
5. **Reproduce the Issue**: Try to reproduce the error outside of your application (e.g., through a web browser) to get a clearer understanding of the error context.

### Common Issues That Cause This Error
- **Incorrect Tenant Name or ID**: Using a tenant name or ID that does not exist or is not correctly formatted.
- **Cross-Environment Misconfiguration**: Attempting to access an Azure AD application under a cloud environment that the tenant does not belong to.
- **Domain Not Registered**: When signing in with an email address, the domain is not recognized by Azure AD.
- **Application Misconfiguration**: Redirect URIs not matching what is registered in the Azure portal.
- **Expired or Invalid Application Credentials**: The application might be using expired client secrets or certificates.

### Step-by-Step Resolution Strategies
1. **Confirm Tenant Information**:
   - Log in to the Azure portal: [Azure Portal](https://portal.azure.com)
   - Navigate to Azure Active Directory > Properties and check the Tenant ID and Domain Names.
   - If accessing based on email, ensure the domain is listed under your Azure AD.

2. **Review Application Registration**:
   - Go to Azure Active Directory > App registrations.
   - Find the application and verify the Application (client) ID and redirect URIs.
   - Ensure the application is permitted for sign-in in the correct tenant.

3. **Provide Correct Redirect URI**:
   - Under App registrations, select your application and go to Authentication.
   - Verify that the redirect URLs are exactly matching what you are using in your requests.

4. **Adjust Application Settings (if needed)**:
   - In your application code/configuration, ensure that the tenant ID/name is correctly referenced and is the one configured in Azure AD.
   - Modify any cross-cloud request URLs or settings as per environment requirements.

5. **Check Role and Permissions**:
   - Ensure that your application has the necessary API permissions granted and consented to access resources in the tenant.

6. **Test Authentication**:
   - Use tools like Postman or JWT.io to simulate the authentication request to see if the same error arises.
   - If using any libraries (like MSAL), make sure they are up to date.

### Additional Notes or Considerations
- Keep in mind that Azure AD multi-tenant applications will behave differently when trying to sign in from tenants that are not part of the original application registration.
- If you’re managing multiple tenants, be extra cautious with tenant-specific details during development/deployment.

### Documentation for Guidance
- Azure AD Sign-In Troubleshooting: [Azure AD Sign-In Errors](https://docs.microsoft.com/en-us/azure/active-directory/develop/troubleshoot-authentication)
- Overview of Azure AD Tenants: [What is Azure Active Directory?](https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-overview)
- Working with App Registrations: [Introduction to Azure AD app registrations](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)

### Advice for Data Collection (Event Viewer Logs, Network Tracing)
- **Event Viewer Logs**: Check for any related logs under "Windows Logs > Applications and Services Logs" on client machines for Azure AD or authentication errors.
- **Network Trace**:
   - Use tools like **Netmon**, **Wireshark**, or **Fiddler** to capture the requests/responses made during the sign-in attempt.
   - Look for errors in the HTTP responses that may provide insight into what is going wrong, focusing on 4xx status codes.

By following this guide, you should be able to troubleshoot and resolve the AADSTS90002 error effectively.