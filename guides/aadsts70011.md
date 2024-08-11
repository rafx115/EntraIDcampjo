# AADSTS70011: InvalidScope - The scope requested by the app is invalid.


## Troubleshooting Steps
Error Code: AADSTS70011 - InvalidScope

**Initial Diagnostic Steps:**
1. Verify the scope requested by the app.
2. Check the app's permissions and required scopes.

**Common Issues:**
1. Incorrectly configured scopes in the app's manifest file.
2. Mismatch between the requested scope by the app and the scopes configured in the authentication provider (e.g., Azure AD).
3. Missing consent for the required scope.
4. Insufficient permissions assigned to the app registration.

**Step-by-Step Resolution Strategies:**
1. **Verify Scope Configuration:**
   - Check the app's code or configuration to ensure that the requested scope matches the scopes defined in the authentication provider.
   - Validate if the requested scope is correct and valid for the operation being performed.

2. **Grant Required Permissions:**
   - Navigate to the Azure portal and go to the Azure Active Directory.
   - Locate the registered application causing the error.
   - Add the necessary API permissions and scopes to the app registration.
   - Make sure the required permissions are consented to by an admin or the user.

3. **Consent to Scopes:**
   - If the error is related to missing consent for the required scope, ensure that the consent is granted.
   - Trigger the consent flow for the user or admin to approve the requested scopes.

4. **Check Manifest Configuration:**
   - Review the manifest file of the app registration.
   - Verify that the "requiredResourceAccess" section in the manifest contains the expected scopes with the correct resource IDs.

**Additional Notes or Considerations:**
- Monitor the Azure AD logs for more specific details on the error and its source.
- Keep track of any recent changes in permissions or scopes that might have triggered the error.

**Documentation for Guidance:**
- Microsoft Azure Documentation: [Troubleshoot Azure AD error codes](https://docs.microsoft.com/en-us/azure/active-directory/develop/troubleshoot-error-codes)
- Azure AD scope documentation: [Understanding scopes in Azure AD apps](https://docs.microsoft.com/en-us/azure/active-directory/develop/scopes)
- App registration in Azure AD: [Manage app registration in Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)