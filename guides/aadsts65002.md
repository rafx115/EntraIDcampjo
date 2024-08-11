
# AADSTS65002: Consent between first party application '{applicationId}' and first party resource '{resourceId}' must be configured via preauthorization - applications owned and operated by Microsoft must get approval from the API owner before requesting tokens for that API. A developer in your tenant might be attempting to reuse an App ID owned by Microsoft. This error prevents them from impersonating a Microsoft application to call other APIs. They must move to another app ID they register.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS65002 Error Code

#### Initial Diagnostic Steps:
1. **Confirm the Application ID and Resource ID:** Ensure that the correct Application ID and Resource ID have been provided in the request that triggered the error.
2. **Check Permissions:** Verify the permissions being requested by the application and ensure that they align with the consent configuration.
3. **Review App Ownership:** Determine if the App ID being used is owned by Microsoft or another entity within your tenant.

#### Common Issues:
- **Misconfigured Consent:** Consent between the first-party application and resource may not be properly configured.
- **Unauthorized Use of Microsoft App ID:** Attempts to reuse an App ID owned by Microsoft can trigger this error.
- **Incorrect Permissions:** Requesting tokens for APIs without appropriate preauthorization can also lead to this issue.

#### Step-by-Step Resolution Strategies:
1. **Verify Application Ownership:**
    - Identify the ownership of the application causing the error. If it is owned by Microsoft, it requires special approval for accessing certain APIs.
2. **Check for Preauthorization:** 
    - Ensure that the necessary consent settings have been configured for the application to access the specific resource securely.
3. **Change App ID:**
    - If the application is attempting to impersonate a Microsoft-owned application, advise the developer to register a new App ID and use that for requesting tokens.
4. **Reconfigure Permissions:** 
    - Adjust the permissions requested by the application to match the preauthorization requirements of the targeted APIs.

#### Additional Notes or Considerations:
- **API Owner Approval:** Applications owned and operated by Microsoft must obtain approval from the API owner before requesting tokens, following the preauthorization process.
- **Developers' Understanding:** Communicate the importance of correctly registering and managing App IDs to prevent such errors in the future.

#### Documentation for Guidance:
- [Microsoft Identity platform documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-permissions-and-consent)
- [Azure AD error codes and messages](https://docs.microsoft.com/en-us/azure/active-directory/develop/reference-aadsts-error-codes)

By following these steps and considering the provided guidance, you can troubleshoot and resolve the AADSTS65002 error effectively. If further assistance is required, you may refer to the official documentation or reach out to Microsoft support for additional help.