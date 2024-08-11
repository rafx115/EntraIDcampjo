# AADSTS16000: InteractionRequired - User account '{EmailHidden}' from identity provider '{idp}' doesn't exist in tenant '{tenant}' and can't access the application '{appid}'({appName}) in that tenant. This account needs to be added as an external user in the tenant first. Sign out and sign in again with a different Microsoft Entra user account. This error is fairly common when you try to sign in to Microsoft Entra admin center by using personal Microsoft Account and no directory associated with it.


## Troubleshooting Steps
Certainly! The AADSTS16000 error occurs when a user attempts to access an application within a particular Microsoft Entra (formerly Azure Active Directory/AAD) tenant but the user account they are using does not exist within that tenant. Below is a detailed troubleshooting guide for this error.

### Troubleshooting Guide for AADSTS16000 Error

#### Initial Diagnostic Steps:
1. **Verify User Account Type**:
   - Check if the user account attempting to sign in is a personal Microsoft Account (MSA) or a work/school account associated with the specific tenant.
  
2. **Check the Directory Association**:
   - Ensure that there is a directory associated with the account. Personal Microsoft Accounts often lack access to organizational resources.

3. **Identify the Tenant**:
   - Confirm the tenant ID and ensure you are trying to access the correct tenant, particularly if the email or user account is associated with multiple tenants.

#### Common Issues Causing this Error:
1. **Account Type Misuse**:
   - Users attempting to access the tenant using a personal Microsoft Account instead of a corporate account.

2. **User Not Added to the Tenant**:
   - If the account is an organizational account, it may not have been invited or added directly to the specific tenant.

3. **Misconfiguration in Application Registration**:
   - There could be an issue with the application registration settings, preventing users from accessing it.

4. **Outdated Session**:
   - The user might be signed in with credentials from a previous session, which may conflict with the current login attempt.

#### Step-by-Step Resolution Strategies:
1. **Ensure Correct Account Usage**:
   - Sign out of the Microsoft Entra admin center and ensure you are signing in with the appropriate organizational account that belongs to the tenant.

2. **Invite the User as an External User**:
   - If the account belongs to an external user (e.g., a partner or contractor), perform the following:
     - Admins can add the user through the Azure portal:
       1. Navigate to the Azure Active Directory section.
       2. Click on "Users."
       3. Select "New guest user" (External User).
       4. Enter the email of the user and send the invitation.
   
3. **Use Different Account**:
   - If an organizational account is intended for access, ensure that any session issues are resolved and use an account that has been properly added to the tenant.

4. **Confirm Application Permissions**:
<<<<<<< HEAD:guides/Other/aadsts16000.md
   - Check if the application (identified by `{appid}`) has been configured to allow access to the users tenant and permissions have been granted.
=======
   - Check if the application (identified by `{appid}`) has been configured to allow access to the user�s tenant and permissions have been granted.
>>>>>>> 8ca1440664e61dbdf9b1aa83f352634474c59c2f:guides/aadsts16000.md

5. **Clear Cache and Cookies**:
   - Users can sign out, clear their browser's cache and cookies, and attempt to sign in again to eliminate session-related conflicts.

#### Additional Notes or Considerations:
- In some cases, users may need to wait for the external invitation email and accept it before they can access resources in the tenant.
- It is also recommended to ensure that email filtering does not block the invitation email.

#### Documentation for Guidance:
- Add Users to your Azure AD tenant: [Microsoft Docs](https://docs.microsoft.com/en-us/azure/active-directory/users/groups/assign-group-roles)
- Change account settings: [Microsoft Docs](https://support.microsoft.com/en-us/account-billing/manage-your-microsoft-account-bad5b3ce-2a45-6e1d-b71b-e1d52705196e)
  
#### Test Accessibility of Documentation:
- Utilize a web browser to navigate to the provided links to ensure they are reachable and up-to-date.

#### Advice for Data Collection:
- Keep a record of the user's attempts, including the email address used, the time of the attempt, and any messages received.
- Collect screenshots of the error message and any relevant logs if available to assist in a deeper investigation if needed.

This guide should aid in addressing the AADSTS16000 error efficiently, helping users to resolve access issues to Microsoft Entra resources within specific tenant configurations.

Category: Other