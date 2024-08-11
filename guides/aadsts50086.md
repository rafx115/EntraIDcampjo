# AADSTS50086: SasNonRetryableError


## Troubleshooting Steps
**Troubleshooting Guide for AADSTS50086 Error Code (SasNonRetryableError)**

**Initial Diagnostic Steps:**
1. Understand the context in which the error occurred. Determine if the error arises during user sign-in, authorization requests, token issuance, etc.
2. Check whether the error is consistently reproducible or intermittent.
3. Verify the specific API, application, or service affected by the error.
4. Look for any recent changes in configurations, permissions, or updates that might have triggered the error.

**Common Issues causing AADSTS50086 Error:**
1. Incorrect client application configuration such as invalid client ID, redirect URIs, or authentication settings.
2. Misconfigured permissions or consent issues.
3. Token issuance failures due to expired or revoked certificates.
4. Network connectivity issues affecting authentication flow.
5. Token validation problems on the receiving end.

**Step-by-Step Resolution Strategies:**
1. **Validate Client Application Configuration:**
   - Ensure that the client ID and secret are correct and corresponding to the application registration in Azure Active Directory.
   - Check the redirect URIs and ensure they match the settings in Azure AD.
   - Verify that the authentication protocols (like OAuth, OpenID Connect) are correctly configured based on the application requirements.

2. **Review Permissions and Consent:**
   - Confirm that the required permissions are correctly set up for the application.
   - Ensure that users have consented to the necessary permissions.
   - Check if there are any conflicting or overlapping permissions that might lead to the error.

3. **Certificate and Token Management:**
   - Renew or update any expired certificates used for token signing or encryption.
   - Verify the token signing and validation process in the application code.
   
4. **Troubleshoot Network and Connectivity:**
   - Check for any firewall rules or network restrictions that might block the authentication requests.
   - Ensure that the application can reach the Azure AD endpoints and vice versa.

**Additional Notes or Considerations:**
- Keep track of Azure AD service health status, as outages or incidents on the Azure side can also lead to such errors.
- Review Azure AD logs, particularly the Audit and Sign-ins logs, to get more insights into the error source.

**Documentation for Guidance:**
- Azure Active Directory documentation provides detailed step-by-step guides and troubleshooting tips for various scenarios. You can refer to the official Microsoft documentation: [Azure AD Error Codes](https://docs.microsoft.com/en-us/azure/active-directory/develop/reference-aadsts-error-codes)

By following these steps and considering the common issues outlined above, you should be able to diagnose and resolve the AADSTS50086 error with the SasNonRetryableError description effectively. If the issue persists, consider reaching out to Azure AD support for further assistance.