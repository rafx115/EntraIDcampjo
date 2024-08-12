# AADSTS51004: UserAccountNotInDirectory - The user account doesn’t exist in the directory. An application likely chose the wrong tenant to sign into, and the currently logged in user was prevented from doing so since they did not exist in your tenant. If this user should be able to log in, add them as a guest. For further information, please visitadd B2B users.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS51004: UserAccountNotInDirectory

#### Initial Diagnostic Steps
1. **Verify User Account Existence**: Check if the user account mentioned in the error is part of your Azure Active Directory (AAD) tenant. You can do this by logging into the Azure portal and navigating to Azure Active Directory > Users.
2. **Check Tenant Information**: Confirm that the user is trying to authenticate against the correct tenant. The tenant ID and the domain name should match the expected configuration for your application.
3. **Identify the Application**: Determine which application the user is trying to access and the type of authentication flow being utilized.
4. **Notice Error Context**: If practical, gather contextual information about when and where the error is occurring (e.g., app type, platform, etc.).

#### Common Issues that Cause This Error
- **User Not in Tenant**: The most common reason is that the user does not exist in the directory.
- **Wrong Tenant Selection**: The user might be attempting to sign into the wrong Azure tenant.
- **Not Invited as Guest User**: If the user is from a different organization, they may need to be invited as a guest user.
- **Account State**: The user account could be disabled, deleted, or unverified.
- **Incorrect Application Setup**: Configuration issues with the application like misconfigured redirect URIs or incorrect tenant information.

#### Step-by-Step Resolution Strategies
1. **Check User Account**:
   - In your Azure AD portal, go to **Users** and search for the user's email.
   - If the user is not listed, they need to be added.

2. **Add User as Guest (if applicable)**:
   - If the user is external (part of another organization), navigate to **Azure Active Directory > Users > New guest user**.
   - Fill in the user’s email, select an invitation type, and follow the prompts to invite them.

3. **Confirm Tenant Information**:
   - Ensure that the user is signing in using the correct tenants' domain. The domain can be specified in the login URL.
   - Verify that the application is configured to allow users from the intended tenant.

4. **Application Configuration**:
   - Navigate to the application registration in Azure AD.
   - Ensure that the `Redirect URIs` and `Application (client) ID` configurations are correct.
   - Check API permissions if the application is using them.

5. **Account State Check**:
   - Verify the user account’s status (enabled/disabled) by viewing the user properties in the Azure AD portal.

6. **Testing**:
   - After making changes, ask the user to attempt to log in again and verify if the problem is resolved.

#### Additional Notes or Considerations
- **Multi-Tenant Applications**: If the application is intended to be multi-tenant, ensure that it is set up correctly to accept users from external tenants.
- **Guest User Policies**: Understand your Azure AD’s policies regarding guest users, as they can prevent effective collaboration across organizations.
- **User Invitations**: Invitations sent to users may take time to arrive; make sure they check their inbox, including spam or junk folders.

#### Documentation for Guidance
- [Azure AD: Add guest users](https://docs.microsoft.com/en-us/azure/active-directory/external-identities/what-is-b2b) 
- [Application registration in Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)
- [Managing User Accounts](https://docs.microsoft.com/en-us/azure/active-directory/user-help/user-help-accounts)

#### Data Collection for Troubleshooting
- **Event Viewer Logs**: Check for application logs related to the authentication to gather details about the error.
- **Network Tracing**: Use tools like **Fiddler** or **Network Tracing** in your browser’s developer tools to capture network requests and responses during authentication. Look specifically for failures in HTTP status codes or detailed error messages.
- **Inspecting Azure Logs**: Review Azure AD sign-in logs under Azure Active Directory > Sign-ins for detailed logs on user sign-in attempts and any errors that occurred.

By following this structured troubleshooting guide, you should be able to diagnose and resolve the AADSTS51004 error effectively.