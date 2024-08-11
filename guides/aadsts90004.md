# AADSTS90004: InvalidRequestFormat - The request isn't properly formatted.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS90004

#### Description
AADSTS90004 indicates that there is an issue with the format of a request made to Azure Active Directory (Azure AD). This can often occur when an application attempts to authenticate or access a resource, but the request does not meet the expected format.

---

### Initial Diagnostic Steps

1. **Review Error Message**: Take a close look at the complete error message provided along with AADSTS90004. It may contain additional details about which part of the request is improperly formatted.

2. **Check Request Payload**: Review the request payload and headers being sent to Azure AD. This can be done via browser developer tools or server logs, depending on the context (web app, API, etc.).

3. **Identify Components of the Request**:
   - Verify the URL being called.
   - Ensure that the HTTP method (GET, POST, etc.) is appropriate for the request.
   - Confirm that required parameters are included and correctly formatted.

---

### Common Issues That Cause This Error

1. **Malformed URL**: The request URL may have incorrect syntax, such as missing parameters or incorrect query string formatting.

2. **Missing Scope**: The scope parameter in OAuth requests may be missing or incorrectly specified.

3. **Invalid Client ID**: The application might be using an invalid or malformed client ID.

4. **Incorrect Redirect URI**: The specified redirect URI may not match any URIs registered in Azure AD.

5. **Data Type Issues**: Parameter types might not match the expected format (e.g., strings where integers are expected).

6. **Issue with the Authorization Code**: The authorization code might be expired or malformed.

---

### Step-by-Step Resolution Strategies

1. **Validate Request URL**:
   - Ensure that the base URL and endpoint are correct according to the Azure documentation.
   - Verify that the query string parameters are properly encoded.

2. **Review OAuth Parameters**:
   - Make sure that all required OAuth parameters are present (client_id, scope, redirect_uri, response_type, etc.).
   - Verify that the scope is correctly formatted and includes valid permissions.

3. **Verification of Client ID and Secret**:
   - Double-check the client ID used in the request matches one that is registered in your Azure portal.
   - If applicable, ensure the client secret is also correct.

4. **Check Redirect URIs**:
   - Log in to the Azure portal and navigate to the registered application. Ensure that the redirect URI in your request exactly matches one configured in the app registration.

5. **Debugging Tools**:
   - Use tools like Postman or Fiddler to send the requests. This can help to isolate problems in the request format or help identify malformed data.

6. **Review Logs**:
   - Check Azure AD sign-in logs for any additional context or details about the request failure.

7. **Test with Variations**:
   - If you suspect a specific parameter might be causing the issue, try sending similar requests with variations in those parameters to determine if there are formatting requirements you're not meeting.

---

### Additional Notes or Considerations

- **Version Compatibility**: Confirm that the library or SDK you are using for Azure AD authentication is up-to-date and compatible with your Azure setup.
  
- **Rate Limiting**: Ensure your requests are not being throttled or blocked due to excessive or invalid requests.

- **Environment Differences**: Check if the issue is specific to a certain environment (development, staging, production) and confirm that configuration settings match.

---

### Documentation and Resources

- Azure AD Authentication Flow: [Microsoft Identity Platform Documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-overview)
- OAuth 2.0 Authorization Code Flow: [Microsoft Azure OAuth 2.0 Documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow)
- Azure AD Sign-in Logs: [Monitor Sign-in activity in Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/reports-monitoring/concept-sign-ins)

**Check Documentation Reachability**: The above links have been verified to be reachable as of now. Please ensure internet access when checking them.

---

### Advice for Data Collection

- **Capture Raw Requests**: Use tools like Fiddler, Charles Proxy, or built-in browser developer tools to capture and inspect the raw HTTP requests being sent to Azure AD.
  
- **Error Response Information**: Collect complete error responses, including headers, as they may provide insights into the malformed request.

- **Application Logs**: Enable detailed logging in your application to capture authentication and API request errors.

By following this structured troubleshooting guide, you should be able to identify and resolve issues related to the AADSTS90004 error effectively.