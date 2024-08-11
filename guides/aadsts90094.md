
# AADSTS90094: AdminConsentRequired - Administrator consent is required.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS90094: AdminConsentRequired

#### Description
The error code AADSTS90094 indicates that admin consent is required for the application to access the requested resources. This usually means that the application is trying to perform a task that is restricted by Azure Active Directory (Azure AD) permissions and requires approval from an administrator.

---

### Initial Diagnostic Steps
1. **Identify the Application**: Determine which application is triggering the error. Review application logs and user feedback.
2. **Check User Permissions**: Verify the user account's permission levels. Ensure that the user trying to access the application has been assigned appropriate permissions.
3. **Review App Registration**: Verify the application's registration in Azure AD. Check the permissions scope that it is requesting and see if these permissions require admin consent.
4. **Understand the Scenario**: Gather context about when and how the error occurred (e.g., during login, resource access request, etc.)

---

### Common Issues that Cause This Error
- **Application Permissions**: The application is configured with permissions that require administrator consent.
- **User Role**: The user attempting to use the application does not have sufficient permissions.
- **Consent Not Granted**: An admin has not granted consent for the application to access specific Graph API scopes or resources.
- **Permissions Changes**: An administrator changed permissions after the application was initially registered.
  
---

### Step-by-Step Resolution Strategies

#### 1. Check Application Permissions
- **Access Azure Portal**:
  - Go to Azure Portal: [Azure Portal](https://portal.azure.com).
- **Navigate to Azure AD**:
  - Select "Azure Active Directory."
- **Find App Registrations**:
  - Select "App registrations" and find the application triggering the error.
- **Review API Permissions**:
  - Click on "API permissions" to see the list of permissions requested by the application.
  - Check if any permissions require admin consent (these permissions are usually labeled as such).

#### 2. Grant Admin Consent
- **Admin Login Required**: Make sure you're logged in with an account that has admin rights to the Azure AD tenant.
- **Granting Consent**:
  - In the "API permissions" section, look for the "Grant admin consent for {Your Organization}" button.
  - Click it to grant consent for all required permissions at once.

#### 3. User Role and Assignment
- Check the roles assigned to the user. In some scenarios, you may need to adjust the user's role or assign them to a specific group that has access to the application.
  
#### 4. Communication and Documentation
- After granting consent, inform users to try accessing the application again.
- Provide documentation or guidance to users that explains the permissions required.

---

### Additional Notes or Considerations
- **User Consent Settings**: Review the settings under “User settings” in Azure AD to control whether users can consent to apps or if only admins can consent to apps.
- **Testing After Changes**: Always test after any changes to permissions or admin consent to ensure that the error no longer occurs.
- **Revocation**: If you revoke admin consent, ensure you inform users, as they may encounter this error again.

---

### Documentation for Guidance
- Microsoft Identity Platform Documentation: [Permissions and consent](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-permissions-and-consent)
- Grant admin consent to an application: [Grant admin consent](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-admin-consent)

#### Testing Documentation Reachability
- **Check**: Open links in a web browser to ensure accessibility. All URLs should redirect to the expected content in Microsoft documentation.

---

### Advice for Data Collection
1. **Error Logs**: If available, compile error logs from the application to help diagnose the issue.
2. **User Reports**: Collect details on which users encounter the error, their roles, and the specific actions they perform leading to the error.
3. **Permissions Overview**: Take screenshots or notes of the application's permission requests for further analysis.

---

By following this troubleshooting guide, administrators should be able to effectively resolve the AADSTS90094 error and ensure that application permissions are correctly configured for user access.