# AADSTS51004: UserAccountNotInDirectory - The user account doesn�t exist in the directory. An application likely chose the wrong tenant to sign into, and the currently logged in user was prevented from doing so since they did not exist in your tenant. If this user should be able to log in, add them as a guest. For further information, please visitadd B2B users.


## Troubleshooting Steps
### Error Code: AADSTS51004 - UserAccountNotInDirectory

#### Initial Diagnostic Steps:
1. **Confirm the User's Existence**: Verify that the user account does not exist in the specific directory where the application is attempting to sign in.
2. **Check Tenant and User Account Association**: Ensure that the user should indeed have access and check the tenant association where the user should be added.

#### Common Issues:
- Application choosing the wrong tenant to sign into.
- User not existing in the directory the application is attempting to sign in.
- Failure to properly invite the user as a guest if they should have access.

#### Step-by-step Resolution Strategies:
1. **Check Application Configuration**:
   - Confirm that the correct tenant is configured within the application settings.
   - Ensure that the correct directory is selected for user authentication.

2. **Manually Add User as a Guest**:
   - If the user should have access, add them as a guest user in your directory:
     - Invite the user through Azure Active Directory as a guest user.
     - Grant the necessary permissions to the guest user within your tenant.

3. **User Verification**:
   - Verify the user email address to ensure that it corresponds to the correct user account.
   - Confirm the user's presence in the expected directory.

4. **Check Azure B2B Users**:
   - If the user is an external guest user, verify the guest user invitation and acceptance status in Azure B2B settings.

#### Additional Notes or Considerations:
- **Directory Relationship**: Validate the relationship between directories, especially if dealing with guest users from external organizations.
- **Permissions and Role Assignment**: Ensure the user has the appropriate roles and permissions assigned within the directory to access the application.
- **Logging and Monitoring**: Monitor sign-in logs for additional insights into the error and user activities.

#### Documentation for Guidance:
- For more detailed steps and information, refer to Microsoft's official documentation on resolving Azure AD authentication errors: [Troubleshoot user and service principal sign-in errors with Azure Active Directory](https://docs.microsoft.com/en-us/azure/active-directory/reports-monitoring/reference-reports-errors)