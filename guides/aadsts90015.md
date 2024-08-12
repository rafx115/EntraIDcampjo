
# AADSTS90015: QueryStringTooLong - The query string is too long.


## Troubleshooting Steps
## Troubleshooting Guide for Error Code AADSTS90015

### Error Description
**AADSTS90015: QueryStringTooLong - The query string is too long.**

This error indicates that the URL being used to authenticate against Azure Active Directory (AAD) has exceeded the maximum length allowed for a query string. This can happen in various scenarios where a large amount of data is being sent as part of the OAuth2 or OpenID Connect authentication process.

### Initial Diagnostic Steps
1. **Review URL Length:**
   - Check the length of the URL being generated for the authentication request. The maximum length for a URL is generally about 2000 characters, but this can vary depending on the browser and server configuration.

2. **Identify the Context:**
   - Determine in which application or service the error occurs, such as a web app, mobile app, or API integration.

3. **Log Detailed Error Messages:**
   - Enable more detailed logging in your application to capture the full request details leading to the error.

### Common Issues That Cause This Error
1. **Excessive Query Parameters:**
   - The application might be appending too many parameters to the URL during redirections, especially if using state or scope variables with large payloads.

2. **Large Tokens or ID Claims:**
   - Tokens created during authentication that contain a large number of claims or information can inflate the query string.

3. **Misconfiguration:**
   - Incorrect settings in the application, such as enabling multiple authentication providers or using extensive scopes, may lead to bloated queries.

4. **Session Information or State Data:**
   - Applications that pass session data or state information through the query string may inadvertently send too much data.

### Step-By-Step Resolution Strategies
1. **Shorten the URL:**
   - Minimize the number of parameters and their values. Remove any unnecessary information or claims that aren’t essential for authentication.

2. **Use POST Instead of GET:**
   - If applicable, shift from using a GET request (which appends data to the URL) to a POST request for sending data. The OAuth flows typically use GET, but some authorization flows may allow for POST.

3. **Use Application State:**
   - Consider storing state information server-side and referencing it using an identifier in the query string rather than sending the entire state.

4. **Optimize Scopes:**
   - Review the scopes requested during authentication and limit them to only the necessary ones required by the application.

5. **Implement Chunked Data:**
   - If large datasets are involved, consider breaking them into smaller chunks or utilizing alternative methods of sending data (like storing in a database).

6. **Review Redirect URIs:**
   - Ensure that any redirect URIs configured in the Azure portal are correct and optimized to avoid unnecessary data transfer.

### Additional Notes or Considerations
- Ensure that all apps and services adhere to the length limitations specified by both AAD and typical browsers.
- Monitor the application for changes in behavior after resolving the error.

### Documentation for Guidance
- [Azure Active Directory Authentication documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/)
- [Best practices for Azure Active Directory authentication](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-best-practices)
- [OAuth 2.0 and OpenID Connect documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-protocols)

### Advice for Data Collection
If further investigation is needed, consider collecting the following data:
- **Event Viewer Logs:**
  - Check the application logs for any specific errors or warnings related to authentication processes.
  
- **Network Trace (Nettrace):**
  - Use tools like Wireshark or Fiddler to capture the network traffic. Look specifically for the authentication request and response.

- **Fiddler Capture:**
  - Conduct a session with Fiddler running to capture the full request URL, including query parameters, and analyze them for length and content.

By following the outlined guide, you should be able to diagnose and resolve the AADSTS90015 error effectively.