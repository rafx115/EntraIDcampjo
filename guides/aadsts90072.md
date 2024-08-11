
# AADSTS90072: PassThroughUserMfaError - The external account that the user signs in with doesn't exist on the tenant that they signed into; so the user can't satisfy the MFA requirements for the tenant. This error also might occur if the users are synced, but there is a mismatch in the ImmutableID (sourceAnchor) attribute between Active Directory and Microsoft Entra ID. The account must be added as an external user in the tenant first. Sign out and sign in with a different Microsoft Entra user account. For more information, please visitconfiguring external identities.


## Troubleshooting Steps
**Troubleshooting Guide for AADSTS90072: PassThroughUserMfaError**

### Overview:
The `AADSTS90072` error signifies that the user attempting to sign in does not exist in the tenant they are accessing. This can happen for external accounts or accounts that are synced from on-premises Active Directory, where there is a mismatch in the ImmutableID.

### Initial Diagnostic Steps:
1. **Verify the User's Account**:
   - Check if the account the user is trying to access exists in the tenant Azure Active Directory (Azure AD).
   - Ensure the user is using the correct sign-in credentials associated with the tenant.

2. **Check the Tenant Type**:
   - Determine if the user is attempting to sign in to the correct tenant, especially if the user has accounts in multiple tenants.

3. **Examine MFA Requirements**:
   - Confirm if Multi-Factor Authentication (MFA) is configured for the tenant and if the user meets those requirements.

### Common Issues that Cause This Error:
1. **User Not Provisioned**:
   - The external account has not been provisioned or invited to the tenant.

2. **ImmutableID Mismatch**:
   - The ImmutableID (sourceAnchor) values between the on-premises Active Directory and Azure AD do not match, causing the MFA validation to fail.

3. **Account Type Issues**:
   - Users may be explicitly trying to sign in with personal Microsoft accounts instead of work or school accounts.

4. **Tenant Configuration**:
   - Incorrect settings in Azure AD regarding external identities or guest access.

### Step-by-Step Resolution Strategies:
1. **Add User as External User in the Tenant**:
   - Go to Azure Active Directory.
   - Navigate to "Users" > "New guest user".
   - Enter the user's email address and add them as a guest to the tenant.

2. **Verify Users in Active Directory**:
   - If the user is synced from on-premises Active Directory:
     - Check the Active Directory for accurate ImmutableID values.
     - Ensure that the correct values are synced to Azure AD using the Azure AD Connect tool.

3. **Recheck ImmutableID Sync**:
   - For synced users, use the Azure AD Connect tool to verify synchronization settings.
   - Check if any attributes have been updated recently and need re-syncing.

4. **Sign Out and In with the Correct Account**:
   - Have the user sign out from all Office and Microsoft services.
   - Direct them to sign in again with the appropriate account associated with the target tenant.

5. **Review and Adjust External Identity Settings**:
   - In Azure Active Directory, go to "External Identities" and check the settings related to guest users and external collaboration.

### Additional Notes or Considerations:
- Encourage users to keep a record of which accounts are used for which tenants to avoid confusion.
- If the issue persists after following the above steps, consider resetting the user's MFA settings.

### Documentation for Guidance:
1. **Microsoft’s Official Documentation**:
   - **Managing Guest Access**: [Link to managing guest access in Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/b2b/manage-user-guest-access)
   - **User account provisioning**: [Link to user provisioning documentation](https://docs.microsoft.com/en-us/azure/active-directory/external-identities/what-is-external-identities)
   - **Azure AD Connect**: [Link to Azure AD Connect](https://docs.microsoft.com/en-us/azure/active-directory/hybrid/deploy/plan-connect)

### Test Documentation Accessibility:
- **Reach the links** provided in the documentation. Use a web browser to visit:
   - [Managing Guest Access in Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/b2b/manage-user-guest-access)
   - [User Account Provisioning Documentation](https://docs.microsoft.com/en-us/azure/active-directory/external-identities/what-is-external-identities)
   - [Azure AD Connect Documentation](https://docs.microsoft.com/en-us/azure/active-directory/hybrid/deploy/plan-connect)

### Advice for Data Collection:
- Gather the following information during the troubleshooting process:
  - The tenant ID and the domain associated with the tenant.
  - The exact user email that is experiencing the issue.
  - The logs from Azure AD that show failed login attempts, focusing on timestamps and error codes.
  - Any recent changes made to the user account, permissions, or tenant settings.

This troubleshooting guide aims to provide a comprehensive approach to resolving the AADSTS90072 error by identifying causes, offering resolutions, and providing documentation links for further assistance.