# AADSTS80012: OnPremisePasswordValidationAccountLogonInvalidHours - The users attempted to log on outside of the allowed hours (this is specified in AD).


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS80012

#### Overview
The error code AADSTS80012 indicates that a user has attempted to log on outside of the allowed hours as specified in Active Directory (AD). This generally occurs in environment setups where user logon times are restricted based on organizational policy.

---

### Initial Diagnostic Steps
1. **Check Time Zone Settings**:
   - Verify the time zone settings on both client and server components (AD servers, Azure AD, and the logging in device).

2. **Review User Logon Hours**:
   - Check the allowed logon hours for the user in Active Directory Users and Computers (ADUC) by locating the user's properties and reviewing the Account tab.

3. **Local Time vs AD Time**:
   - Ensure that the local time for the user is within the allowed logon period as set in AD.

---

### Common Issues That Cause This Error
1. **User’s Allowed Hours**:
   - The user is legitimately trying to log on outside the allowed timeframe configured in AD.

2. **Incorrect User Time Settings**:
   - User’s local machine might have incorrect time or time zone settings leading to confusion about logon times.

3. **AD Replication Delays**:
   - Changes made to user accounts may take time to propagate across AD. Look for replication issues.

4. **Misconfigured Policies**:
   - Group policies or organizational settings may be misconfigured, leading to stricter logon hour policies than intended.

5. **Time Synchronization Issues**:
   - Ensure that all machines (users' and servers') are synchronized properly with a Network Time Protocol (NTP) server.

---

### Step-by-Step Resolution Strategies
1. **Verify User Logon Hours**:
   - Open **Active Directory Users and Computers**.
   - Find the user in question.
   - Right-click on the user and select **Properties**.
   - Check under the **Account** tab for **Logon Hours** and adjust if necessary.

2. **Correct Any Time Zone issues**:
   - On the user’s machine: Right-click the time in the system tray -> Adjust date/time -> Ensure correct time zone is selected.
   - On AD servers: Make sure NTP settings are correctly set to keep the server in sync with the correct time.

3. **Review AD Replication**:
   - Use the command `repadmin /replsum` in the command prompt on your Domain Controller to check the health and state of AD replication.
   - If issues are found, follow up on local Domain Controller replication processes.

4. **Test Logon Hours with Different User Account**:
   - Attempt to log in with another account during the time the error occurred to confirm if the issue is user-specific.

5. **Group Policy Review**:
   - Use **Group Policy Management** console to review any policies that might be affecting logon hours. Make necessary adjustments.

6. **Consult the Event Viewer**:
   - Open Event Viewer (Run -> `eventvwr.msc`).
   - Check under **Windows Logs** -> **Security** for any relevant warning or error messages when the user attempted to log in.

---

### Additional Notes or Considerations
- It is essential to communicate any changes with the user to prevent future confusion.
- Keep in mind that the user's logon hours affect their ability to access services in other parts of the organization.

---

### Documentation for Further Guidance
- [Manage User Account Properties in Active Directory](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/manage-user-account-properties-in-active-directory)
- [Active Directory Replication](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/ad-replication-overview)

---

### Advice for Data Collection
When troubleshooting this issue, be prepared to gather the following data:

1. **Event Viewer Logs**:
   - Focus on the Security and Application logs to track authentication failures and other related issues.

2. **Network Traces**:
   - Use tools like **NetTrace** or **Wireshark** to capture packets during logon attempts if applicable.

3. **Fiddler**:
   - If the user is accessing web-based applications, use Fiddler to capture HTTP/S requests and responses to and from the Azure AD endpoints.

4. **Log Gatherer**:
   - Consider using scripts or tools to collect logs automatically if multiple users are affected, to ease the analysis process.

This guide outlines the steps and considerations needed to troubleshoot AADSTS80012 effectively. By following these steps, you should be able to identify and resolve the underlying issue causing this logon error.