# AADSTS50020: UserUnauthorized - Users are unauthorized to call this endpoint. User account '{email}' from identity provider '{idp}' does not exist in tenant '{tenant}' and cannot access the application '{appid}'({appName}) in that tenant. This account needs to be added as an external user in the tenant first. Sign out and sign in again with a different Microsoft Entra user account. If this user should be a member of the tenant, they should be invited via theB2B system. For additional information, visitAADSTS50020.


## Troubleshooting Steps
**Error Code: AADSTS50020 - UserUnauthorized**

**Description:** Users are unauthorized to call this endpoint. User account '{email}' from identity provider '{idp}' does not exist in tenant '{tenant}' and cannot access the application '{appid}'({appName}) in that tenant. This account needs to be added as an external user in the tenant first. Sign out and sign in again with a different Microsoft Azure user account. If this user should be a member of the tenant, they should be invited via the B2B system.

**Initial Diagnostic Steps:**
1. Double-check the user account email provided in the error message.
2. Verify the identity provider (idp) mentioned in the error message.
3. Ensure the tenant (organization) mentioned in the error message.
4. Check the application ID (appid) and application name mentioned in the error message.

**Common Issues That Cause This Error:**
1. User account is not part of the specified tenant.
2. User account needs to be added as an external user to access the application.
3. User account might exist in a different tenant and not authorized to access the current application.
4. Incorrect configuration of the B2B system for inviting users to the tenant.

**Step-by-Step Resolution Strategies:**
1. **Check User Account and Tenant:** Verify that the user account '{email}' is intended to access the application '{appName}' in the specified tenant. If not, ensure the correct user account is being used.
   
2. **Add User as an External User:** If the user account needs to be added as an external user, follow these steps:
    - Go to Azure Active Directory in the Azure portal.
    - Select 'Users' and then 'New guest user'.
    - Add the user's email address and send the invitation.

3. **Sign Out and Sign In Again:** Sign out of the current Microsoft Azure user account and sign in again with a different account that has the necessary permissions to access the application.

4. **Invite via B2B System:** If the user should be a member of the tenant, invite them via the B2B system following the guidelines provided by Microsoft.
   
**Additional Notes or Considerations:**
- Ensure that the user account has the appropriate permissions and roles assigned within the Azure Active Directory.
- Verify the identity provider (idp) configuration and ensure it is correctly set up to authenticate users.
- Regularly monitor user access and permissions to prevent unauthorized access to resources.

**Documentation:**
For detailed guidance and official documentation on managing users and access in Azure Active Directory, refer to Microsoft Azure's official documentation: [Azure Active Directory Documentation](https://docs.microsoft.com/en-us/azure/active-directory/).