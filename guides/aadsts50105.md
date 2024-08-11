
# AADSTS50105: EntitlementGrantsNotFound - The signed in user isn't assigned to a role for the signed in app. Assign the user to the app. To learn more, see the troubleshooting article for errorAADSTS50105.


## Troubleshooting Steps
### Troubleshooting Guide: AADSTS50105 Error Code

#### Error Description:
AADSTS50105 - EntitlementGrantsNotFound: The signed-in user isn't assigned to a role for the signed-in app. Assign the user to the app.

#### Initial Diagnostic Steps:
1. **Confirm User Role Assignment:** Check if the user in question has been assigned a role within the application.
2. **Review App Permissions:** Verify the app's permissions and roles setup in Azure Active Directory (AAD).
3. **Check User Attributes:** Ensure that the user's attributes and profile data are correctly configured in AAD.

#### Common Issues:
1. **Role Assignment Missing:** The user may not have been assigned any role within the application.
2. **Incorrect App Configuration:** Misconfiguration of app roles and permissions in AAD could lead to this error.
3. **User Profile Mismatch:** Discrepancies in the user's profile stored in AAD can also cause this issue.

#### Step-by-Step Resolution Strategies:
1. **Assign Role to User:**
   - Go to Azure Portal and navigate to the application's settings.
   - Find the user that encountered the error and assign them the appropriate role.
  
2. **Verify App Permissions:**
   - Review the application's manifest in Azure AD to ensure that the correct roles are defined.
   - Check that the user's role assignment aligns with the app's permissions.

3. **Confirm User Attributes:**
   - Double-check the user's profile in Azure AD for any inconsistencies.
   - Make sure the required attributes for role assignment are properly set.

#### Additional Notes or Considerations:
- **User Confirmation:** Request the user to sign out and then sign in again to ensure the changes take effect.
- **Role Mapping:** Verify if the user's role aligns with the specific permissions required for the app.
- **Troubleshooting Tools:** Utilize Azure AD logs and diagnostic tools for further investigation if needed.

#### Documentation:
Microsoft Azure documentation provides detailed steps and guidance for troubleshooting AADSTS50105 errors.
- [Azure AD error code reference](https://docs.microsoft.com/en-us/azure/active-directory/develop/reply-url)
- [Troubleshooting AADSTS50105 error](https://docs.microsoft.com/en-us/azure/active-directory/develop/troubleshoot-errors)