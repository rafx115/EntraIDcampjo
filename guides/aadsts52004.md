# AADSTS52004: DelegationDoesNotExistForLinkedIn - The user has not provided consent for access to LinkedIn resources.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS52004

**Error Code Description:**  
**AADSTS52004: DelegationDoesNotExistForLinkedIn**  
The user has not provided consent for access to LinkedIn resources.

---

### Initial Diagnostic Steps
1. **Confirm User Information**:
   - Verify the account used for authentication. Ensure it is a valid user connected to an Azure Active Directory (AAD) tenant.

2. **Check Application Registration**:
   - Identify the application that the user is trying to access and ensure it is registered correctly in the Azure portal.

3. **Review LinkedIn Integration**:
   - Ensure that the LinkedIn service is integrated correctly with the Azure AD application.

### Common Issues Causing This Error
- **Lack of User Consent**: The user has not granted the necessary permissions for the application to access LinkedIn resources.
- **Incorrect Application Permissions**: The permissions required for LinkedIn integration might not be correctly configured.
- **Expired or Revoked Consent**: Previous user consent may have expired or been revoked.
- **Application Incorrectly Setup**: The app might not have the LinkedIn API permissions enabled.

### Step-by-Step Resolution Strategies
1. **Check Application Permissions**:
   - Go to the Azure portal → Azure Active Directory → App registrations → [Your Application].
   - Navigate to **API permissions** and verify that the LinkedIn permissions are listed and correctly configured.
   - If permissions are missing, click on **Add a permission** and select LinkedIn to add the necessary permissions.

2. **User Consent**:
   - Confirm that the user has provided the necessary consent for the application.
   - You can prompt the user to re-authenticate and grant consent. This can often be done by navigating to the application’s URL in a browser and signing in.

3. **Admin Consent**:
   - If the application requires admin-level permissions, ensure that admin consent has been granted.
   - This can typically be done in the Azure portal by an administrator approving permissions.

4. **Check for Refresh Tokens**:
   - Verify if the user’s refresh token is still valid. If the token has expired, the user will need to sign in again.

5. **Review LinkedIn API Status**:
   - Ensure that there are no outages or issues with the LinkedIn API service. You can check LinkedIn’s status page for that information.

6. **Testing**:
   - After making the necessary changes, perform a test to ensure that the error has been resolved. Have the user log back into the app and check if they can now access LinkedIn resources.

### Additional Notes or Considerations
- It's crucial that the LinkedIn integration aligns with any organizational policies related to user data and consent.
- If changes are made to application permissions or account settings, it is advisable to wait a few minutes before retesting, as changes may take time to propagate.
- Ensure that the application is using the correct OAuth scopes when requesting LinkedIn access.

### Documentation for Guidance
- [Microsoft Documentation on AADSTS Authentication Error Codes](https://docs.microsoft.com/en-us/azure/active-directory/develop/reference-aadsts-error-codes)
- [Azure AD App Registrations - API Permissions](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-app-permissions)
- [LinkedIn API Documentation](https://docs.microsoft.com/en-us/linkedin/shared/integrations/people/profile-api)

### Advice for Data Collection - Event Viewer Logs, NetTrace, Fiddler
- **Event Viewer Logs**: Check logs on the server where the application is hosted to see if any authentication or error logs provide additional insights.
- **Network Traces**: Use tools such as **NetTrace** to capture the traffic and look for specific requests that might show failed API calls or errors in detail.
- **Fiddler**: Use Fiddler to inspect HTTP requests and responses between client and server. Look specifically for authorization headers and responses from LinkedIn that could indicate what permission is lacking.

Collecting these logs and traces can provide more context around the authentication process and help narrow down the root cause of the issue.