# AADSTS50194: Application '{appId}'({appName}) isn't configured as a multitenant application. Usage of the /common endpoint isn't supported for such applications created after '{time}'. Use a tenant-specific endpoint or configure the application to be multitenant.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS50194 Error Code

**Error Code:** AADSTS50194  
**Description:** "Application '{appId}' ({appName}) isn't configured as a multitenant application. Usage of the /common endpoint isn't supported for such applications created after '{time}'. Use a tenant-specific endpoint or configure the application to be multitenant."

---

### Initial Diagnostic Steps

1. **Identify the Application:**
   - Note the `{appId}` and `{appName}` from the error message.
   - Determine the application's function and intended audience (single-tenant or multitenant).

2. **Check Endpoint Usage:**
   - Identify which endpoint your application is trying to use (`/common`, `/organizations`, `/consumers`).
   - Note that single-tenant applications must not use the `/common` endpoint.

3. **Review Application Configuration:**
   - Visit the Azure portal to check the app registration settings for the application.

---

### Common Issues that Cause this Error

1. **Application Not Configured as Multitenant:**
   - The application is registered as single-tenant but attempting to authenticate using the multitenant `/common` endpoint.

2. **Endpoint Mismatch:**
   - Use of `/common` endpoint when the application is single-tenant, leading to this error.

3. **Recent Changes to the Application:**
   - Applications created after a certain date must explicitly be made multitenant; older applications may have defaulted to being multitenant.

4. **Misconfigured Permissions:**
   - The application might also have insufficient permissions for the operation intended.

5. **Session or Token Issues:**
   - Tokens may be cached incorrectly, leading to confusion in authentication attempts.

---

### Step-by-Step Resolution Strategies

1. **Review Application Registration:**
   - Go to the [Azure Portal](https://portal.azure.com).
   - Navigate to the "Azure Active Directory" → "App registrations."
   - Find your application using the `{appId}` or `{appName}`.

2. **Change Application to Multitenant:**
   - In the app's registration page, select "Authentication."
   - Under "Supported account types," change the option to "Accounts in any organizational directory (Any Azure AD directory - Multitenant)."

3. **Update API Permissions:**
   - Check the "API permissions" section to ensure that the appropriate permissions are granted.
   - If required, add the permissions needed for your application and ensure they are granted admin consent.

4. **Update Application Logic:**
   - Modify any hardcoded endpoint references in your application to a tenant-specific endpoint if you do not want the application to be multitenant.

5. **Test the Application:**
   - After making changes, test the application using the new configuration and endpoints to ensure that the error no longer appears.

6. **Monitor and Validate:**
   - Use Azure's logs and monitoring tools to check for issues after resolution.

---

### Additional Notes/Considerations

- **Understand Multitenancy:** Make sure you understand multitenancy implications for your application, such as user data isolation and consent framework.
- **Documentation Review:** Familiarize yourself with Azure's guidelines on app registrations and multitenancy to ensure compliance.

---

### Documentation for Guidance

- Azure Active Directory Documentation: [Microsoft Identity Platform documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/)
- App registration settings: [Register an application with Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)
- Multitenant applications: [Transform your app into a multitenant application](https://docs.microsoft.com/en-us/azure/active-directory/develop/scenario-desktop-authenticate)

---

### Advice for Data Collection (Event Viewer Logs, NetTrace, Fiddler)

- **Event Viewer Logs:**
  - Check logs on both the client and the server for any specific error codes or messages that may provide additional context for the failure.

- **Network Tracing:**
  - Use `network tracing` tools to log and analyze the communication between your application and Azure AD. Capture the details during the authentication flow to verify endpoint access.

- **Fiddler:**
  - Use Fiddler to inspect HTTP requests/responses to verify correct endpoints, see tokens being sent/received, and identify issues in the OAuth flow.

Following these steps should assist in diagnosing and resolving the AADSTS50194 error effectively. If further issues arise, consider engaging Microsoft support for advanced troubleshooting.