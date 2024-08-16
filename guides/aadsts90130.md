# AADSTS90130: NonConvergedAppV2GlobalEndpointNotSupported - The application isn't supported over the/commonor/consumersendpoints. Use the/organizationsor tenant-specific endpoint instead.


## Troubleshooting Steps
When encountering the AADSTS90130 error with its description "NonConvergedAppV2GlobalEndpointNotSupported," it indicates that the application you are trying to use cannot be accessed through the "/common" or consumer endpoints of Azure AD. Instead, it requires an "/organizations" endpoint or a tenant-specific endpoint.

### Troubleshooting Guide

#### Initial Diagnostic Steps
1. **Identify the Application:** Determine which application is generating the error and its intended audience (consumers or organizations).
2. **Verify Endpoint Usage:** Check if the application is configured to use the correct Azure AD endpoint. The endpoints to check are:
   - **Common Endpoint:** `https://login.microsoftonline.com/common`
   - **Organization Endpoint:** `https://login.microsoftonline.com/organizations`
   - **Tenant-Specific Endpoint:** `https://login.microsoftonline.com/{tenantID}`

#### Common Issues that Cause This Error
1. **Incorrect Endpoint Configuration:** The application may be mistakenly configured to use the "/common" endpoint instead of the correct endpoint that is needed for its intended audience.
2. **Application Type Mismatch:** The application might be using features or APIs that are only supported for organizational accounts and not for consumer accounts.
3. **Token Endpoint Misconfiguration:** Token exchanges may be incorrectly directed at the consumer endpoint when they should be aimed at the organizational endpoint.

#### Step-by-Step Resolution Strategies
1. **Update the Application Configuration:**
   - Access the application's registration in the Azure portal.
   - Ensure that the endpoints used in API calls, redirects, and authorization requests are the correct type:
     - Use `/organizations` for applications targeting organizational accounts.
     - Use a tenant-specific endpoint in the following format for tenant-based applications:
       `https://login.microsoftonline.com/{Tenant-ID}`
  
2. **Modify Application Code:**
   - If you have code or settings specifying the Azure AD endpoint, ensure that they point to the appropriate endpoint based on the application’s requirements.
   - Review your OAuth 2.0 flow to ensure the correct audience is being referenced.

3. **Testing the Change:**
   - After making modifications, perform tests to confirm the application can authenticate successfully.
   - Use Postman or equivalent tools to simulate authentication and ensure the calls return expected responses.

4. **Review Application Permissions:**
   - Check that the application has the necessary permissions set in Azure AD specified for the organization type, which may also impact the authentication flow.

#### Additional Notes or Considerations
- Ensure the application is properly categorized in Azure AD as either "Web", "Public Client", or "Single Page Application" based on its intended use case.
- Always verify the required permissions are also consistent with the endpoint you are using. Mismatches can cause authentication failures.
- If using multi-tenancy in your application, ensure you're handling responses properly to avoid endpoint type mismatches.

#### Documentation for Guidance
- For Azure AD endpoints:
  - [Azure Active Directory endpoints](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-v2-protocols)
- For configuring applications in Azure AD:
  - [Register an application in Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)
- For OAuth 2.0 and OpenID Connect in Azure AD:
  - [Use OAuth 2.0 to access the Microsoft Graph](https://docs.microsoft.com/en-us/graph/auth-v2-user)

#### Advice for Data Collection
If further investigation is needed, collect diagnostic information using:

- **Event Viewer Logs:**
  - Navigate to Event Viewer on the server or client machine and filter for logs related to authentication or application errors.
  
- **Network Tracing:** 
  - Use `nettrace` or `Fiddler` to capture and examine network traffic. Look specifically for the requests to the Azure AD endpoints and the responses returned. This will help identify where the failure occurs and if the wrong endpoint is being called.

- **Fiddler:**
  - Set breakpoints on requests to analyze request/response headers and ensure the authentication flow is being executed correctly.

By following these troubleshooting steps, it should be possible to resolve the AADSTS90130 error and ensure proper authentication for the intended audience of your application.