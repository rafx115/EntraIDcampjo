# AADSTS90007: InvalidSessionId - Bad request. The passed session ID can't be parsed.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS90007: "InvalidSessionId"

This error typically occurs when working with Azure Active Directory (AAD) authentication, indicating that the session ID provided in the request could not be parsed or is invalid. Below is a detailed troubleshooting guide to help you diagnose and resolve this error.

#### Initial Diagnostic Steps

1. **Verify the Context:**
   - Identify when the error occurs (e.g., during user authentication, token acquisition, etc.).
   - Determine the environment where the error is encountered (e.g., web application, mobile app, API).

2. **Check for Recent Changes:**
   - Review if any recent changes have been made to the authentication configuration, codebase, or the environment.
   - Confirm if updates to libraries or frameworks used in the application might be contributing to the issue.

3. **Review Error Logs:**
   - Examine application logs to gather further details about the occurrence of the error.
   - Look for additional error messages that might provide context.

#### Common Issues that Cause This Error

1. **Expired Session or Cookies:**
   - Session IDs can expire or be invalidated. Check if the user session is still active.

2. **Malformed Session ID:**
   - Ensure that the session ID being sent is correctly formed and base64 encoded properly, if applicable.

3. **Cross-Domain Issues:**
   - If your application makes requests across different domains, ensure that the session ID is being correctly passed and is still valid.

4. **Multiple Authentication Protocols:**
   - Check if multiple authentication protocols are being utilized and ensure they are compatible.

5. **Incorrect Redirection during Authentication:**
   - Ensure that any redirects during the OAuth/OpenID Connect flow are valid and do not alter session information.

#### Step-by-Step Resolution Strategies

1. **Clear Browser Cache and Cookies:**
   - Advise users to clear their browser cache and cookies, potentially eliminating any stale session IDs or corrupted data.

2. **Check Application Code:**
   - Review the application code that handles session IDs during authentication. Ensure there are no unintentional modifications.

3. **Session Configuration Review:**
   - Inspect your application settings regarding session management in Azure AD. Ensure your app is correctly set up to handle sessions.

4. **Check for Middleware Issues:**
   - If using middleware for authentication (e.g., OWIN, ASP.NET Core middleware), ensure it’s configured properly to handle session IDs.

5. **Implement Robust Error Handling:**
   - Update error handling in your application to gracefully handle invalid session IDs and prompt users to re-authenticate if necessary.

6. **Test Different Browsers/Devices:**
   - Test the application in different browsers or devices to rule out browser-specific session management issues.

7. **Re-create the Authentication Flow:**
   - If the issue persists, consider re-creating the authentication flow to determine if the error arises during a specific part of the process.

#### Additional Notes or Considerations

- Ensure the client application is registered correctly in Azure AD with the correct redirect URI and settings as required.
- Consider implementing logging on user sessions to track when and how sessions are established and invalidated.

#### Documentation Resources

- [Azure Active Directory Authentication Protocols](https://docs.microsoft.com/en-us/azure/active-directory/develop/authentication-scenarios)
- [Handle errors in Azure AD authentication](https://docs.microsoft.com/en-us/azure/active-directory/develop/errors)
- [ASP.NET Core Authentication documentation](https://docs.microsoft.com/en-us/aspnet/core/security/authentication/)

#### Data Collection and Diagnostic Tools

1. **Event Viewer Logs:** 
   - Check the Windows Event Viewer logs for any errors related to authentication or application crashes that coincide with the error occurrence.

2. **.NET Trace Logs:**
   - Enable and review .NET trace logs for detailed logs regarding authentication issues. You can configure tracing in your application settings to capture authentication events.

3. **Fiddler:**
   - Use Fiddler to inspect HTTP requests and responses. Look for the requests that include the session ID and analyze the responses for clues to why the session ID might be invalid.

4. **Network Traces:**
   - Collect full network traces if using tools like Wireshark to analyze the flow of the session, especially during the authentication phase.

By following these troubleshooting steps and utilizing available tools and documentation, you should be able to resolve the AADSTS90007 error efficiently. If the issue persists despite these efforts, consider reaching out to Azure support for further assistance.