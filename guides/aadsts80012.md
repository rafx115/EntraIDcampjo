
# AADSTS80012: OnPremisePasswordValidationAccountLogonInvalidHours - The users attempted to log on outside of the allowed hours (this is specified in AD).


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS80012 - OnPremisePasswordValidationAccountLogonInvalidHours

The error code AADSTS80012 indicates that the user attempted to log on outside of the allowed hours defined in Active Directory (AD). This error is associated with enterprise environments where user access is restricted by time, likely for security or compliance purposes.

#### 1. Initial Diagnostic Steps
- **Verify User Accounts and Credentials**: Ensure that the user account that is encountering the issue is valid and that they are entering the correct password.
- **Check the Error Message**: Confirm the exact error code and message being received. Sometimes, slight variations in the error code can give clues to different underlying issues.
- **Determine the User's Time Zone**: Ascertain what time zone the user is in and cross-reference that with the allowed logon hours set in AD. 
- **Check Login Times**: Identify when the user attempted to log in and compare that against the allowed hours defined in AD.

#### 2. Common Issues That Cause This Error
- **Misconfigured Allowed Logon Hours**: The user may be attempting to log on during a period that is not permitted by the AD's configuration.
- **Daylight Saving Time or Time Zone Issues**: If the AD's allowed hours are not synced with the user's current local time, this can result in the error.
- **User Account Misconfiguration**: Issues with the account such as being disabled, locked out, or misconfigured may contribute to login issues, even if allowed hours seem correct.
- **Network Time Protocol (NTP) Sync Issues**: If the server and user devices are not properly syncing time, this could lead to discrepancies in determining allowed hours.

#### 3. Step-by-Step Resolution Strategies
1. **Review Allowed Logon Hours in AD**:
   - Open Active Directory Users and Computers.
   - Locate the user account and right-click to select "Properties".
   - Navigate to the "Account" tab and look for "Logon hours".
   - Confirm the configuration allows login during the time the user is attempting to access.

2. **Check User's Local Time**:
   - Verify the user’s device time.
   - Ensure the device is set to the correct time zone and has accurate time (manually set or automatic sync).

3. **Adjust Allowed Logon Hours if Necessary**:
   - If the user's logon times need adjusting:
     - In AD, update the "Logon hours" for the user as per organizational policies.
     - Ensure changes are adequately communicated to affected users.

4. **Verification of Account Status**:
   - Verify that the user account isn’t disabled or locked out.
   - Make any necessary adjustments if the account is not in good standing.

5. **Monitor NTP Configuration**:
   - Ensure that your domain controllers are properly syncing time with a trusted time source.
   - Command: `w32tm /query /status` can be used on domain controllers to check NTP status.

6. **Test Login**:
   - After adjustments, have the user try to log in again within the allowed hours.

#### 4. Additional Notes or Considerations
- Be aware that network latency or domain replication delays can sometimes cause temporary issues with account permissions. 
- Ensure that any changes made to AD permissions or settings are documented for future reference and auditing.
- Keep in mind that administrative tasks in AD might require sufficient privileges; ensure you have proper access rights.

#### 5. Documentation for Guidance
- Microsoft Documentation on **Active Directory User Account Management**: [Managing User Accounts](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/manage/user-management)
- Microsoft Documentation on **Troubleshooting AAD Integration Issues**: [Troubleshooting Azure Active Directory](https://docs.microsoft.com/en-us/azure/active-directory/hybrid/tshoot-connect-issues)

#### 6. Test Documentation Reachability
- Ensure the documentation links provided above are accessible by visiting them directly through a browser.

#### 7. Advice for Data Collection
- Gather details about the user’s attempted login times and any policies configured in AD.
- Document any error messages received by the user during the login attempt.
- If issues persist, consider collecting logs from the application or service the user is trying to access, as well as any relevant server or authentication logs from event viewers.