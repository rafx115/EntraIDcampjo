# AADSTS90102: InvalidUriParameter - The value must be a valid absolute URI.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS90102

#### Overview
The error code AADSTS90102, with the description "InvalidUriParameter - The value must be a valid absolute URI," indicates that the Azure Active Directory (AAD) encountered an invalid URI parameter in a call related to authentication or authorization. This can happen during various AAD operations such as login, token requests, or when configuring application settings.

---

### Initial Diagnostic Steps

1. **Reproduce the Issue**: Attempt to reproduce the error in a controlled environment to confirm its occurrence. Gather information about the actions that lead to this error.

2. **Check Input Values**: Look at the parameters being sent in the request, especially any URIs. Ensure that the URIs are absolute and correctly formatted.

3. **Review Documentation**: Compare your configuration against Microsoft's documentation to ensure you're using the expected formats and parameters.

4. **Check Application Logs**: Gather logs from your application that include the request or operation triggering the error for additional context.

---

### Common Issues That Cause This Error

1. **Malformed URIs**: The URI provided is missing parts or incorrectly formatted, e.g., missing the protocol (http/https), slashes, or hostnames.

2. **Relative URIs**: Using a relative URI instead of an absolute URI. An absolute URI must contain:
   - Scheme (http/https)
   - Hostname
   - Optionally, port, path, query parameters, etc.

3. **Configuration Errors**: Incorrect settings in Azure AD, such as incorrect redirect URIs in the application registration.

4. **URL Encoding Issues**: Special characters in the URI not being correctly URL-encoded.

5. **Environment Issues**: In cases of multiple environments (e.g., dev, test), using the wrong environment URI configurations.

---

### Step-by-Step Resolution Strategies

1. **Identify Where the Error Occurs**:
   - Determine the specific operation or API call that results in the error.

2. **Validate URIs**:
   - Check the URI values being passed in the request. They should be absolute URIs.
   - Example of a valid URI: `https://example.com/callback`.

3. **Inspect Application Registration**:
   - Navigate to Azure Portal > Azure Active Directory > App registrations.
   - Select the application experiencing issues.
   - Check the "Redirect URIs" and ensure they are all valid absolute URIs.

4. **Correct Any Malformed URIs**:
   - Fix any typos or syntax issues in the URI.
   - Ensure there are no unintended spaces or illegal characters.

5. **Review API Documentation**:
   - Ensure that the parameters being passed align with the API documentation and that you are using the correct API endpoints.

6. **Test the Changes**:
   - After making changes, test the application to see if the error persists.

7. **Use Tools for Validation**:
   - Use online tools or libraries in your programming language to validate URIs if necessary.

---

### Additional Notes or Considerations

- **Different environments**: Ensure that the correct configuration for the environment you're working with is being used.
  
- **Security and Permissions**: Validate that any changes made still conform to your application's security model and Azure AD's permission structure.

- **Team Coordination**: If multiple team members are involved in configuration, ensure clear communication regarding changes.

---

### Documentation Where Steps Can Be Found for Guidance

- [Azure AD Application Registration Documentation](https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)
- [Azure Active Directory Authentication Library (ADAL) Documentation](https://learn.microsoft.com/en-us/azure/active-directory/develop/active-directory-authentication-libraries)
- [How to: Configure the Redirect URI](https://learn.microsoft.com/en-us/azure/active-directory/develop/msal-authentication#redirect-uri)

---

### Advice for Data Collection

1. **Event Viewer**:
   - Check Windows Event Logs for any related entries if it involves a local application/server.

2. **Network Tracing**:
   - Utilize network tracing tools like Fiddler or Wireshark to examine the HTTP requests/responses. Look for the specific request that triggers the error and inspect the parameters being sent.

3. **Debugging Tools**:
   - If developing locally, consider utilizing integrated development environment (IDE) debugging tools to step through authentication flows.

4. **Logs Collection**:
   - Ensure you have logging in place in your application to track errors. Collect logs that show input parameters, response status, and any exceptions raised.
   
By systematically following this guide, you should be able to diagnose and resolve the error AADSTS90102 effectively.