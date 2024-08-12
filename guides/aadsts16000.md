# AADSTS16000: InteractionRequired - User account '{EmailHidden}' from identity provider '{idp}' doesn't exist in tenant '{tenant}' and can't access the application '{appid}'({appName}) in that tenant. This account needs to be added as an external user in the tenant first. Sign out and sign in again with a different Microsoft Entra user account. This error is fairly common when you try to sign in to Microsoft Entra admin center by using personal Microsoft Account and no directory associated with it.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS16000

**Error Code:** AADSTS16000  
**Description:** InteractionRequired - User account '{EmailHidden}' from identity provider '{idp}' doesn't exist in tenant '{tenant}' and can't access the application '{appid}'({appName}) in that tenant. This account needs to be added as an external user in the tenant first. Sign out and sign in again with a different Microsoft Entra user account.

---

#### Initial Diagnostic Steps

1. **Identify the User and Account Information**
   - Confirm the email address being used for login.
   - Check whether the email address is a personal Microsoft account or a work/school account.

2. **Check Tenant Configuration**
   - Verify the Azure Active Directory (Azure AD) tenant settings.
   - Ensure you have valid access to the Azure AD tenant associated with the application.

3. **Application Permissions**
   - Review the application permissions in Azure AD to verify what accounts are allowed to access the application.

---

#### Common Issues That Cause This Error

1. **Wrong Account Type**
   - Users attempting to log in with a personal Microsoft Account (e.g., `@hotmail.com`, `@outlook.com`) instead of an organizational account.

2. **User Not Added**
   - The user account is not registered or added as an external guest user in the Azure AD tenant.

3. **Directory Associations**
   - The user’s Microsoft account is not associated with the Azure AD directory either because it hasn't been invited or it has not been accepted.

---

#### Step-by-Step Resolution Strategies

1. **Log Out and Use the Correct Account**
   - Sign out of all Microsoft accounts.
   - Log in using the correct organizational account (work/school) associated with the Azure AD tenant.

2. **Add the User as an External Guest**
   If the user needs access and is using a personal Microsoft Account:
   - An admin can invite the user as a guest:
     1. Sign in to the Azure portal).
     2. Navigate to Microsoft Entra (Azure Active Directory) > Users > New guest user.
     3. Provide the email address of the user and fill out the necessary fields.
     4. Click on "Invite" after completing the form.
   
3. **Accept Invite**
   - Once invited, the user should check their email for the invitation link. They must accept the invitation to gain access.

4. **Directory Settings**
   - Ensure that the tenant configuration allows external guests if that’s the route chosen.

5. **Review App Registration**
   - If issues persist, ensure that the application is properly configured to allow guest users:
     1. Navigate to Azure Active Directory > App registrations.
     2. Select the application, and review the User assignment (if applicable) under "Authentication".
     3. Make sure the application is set up to allow users to self-assign if needed.

---

#### Additional Notes or Considerations

- Ensure to handle permissions and access levels with care, especially when adding external guests.
- Use the Azure AD Access Reviews for periodic checks on user's access and permissions.
- Double-check any conditional access policies that might inadvertently block access.

---

#### Documentation Where Steps Can Be Found

- [Microsoft Entra (Azure AD) Documentation](https://docs.microsoft.com/en-us/azure/active-directory/)
- [How to add users to Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/users/users-assign-roles)
- [How to invite external users to Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/b2b/add-users-portal)
- [Azure AD Application Permissions](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-app-permissions)

---

#### Advice for Data Collection (Event Viewer, NetTrace, Fiddler)

If troubleshooting does not resolve the issue:

- **Event Viewer Logs**
  - Check the Application and Service Logs on Windows for any related application errors while trying to authenticate.

- **NetTrace**
  - Capture network traces to identify request-response issues during authentication. Use tools like Wireshark or Fiddler.

- **Fiddler**
  - Use Fiddler to capture the HTTP(S) requests during the sign-in attempt. Look for any failed requests or errors returned by the Azure AD endpoint.

By following these guidelines, you should be able to resolve or identify the cause of the error AADSTS16000 effectively.