# AADSTS90120: InvalidDeviceFlowRequest - The request was already authorized or declined.


## Troubleshooting Steps
## Troubleshooting Guide for AADSTS90120: InvalidDeviceFlowRequest

### Overview

The AADSTS90120 error code occurs primarily in Microsoft Authentication scenarios, particularly when using the OAuth 2.0 Device Authorization Grant flow. It indicates that a request has already been authorized or declined, which can lead to a frustrating user experience.

### Initial Diagnostic Steps

1. **Reproduce the Error**: Attempt to reproduce the error by following the same steps that led to the issue. Document the specific request being made and the response received.

2. **Check Application Logs**: Review the application logs to check for any related errors or warnings around the time the AADSTS90120 error occurred. This can provide context about what the user was doing before encountering the error.

3. **Review Authentication Requests**: Inspect the parameters sent in the device authorization request to ensure they are correct and complete.

4. **Verify User State**: Ensure that the user attempting to authenticate has not already authorized the app or declined the request.

### Common Issues that Cause This Error

1. **Token Already Used**: The device code has already been exchanged for tokens, hence repeating the exchange without revoking will lead to this error.

2. **User Declined Authorization**: The user may have explicitly declined the request previously.

3. **Expiration of Codes**: Device codes may expire after a certain period, leading to this error if the same code is reused.

4. **Rate Limiting**: Too frequent requests may lead to throttling from the Azure AD side.

5. **Invalid Redirect URI**: The redirect URI provided in the request might not match the one registered in the Azure AD app settings.

### Step-by-Step Resolution Strategies

1. **Terminate Current Sessions**: If applicable, ensure that any current sessions or device codes are terminated. The user may need to retry with a fresh authorization request.

2. **Generate New Device Code**:
   - Call the `POST /devicecode` endpoint again to obtain new device and user codes. Ensure the previous codes are not in use anymore.

3. **Inform the User**: Notify the user about the requirement to approve the authorization flow again. Provide instructions on how to authorize the app if needed.

4. **Review Application Registration**:
   - Ensure the application's configuration in Azure AD is correct, particularly around redirect URIs and permissions.
   - Validate if the `Allow public client flows` setting is enabled, if applicable.

5. **Testing and Validation**:
   - After applying changes, conduct a test with a clean user session to confirm that the authorization flow works as expected.

### Additional Notes or Considerations

- When developing applications using device flow, consider implementing error handling for known scenarios like AADSTS90120. This can improve user experience by providing clear instructions on what to do next.
- Ensure that your application has appropriate permissions in Azure AD, and that necessary consent has been given.

### Documentation for Guidance

- [Microsoft Identity Platform Documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/)
- [Device Authorization Grant Specification](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth-device-flow)
- [Handling Authorization Errors](https://docs.microsoft.com/en-us/azure/active-directory/develop/authentication-scenarios)

### Test the Documentation Reachability

You can verify the links provided are working by visiting them in a web browser. Ensure they lead to the expected Microsoft documentation pages.

### Advice for Data Collection

- **Log Details**: Collect error logs from the application detailing the request parameters, user identifiers, and timestamps.
- **Gather User Feedback**: If possible, get feedback from users on what they were doing when the error occurred.
- **Monitor Azure AD Logs**: Use Azure AD sign-in logs to gather more context about the authentication request flow.
- **Network Requests**: Utilize tools like Fiddler or browser dev tools to collect network requests and responses pertaining to authentication flows.

With this troubleshooting guide, you should be able to identify, resolve, and mitigate the issues causing the AADSTS90120 error effectively.