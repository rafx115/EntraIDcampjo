# AADSTS90100: InvalidRequestParameter - The parameter is empty or not valid.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS90100

**Error Code:** AADSTS90100  
**Description:** InvalidRequestParameter - The parameter is empty or not valid.

#### 1. Initial Diagnostic Steps:
- **Check the Request URI:** Verify that the URI used in the request is correctly aligned with the expectations outlined in the Azure AD documentation.
- **Examine Request Parameters:** Review the request parameters being sent, ensuring none of them are empty or incorrectly formatted.
- **Review Authentication Flow:** Confirm that the correct authentication flow (OAuth2, OpenID Connect, etc.) is being used for the given scenario.

#### 2. Common Issues that Cause this Error:
- **Missing or Invalid Parameters:** Required parameters (like `client_id`, `client_secret`, `redirect_uri`, etc.) are absent or malformed.
- **Incorrect Scopes:** The scope parameter may contain values that are not allowed or improperly formatted.
- **API Endpoint Issues:** Incorrect endpoint or resource ID specified in the request.
- **Malformed JSON:** If using JSON, ensure that the syntax is correct and adheres to the required schema.

#### 3. Step-by-Step Resolution Strategies:
1. **Verify Client ID and Secret:**
   - Ensure that the `client_id` and `client_secret` parameters used are correct and registered in Azure AD.
   - Check whether the `client_secret` has expired or has been regenerated.

2. **Inspect Redirect URI:**
   - Confirm the `redirect_uri` in the request matches one of the registered redirect URIs for the application in Azure AD.
   - Ensure the URI encoding is correct.

3. **Validate Required Parameters:**
   - Make a checklist of required parameters for the specific request (e.g., for token acquisition) and check off each one as you verify its presence and validity.

4. **Check Scopes:**
   - Validate that the scopes requested in your authorization request are correctly specified and pertain to the application’s permissions in Azure AD.
   - Ensure you’re not making unsupported scope requests.

5. **Review Application Manifest:**
   - Access the Azure portal and validate that your application’s manifest is configured properly, ensuring permissions, redirect URIs, and other settings are correctly specified.

6. **Consult Logs:**
   - If the error persists, review quiet logs during the request process for more insight. This could be helpful for deeper debugging.

#### 4. Additional Notes or Considerations:
- **Request Logging:** Enable detailed logging in your application to capture the requests being sent to Azure AD, which can be helpful for pinpointing issues.
- **Environment-Specific Configuration:** Be aware that development, test, and production configurations may differ, and issues could arise from environment mismatches.
- **API Version:** Ensure that you are using the correct API version in your requests, as parameters might change between versions.

#### 5. Documentation for Guidance:
- Azure AD Authentication documentation: [Microsoft Identity Platform documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/)
- OAuth 2.0 Authorization Code Flow: [Authorization Code Flow](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code)
- Common Azure AD error codes: [Azure AD error codes](https://learn.microsoft.com/en-us/azure/active-directory/develop/reference-aad-error-codes)

#### 6. Advice for Data Collection:
- **Event Viewer Logs:** If applicable, check the application logs or system logs through the Windows Event Viewer for any related error messages.
- **Network Tracing:** Use tools like Netmon or netsh trace to collect network traces. These can be reviewed to ensure requests and responses are as expected during the authentication flow.
- **Fiddler:** Use Fiddler to intercept and inspect HTTP(S) requests sent to Azure AD to analyze the exact parameters being transmitted. Check for malformed requests, especially if you're making REST calls.

### Closing Notes:
Ultimately, resolving AADSTS90100 involves ensuring that all request parameters meet Azure AD specifications. By following the troubleshooting steps outlined above, you can systematically identify and fix the issues causing this error.