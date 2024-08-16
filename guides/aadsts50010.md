# AADSTS50010: AudienceUriValidationFailed - Audience URI validation for the app failed since no token audiences were configured.


## Troubleshooting Steps
Certainly! Here’s a detailed troubleshooting guide for the error code AADSTS50010 with the message "AudienceUriValidationFailed - Audience URI validation for the app failed since no token audiences were configured."

### Troubleshooting Guide for AADSTS50010

#### 1. Initial Diagnostic Steps

- **Check Application Registration**: Confirm that the application is properly registered in Azure Active Directory (AAD).
- **Identify Users Affected**: Determine which users are experiencing the issue to narrow down the scope.
- **Verify Application IDs**: Identify the application ID that is associated with the authentication request and ensure it matches the registered application.

#### 2. Common Issues that Cause This Error

- **Missing Audience URI**: The application registration does not have a specified audience URI in AAD.
- **Incorrect Configuration**: The API query from clients does not match any of the expected audience configurations in the app registration.
- **Token Issuance Problem**: The issuing authority may not be configured correctly to accept the audience from the application.

#### 3. Step-by-Step Resolution Strategies

1. **Review Application Registration**:
   - Navigate to the Azure portal (portal.azure.com).
   - Go to "Azure Active Directory" > "App registrations" > Select the application in question.
   - Under the section "Authentication", ensure the appropriate `Redirect URIs` and `Implicit grant and hybrid flows` (if applicable) are set.

2. **Configure Audience URIs**:
   - In the “Expose an API” section, ensure that you have defined the `Application ID URI` and any scopes. This URI is part of the audience claim in the token.
   - If necessary, add new audience URIs that match what your application expects.

3. **Check Token Configuration**:
   - If you're using a custom token acquisition process, ensure that the request for tokens includes the correct audience.
   - In the `Manifest` of the application registration, check the `knownClientApplications` array and ensure it’s not leading to audience mismatches.

4. **Test the Application**: 
   - After adjusting the settings, attempt to authenticate with the application again to see if the error persists.

5. **Use Azure AD Graph Explorer**:
   - Utilize the Graph Explorer to make calls to retrieve the tokens for verification and ensure the audience claim matches what is expected.

#### 4. Additional Notes or Considerations

- **Multiple Tenants**: If your application is utilizing multiple tenants, ensure that configuration includes the audience settings for each tenant.
- **Token Cache**: Sometimes, cached tokens may interfere. Users should log out and log in again to clear tokens.
- **Debugging Application Logic**: Ensure your application doesn’t mess with audience claim verification in custom authentication logic.

#### 5. Documentation for Guidance

- Azure AD App Registration: [App registrations in the Azure portal](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)
- Token validation overview: [Validating tokens](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-tokens)
- Using Azure AD for authentication in applications: [Authentication Scenarios for Azure Active Directory](https://docs.microsoft.com/en-us/azure/active-directory/develop/authentication-scenarios)

#### 6. Advice for Data Collection with Event Logs, Nettrace, and Fiddler

- **Event Viewer Logs**:
  - Check the Event Viewer on your application host (if applicable) for relevant authentication errors.
  - Look under “Security” logs for failed authentication attempts that might provide more detail on the issue.

- **Nettrace**:
  - Use NetTracing to gather details on requests and responses sent from your application to Azure AD to view headers and allowed audiences.

- **Fiddler**:
  - Use Fiddler to capture the HTTP requests made to Azure AD while authenticating. Look specifically at URI requests and their response codes.
  - Look for the `aud` (audience) claim in the token responses to see if they match the expected values.

By following this troubleshooting guide, you should be able to diagnose and resolve the `AADSTS50010` error effectively.