
# AADSTS90020: The SAML 1.1 Assertion is missing ImmutableID of the user. Developer error - the app is attempting to sign in without the necessary or correct authentication parameters.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS90020

**Error Description**: AADSTS90020 indicates that the SAML 1.1 Assertion is missing the `ImmutableID` of the user. This is typically a developer error, suggesting that the application is attempting to sign in without the required or correct authentication parameters.

#### Initial Diagnostic Steps
1. **Identify the Context**:
   - Determine where the error occurred: during login, token acquisition, or while making API calls.
   - Identify the application involved and the specific SAML configuration it uses.

2. **Review Logs**:
   - Check the application logs for additional error messages or warnings around the time the AADSTS90020 error was reported.
   - Look for any prior exceptions that might indicate a misconfiguration or issue.

3. **Verify User Attributes**:
   - Confirm the attributes being sent in the SAML assertion. The `ImmutableID` attribute should be included.

#### Common Issues That Cause This Error
1. **Missing ImmutableID**:
   - The SAML assertion does not include the `ImmutableID` attribute, which is essential for Azure AD to map the SAML token to the corresponding user.

2. **Incorrectly Configured Application**:
   - The application may not be configured to request or send the required claims.

3. **SAML Configuration Issues**:
   - The Service Provider (SP) and Identity Provider (IdP) configuration might not be aligned.

4. **User Not Provisioned**:
   - The user signing in might not be provisioned in Azure AD, leading to the 'ImmutableID' being undefined.

#### Step-by-Step Resolution Strategies
1. **Check SAML Assertion**:
   - Use a tool or library that decodes and inspects SAML assertions. Look for the `ImmutableID` in the assertion.
   - If it's missing, the SAML issuer may need to be updated to include it.

2. **Update SAML Configuration**:
   - If you are using a third-party identity provider, review their documentation to ensure your application is requesting the correct attributes including `ImmutableID`.
   - If you are implementing your own IdP, update it to include `ImmutableID` in the SAML response.

3. **Configure Claims in Azure AD**:
   - Go to Azure AD and access the section for your application.
   - Under "Token configuration", ensure that the `ImmutableID` claim is set to be issued in the SAML assertion.
   - Validate the claims mapping and ensure the correct attribute from your directory is linked to `ImmutableID`.

4. **Test with Sample Users**:
   - Provision test users in Azure AD and ensure they include the `ImmutableID`. Use these accounts to test the login process.
   
5. **Review Documentation**:
   - Refer to Microsoft's documentation on setting up SAML applications and configuring claims for Azure AD.
   - Link: [Azure AD SAML Authentication Documentation](https://learn.microsoft.com/en-us/azure/active-directory/develop/active-directory-protocols-saml)
   - Check the links for step-by-step guidance on configuring SAML assertions properly.

#### Additional Notes or Considerations
- Always trace changes in claims configurations in your Azure AD as they can affect multiple apps if not done carefully.
- Make sure the application identity is well-documented and share the configuration details with your development and ops teams.

#### Documentation Where Steps Can Be Found
- Microsoft Documentation: [Azure Active Directory SAML Protocol](https://learn.microsoft.com/en-us/azure/active-directory/develop/active-directory-protocols-saml)
- Documentation is regularly updated, so always check the latest resources.

#### Test the Documentation Can Be Reached
To ensure the documentation links provided are accessible:
1. Open a web browser.
2. Navigate to [Azure Active Directory SAML Protocol Documentation](https://learn.microsoft.com/en-us/azure/active-directory/develop/active-directory-protocols-saml).
3. Verify that the page loads successfully and that the content is accessible.

#### Advice for Data Collection
- Collect logs and error messages from both your application and Azure AD during each sign-in attempt.
- If you have access to a SAML assertion debugger, log the content of the SAML assertions to see what attributes are being sent.
- Ensure you gather details on the environment (production, staging, etc.), users affected, and steps to reproduce the error.

By following this troubleshooting guide, you should be able to identify and resolve the AADSTS90020 error effectively. Make sure to involve developers familiar with SAML and Azure AD for more complex issues.