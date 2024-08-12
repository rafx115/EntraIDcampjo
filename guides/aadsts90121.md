
# AADSTS90121: InvalidEmptyRequest - Invalid empty request.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS90121: "InvalidEmptyRequest - Invalid empty request"

The AADSTS90121 error typically indicates that a request to Azure Active Directory (AAD) is missing required parameters. This error suggests that the authentication request was either empty or did not contain the necessary data for AAD to process it.

---

### Initial Diagnostic Steps

1. **Identify Context of Issue**:
   - Determine the environment in which the issue is occurring (e.g., web application, mobile application, service).
   - Identify whether the request was initiated by a user action or programmatically.

2. **Reproduce the Error**:
   - Try to reproduce the error in a controlled environment. 
   - Note the exact actions taken leading up to the error.

3. **Check Request Logs**:
   - If available, check any logging that may show the request parameters sent to AAD.

---

### Common Issues that Cause this Error

1. **Missing Required Parameters**:
   - The request to AAD is missing essential parameters such as `client_id`, `redirect_uri`, `response_type`, etc.

2. **Malformed Authentication Request**:
   - The authentication request might be incorrectly formatted (e.g., invalid query string).

3. **Issues with Client Application Configuration**:
   - The Azure AD application settings may be incorrectly configured.

4. **User Permissions**:
   - The user may lack the necessary permissions or roles to access the resource.

5. **CORS Issues**:
   - Cross-Origin Resource Sharing (CORS) might be blocking requests from specific domains.

---

### Step-by-step Resolution Strategies

1. **Examine the Authentication Request**:
   - Review the request being sent to AAD. Ensure all required parameters are present and correctly formatted.
   - The minimum parameters needed for a typical OAuth 2.0 authorization flow include:
     - `client_id`
     - `response_type`
     - `redirect_uri`
     - `scope`

2. **Review Azure AD Application Settings**:
   - Go to the [Azure Portal](https://portal.azure.com/).
   - Navigate to **Azure Active Directory** > **App registrations**.
   - Select the application that is generating the error.
   - Check the **Redirect URIs**, **Application ID**, and **Client Secret**.
   - Ensure that your app has the required permissions and consented for them.

3. **Test with Different Browsers or Devices**:
   - Sometimes browser-specific settings or extensions can interfere with request flows.
   - Try testing using different browsers or devices to rule out client-side issues.

4. **Use Fiddler or Browser Developer Tools**:
   - Use tools like Fiddler or browser developer tools (F12) to capture the network request.
   - Inspect the request being sent to the AAD endpoint and verify if all parameters are being passed correctly.

5. **Inspect CORS Configuration**:
   - If applicable, review the CORS settings of the application. Ensure that the domains are correctly specified in Azure AD.

6. **Error Handling in Code**:
   - Ensure that your application code correctly handles empty or invalid responses.
   - Implement proper error logging to capture more context when the error occurs.

---

### Additional Notes or Considerations

- Ensure that any changes to user permissions and application configurations are tested in a non-production environment first.
- Review any updates or changes made to the Azure AD service or application libraries that may impact the authentication flow.
- Consider implementing user feedback mechanisms or logging to understand how frequently this error occurs.

---

### Documentation References

- [Understanding Azure AD error codes](https://learn.microsoft.com/en-us/azure/active-directory/develop/active-directory-error-codes)
- [OAuth 2.0 Authorization Code Grant](https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow)
- [Best practices for application registrations](https://learn.microsoft.com/en-us/azure/active-directory/develop/best-practices-application-registration)

---

### Advice for Data Collection

1. **Event Viewer Logs**:
   - If using a Windows environment, check the Event Viewer for any relevant application logs.
   - Navigate to **Windows Logs** > **Application** and filter for errors or warnings related to your application.

2. **Network Traces with Fiddler/NetTrace**:
   - Use Fiddler to log HTTP(s) traffic to inspect the requests/responses.
   - Enable detailed logging features to capture payloads and headers.

3. **Browser Dev Tools**:
   - Use the Network tab in the browser’s developer tools to view the requests made to AAD, checking for malformed URLs or missing parameters.

4. **Document Findings**:
   - Keep a log of error occurrences, including timestamps, actions taken, and any patterns or correlations observed.

By following these steps, you should be able to diagnose and resolve the AADSTS90121 "Invalid empty request" error effectively.