
# AADSTS65002: Consent between first party application '{applicationId}' and first party resource '{resourceId}' must be configured via preauthorization - applications owned and operated by Microsoft must get approval from the API owner before requesting tokens for that API. A developer in your tenant might be attempting to reuse an App ID owned by Microsoft. This error prevents them from impersonating a Microsoft application to call other APIs. They must move to another app ID they register.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS65002

Error AADSTS65002 occurs during authentication/authorization processes within Azure Active Directory (AAD), specifically indicating that a first-party application is trying to access a resource (API) without the necessary consent configuration. Here’s a detailed troubleshooting guide to assist you in resolving this issue.

---

#### Initial Diagnostic Steps

1. **Identify the Application and Resource IDs**:
   - Review the error description to extract the `{applicationId}` and `{resourceId}`.
   - Identify the application attempting to authenticate and the resource it is trying to access.

2. **Check Application Ownership**:
   - Determine if the application ID (`{applicationId}`) belongs to your organization or is owned by Microsoft (first party).
   - Use Azure AD portal to verify the app registration details.

3. **Review the Authentication Flow**:
   - Identify if the application is using OAuth or other authentication methods.
   - Check if the request includes the necessary scopes for accessing the resource.

---

#### Common Issues That Cause This Error

1. **Using a Microsoft-Owned Application ID**: 
   - Attempting to use an application ID that is registered by Microsoft (e.g., Microsoft Graph) without proper pre-authorization.

2. **Lack of Consent Configuration**:
   - The application has not been granted the necessary permissions for the requested resource (API).

3. **Misconfigured App Registration**:
   - The application might be misconfigured in AAD, leading to incorrect authentication requests.

4. **Scope Issues**:
   - The required scopes are not included in the token request.

---

#### Step-by-Step Resolution Strategies

1. **Change Application ID**:
   - If the application ID is owned by Microsoft (e.g., for Microsoft platforms/SDKs):
     - Create a new application using your organization's Azure AD and register it.
     - Replace the current application ID with this new ID in your application.

2. **Set Up Pre-Authorization**:
   - If you are trying to access a Microsoft-owned API (such as Microsoft Graph API):
     - Follow the pre-authorization request process. This typically involves:
       - Contacting the API owner to request consent (in case of MS APIs, this may involve filling out forms as per Microsoft’s guidelines).
       - They may provide you with the necessary permissions or setup required for your application.

3. **Grant Permissions**:
   - For registered applications in your organization:
     - Navigate to Azure Active Directory > App registrations.
     - Select your application, then go to **API permissions**.
     - Ensure that the permissions for the required resources are correctly set and grant admin consent if necessary.

4. **Review and Update Scopes**:
   - Verify that the scopes included in the token request match the permissions your application has been granted during the registration in AAD.

5. **Review Application Manifest**:
   - Check if the application's manifest contains the proper configuration for the required API permissions.

---

#### Additional Notes or Considerations

- **Reaching Out to API Owners**: Microsoft does not automatically grant approvals for API access. Ensure that you follow the protocol for requesting the necessary permissions.
- **Testing with Proper Credentials**: Always test with a user account that has admin privileges to ensure that permissions issues are not affecting the result.
- **Environment Consistency**: Ensure that endpoints (production, staging, etc.) are configured correctly and consistently.

---

#### Documentation for Guidance

- Azure Active Directory: [Register an application with Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)
- Azure AD API Permissions: [Configure permissions in Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-app-permissions-and-admin-consent)
- Pre-Authorization Process: [Requesting permissions for a Microsoft-owned API](https://docs.microsoft.com/en-us/azure/active-directory/develop/scenario-user-impersonation)

---

#### Data Collection via Event Viewer Logs, Nettrace, Fiddler

- **Event Viewer Logs**:
  - Check the Event Viewer for any logs corresponding to failed authentication attempts. Look under "Applications and Services Logs" > "Microsoft" > "Windows" > "Identity" for relevant event logs.

- **NetTrace**:
  - Use network tracing tools to capture outgoing HTTP requests to AAD. Check for the request/response details, including any error codes and messages returned.

- **Fiddler**:
  - Utilize Fiddler to inspect the request and response headers while making authorization requests to AAD. This can help you verify the structure of the requests, including the authorization header and scopes included.

By following this guide, you should be able to diagnose and resolve the AADSTS65002 error effectively. If additional issues arise, consider reaching out to Microsoft support for more in-depth assistance.