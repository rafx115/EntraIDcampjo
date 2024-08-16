# AADSTS90095: AdminConsentRequiredRequestAccess-  In the Admin Consent Workflow experience, an interrupt that appears when the user is told they need to ask the admin for consent.


## Troubleshooting Steps
Certainly! The error code AADSTS90095 indicates that an application is trying to access resources that require admin consent in the Azure Active Directory (Azure AD) environment, but the user does not have enough privileges to grant that access. Here’s a detailed troubleshooting guide for resolving this issue:

### Troubleshooting Guide for AADSTS90095

#### Initial Diagnostic Steps
1. **Verify User Role**:
   - Confirm the role of the user attempting the operation. Users should be in roles with sufficient privileges (such as Global Administrator or Privileged Role Administrator) to provide admin consent.

2. **Check Azure AD Permissions**:
   - Review the permissions requested by the application. These can often be found in the Azure Portal under Azure Active Directory > App registrations > [Your Application] > API permissions.

3. **Understand the Application's Consent Requirements**:
   - Identify whether the application requires admin consent by checking the permissions specified in its manifest or in the Azure portal.

#### Common Issues that Cause This Error
- **Insufficient Permissions**: The user attempting to access the application does not have permissions to grant consent.
- **Request for High-Level Permissions**: The application is requesting permissions that require admin consent (like access to all users' profiles).
- **Tenant Policies**: Your Azure AD tenant policies might restrict granting consent based on certain conditions.
- **User Type**: The user may be a "Member" rather than a "Guest" or not affiliated with the tenant in a way that allows them to request consent.

#### Step-by-Step Resolution Strategies
1. **If You Are an Admin**:
   - **Review Consent Requests**:
     - Go to Azure Portal > Azure Active Directory > Enterprise applications > [Your Application] > User consent settings.
     - You can review and provide admin consent directly if you have the necessary privileges.

   - **Grant Admin Consent for API Permissions**:
     1. In the Azure Portal, navigate to Azure Active Directory.
     2. Click on “App registrations”.
     3. Select the application encountering the error.
     4. Go to “API permissions”.
     5. Click on “Grant admin consent for [Your Organization]”.

2. **If You Are Not an Admin**:
   - **Contact Your Administrator**: 
     - Inform them of the need for admin consent. Provide them with details about the application and what permissions it requires.
     - Share the error code AADSTS90095 and its description to help them understand the issue.

3. **Adjust Tenant Settings (if applicable)**:
   - If you manage the Azure AD tenant, consider reviewing the user consent settings under Azure Active Directory > User settings to determine if users are allowed to consent to apps or if this is restricted.

#### Additional Notes or Considerations
- **User Notification**: Users encountering this error should be informed of what permissions are needed and that they need to reach out to an admin.
- **Documentation**: Azure documentation provides extensive guidance on managing app registrations and consent:
  - [Managing user consent for apps](https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-user-consent)
  - [Grant admin consent to an application](https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-admin-consent)

#### Advice for Data Collection
1. **Event Viewer Logs**: Collect logs from the Event Viewer if the issue seems related to a specific application’s integration with Azure AD.
   - Check under "Applications and Services Logs" for relevant Azure AD events.

2. **Network Traces**:
   - Use tools like `nettrace` to capture networking traffic if there's suspicion of connectivity issues.

3. **Fiddler**:
   - Utilize Fiddler to monitor the HTTP traffic and observe the details of the REST API calls made to Azure AD, including response codes and bodies. Look for detailed error messages or headers returned by Azure.

### Conclusion
By following the steps outlined in this troubleshooting guide, you should be equipped to address the AADSTS90095 error effectively. Engaging with your Azure AD administrators and using the documentation provided will also help facilitate a resolution.