# AADSTS90117: InvalidRequestInput


## Troubleshooting Steps
The error code AADSTS90117 with the description "InvalidRequestInput" indicates that there is an issue with the input parameters in the request made to Azure Active Directory (AAD). Below is a detailed troubleshooting guide that covers initial diagnostics, common causes, resolution strategies, and additional considerations.

### Troubleshooting Guide for AADSTS90117

#### Initial Diagnostic Steps
1. **Verify Error Details**:
   - Record the error message that appears with AADSTS90117. Make sure to note the full error response, including any extra information provided.
   
2. **Check the Request URL**:
   - Examine the URL used to initiate the authentication request. Ensure it follows the format required by Azure AD.
   
3. **Review Application Configuration**:
   - Confirm that the application is registered correctly in the Azure portal, including proper redirect URIs and permissions.

4. **Assess the Input Parameters**:
   - Look at the parameters sent in the request (e.g., scope, response_type, client_id). Ensure there are no typos or incorrect values.

#### Common Issues that Cause This Error
1. **Incorrect Redirect URI**:
   - The redirect URI in the authentication request must match one of the redirect URIs registered in the Azure portal.

2. **Malformed Request Parameters**:
   - Any misspelled or unsupported parameters within the request can result in this error.

3. **Client ID or Secret Issues**:
   - The client ID used in the request may be incorrect, or the client secret may not be properly configured.

4. **Invalid Scopes**:
   - The scopes requested might be invalid or not permitted for the application.

5. **Application Permission Issues**:
   - The application being accessed may not have the required permissions or consent has not been provided.

#### Step-by-step Resolution Strategies
1. **Check Application Registration**:
   - Go to the Azure portal > Azure Active Directory > App registrations.
   - Locate your application and confirm that the redirect URIs are correct.

2. **Review the Authentication Request**:
   - Confirm that the necessary parameters are included in the authentication request. Required parameters typically include:
     - `client_id`
     - `response_type`
     - `redirect_uri`
     - `scope`
   - Ensure there are no typos or unsupported values.

3. **Validate Scopes**:
   - Visit the API permissions section of your app registration and verify that the requested scopes match those configured.

4. **Verify Client Credentials**:
   - Ensure the client ID is correctly set in the application code.
   - If using a client secret, check that it matches the one in Azure AD.

5. **Test the Endpoint URL**:
   - Use a tool like Postman or a web browser to manually test the authentication endpoint with the parameters you're using. Ensure you can replicate the error.

6. **Review Logs**:
   - Check Azure AD sign-in logs (Azure portal > Azure Active Directory > Sign-ins) for additional context around the error.

#### Additional Notes or Considerations
- **Caching Issues**: Sometimes, caching may cause old settings to be referenced. Clear your application cache or try from a different client.
- **Network Configuration**: Ensure there are no network issues that might be interfering with your requests.
- **Role Assignments**: If roles are involved, ensure users have the proper roles assigned to access the application.

#### Documentation for Guidance
- [Azure AD Authentication Overview](https://learn.microsoft.com/en-us/azure/active-directory/develop/authentication-scenarios)
- [Troubleshooting OAuth 2.0 and OpenID Connect](https://learn.microsoft.com/en-us/azure/active-directory/develop/troubleshoot-oauth)
- [App Registration in Azure Active Directory](https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)

#### Advice for Data Collection
- **Event Viewer Logs**: Check the Event Viewer on the client machine for any application or system logs that may provide more context around the error.
- **NetTrace and Fiddler**: Use tools like NetMon or Fiddler to capture network traffic. Look for the request that results in the error and examine the full HTTP response, including the request headers and body.
- **Diagnostics**: Enable "Application Insights" in your application (if applicable) to gather more telemetry data and exceptions that may relate to user authentication issues.

By following these steps and considerations, you should be able to identify the cause of the AADSTS90117 error and apply the necessary resolutions to mitigate it.