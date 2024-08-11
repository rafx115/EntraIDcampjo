
# AADSTS90095: AdminConsentRequiredRequestAccess-  In the Admin Consent Workflow experience, an interrupt that appears when the user is told they need to ask the admin for consent.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS90095 Error Code

**Error Description:** AADSTS90095 indicates that a user is attempting to access a resource that requires admin consent, but they do not have the necessary permissions to proceed without it. This can commonly occur during the use of applications that integrate with Azure Active Directory (Azure AD). 

---

### Initial Diagnostic Steps

1. **Identify the User Role:**
   - Check whether the user encountering the error has sufficient permissions or is a member of the necessary roles in Azure AD.

2. **Understand Application Permissions:**
   - Determine which application the user is trying to access and what permissions it requests. 

3. **Check for Admin Consent Workflow:**
   - Verify if the application has been registered properly in Azure AD and if it requires admin consent for certain operations.

---

### Common Issues That Cause this Error

1. **Insufficient User Permissions:**
   - The user does not have the necessary permissions to access the application or resource.

2. **Missing Admin Consent:**
   - Admin consent has not been granted for the permissions that the application is requesting.

3. **Application Registration Issues:**
   - There could be issues with the application registration in Azure AD, such as incorrect redirect URIs or scopes.

4. **Conditional Access Policies:**
   - Conditional Access policies might be preventing access, especially for apps that require high levels of permission.

---

### Step-by-Step Resolution Strategies

1. **Confirm User Permissions:**
   - Navigate to Azure Portal > Azure Active Directory > Users.
   - Check if the user is part of the correct groups or roles.

2. **Examine Application Permissions:**
   - Go to Azure Portal > Azure Active Directory > App registrations.
   - Locate the application in question and check under "API permissions" to see what permissions are requested.
   - Ensure that permissions marked as "requires admin consent" are listed.

3. **Request Admin Consent:**
   - If the user requires admin consent, they should notify their administrator.
   - As an admin, navigate to the Azure Portal > Azure Active Directory > App registrations > your app > API permissions > Grant admin consent for [Tenant Name].

4. **Review Application Registration:**
   - Check the application properties under Azure Portal > Azure Active Directory > App registrations:
     - Verify Redirect URIs and application ID.
     - Ensure that required permissions are precisely set.

5. **Check Conditional Access Policies:**
   - Review Azure AD > Security > Conditional Access.
   - Ensure that there are no policies in place that would prevent the application from being accessed.

---

### Additional Notes or Considerations

- **User Training:**
  Ensure users are properly trained on how to identify whom to contact for admin consent and what information to provide.

- **Admin Consent Workflow:**
  Familiarize yourself with the Admin Consent Workflow, as it assists in managing requests from users, which can streamline the consent process.

- **Auditing User Activities:**
  Enable audit logs to track user access attempts, which may provide insight into the frequency and causes of these errors.

---

### Documentation References

- [Microsoft Identity Platform Documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/)
- [Grant admin consent for an application](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-admin-consent)
- [Manage Azure Active Directory app registrations](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)

### Test Reachability of Documentation

- Validate that the documentation links provided are accessible. Open a browser and navigate to the URLs listed to ensure they are available and provide relevant information.

### Advice for Data Collection

1. **User Information:**
   - Collect usernames, roles, and the exact application they are attempting to access.

2. **Error Messages:**
   - Take note of the full error message and any additional codes or messages provided in the user’s context.

3. **Timestamps:**
   - Record the time and date when the issue occurred for audit and support tracking.

4. **Tenant Information:**
   - Document details about the Azure AD tenant to assist in troubleshooting permission-related issues.

5. **Screenshots:**
   - Encourage users to take screenshots of the error message or their activity before receiving the error.

---

By following this detailed troubleshooting guide, administrators and users can effectively identify and resolve **AADSTS90095** related issues, ensuring smoother accessibility to Azure AD integrated applications.