# AADSTS90081: OrgIdWsFederationMessageInvalid - An error occurred when the service tried to process a WS-Federation message. The message isn't valid.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS90081: OrgIdWsFederationMessageInvalid

#### Initial Diagnostic Steps:
1. **Verify Error Code**: Make sure the error code received is indeed AADSTS90081, indicating an issue with processing a WS-Federation message.
2. **Check Logs**: Review relevant logs or error messages for additional details on the specific error scenario.
3. **Check Configuration**: Ensure that the configuration related to WS-Federation authentication in your service provider (SP) and Azure Active Directory (AD) is correctly set up.
   
#### Common Issues Leading to This Error:
1. **Invalid Message Format**: The WS-Federation message being sent is not formatted correctly or is missing mandatory parameters.
2. **Incorrect URL**: The endpoint or URL being used for WS-Federation authentication is incorrect or inaccessible.
3. **Token Signing Issues**: Problems with token signing keys or certificates used in the WS-Federation process.
   
#### Step-by-Step Resolution Strategies:
1. **Validate WS-Federation Message**:
   - Check the contents of the WS-Federation message being exchanged between SP and AD to ensure it meets the required format and includes all necessary data.

2. **Review Endpoint Configuration**:
   - Verify that the URLs and endpoints used for WS-Federation authentication are accurate and accessible.

3. **Check Token Signing**:
   - Ensure that the token signing keys or certificates used for WS-Federation are valid and correctly configured on both the SP and AD sides.

4. **Inspect Request/Response Handling**:
   - Review how the WS-Federation messages are being processed by your service and ensure that the handling logic is implemented correctly.

5. **Test with a Known Good Configuration**:
   - Use a known working configuration to pinpoint whether the issue lies in the setup or configuration of the current environment.

#### Additional Notes or Considerations:
- **Token Lifetimes**: Ensure that token lifetimes are appropriately configured to avoid token expiration causing authentication issues.
- **Network Connectivity**: Check network settings to ensure there are no connectivity issues between the SP and AD during WS-Federation exchanges.

#### Documentation for Further Guidance:
- Microsoft Azure AD documentation on troubleshooting WS-Federation issues: [Troubleshoot Single Sign-On with Azure Active Directory](https://docs.microsoft.com/en-us/azure/active-directory/hybrid/how-to-connect-fed-error)
- Microsoft Tech Community forums and support resources for specific error discussions and resolutions.