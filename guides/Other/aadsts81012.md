# AADSTS81012: DesktopSsoMismatchBetweenTokenUpnAndChosenUpn - The user trying to sign in to Microsoft Entra ID is different from the user signed into the device.


## Troubleshooting Steps
## Troubleshooting Guide for AADSTS81012 Error

### Error Description
The error code **AADSTS81012** indicates a mismatch between the user signing into a Microsoft Entra ID (formerly Azure Active Directory) account and the user currently signed into the device. More specifically, it suggests that there is a conflict between the user principal name (UPN) of the authenticated user on the device and the one expected by the authentication service.

### Initial Diagnostic Steps
1. **Identify the User Accounts:**
   - Check the account details of the user who is attempting to sign in. Specifically, verify the UPN (e.g., user@domain.com).
   - Check the account details of the user currently logged into the Windows device.

2. **Review Sign-in Method:**
   - Determine if the user is attempting to sign in via:
     - Microsoft Office applications
     - Windows sign-in
     - Microsoft Teams or other services

3. **Check User Permissions:**
   - Confirm that the user has the necessary permissions to access the application or service.

### Common Issues Causing This Error
- User logged into the PC with a different Microsoft Entra ID account than the one trying to access the application.
- Cached credentials or sessions that might contain stale or incorrect user information.
- Domain synchronization issues in a corporate environment, especially for users in on-premises Active Directory.

### Step-by-Step Resolution Strategies

#### Step 1: Verify User Accounts
- **Action:** Ensure that the UPN of the user attempting to sign in matches the user logged into the device.
- **Solution:** Sign out the current user and sign in with the account that matches the UPN needed for the application.

#### Step 2: Clear Cached Credentials
- **Action:** Clear any saved credentials that might lead to mismatched logins.
- **Solution:**
  - Open **Control Panel** > **User Accounts** > **Credential Manager**.
  - Remove any existing Microsoft Entra ID or Office 365 credentials.
  - Restart the application and attempt to sign in again.

#### Step 3: Check Microsoft Account Settings
- **Action:** Ensure that the settings on the device allow access to the application.
- **Solution:**
  - Open **Settings** > **Accounts**.
  - Confirm that the Microsoft account shown matches what is required.

#### Step 4: Check for Group Policy Settings (For Domain-Renamed Users)
- **Action:** If you're using a domain environment, check Group Policy for account restrictions.
- **Solution:** Consult with your IT administrator to review any Group Policy Object (GPO) settings that might restrict access.

#### Step 5: Test with Different Applications
- **Action:** Attempt to access different Microsoft applications.
- **Solution:** This can help determine if the issue is specific to a single service or application.

#### Step 6: Reinstall Applications (if necessary)
- **Action:** If clearing cached credentials doesn’t work, consider reinstalling the affected applications (e.g., Office).
- **Solution:**
  - Uninstall the application from **Settings** > **Apps** and then reinstall.

### Additional Notes or Considerations
- Ensure that your device is up to date with the latest Windows updates and patches.
- For organizations with hybrid setups, verify that the Azure AD Connect synchronization is functioning correctly.
- If the user needs to switch accounts frequently, consider using an incognito mode when accessing applications via a browser to avoid cached credentials.

### Documentation Links
For detailed instructions and further reading, you can refer to the following Microsoft documentation:
- [Troubleshooting errors in Microsoft Entra ID](https://docs.microsoft.com/en-us/azure/active-directory/develop/troubleshoot-authentication)
- [How to clear cached credentials](https://support.microsoft.com/en-us/windows/manage-credentials-in-windows-10-94f62d7e-98e4-63fc-e9b7-e74798f54c50)
- [Azure AD Connect: Troubleshooting Synchronization](https://docs.microsoft.com/en-us/azure/active-directory/hybrid/tshoot-connect-sync)

**Test Documentation Reachability:**
- Ensure the links provided above lead to live pages. This can be done by clicking each link and checking that they load properly.

### Advice for Data Collection
- Collect detailed logs around the sign-in attempt, including timestamps and any relevant error messages displayed.
- Use Azure AD Sign-in logs in the Azure portal to gain insights into authentication attempts (available at `Azure Active Directory > Sign-ins`).

By following this troubleshooting guide, you can effectively address AADSTS81012 error and help users successfully sign into Microsoft Entra ID.

Category: Other