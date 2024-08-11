
# AADSTS90084: OrgIdWsFederationGuestNotAllowed - Guest accounts aren't allowed for this site.


## Troubleshooting Steps
Error Code: AADSTS90084 - OrgIdWsFederationGuestNotAllowed

**Initial Diagnostic Steps:**
1. Verify if the user account experiencing the issue is a guest account in the Azure Active Directory.
2. Check the site settings to ensure guest accounts are allowed or restricted.
3. Review any recent changes made to the Azure Active Directory settings that might have caused the issue.

**Common Issues Causing the Error:**
1. Incorrect Azure Active Directory settings or permissions configurations.
2. Site settings prohibiting guest accounts from accessing the site.
3. Mismatch in authentication protocols or configurations between Azure Active Directory and the site.
4. User account type misconfiguration.

**Step-by-Step Resolution Strategies:**
1. **Check Azure Active Directory Settings:**
   - Sign in to the Azure portal.
   - Navigate to Azure Active Directory > Users.
   - Verify the user account in question and check if it is a guest account.
   - If the account is a guest account, ensure that guest access is allowed for the site.

2. **Review Site Settings:**
   - Access the site settings where the error is occurring.
   - Check the guest access configurations to confirm if they are allowed or restricted.
   - Adjust the settings to permit guest accounts if necessary.

3. **Verify Authentication Configurations:**
   - Ensure that the authentication protocols and configurations are consistent between Azure Active Directory and the site.
   - Make any necessary adjustments to align the settings.

4. **Update User Account Type:**
   - If the user account type is incorrectly configured, update the account type to resolve the issue.
   
**Additional Notes or Considerations:**
- It's important to communicate with the site administrators or IT support team to discuss any recent changes that might have led to the error.
- Testing the configurations in a non-production environment can help avoid service interruptions.

**Documentation for Guidance:**
1. Microsoft Azure Active Directory documentation: 
   - [Guest user access in Azure AD B2B](https://docs.microsoft.com/en-us/azure/active-directory/external-identities/collaboration-guest-user)
   - [How to manage guest access in Azure Active Directory using the Azure portal](https://docs.microsoft.com/en-us/azure/active-directory/external-identities/collaboration-guest-user#managing-guests)

By following these steps and guidance from the documentation, you should be able to troubleshoot and resolve the error code AADSTS90084 related to the OrgIdWsFederationGuestNotAllowed issue effectively.