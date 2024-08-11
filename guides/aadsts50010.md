
# AADSTS50010: AudienceUriValidationFailed - Audience URI validation for the app failed since no token audiences were configured.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS50010: AudienceUriValidationFailed

#### Error Description
**AADSTS50010**: This error occurs when the Azure Active Directory (AAD) receives a token that does not match any of the configured audience URI values for the app. In essence, the application does not recognize the token as coming from a valid source.

---

### Initial Diagnostic Steps
1. **Verify Application Registration**:
   - Ensure that the application registration in Azure AD is correct and active.
   - Check if the application is enabled.

2. **Check Token Details**:
   - Use tools such as [JWT.io](https://jwt.io) to decode the token and inspect its `aud` (audience) claim.
   - Identify the audience specified in the token.

3. **Logs Review**:
   - Review the Azure AD sign-in logs to gather more context around the failed authentication attempts to understand which request is failing.

4. **Authentication Flow Check**:
   - Confirm which authentication method (e.g., client credentials, authorization code flow, etc.) the application is using.

---

### Common Issues that Cause AADSTS50010
1. **Missing Audience Configuration**:
   - The application does not have any audience values configured within Azure AD.

2. **Incorrect Redirect URI**:
   - The redirect URI specified during the initial application registration does not match the request made from the application.

3. **Token Issued for Another Application**:
   - The token presented is issued for a different application entirely or a different audience.

4. **Scope Misconfiguration**:
   - The scopes requested for the token do not align with the configured application.

---

### Step-by-Step Resolution Strategies
1. **Configure Audience URI**:
   - Go to the Azure portal.
   - Navigate to **Azure Active Directory > App registrations**.
   - Select your application.
   - Under the **Token configuration** blade, ensure you have set the audience claims correctly.
   - If you need to add an audience, do so following the format for your application.

2. **Check Redirect URIs**:
   - Confirm that the redirect URI in your application matches the one registered in Azure AD exactly.
   - Navigate to **Authentication** in your app registration and ensure the URIs are correct.

3. **Validate Token Audience**:
   - If you have set up multiple audiences, ensure that the token's audience matches at least one of the configured audiences in the Azure AD app.

4. **Adjust API Permissions**:
   - Under the **API permissions** section, ensure the application has the necessary permissions to request tokens for the specified audience.

5. **Testing Changes**:
   - After making changes, attempt to authenticate again and see if the error persists.
   - It may take a few moments for the changes to propagate in Azure.

6. **Review Application Code**:
   - Review the code handling authentication to ensure the expected audience is being requested.

---

### Additional Notes or Considerations
- Make sure to test the application in a controlled environment after updates to avoid unintended disruptions.
- If your application is using a library like Microsoft Identity Web or MSAL, consult its documentation for retrieving tokens and setting audience claims effectively.
  
---

### Documentation and Resources
- [Azure AD App Registration Documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)
- [Troubleshooting Azure AD Token Issues](https://docs.microsoft.com/en-us/azure/active-directory/develop/msal-net-attributes)
- [Understanding Azure AD Authentication Scenarios](https://docs.microsoft.com/en-us/azure/active-directory/develop/authentication-scenarios)

_**Test the Documentation**: All links provided above are accessible as of October 2023. Please check the documentation for any updates or version changes._

---

### Advice for Data Collection
- Always collect the token and its claims before analytics. Use JWT-decode or similar tools.
- Capture the request/response logs surrounding the authentication to help identify where the issue may arise from.
- Document the steps taken during troubleshooting for future reference and team communication.

By following these steps, you can effectively diagnose and resolve the AADSTS50010 error related to Audience URI validation failures.