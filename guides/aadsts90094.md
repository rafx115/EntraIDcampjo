# AADSTS90094: AdminConsentRequired - Administrator consent is required.


## Troubleshooting Steps
## Troubleshooting Guide for AADSTS90094: AdminConsentRequired

### Description
The error code **AADSTS90094** indicates that administrator consent is required for the application that the user is trying to access. Typically, this means that the application requires permissions beyond what is granted to standard users and needs an administrator to approve those permissions.

### Initial Diagnostic Steps
1. **Identify the Application**: Determine which application is generating the AADSTS90094 error and understand the permissions it is requesting.
  
2. **Check the User’s Role**: Confirm whether the user encountering the error has necessary permissions. Non-admin users may lack rights to consent to certain permissions.

3. **Review the Error Message**: Specifically look for the scopes that require admin consent in the error details.

4. **Attempt to Sign in Again**: Sometimes, transient errors can occur. Retry the sign-in process to rule out temporary issues.

### Common Issues that Cause this Error
- **Required Permissions**: The application may request application permissions or delegated permissions that require admin consent.
- **Conditional Access Policies**: There may be policies that restrict access to applications.
- **User Type**: The user may not belong to a group of users that can consent to the required permissions.
- **Multi-Tenant Applications**: In multi-tenant scenarios, certain permissions might need additional consent from the tenant admin.

### Step-by-Step Resolution Strategies

1. **Review Application Permissions**:
   - In the Azure portal, navigate to **Azure Active Directory > App registrations**.
   - Locate and click on the application to review its permissions under **API permissions**.
   - Understand which permissions require admin consent (marked with a yellow warning icon).

2. **Admin Consent Process**:
   - An Azure AD administrator needs to provide consent to these permissions. This can be done via:
     - Direct admin consent through the Azure portal:
       - Go to **API permissions** for the application.
       - Click on **Grant admin consent for [Your Organization]**.
     - Alternatively, use a URL to initiate admin consent:
       ```
       https://login.microsoftonline.com/{tenant-id}/adminconsent?client_id={client-id}
       ```

3. **Modify Scope Requests**:
   - If appropriate, review the application's permissions and modify the requested scopes to limit those that require admin consent.

4. **Validation**:
   - After granting consent, have the user retry to access the application and confirm whether the error persists.

5. **Documentation for Admins**:
   - Share information with your administrator about how to grant admin consent through Microsoft’s official documentation.

### Additional Notes or Considerations
- Ensure that the user is aware of which application they are accessing and the scopes required.
- Inform your administrators of any conditional access policies or security settings that may impact application access.
- Testing with multiple accounts may help rule out issues with specific user accounts.

### Documentation for Further Guidance
- **Azure Active Directory Documentation**: [Manage App Registration Permissions and Consent](https://docs.microsoft.com/en-us/azure/active-directory/develop/azure-ad-apps/quickstart-v2-nodejs-webapi#configure-a-web-api-to-support-oauth-2)
- **Understanding Permission Levels**: [API Permissions in Azure Active Directory](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-app-permissions-and-admin-consent)
- **Admin Consent Documentation**: [Granting Admin Consent](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-admin-consent)

### Advice for Data Collection
If further investigation is needed and you suspect a deeper-rooted issue, consider collecting the following data:

- **Event Viewer Logs**:
  - Check for any errors related to Azure AD authentication events or application logs.
  
- **Network Tracing Tools**:
  - **NetTrace**: Use this tool to capture detailed network activity if your application issues arise from network interaction.
  - **Fiddler**: Use Fiddler to monitor HTTP traffic to diagnose what scopes are being requested and if there's a failure in response.

- **Monitoring Logs**:
  - Monitor Azure AD sign-in logs to review the sign-in attempts, errors, and codes.

By following this detailed guide and recommendations, you should be able to effectively troubleshoot and resolve the AADSTS90094 error.