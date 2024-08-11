# AADSTS50020: UserUnauthorized - Users are unauthorized to call this endpoint. User account '{email}' from identity provider '{idp}' does not exist in tenant '{tenant}' and cannot access the application '{appid}'({appName}) in that tenant. This account needs to be added as an external user in the tenant first. Sign out and sign in again with a different Microsoft Entra user account. If this user should be a member of the tenant, they should be invited via theB2B system. For additional information, visitAADSTS50020.


## Troubleshooting Steps
Certainly! The error code AADSTS50020 refers to an unauthorized access attempt where a user account does not exist in the specified Azure Active Directory (Azure AD) tenant. Below is a detailed troubleshooting guide designed to help resolve this issue.

### Detailed Troubleshooting Guide for AADSTS50020 Error Code

#### **Initial Diagnostic Steps**
1. **Identify User Account**: Confirm the user account from the error message (e.g., `'{email}'`). This email is the account attempting to access the application.
2. **Check Tenant and App Details**: Note the tenant ID `'{tenant}'` and application ID `'{appid}'`, along with the application name `'{appName}'`.
3. **Determine Identity Provider (IdP)**: Identify the identity provider denoted by `'{idp}'`. This could be an external provider such as Microsoft, Google, etc.
4. **Access Attempt Context**: Understand the context in which the user is trying to access the application (e.g., direct login to the application, through a service, etc.).

#### **Common Issues that Cause AADSTS50020**
- The user account attempting to log in is not registered in the Azure AD tenant.
- The user account is external (guest) and has not been invited into the tenant via the B2B collaboration feature.
- The application is configured to only allow specific user types, and the current user does not meet those criteria.
- There may be a mismatch or misconfiguration regarding the identity provider.

#### **Step-by-Step Resolution Strategies**
<<<<<<< HEAD:guides/Other/aadsts50020.md
1. **Check Users Existence in the Tenant**:
   - Log in to the Azure Portal.
   - Navigate to **Azure Active Directory** > **Users**.
   - Search for the users email. If not found, the user needs to be invited.
=======
1. **Check User�s Existence in the Tenant**:
   - Log in to the Azure Portal.
   - Navigate to **Azure Active Directory** > **Users**.
   - Search for the user�s email. If not found, the user needs to be invited.
>>>>>>> 8ca1440664e61dbdf9b1aa83f352634474c59c2f:guides/aadsts50020.md

2. **Invite User as an External User (if applicable)**:
   - If the user is external, go to **Azure Active Directory** > **Users**.
   - Click on **New guest user**.
   - Enter the user's email and provide a personalized message, if desired.
   - Click **Invite**.

3. **Assign Application Access**:
   - After inviting the user, ensure that the user is assigned to the application:
     - Navigate to **Azure Active Directory** > **Enterprise Applications**.
     - Select the application `'{appName}'`.
     - Go to **Users and groups**, and add the new user if necessary.

4. **User Account Type and Role Verification**:
   - Verify that the user account type (member or guest) meets the application requirement. If the application does not accept guest accounts, update the settings accordingly.
   - Ensure the user has the appropriate roles if role-based access is implemented.

5. **User Re-login**:
   - Once the above steps are completed, instruct the user to sign out and sign back in.
   - Verify the access to the application.

#### **Additional Notes or Considerations**
- Make sure to check the tenant settings to ensure guest access is enabled if the user is an external party.
- Review the application settings and the manifest to check access policies and restrictions regarding user assignments.
- Ensure that the application is configured correctly in terms of redirect URIs and permissions.

#### **Documentation for Guidance**
- Azure AD User Management: [Manage Users in Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/users/users)
- Azure AD B2B Collaboration: [B2B Collaboration Overview](https://docs.microsoft.com/en-us/azure/active-directory/external-identities/what-is-b2b)
- Azure AD Application Management: [Manage Azure AD Applications](https://docs.microsoft.com/en-us/azure/active-directory/develop/app-management)

#### **Test Document Reachability**
- Visit the above links to verify they are functional and contain the necessary information.
- If the links result in a 404 error or are unreachable, check the Microsoft documentation home page for updates or changes.

#### **Advice for Data Collection**
- Gather information about the user's login attempts, such as timestamps and error messages.
- Collect screenshots, if possible, highlighting the error to clarify the issue.
- Note any recent changes made in the Azure AD tenant or application configuration that may have led to the issue.

### Conclusion
Following this detailed guide should help resolve the AADSTS50020 error code. By systematically investigating user account statuses, application permissions, and ensuring proper external user processes, you can meet the access needs for your users effectively.

Category: Other