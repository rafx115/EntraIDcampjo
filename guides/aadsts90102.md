
# AADSTS90102: InvalidUriParameter - The value must be a valid absolute URI.


## Troubleshooting Steps
Certainly! The error code **AADSTS90102**, indicating "InvalidUriParameter - The value must be a valid absolute URI," typically arises in scenarios related to OAuth or OpenID Connect authentication when the URI parameter(s) specified in a request are not formatted correctly. Here’s a detailed troubleshooting guide for this issue.

### Initial Diagnostic Steps

1. **Check the Error Message:** Identify the specific URI parameter mentioned in the error message.
2. **Review the Request:** Examine the request (like the authorization request URL) leading to this error to identify any URI parameters that might be incorrectly formatted.
3. **Reproduce the Error:** If possible, replicate the error in a controlled environment to understand the exact conditions that cause the failure. 

### Common Issues that Cause this Error

1. **Malformed URI:** The specified URI is not formatted as an absolute URI (e.g., it might be a relative URL or missing the protocol).
2. **Missing Required Parameters:** Required parameters might be omitted from the URI.
3. **Wrong Parameter Value:** Sometimes, even valid-looking URIs can contain incorrect values or formats (e.g., missing scheme like http or https).
4. **Incorrect Application Registration:** The application being used might not be correctly configured to handle the URIs being passed.

### Step-by-Step Resolution Strategies

1. **Verify the URI Format:**
   - Ensure that the URI is absolute, meaning it should include the scheme (http:// or https://), host, and path as necessary. For example:
     - Correct: `https://example.com/callback`
     - Incorrect: `example/callback`
  
2. **Check Application Registration:**
   - Log into Azure portal and navigate to the Azure Active Directory.
   - Go to "App registrations," select your application, and check the following:
     - Redirect URIs: Ensure that all specified redirect URIs are absolute and accurately listed.
     - Application ID URI: Ensure that it is set correctly if needed.

3. **Examine OAuth/OpenID request parameters:**
   - If you are making an OAuth or OpenID request, ensure that the parameters such as `redirect_uri`, `scope`, and `response_type` are correctly specified and properly encoded in the URL.

4. **Consult Documentation:**
   - Visit the official Microsoft documentation related to Azure Active Directory to review any specific requirements for URIs.
   - Documentation Links:
     - [Azure AD Authentication documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/authentication-scenarios)
     - [Redirect URIs in Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/develop/v1-app-redirect-uri)

5. **Logging and Debugging:**
   - Implement logging in your application to capture the generated URIs before making authentication requests.
   - Utilize tools like Fiddler or browser developer tools to inspect outgoing requests.

### Additional Notes or Considerations

- **Encoding:** Be cautious of encoding issues in URIs; characters may need to be URL-encoded.
- **Security:** Ensure that sensitive information is not included in URIs as query parameters.
- **Multiple Environments:** Consider the possibility of having different configurations for different environments (development, staging, production).

### Test the Documentation Reachability

To ensure that the documentation is accessible:
1. Open a web browser.
2. Navigate to the URL: [https://docs.microsoft.com/en-us/azure/active-directory/develop/authentication-scenarios](https://docs.microsoft.com/en-us/azure/active-directory/develop/authentication-scenarios)
3. Verify the page loads properly, and the relevant information is available.

### Advice for Data Collection

1. **Request Logs:** Collect logs from the request-making component of your application.
2. **Error Responses:** Keep copies of any full error messages returned from Azure Active Directory.
3. **Configuration Snapshots:** Capture screenshots or text exports of your application’s settings within the Azure portal to reference when troubleshooting.
4. **User Reports:** Document any user reports related to authentication issues for patterns or common configurations.

By following these steps and considerations, you should be able to diagnose and fix the AADSTS90102 error effectively. If issues persist even after these resolutions, it may be helpful to engage with Microsoft Support for more in-depth troubleshooting.