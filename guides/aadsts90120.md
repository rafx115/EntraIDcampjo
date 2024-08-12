# AADSTS90120: InvalidDeviceFlowRequest - The request was already authorized or declined.


## Troubleshooting Steps
The error code AADSTS90120, which refers to `InvalidDeviceFlowRequest - The request was already authorized or declined`, often occurs in environments where OAuth 2.0 Device Code Flow is implemented, typically for scenarios like authenticating devices and applications that may not have a browser.

### 1. Initial Diagnostic Steps
1. **Verify the Context**: 
   - Identify the application or service that is returning the error.
   - Confirm that you are using the correct device code flow URLs and parameters as per Azure AD guidelines.
  
2. **Check User Interaction**: 
   - Ensure that the end user hasn't already completed the authorization process or declined it. If the user sees a screen indicating that they need to authorize, they might not be doing so correctly.

3. **Endpoint Verification**: 
   - Confirm that the correct OAuth endpoints are being used, and they comply with the application's configurations.

### 2. Common Issues that Cause This Error
1. **Authorization Status**: 
   - The user has already authorized or declined the device code request.
   
2. **Expired Device Code**: 
   - Device codes are valid for a specific time. If a request is made after the code has expired, the request will be invalid.

3. **Multiple Requests**: 
   - If multiple authorization requests are sent from the same device or application context, it can confuse the state of authorization.

4. **Misconfigured Application Registration**: 
   - The Azure AD app registration might have incorrect redirect URIs or permissions that prevent successful authorization.

### 3. Step-by-Step Resolution Strategies
1. **Re-initiate the Device Code Flow**:
   - Generate a new device code for logging in.
   - This can usually be done by re-invoking the device code request endpoint.

   **Example**: 
   ```http
   POST https://login.microsoftonline.com/{tenant}/oauth2/v2.0/devicecode
   Content-Type: application/x-www-form-urlencoded

   client_id={your_client_id}&scope={scope}
   ```

2. **Monitor User Actions**:
   - Instruct the user to check if they have already completed the authorization and confirm whether they received a success or failure message from Azure AD.

3. **Review Expiry Settings**:
   - If the Device Code is expired, it needs to be re-initiated. Device codes are typically valid for about 10 minutes before expiry.

4. **Inspect Application Settings**:
   - Validate the application registration in the Azure portal to confirm permissions, redirect URIs, and configurations are as expected.

5. **Testing and Monitoring**:
   - Utilize test applications to ensure workflows function correctly under different scenarios, including a fresh code generation.

### 4. Additional Notes or Considerations
- **User Communication**: Make sure to clarify to the users what to expect and guide them on steps to follow when prompted for the device code.
- **Safety with Multiple Requests**: Limit the attempts to get a device code to avoid flooding the backend service with requests.

### 5. Documentation for Guidance
- [Microsoft Identity Platform Documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/)
- [Device Code Flow Overview](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth-device-code)

### 6. Advice for Data Collection
- **Event Viewer Logs**: 
   - Check the event viewer logs on both the client and server for any related application errors or warnings.
  
- **NetTrace**: 
   - If you have tools like Network Monitor or Wireshark, consider capturing network traces of the attempt to authorize the device code workflow.

- **Fiddler**: 
   - Use Fiddler to intercept HTTP/HTTPS communications between the client and Azure AD, which can help analyze the requests/responses being sent/received during the authorization process.

### Summary
In summary, the AADSTS90120 error typically indicates an issue with the state of the device code request. Following the outlined troubleshooting steps, ensuring proper application registration, and closely monitoring user actions can help mitigate this issue effectively. Be proactive in updating documentation and providing feedback based on user interactions to continuously enhance the authentication process.