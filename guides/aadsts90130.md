
# AADSTS90130: NonConvergedAppV2GlobalEndpointNotSupported - The application isn't supported over the/commonor/consumersendpoints. Use the/organizationsor tenant-specific endpoint instead.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS90130

**Error Code:** AADSTS90130  
**Description:** NonConvergedAppV2GlobalEndpointNotSupported - The application isn't supported over the /common or /consumer endpoints. Use the /organizations or tenant-specific endpoint instead.

---

### Initial Diagnostic Steps

1. **Confirm the Error Message:** Double-check the exact error code and description to ensure it matches AADSTS90130.
2. **Identify Application Type:** Determine whether the application is intended for a specific organization, a multi-tenant application, or only for personal Microsoft accounts.
3. **Review Authentication Request:** Inspect the authentication request URL to see if it is using the /common or /consumer endpoints.
4. **Check User Context:** Identify if the user trying to authenticate belongs to a tenant (organization) or is a personal account.

---

### Common Issues that Cause This Error

1. **Using Incorrect Endpoint:** Attempting to authenticate using the /common or /consumer endpoints for an application that is intended for organizational use only.
2. **Application Configuration Mismatch:** The application may be configured incorrectly in Azure AD to allow only organizational sign-ins.
3. **Token Request Issues:** Issues with how tokens are being requested or returned by the application.

---

### Step-by-Step Resolution Strategies

1. **Update the Authentication Request Endpoint:**
   - For organizational applications, replace the endpoint in your authentication request URL from:
     ```
     https://login.microsoftonline.com/common/oauth2/v2.0/authorize
     ```
     to:
     ```
     https://login.microsoftonline.com/{tenant-id}/oauth2/v2.0/authorize
     ```
   - Alternatively, use the `/organizations` endpoint:
     ```
     https://login.microsoftonline.com/organizations/oauth2/v2.0/authorize
     ```

2. **Check Application Settings in Azure AD:**
   - Navigate to the Azure Portal.
   - Go to **Azure Active Directory** > **App registrations**.
   - Find your application and ensure that it is set up to accept sign-ins from the correct types of users (either organizational or personal).

3. **Modify App Registration Permissions:**
   - Ensure that APIs required for the application are properly set in the application registration.
   - Adjust permissions to make sure it aligns with intended users (e.g., for organizational users, select "Accounts in this organizational directory only").

4. **Review API and Redirect URI Configuration:**
   - Confirm that the redirect URIs defined in the app registration are correct and that they match the requests made by your application.

5. **Test the Configuration:**
   - After making adjustments, attempt to authenticate again using the updated endpoint and application configuration.

---

### Additional Notes or Considerations

- **Testing:** It’s a good practice to test authentication with both a tenant-specific account and a personal account (if applicable) to ensure that the application behaves as expected for both scenarios.
- **Endpoint Usage:** Remember that the /common endpoint is generally used for applications that are intended for a wide array of users, including both personal and organizational accounts. Ensure that your application's intended audience matches the endpoint being utilized.

---

### Documentation References

- **Microsoft Authentication Library (MSAL) documentation:** [MSAL Overview](https://docs.microsoft.com/en-us/azure/active-directory/develop/msal-overview)
- **Azure AD Authentication Endpoints:** [Authentication Scenarios](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow#authentication-endpoints)
- **Configure app registration in Azure AD:** [Register an application with the Azure AD portal](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)

### Testing the Documentation

1. Visit the links provided above to ensure they are reachable and provide relevant, detailed information.
2. Make sure to check across different browser sessions or networks to rule out any local source issues.

---

### Advice for Data Collection

- Collect logs from the application trying to authenticate, including request URLs, HTTP response codes, and error messages returned.
- Use tools like Fiddler or browser developer tools to capture detailed information about the authentication requests and responses.
- If applicable, gather information about the user accounts and any specific tenant settings that may influence authentication behavior.

Following this troubleshooting guide should help you resolve the AADSTS90130 error effectively and provide a deeper understanding of Azure Active Directory authentication issues.