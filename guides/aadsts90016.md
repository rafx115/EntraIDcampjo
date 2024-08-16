# AADSTS90016: MissingRequiredClaim - The access token isn't valid. The required claim is missing.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS90016 Error Code

**Error Description:**
AADSTS90016 indicates that the access token is not valid due to a missing required claim. This can occur in scenarios where specific claims are needed for validating the token for scope, audience, or other requirements set by the application using Azure Active Directory (Azure AD).

#### Initial Diagnostic Steps

1. **Identify the Application and User:**
   - Determine which application the user was trying to access when the error occurred.
   - Identify the user account and the specific circumstances under which the error was observed.

2. **Check Token Details:**
   - Use a tool like [JWT.io](https://jwt.io/) to decode the JWT token (if available). Analyze the claims present in the token and check for missing claims that your application expects.

3. **Review the Azure AD Logs:**
   - Go to the Azure portal and navigate to the Azure Active Directory.
   - Check the Sign-ins logs for the specific error. Review timestamps and any additional error messages that might indicate what is missing.

#### Common Issues That Cause This Error

1. **Misconfiguration of Application Permissions:**
   - The application might be missing required API permissions that are necessary for the user to receive the claims needed.

2. **Missing Claims in Token Configuration:**
   - There may be specific claims that need to be included in the token but are not configured in Azure AD's token configuration options.

3. **User's Role or Group Membership:**
   - The user might need to be part of a specific group or role that is configured to receive the claims required by the application.

4. **Application Registration Issues:**
   - If the application is improperly registered in Azure AD, it may not receive the correct claims when requesting tokens.

5. **Scope and Audience Mismatch:**
   - The requested scopes in the token request might not align with the scopes for which the claims are issued.

#### Step-By-Step Resolution Strategies

1. **Application Registration Configuration:**
   - Ensure that the application is correctly registered in Azure AD. Confirm that:
     - Redirect URIs are correctly set.
     - Required API permissions are added and have been consented by a user with admin privileges.

2. **Check Token Configuration:**
   - Go to the Azure Active Directory > App registrations > Your app > Token configuration.
   - Ensure that the necessary claims are included in the token. If they are not, add the required claims.

3. **Modify Required Claims:**
   - Modify the application to ensure that it correctly requests the necessary claims by adjusting scopes in authentication flows.

4. **Update API Permissions:**
   - Verify that permissions requested match the capabilities and required claims for your application:
     - Navigate to Azure AD > App registrations > Your app > API permissions.
     - Ensure that the user has been granted the necessary permissions. If permissions have been added recently, ensure users have consented to them.

5. **User Role/Group Verification:**
   - Check if the user is part of any groups or roles that need to be present for the required claims to be included in the token.
   - Consider assigning additional roles if needed.

6. **Testing:**
   - After making changes, have an affected user reproduce the authentication flow that previously resulted in AADSTS90016.

#### Additional Notes or Considerations

- Verify that all changes made are correctly saved in Azure AD.
- If you are working in a development or testing environment, ensure that settings do not differ from production.
- Be mindful of privacy and sensitivity of data when sharing tokens or error logs.

#### Documentation for Guidance

- [Microsoft Documentation on AADSTS Error Codes](https://learn.microsoft.com/en-us/azure/active-directory/develop/reference-aadsts-error-codes)
- [Azure Active Directory Token Configuration Overview](https://learn.microsoft.com/en-us/azure/active-directory/develop/active-directory-optional-claims)
- [Creating and managing app registrations](https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)

#### Advice for Data Collection (Event Viewer Logs, Nettrace, Fiddler)

- **Event Viewer Logs:**
  - Check the Event Viewer on the client machine or server for any related logs under “Windows Logs” -> “Application.”
- **Network Trace Tools such as NetTrace or Fiddler:**
  - Use Fiddler or similar tools to capture requests as they are made to Azure AD. Look for the request payload and responses.
  - Analyze the headers and body for any missing information or discrepancies in the request to Azure AD.

Collecting this data can help diagnose and troubleshoot the specific conditions under which the error is occurring.