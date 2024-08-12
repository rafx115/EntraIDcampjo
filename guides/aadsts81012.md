# AADSTS81012: DesktopSsoMismatchBetweenTokenUpnAndChosenUpn - The user trying to sign in to Microsoft Entra ID is different from the user signed into the device.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS81012 Error

#### Error Description:
**Error Code:** AADSTS81012  
**Description:** DesktopSsoMismatchBetweenTokenUpnAndChosenUpn - The user trying to sign in to Microsoft Entra ID is different from the user signed into the device.

This error occurs when the user attempting to sign in to Microsoft Entra ID (Azure AD) is not the same as the authenticated user on the device. This typically manifests in environments where automatic silent sign-in is expected but is hindered by a user mismatch.

---

### Initial Diagnostic Steps
1. **Verify User Identity:**
   - Confirm that the user trying to sign in is indeed the one who is logged into the device.
   - Check the username and UPN (User Principal Name).

2. **Check Device Sign-in:**
   - Navigate to **Settings > Accounts > Your Info** and check that the account matches the account attempting to authenticate.

3. **Review Account Type:**
   - Ensure the logged-in user is indeed a part of the Azure AD tenant.

4. **Identify Authentication Method:**
   - Determine if the authentication is being done through a specific application, browser, or OS-level sign-in.

---

### Common Issues That Cause This Error
1. **Multiple User Accounts:**
   - Multiple accounts on the device can lead to confusion regarding which account is attempting to sign in.

2. **Cached Credentials:**
   - Cached or stored credentials in the device may not match the intended sign-in account.

3. **Policy Restrictions:**
   - Group policies or Conditional Access policies might complicate login scenarios if there are mismatches in UPNs.

4. **Profile Corruption:**
   - A corrupted user profile can lead to sign-in issues.

5. **Incorrect Device Registration:**
   - The device may not be properly registered with the correct user UPN.

---

### Step-by-Step Resolution Strategies
1. **Log Out of Conflicting Accounts:**
   - Ensure that all Microsoft accounts signed in to the device are logged out. Then attempt to sign in with the intended Azure AD account.

2. **Clear Cached Credentials:**
   - Go to the Credential Manager in Windows and remove any inherited or stored credentials related to Microsoft accounts.

3. **Verify Azure AD Join Status:**
   - Check if the device is properly joined to Azure AD. Navigate to **Settings > Accounts > Access work or school** and ensure the account is displayed correctly.

4. **Re-register the Device:**
   - If necessary, you can remove and re-add the device in Azure AD. 
     - Go to **Settings > Accounts > Access work or school**.
     - Disconnect from the Azure AD account, then reconnect.

5. **Adjust Group Policies:**
   - If applicable, review and adjust Group Policies related to user accounts and logins that might disrupt sign-in.

6. **Profile Repair or Creation:**
   - Consider creating a new user profile on the device to verify if the issue persists or repair the existing user profile.

---

### Additional Notes or Considerations
- **Updates:** Ensure that Windows and all applications related to Microsoft sign-in are updated to the latest versions.
- **Application Permissions:** If you are using a specific application, check if it needs permissions to access the identity of the user who is logged in.

---

### Documentation for Guidance
- [Microsoft Entra ID Overview](https://learn.microsoft.com/en-us/azure/active-directory/)
- [Resolve common sign-in issues for Azure Active Directory](https://learn.microsoft.com/en-us/azure/active-directory/user-help/user-help-sign-in-issues)
- [Windows 10 Troubleshooter for Azure AD Issues](https://learn.microsoft.com/en-us/troubleshoot/windows-client/deploy/troubleshoot-azure-ad-join)
- [Credential Manager in Windows](https://support.microsoft.com/en-us/help/12408/windows-10-manage-credentials)

---

### Advice for Data Collection
- **Event Viewer Logs:**
  - Collect logs from the Windows Event Viewer under **Applications and Services Logs > Microsoft > Windows > AAD**. Look for authentication-related errors or warnings.

- **Network Trace:**
  - Use tools like `netsh trace` or `Wireshark` to capture network packets to identify where the sign-in is failing.

- **Fiddler:**
  - Install and set up Fiddler to capture HTTP(s) traffic related to authentication requests. Examine the requests and responses for errors or mismatches.

- **Review Authentication Logs:**
  - Utilize Azure AD Sign-in logs in the Azure portal for additional insights on the sign-in attempt and check for any anomalies or insights.

By following these steps, you should be able to diagnose and resolve the AADSTS81012 error effectively.