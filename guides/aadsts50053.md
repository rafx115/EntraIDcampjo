
# AADSTS50053: This error can result from two different reasons:IdsLocked - The account is locked because the user tried to sign in too many times with an incorrect user ID or password. The user is blocked due to repeated sign-in attempts. SeeRemediate risks and unblock users.Or, sign-in was blocked because it came from an IP address with malicious activity.To determine which failure reason caused this error, sign in to theMicrosoft Entra admin centeras at least aCloud Application Administrator.  Navigate to your Microsoft Entra tenant and thenMonitoring & health->Sign-in logs.  Find the failed user sign-in withSign-in error code50053 and check theFailure reason.


## Troubleshooting Steps
Here's a comprehensive troubleshooting guide for the error code AADSTS50053, including diagnostic steps, common issues, resolution strategies, additional notes, documentation, and advice for data collection:

### AADSTS50053 Troubleshooting Guide

#### Overview of the Error
Error code AADSTS50053 indicates that the sign-in was blocked for one of two reasons:
1. The user account is locked due to too many incorrect sign-in attempts (IdsLocked).
2. The sign-in was blocked from an IP address recognized for malicious activity.

---

### Initial Diagnostic Steps
1. **Review the Error Message**: Understand the nature of the error as described in the message.
2. **Sign-in Attempt Confirmation**: Confirm if the user has received notifications about account lockout or sign-in failures.
3. **Access the Microsoft Entra Admin Center**: Ensure you have the required role (at least Cloud Application Administrator) to view sign-in logs.

---

### Common Issues That Cause this Error
- **Incorrect Credentials**: Users may be entering incorrect usernames or passwords repeatedly.
- **Account Lockout Policy**: Many organizations enforce an account lockout policy after a specified number of failed login attempts.
- **High-Risk IP Address**: The log may indicate the user's sign-in was from an IP address flagged for suspicious activity.
- **User Behavior**: Users may have tried to sign in from various locations/devices incorrectly.

---

### Step-by-Step Resolution Strategies
#### Step 1: Access the Sign-in Logs
1. Log in to the **Microsoft Entra admin center**.
2. Navigate to **Monitoring & health** > **Sign-in logs**.
3. Filter the logs by the user facing the issue and search for the error code **50053**.

#### Step 2: Identify the Failure Reason
- Look for the **Failure Reason** field in the sign-in logs for the specific entry corresponding to the user. This will indicate if the issue was due to the account being locked or a blocked IP address.

#### Step 3: If Account is Locked
1. **Unlock the Account**:
   - Follow the procedures for unblocking users as per your organization’s policy. Usually, this might require an admin to reset the account status.
   - Use the option to reset the user password, if applicable.
  
2. **Educate the User**:
   - Inform the user about the password policy and encourage them to use the correct credentials.
   - Advise them to use the self-service password reset feature, if available.

#### Step 4: If Sign-in Was Blocked Due to IP Address
1. **Check the IP Address**:
   - Examine the IP address from which the user attempted to sign in. Cross-reference this with your organization’s recognized safe IP ranges.
   
2. **Review Security Threats**:
   - Ensure that the IP address is not a source of confirmed malicious activity. Block or allow the IP address as per your findings.

3. **Monitor Account Activity**:
   - Check if the user account shows signs of suspicious activity and take remedial action if necessary.

---

### Additional Notes or Considerations
- **User Communication**: Keep the affected user informed throughout the process. Clear communication is vital to maintain trust and transparency.
- **Policy Review**: Regularly review account lockout policies to adjust thresholds based on user behavior and security needs.
- **Conditional Access Policies**: Consider implementing or revising conditional access policies based on risk assessment results.

---

### Documentation for Guidance
Refer to the following Microsoft documentation:
- [Azure Active Directory Sign-In errors](https://docs.microsoft.com/en-us/azure/active-directory/authenticate/sign-in-errors)
- [Monitor sign-ins in Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/reports-monitoring/howto-sign-ins)
- [Troubleshoot account lockout](https://docs.microsoft.com/en-us/azure/active-directory/authentication/howto-troubleshoot-account-lockout)

---

### Data Collection for Further Analysis
If the issue persists after performing the above steps:
1. **Event Viewer Logs**: On the user's device, check the Application and System logs for any errors that coincide with the sign-in attempts.
  
2. **Network Tracing**:
   - Use Nettraceto capture the traffic during the login attempts to see if there are connectivity issues.
   
3. **Fiddler**: Enable Fiddler to trace HTTP traffic, which can help identify failure reasons returned by Azure AD during the login process.

---

By following this guide, you should be equipped to effectively troubleshoot and resolve AADSTS50053 errors.