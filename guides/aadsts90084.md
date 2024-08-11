
# AADSTS90084: OrgIdWsFederationGuestNotAllowed - Guest accounts aren't allowed for this site.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS90084

#### Error Description:
**AADSTS90084: OrgIdWsFederationGuestNotAllowed - Guest accounts aren't allowed for this site.**

This error occurs when a user attempts to access an Azure Active Directory (Azure AD) resource using a guest account, but the organization’s settings do not permit guest access.

### Initial Diagnostic Steps
1. **Reproduce the Error:**
   - Attempt to access the application or resource that is returning the error. Take note of the exact circumstances under which the error occurs (user role, the application being accessed, etc.).

2. **Check User Status:**
   - Verify whether the user attempting to access the resource is a guest user in the Azure AD tenant. Guest users typically have a different user type than internal users.

3. **Review Azure AD Configuration:**
   - Log in to the Azure portal and navigate to **Azure Active Directory** > **Users**. Check if the user in question is marked as a guest.

### Common Issues That Cause This Error
- The organization has guest access disabled in Azure AD settings.
- User policies within Azure AD restrict access to non-members (guests).
- The application being accessed does not support guest accounts or has specific policies limiting access.
- Federation settings in Azure AD are preventing guest access.

### Step-by-Step Resolution Strategies

1. **Verify Guest Access Settings:**
   - Navigate to **Azure Active Directory** > **External Identities** > **External collaboration settings**.
   - Confirm that the option “Guest users permissions are limited” is configured according to organizational policy. If it is enabled, consider allowing guest access if organizational policy permits.

2. **Adjust User Permissions:**
   - If the organization allows guests, make sure that the user is set up correctly:
     - In Azure Active Directory, ensure that the user has the appropriate roles assigned to access the desired resource.
  
3. **Modify Application Settings:**
   - Check the application's configuration to see if it has settings restricting guest access. This can often be found in the application’s management settings in Azure AD.
   - Review any API permissions that may potentially block guest users.

4. **Update Access Policies:**
   - If necessary, create a Conditional Access policy that explicitly allows guest users to access certain resources:
     - Go to **Azure Active Directory** > **Security** > **Conditional Access**, and configure rules that allow access for guest users as needed.
  
5. **Consult Tenant Administrator:**
   - If you don’t have access to make these changes, consult with an Azure AD administrator for your organization. They may need to adjust settings or grant the user different permissions.

### Additional Notes or Considerations
- Review organizational policy on guest access to ensure compliance with data privacy regulations.
- If the organization frequently collaborates with external users, consider defining clear guest access policies.
  
### Documentation for Guidance
- [Manage guest access in Azure Active Directory](https://docs.microsoft.com/en-us/azure/active-directory/external-identities/guests)
- [Assign Azure AD roles to users](https://docs.microsoft.com/en-us/azure/active-directory/roles/permissions-reference)
- [Conditional Access documentation](https://docs.microsoft.com/en-us/azure/active-directory/conditional-access/overview)

**Test the Documentation Reachability:**
- Ensure that the links provided in the documentation section are accessible and lead to the correct pages. You can do this by clicking the links or copying them into a browser directly.

### Advice for Data Collection
- **User ID and Role**: Gather user IDs and their respective roles within Azure AD.
- **Error Logs**: Capture any error logs or messages that occur during the connection attempt.
- **Azure AD Configuration Screenshots**: Take screenshots of any relevant Azure AD configurations that may relate to guest access and permissions for future reference.
- **Access Timing**: Note the time and date of the issue occurrence as this information may help in diagnostics.

By following these steps, you should be able to diagnose and resolve the AADSTS90084 error efficiently, ensuring compliance with your organization’s policies regarding guest access.