# AADSTS90004: InvalidRequestFormat - The request isn't properly formatted.


## Troubleshooting Steps
## Troubleshooting Guide for AADSTS90004 Error

### Error Description
The error code **AADSTS90004** indicates a problem with the request format sent to Azure Active Directory (AAD). Specifically, the error message "InvalidRequestFormat - The request isn't properly formatted." highlights that the request you made to the identity service has syntactical or structural issues.

### Initial Diagnostic Steps
1. **Verify the Request URL**: Check the URL where the request is sent. Ensure that it adheres to the expected format and includes all necessary parameters.
2. **Review Request Method**: Confirm whether the HTTP method used (GET, POST, etc.) is appropriate for the request type.
3. **Inspect Headers**: Validate any headers included in the request. Required headers such as `Content-Type` must be present and correctly set.
4. **Check Request Body**: If the request includes a body (only applicable for POST requests), confirm that its format is valid JSON or URL-encoded as required.
5. **Authentication Context**: Ensure that the authentication context in which the request is made is valid and correctly configured.

### Common Issues that Cause This Error
- **Malformed Request URL**: Extra characters, incorrect encodings, or missing segments in the URL.
- **Incorrect Headers**: Missing or incorrectly formatted `Content-Type`, `Authorization`, etc.
- **Invalid Request Body**: JSON syntax errors, incorrect parameter names, or missing required fields.
- **Unsupported Request Types**: Usage of outdated or incorrect endpoints that do not accept the current request format.
- **Redirect URI Mismatch**: If OAuth2 is involved, an incorrect redirect URI might be causing formatting issues.

### Step-by-Step Resolution Strategies
1. **Check the Azure AD Application Configuration**:
   - Navigate to the Azure Portal -> Azure Active Directory -> App registrations.
   - Ensure that the settings, including redirect URI, are correctly configured.

2. **Validate the Request Construction**:
   - For using OAuth2 flows, ensure the `grant_type`, `client_id`, `client_secret`, `scope`, and other parameters are correctly named and formatted.
   - Use tools like Postman or curl to test your API calls with the correct parameters.

3. **Review Documentation**:
   - Make sure your usage of the Azure AD APIs adheres to the latest Microsoft documentation. Reference the [Microsoft Identity platform documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/) for details on expected request formats.

4. **Use Fiddler or Postman for Testing**:
   - Use Fiddler or Postman to manually replicate the request and observe detailed responses or errors.

5. **Review Logs**:
   - Look at the Azure AD sign-in logs in the Azure portal to gather more details about the failed request.

6. **Error Handling Logic**:
   - Implement appropriate error handling in your application to give clearer messages or log the responses for failed requests.

### Additional Notes or Considerations
- Upgrading Libraries: If any SDKs or libraries are being used to interact with the Azure AD, ensure they are up to date.
- Rate Limiting: Examine if throttling or rate limiting is affecting your requests.
- Network Issues: Consider checking for firewall or network policies that could alter request formatting.

### Documentation for Guidance
- [Microsoft Identity Platform Overview](https://docs.microsoft.com/en-us/azure/active-directory/develop/overview)
- [OAuth 2.0 Authorization Grant Types](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-implicit-grant-flow)
- [Error Codes in Microsoft Identity Platform](https://docs.microsoft.com/en-us/azure/active-directory/develop/reference-aad-errors)

### Advice for Data Collection
1. **Event Viewer Logs**:
   - Review the Event Viewer on Windows to track down relevant application errors or warnings related to your application’s requests.

2. **Network Trace (NetTrace)**:
   - Use the built-in command in Windows (`netsh trace start`) or network monitoring tools to capture traffic during the request lifecycle.
   - Analyze these traces for unusual patterns or errors.

3. **Fiddler**:
   - Capture Fiddler logs to inspect HTTP requests and responses. Focus on the request that resulted in **AADSTS90004** to identify malformed elements.
   - Ensure that you're examining the raw request/response for any anomalies.

By following these steps and utilizing the above resources, you should be able to diagnose and resolve issues resulting in the AADSTS90004 error effectively.