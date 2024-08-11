# AADSTS70011: InvalidScope - The scope requested by the app is invalid.


## Troubleshooting Steps
## Troubleshooting Guide for AADSTS70011: InvalidScope

### Overview
The error code AADSTS70011 indicates that the scope requested by the application is invalid. This usually occurs when the application is trying to acquire tokens for resources, but the specified scope does not match any defined or permitted scopes in Azure Active Directory (AAD).

### Initial Diagnostic Steps
1. **Check the Error Response**: 
   - Review the full error message in response to the request. There may be additional context that provides insight into which scope is invalid.

2. **Identify the Application**:
   - Confirm which application is generating the error and which API or resource it is trying to access.

3. **Review API Permissions**:
   - Navigate to the Azure portal. Under Azure Active Directory -> App registrations, find the impacted app and review its API permissions.

### Common Issues that Cause This Error
1. **Incorrect Scope Name**:
   - The scope is misspelled or formatted incorrectly. Ensure it's in the correct format, such as `api://{client_id}/{scope}`.

2. **Scopes Not Configured**:
   - The requested scope has not been defined in the API's manifest or the app's settings in Azure AD.

3. **Insufficient Permissions**:
   - The application does not have the requisite permissions granted in Azure AD to request the specific scopes.

4. **Permission Granting**:
   - Changes to the API permissions may not have been consented to by an admin if required, leading to scopes being denied.

5. **Token Type**:
   - The wrong type of token is being requested (for example, trying to get a user token when an app token is needed).

### Step-by-Step Resolution Strategies

#### Step 1: Verify Requested Scope
- Ensure the scope is correctly formatted and valid. Common formats include:
  - `api://<your-api-client-id>/<scope>`
  - `https://<your-api-url>/.default`
- Double-check the scope names against the documentation for the API being accessed.

#### Step 2: Review Application Registration
1. Go to the Azure portal and navigate to "Azure Active Directory".
2. Click on "App registrations" and find the app in question.
3. Select "API permissions" from the left-hand sidebar.
4. Check if the scopes you need are listed here. If not, add them.

#### Step 3: Grant Admin Consent
- If the application requires admin consent for permissions, ensure that it has been granted.
1. Still in API permissions, click "Grant admin consent for <Your Organization>" if it's available.

#### Step 4: Test with Different Scopes
- Try requesting different scopes that are known to be valid for the application.

#### Step 5: Check the Application Manifest
1. Find the app in "App registrations".
2. Click on "Manifest" in the left-hand menu.
3. Ensure the `knownClientApplications` section includes valid scopes if applicable.

### Additional Notes or Considerations
- **Versioning**: If your app or API recently changed, ensure that both the application and the permissions/scopes are updated accordingly.
- **Caching**: Sometimes old tokens may be cached leading to stale permission issues. Clear local caches if applicable.
- **Multiple Environments**: Ensure you are testing against the correct environment (e.g., production vs. development) as scopes may vary.

### Documentation
- [Azure AD Scopes and Permissions](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-app-permissions-and-secure)
- [Troubleshoot authentication issues](https://docs.microsoft.com/en-us/azure/active-directory/develop/troubleshoot-v2-implicit-grant) 

### Testing Document Accessibility
- Ensure the above documentation links are working by attempting to open them in a web browser.

### Advice for Data Collection
1. **Log Response Details**: Capture the full error response including any request ID which can be used for deeper investigation if needed.
2. **Request Content**: Keep records of what was sent in the token request (scopes, response_type, etc.).
3. **Time of Occurrence**: Note when the error occurs to check against service health or outage reports.
4. **Change History**: Document any changes made to the application or associated scopes.

By following this troubleshooting guide, you should be able to identify and resolve the AADSTS70011 error effectively.