# AADSTS90093: GraphUserUnauthorized - Graph returned with a forbidden error code for the request.


## Troubleshooting Steps
Certainly! The error code AADSTS90093 with the description "GraphUserUnauthorized - Graph returned with a forbidden error code for the request" typically indicates that the user does not have the necessary permissions to perform the requested operation on Microsoft Graph API. Here’s a detailed troubleshooting guide for dealing with this error.

### Troubleshooting Guide for AADSTS90093

#### Initial Diagnostic Steps
1. **Review the Error Message**: Analyze the full error response for details. Besides AADSTS90093, other relevant details may help pinpoint the issue (such as the specific Graph API call being made).

2. **Check User Authentication**: Ensure that the user is authenticated properly and has a valid token, which is not expired or revoked.

3. **Identify API Request**: Determine which specific Graph API endpoint and operation triggered the error. This will help narrow down the areas of concern.

4. **Confirm User Role**: Check if the user has the correct roles and permissions assigned in Azure Active Directory (AAD).

#### Common Issues that Cause This Error
1. **Insufficient Permissions**: The user lacks the required permissions to access the specific resource or endpoint.

2. **Scope Mismatch**: The requested scope during authentication may not match the permissions configured in the Azure AD app.

3. **User Account Issues**: The user account could be disabled, not licensed, or not properly set up in AAD.

4. **Application Permissions**: If using application permissions, ensure the application has the correct roles assigned to it in the Azure portal.

5. **Consent Not Granted**: An administrator might need to grant consent for the permissions requested by the app, particularly for permissions that require higher-level access.

#### Step-by-Step Resolution Strategies

1. **Check Permission Assignments**:
   - Navigate to the Azure portal.
   - Go to "Azure Active Directory" > "Users" > [select the user] > "Assigned roles."
   - Ensure the user has appropriate roles and is not blocked.

2. **Verify API Permissions for the App**:
   - In the Azure portal, go to "Azure Active Directory" > "App registrations" > [select your app].
   - Under "API permissions", review the list of delegated and application permissions.
   - Ensure that the required permissions are present and properly configured.

3. **Modify Scopes if Necessary**:
   - When obtaining the token, specify the correct scope that matches your permissions in Azure.
   - Use the Microsoft identity platform to request the necessary scopes.

4. **Administrator Consent**:
   - If certain permissions require admin consent, navigate to "API permissions" in your app registration.
   - Click on "Grant admin consent for [Tenant]".

5. **Check Directory Role**:
   - Some operations may only be allowed for users with certain directory roles. Ensure the user has the proper directory roles if required by the Graph API call.

6. **Retry the Operation**: After changes are made, retry the API call to ensure that the issue is resolved.

#### Additional Notes or Considerations
- Review Microsoft Graph API documentation for specific permission requirements for each API endpoint.
- If operation still fails, consider capturing the full response returned by the API for more clarity on the issue.

#### Documentation for Guidance
- **Microsoft Graph Permissions Overview**: [Microsoft Graph permissions reference](https://docs.microsoft.com/en-us/graph/permissions-reference)
- **Assigning Roles in Azure AD**: [Manage Azure AD roles](https://docs.microsoft.com/en-us/azure/active-directory/roles/manage-roles)
- **Requesting Tokens and Scopes**: [Authorization and scopes](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-authorization-code-flow)

#### Testing Documentation Reachability
Make sure you can access the provided links to confirm that they are valid and reachable.

1. Open a web browser.
2. Enter the provided URLs one by one and check that they lead to the intended documentation pages.

#### Advice for Data Collection
- **Log Error Responses**: Capture full HTTP response details, including status codes and body responses to analyze failures.
- **Audit Logs**: Use Azure AD audit logs to track changes and access attempts related to users and applications.
- **Token Inspection**: Use tools like [JWT.io](https://jwt.io) to decode the JWT token and verify the `scopes` and `roles` included in it.

By following these steps, you should be able to diagnose and resolve the AADSTS90093 error effectively.

Category: Other