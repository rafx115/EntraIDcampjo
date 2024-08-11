
# AADSTS81006: DesktopSsoNoAuthorizationHeader - No authorization header was found.


## Troubleshooting Steps
### Error Code: AADSTS81006 - DesktopSsoNoAuthorizationHeader

#### Initial Diagnostic Steps:
1. **Verify Error Context**: Understand where and when the error occurs – during sign-in, authentication, token validation, etc.
2. **Check Logs**: Review logs or error messages to gather more information about the specific environment and context of the error.
3. **Confirm Environment Setup**: Check if the correct configurations are in place for the authentication process.

#### Common Issues:
1. **Missing Authorization Header**: As indicated by the error message, the issue may stem from the absence of an authorization header, leading to failed authentication.
2. **Incorrect Configuration**: Improper setup of Single Sign-On (SSO) settings, missing tokens, or misconfigured endpoints can also trigger this error.
3. **Outdated Libraries**: Using outdated libraries or SDKs might result in incompatible authentication requests, causing the error.

#### Step-by-Step Resolution Strategies:
1. **Verify Authorization Header**:
   - Ensure that the authorization header is being included in the authentication requests.
  
2. **Check SSO Configuration**:
   - Review the SSO configuration settings to ensure they are correctly set up with the required parameters.

3. **Update Libraries/SDKs**:
   - If using any authentication libraries or SDKs, ensure they are up to date to prevent compatibility issues.

4. **Test in Different Environments**:
   - Test the authentication process in various environments to determine if the issue is environment-specific.

5. **Review Integration Steps**:
   - Double-check the integration steps followed for authentication against the official documentation.

#### Additional Notes or Considerations:
- Ensure that the system time is synchronized to prevent time-related authentication issues.
- Clear any caches or cookies that might be affecting the authentication flow.
- Test the authentication flow with different user accounts to isolate the problem further.

#### Documentation for Guidance:
- [Azure Active Directory error codes and messages](https://docs.microsoft.com/en-us/azure/active-directory/develop/reference-aadsts-error-codes)

Following these troubleshooting steps should help in identifying and resolving the AADSTS81006 error related to the missing authorization header. If the issue persists, consider reaching out to the appropriate support channels for further assistance.