# AADSTS90121: InvalidEmptyRequest - Invalid empty request.


## Troubleshooting Steps
Error Code: **AADSTS90121**  
Description: **InvalidEmptyRequest - Invalid empty request.**

## Troubleshooting Guide for AADSTS90121: InvalidEmptyRequest

### Initial Diagnostic Steps
1. **Check the Error Context**: Identify where the error is occurring. Is it during a specific authentication flow, API call, or user action?
2. **Evaluate the Request**: Examine the request being made. Is it malformed or missing essential parameters?
3. **Check Logging**: Review application and authentication logs for additional context around the error.
4. **Verify User Input**: Ensure that any inputs from users, like passwords or usernames, are correctly formatted and provided.

### Common Issues Causing AADSTS90121
1. **Empty Request**: The request to the Azure Active Directory (AAD) is empty or missing required parameters.
2. **Invalid Redirect URI**: If the app configuration has an incorrect or empty redirect URI, this might lead to an invalid request.
3. **Missing or Incorrect Credentials**: If required credentials such as client ID or client secret are not provided or incorrectly passed.
4. **Insufficient Permissions**: The app may not have the necessary permissions granted in the Azure portal.
5. **Misconfigured App Registration**: The app registration could be incorrectly configured, leading to authentication issues.

### Step-by-Step Resolution Strategies
1. **Inspect and Validate Requests**
   - Check the request format in the response to ensure all required parameters are being sent.
   - Look for missing fields such as `client_id`, `scope`, `response_type`, and `redirect_uri`.

2. **Verify App Registration Settings**
   - Go to the Azure portal and navigate to **Azure Active Directory > App registrations**.
   - Verify that the app has the correct **Redirect URIs** configured as per your application needs.
   - Ensure that all necessary API permissions are granted.

3. **Check Authentication Flow**
   - Validate the authentication flow being used (Authorization Code Flow, Implicit Flow, etc.) aligns with the set up in Azure.
   - Make sure your application properly initializes and constructs the request according to the flow.

4. **Review Client Credentials**
   - Confirm that the `client_id` and `client_secret` are correctly configured in your application configuration settings.
   - Regenerate the client secret if there’s a possibility the current one is compromised.

5. **Look Over Security Restrictions**
   - Verify if there are any Conditional Access policies that may block or require additional checks during sign-in.

### Additional Notes or Considerations
- **Browser Behavior**: Sometimes cached data or cookies in the browser may interfere with the authentication process. Clear the browser cache or try a different browser.
- **API Security Restrictions**: Ensure that your API is properly secured and that authentication scopes required by the app are accurate.

### Documentation
- Azure Active Directory Authentication Overview: [Authentication overview](https://docs.microsoft.com/en-us/azure/active-directory/develop/authentication-scenarios)
- Azure App Registration: [App registrations in Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)
- Common Errors in Azure Active Directory: [Common AAD error codes](https://docs.microsoft.com/en-us/azure/active-directory/develop/reference-aad-error-codes)

**Reachability Test for Documentation**:
1. Access the links provided above and confirm they load correctly in your browser. All should be accessible without error.

### Advice for Data Collection
1. **Collect Request and Response Data**: When reproducing the error, log both the request sent to AAD and the complete error response.
2. **Gather Application Logs**: Review logs from your application that may have further insights into what was happening at the error time.
3. **User Feedback**: If applicable, collect feedback from users experiencing this error for additional context.

By following this troubleshooting guide, most issues related to the AADSTS90121 error can be diagnosed and resolved efficiently.