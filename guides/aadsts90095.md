
# AADSTS90095: AdminConsentRequiredRequestAccess-  In the Admin Consent Workflow experience, an interrupt that appears when the user is told they need to ask the admin for consent.


## Troubleshooting Steps
**Troubleshooting Guide for Error Code AADSTS90095 - AdminConsentRequiredRequestAccess**

**Initial Diagnostic Steps:**
1. Verify the user's permissions and roles within the application or service that triggered the error.
2. Check if the application registration in Azure Active Directory (AAD) has the required permissions and admin consent settings configured correctly.
3. Confirm if the user has attempted to access a resource that requires admin consent.
4. Determine if the organization has specific policies or restrictions that could be influencing the consent workflow.

**Common Issues that Cause this Error:**
1. Insufficient user permissions to access the resource.
2. Misconfigured permissions in the application manifest.
3. Inadequate consent settings for the application registration in Azure AD.
4. Organization-wide settings or policies restricting user access.

**Step-by-Step Resolution Strategies:**
1. **Request Admin Consent:**
   - Instruct the user to contact an administrator within their organization to grant the necessary consent.
2. **Review Application Permissions:**
   - Inspect the application registration in Azure AD and ensure that the required permissions are correctly set.
3. **Check User Roles:**
   - Validate if the user's roles permit access to the requested resource.
4. **Troubleshoot via Azure Portal:**
   - Utilize the Azure Portal to review logs, permissions, and roles related to the error.
5. **Organization Policies:**
   - Review any organization-wide policies that might be restricting access.

**Additional Notes or Considerations:**
- It is essential to clearly communicate with the user regarding the need to involve an admin for consent.
- Ensure that all relevant documentation and guides are easily accessible to provide assistance during troubleshooting.

**Documentation for Guidance:**
- Microsoft Azure Documentation on Admin Consent: [Microsoft Docs - Admin Consent](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-admin-consent)

By following these steps and considering the common causes of the error code AADSTS90095, you should be able to effectively troubleshoot and resolve the issue of AdminConsentRequiredRequestAccess interrupt in Azure Active Directory.