
# AADSTS90094: AdminConsentRequired - Administrator consent is required.


## Troubleshooting Steps
**Error Code AADSTS90094 Troubleshooting Guide: AdminConsentRequired - Administrator consent is required.**

**Initial Diagnostic Steps:**
1. Confirm that the user attempting to access the application has proper permissions.
2. Check if global administrator consent is required for the application.
3. Verify if the application permissions require admin consent.
4. Review any recent changes in permission settings or configurations.

**Common Issues that Cause this Error:**
1. Insufficient permissions assigned to the user.
2. Application permissions are set to require admin consent.
3. Changes in configurations or permissions settings.
4. Incorrect setup of permissions in Azure Active Directory.

**Step-by-Step Resolution Strategies:**
1. **Request Administrator Consent:** 
   - An administrator needs to grant consent for the application. They can do this by visiting the consent URL provided in the error message or through the Azure portal.
2. **Verify Application Permissions:**
   - Check the permissions required by the application and ensure they align with the organization's policies.
3. **Check User Permissions:**
   - Ensure the user has the necessary permissions to access the application.
4. **Review Application Configuration:**
   - Verify the application configuration in Azure Active Directory to ensure it is correctly set up.
5. **Reset Permissions:**
   - If issues persist, consider resetting the permissions for the application and granting consent again.

**Additional Notes or Considerations:**
- It is essential to involve an administrator with sufficient privileges to grant consent.
- Keep track of any changes made to permissions or configurations for future reference.
- Regularly review and update permissions to align with security best practices.

**Documentation for Guidance:**
- Microsoft Azure Active Directory Admin Consent for Applications: https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/grant-admin-consent

By following the steps outlined above, you should be able to resolve the AADSTS90094 error related to AdminConsentRequired successfully. If the issue persists, consider reaching out to your organization's IT support team for further assistance.