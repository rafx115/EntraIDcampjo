# AADSTS70005: UnsupportedResponseType - The app returned an unsupported response type due to the following reasons:response type 'token' isn't enabled for the appresponse type 'id_token' requires the 'OpenID' scope -contains an unsupported OAuth parameter value in the encoded wctx


## Troubleshooting Steps
### Error Code: AADSTS70005 (UnsupportedResponseType)

#### Initial Diagnostic Steps:
1. **Verify App Configuration**: Check the configuration settings of your app and make sure that the response types are properly configured.
2. **Examine OAuth Parameters**: Verify the OAuth parameters being used and ensure they are supported by the authorization server.
3. **Review Scope Permissions**: Verify that the required scopes, like 'OpenID', are correctly set up in your app.

#### Common Issues:
1. **Unsupported Response Type**: The app may be using a response type that is not enabled or supported by the authorization server.
2. **Incomplete Scope Permissions**: Missing or incorrect scopes in the app configuration can lead to this error.
3. **Invalid OAuth Parameters**: The presence of unsupported OAuth parameter values can cause the error.
   
#### Step-by-Step Resolution Strategies:

1. **Check App Configuration**:
   - Go to your app's configuration settings.
   - Ensure that the response type 'token' or 'id_token' is enabled as required.
  
2. **Verify Scope Permissions**:
   - Make sure that the 'OpenID' scope is included when using 'id_token' as a response type.
   - Check and update the scope permissions in your app's configuration.

3. **Review OAuth Parameters**:
   - Validate the OAuth parameters being sent in the request.
   - Ensure that all parameters are supported by the authorization server.
   
4. **Debug WCTX Parameter**:
   - Check the encoded wctx parameter in the request.
   - Remove any unsupported values or parameters causing the issue.

#### Additional Notes or Considerations:
- It's important to carefully review the documentation provided by the service you are integrating with for specific guidance on resolving this error.
- Double-check any changes made to the app configuration before retrying the authorization flow.

#### Documentation:
For detailed guidance on resolving the 'AADSTS70005 - UnsupportedResponseType' error, refer to the official Microsoft documentation:
- [Azure Active Directory error codes](https://docs.microsoft.com/en-us/azure/active-directory/develop/reference-aadsts-error-codes)

For app-specific troubleshooting steps, consult the documentation provided by the Identity Provider or OAuth service you are integrating with.