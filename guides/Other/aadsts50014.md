# AADSTS50014: GuestUserInPendingState - The user account doesnï¿½t exist in the directory. An application likely chose the wrong tenant to sign into, and the currently logged in user was prevented from doing so since they didn't exist in your tenant. If this user should be able to sign in, add them as a guest. For further information, please visitadd B2B users.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS50014: GuestUserInPendingState

The AADSTS50014 error indicates that the user, trying to access an application, is currently in a "pending" state indicating that their account does not exist in the directory of the tenant being accessed. Below is a structured troubleshooting guide to help resolve this issue.

#### Initial Diagnostic Steps

1. **Verify User Identity**: Confirm the identity of the user trying to access the application and make sure they are using the correct email address and credentials.
   
2. **Check Tenant Configuration**: Identify which tenant the user is trying to log into. This can be done by examining the application settings or by discussing with the application owner.

3. **Review Error Details**: Read the full error message provided by Azure AD to gather additional context regarding the specific user and the issue.

#### Common Issues That Cause This Error

1. **User Not Invited**: The user might not have been invited to the tenant, which is the most common cause of this error. 
   
2. **Pending Invitation**: The user may have received an invitation to join the tenant but has not yet accepted it.

3. **Wrong Tenant**: The user might be attempting to access a different tenant where they do not have permissions or credentials.

4. **Inactive Guest Status**: The user could be in a state where their guest access has been suspended or deactivated.

5. **Application Misconfiguration**: The application might be misconfigured to point to an incorrect Azure AD tenant.

#### Step-by-Step Resolution Strategies

1. **Confirm User Invitation Status**:
   - Log into Azure AD portal: [Azure Portal](https://portal.azure.com/)
   - Navigate to **Azure Active Directory** > **Users** > **Pending Invitations**.
   - Check if the user's email appears here. If it does, remind the user to check their email and accept the invitation.

2. **Invite the User as a Guest**:
   - If the user is not in the Pending Invitations, invite them as a guest:
     - Go to **Azure Active Directory** > **Users** > **New guest user**.
     - Enter the user's email and send the invitation.
   - Make sure to notify the user to accept the invitation after it has been sent.

3. **Check User Account Status**:
   - After inviting the user, return to the Users list in Azure AD and ensure that the user account shows as active.

4. **Tenant Verification**:
   - Ensure that the user is trying to access the correct tenant. Verify the tenant ID or domain being used does match the one where the user is invited.

5. **Consult the Application Owner**: 
   - If the issue remains unresolved, contact the application owner to ensure that the application is correctly configured for the intended tenant.

#### Additional Notes or Considerations

- **Invite Resend**: If the invitation has expired (invitations expire after 7 days), you may need to resend it.
- **Multi-Tenant Applications**: Sometimes applications require specific configurations for multi-tenancy; work closely with the app developers if this is the case.

#### Documentation for Further Guidance

- Learn more about inviting and managing guest users in Azure AD: 
  - [Understanding Azure AD B2B](https://docs.microsoft.com/en-us/azure/active-directory/external-identities/what-is-b2b)
  - [Add Guest Users to Azure Active Directory](https://docs.microsoft.com/en-us/azure/active-directory/external-identities/add-users-b2b).
  
- For troubleshooting Azure AD sign-in errors:
<<<<<<< HEAD:guides/Other/aadsts50014.md
  - [Sign-in Troubleshoot](https://docs.microsoft.com/en-us/azure/active-directory/enterprise-users/groups/groups-manageusers).
=======
  - [Sign-in Troubleshoot](https://docs.microsoft.com/en-us/azure/active-directory/enterprise-users/groups/groups-manage�users).
>>>>>>> 8ca1440664e61dbdf9b1aa83f352634474c59c2f:guides/aadsts50014.md

#### Test Accessibility of Documentation

To ensure the documentation links are accessible:
- Click on each link and verify they load properly in your web browser.
  
#### Advice for Data Collection

<<<<<<< HEAD:guides/Other/aadsts50014.md
- **Collect User Information**: Gather the users relevant information such as email address and the tenant they are trying to access.
- **Error Logs**: Collect any detailed error logs or screenshots related to the users sign-in attempts.
=======
- **Collect User Information**: Gather the user�s relevant information such as email address and the tenant they are trying to access.
- **Error Logs**: Collect any detailed error logs or screenshots related to the user�s sign-in attempts.
>>>>>>> 8ca1440664e61dbdf9b1aa83f352634474c59c2f:guides/aadsts50014.md
- **Time of Occurrence**: Note the time of the error occurrence, as this may help in diagnosing the issue further with support if necessary.

Using this guide, you should be well-equipped to troubleshoot and resolve the AADSTS50014 error effectively.

Category: Other