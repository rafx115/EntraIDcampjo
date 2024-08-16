# AADSTS50020: UserUnauthorized - Users are unauthorized to call this endpoint. User account '{email}' from identity provider '{idp}' does not exist in tenant '{tenant}' and cannot access the application '{appid}'({appName}) in that tenant. This account needs to be added as an external user in the tenant first. Sign out and sign in again with a different Microsoft Entra user account. If this user should be a member of the tenant, they should be invited via theB2B system. For additional information, visitAADSTS50020.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS50020

**Error Description:**   
"UserUnauthorized - Users are unauthorized to call this endpoint. User account '{email}' from identity provider '{idp}' does not exist in tenant '{tenant}' and cannot access the application '{appid}'({appName}) in that tenant. This account needs to be added as an external user in the tenant first. Sign out and sign in again with a different Microsoft Entra user account. If this user should be a member of the tenant, they should be invited via the B2B system. For additional information, visit AADSTS50020."

### Initial Diagnostic Steps

1. **Identify the User's Email and Identity Provider:**  
   Record the user account details (email, idp).
   
2. **Check Tenant Information:**  
   Confirm which Azure AD tenant the application is associated with.

3. **Review Application Permissions:**  
   Verify the permissions required for the application to which access is being attempted.

4. **Authenticate the User:**
   Ensure the user is attempting to log in through the correct identity provider.

### Common Issues That Cause This Error

1. **User Not Invited as External User:**  
   The user attempting to access the application has not been added to the Azure AD tenant as an external user.

2. **Incorrect Azure AD Tenant:**  
   The application is attempting to access a different Azure AD tenant than the one the user is assigned to.

3. **B2B Configuration Issues:**  
   Misconfiguration of B2B collaboration settings within the Azure AD.

4. **Sign-In with Wrong Account:**  
   The user is logged in with a Microsoft account that is not part of the tenant or application.

### Step-by-Step Resolution Strategies

1. **Add the User as an External User:**
   - **For Admins:**
     1. Sign in to the Azure portal: [Azure Portal](https://portal.azure.com).
     2. Navigate to "Azure Active Directory".
     3. Click on "Users" and then "New guest user".
     4. Enter the user’s email, set their role if applicable, and invite them.
   - **For Users:**
     - Request an admin to add you as a guest user if you're unable to do this yourself.

2. **Verify Correct Identity Provider:**
   - Ensure you're logging in with the correct account that is allowed access.
   - Consider signing out from all Microsoft accounts and signing back in with the intended account.

3. **Check Application Registration:**
   - Navigate to “Azure Active Directory” > “App registrations” and select the application.
   - Ensure that it has the correct permissions set and that it’s configured for guest sign-in if applicable.

4. **Review B2B Collaboration Settings:**
   - Go to Azure Active Directory > External Identities > External collaboration settings.
   - Ensure that your settings allow guest users to sign in.

5. **Use Azure AD Graph to Check User Status:**
   - Use PowerShell or Azure CLI to confirm the user’s status within the tenant.

### Additional Notes or Considerations

- Ensure compliance with your organization's policy on adding external users.
- Check if the user is in a suspended state or if there are policies affecting their sign-in.
- Consider any conditional access policies that might apply to the user's location or device.

### Documentation Where Steps Can Be Found for Guidance

1. [Add a guest user in Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/external-identities/what-is-identity-b2b)
2. [Azure AD B2B collaboration](https://docs.microsoft.com/en-us/azure/active-directory/external-identities/what-is-b2b)
3. [Manage user roles and permissions](https://docs.microsoft.com/en-us/azure/active-directory/roles/permissions-reference)

### Advice for Data Collection (Event Viewer Logs, Nettrace, Fiddler)

1. **Event Viewer:**
   - Check the Application logs under “Windows Logs” in Event Viewer for any errors related to authentication during login.

2. **Network Monitoring:**
   - Use tools like Fiddler to monitor HTTP(S) requests/responses, especially during the login process to capture potential issues.

3. **Azure AD Logs:**
   - In the Azure portal, navigate to Azure Active Directory > Sign-ins to see the details of failed sign-ins, which may provide more insights.

4. **Nettracing:**
   - If facing issues in a .NET application, consider capturing a network trace with tools like Wireshark or Netsh to inspect the authentication requests.

By following this guide, you should be able to diagnose and resolve the AADSTS50020 error effectively.