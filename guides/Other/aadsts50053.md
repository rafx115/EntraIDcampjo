# AADSTS50053: This error can result from two different reasons:IdsLocked - The account is locked because the user tried to sign in too many times with an incorrect user ID or password. The user is blocked due to repeated sign-in attempts. SeeRemediate risks and unblock users.Or, sign-in was blocked because it came from an IP address with malicious activity.To determine which failure reason caused this error, sign in to theMicrosoft Entra admin centeras at least aCloud Application Administrator.  Navigate to your Microsoft Entra tenant and thenMonitoring & health->Sign-in logs.  Find the failed user sign-in withSign-in error code50053 and check theFailure reason.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS50053 Error Code

#### Introduction
The AADSTS50053 error code indicates that a user's sign-in attempt was unsuccessful, either due to account lockout following multiple failed attempts or because the sign-in attempted came from an IP address associated with malicious activity. This guide will help you troubleshoot and resolve the issue.

---

### Initial Diagnostic Steps
1. **Identify the User**: Determine which user is facing the issue and gather relevant details, such as their username and any recent sign-in attempts.
2. **Access the Microsoft Entra Admin Center**: 
   - Log in to the [Microsoft Entra admin center](https://entra.microsoft.com) with an account that has at least Cloud Application Administrator permissions.
3. **Review Sign-in Logs**:
   - Navigate to **Monitoring & health** > **Sign-in logs**.
   - Filter for the failed sign-in attempts corresponding to the specific user and note the error code (50053) and the associated failure reason.

---

### Common Issues that Cause this Error
1. **Account Lockout**: The user may have entered incorrect credentials multiple times, leading to a lockout.
2. **Blocked IP Address**: The IP address from which the user is trying to sign in may have been flagged due to suspicious or malicious activity.
3. **User Configuration**: User account configurations such as Conditional Access Policies or Identity Protection results may restrict sign-ins.

---

### Step-by-Step Resolution Strategies

#### **If Account is Locked (IdsLocked)**
1. **Locate the Account Status**: In the sign-in logs, confirm the failure reason indicates "IdsLocked".
2. **Unblock the Account**:
   - Navigate to **Users** > **All users** in the Microsoft Entra admin center.
   - Locate the affected user and select the account.
   - Under the account settings, select **Unlock account** or reset the password if necessary.
3. **Inform the User**: Let the user know their account has been unlocked and provide guidance on creating a strong password.

#### **If Sign-in is Blocked from a Malicious IP**
1. **Identify IP Information**: Check if the failure reason indicates the block is based on the IP address.
2. **Investigate with IP Lookup**:
   - Use a service to look up the IP and check if it has been flagged or reported for malicious activity.
3. **Allow Access if Safe**:
   - If the IP is confirmed as safe, you may consider reviewing and potentially whitelisting the IP address in your Conditional Access policies.
4. **Inform the User**: Advise the user on identifying their IP address and suggesting they attempt to sign in using a different, known-safe network.

---

### Additional Notes or Considerations
- **Rate Limiting**: Ensure users are aware of the number of allowed sign-in attempts to prevent lockouts.
- **Multi-factor Authentication (MFA)**: Encourage users to enable MFA to enhance security.
- **Monitoring and Maintenance**: Regularly check sign-in logs for patterns of lockouts or suspicious activity.

---

### Documentation for Further Guidance
- [Microsoft Entra Admin Center documentation](https://learn.microsoft.com/en-us/azure/active-directory/enterprise-users/groups/group-admin-overview)
- [Sign-in logs in the Entra Admin Center](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/security-reports)
- [How to unblock a user account](https://learn.microsoft.com/en-us/azure/active-directory/user-help/user-help-unblock-account)

#### Test Document Reachability
Make sure the links provided above direct you to valid Microsoft documentation when accessed in your browser.

---

### Advice for Data Collection
- **Gather Logs**: Collect sign-in logs and any error codes displayed during the sign-in attempts.
- **User Feedback**: Document specific times and dates of failed sign-in attempts for context.
- **OneDrive for Business**: If applicable, check for any related alerts or user activity in OneDrive or SharePoint.

By following these steps, you should be able to diagnose and resolve the AADSTS50053 error effectively. If the problem persists, consider reaching out to Microsoft Support for additional assistance.

Category: Other