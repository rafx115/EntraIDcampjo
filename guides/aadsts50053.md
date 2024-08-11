# AADSTS50053: This error can result from two different reasons:IdsLocked - The account is locked because the user tried to sign in too many times with an incorrect user ID or password. The user is blocked due to repeated sign-in attempts. SeeRemediate risks and unblock users.Or, sign-in was blocked because it came from an IP address with malicious activity.To determine which failure reason caused this error, sign in to theMicrosoft Entra admin centeras at least aCloud Application Administrator.  Navigate to your Microsoft Entra tenant and thenMonitoring & health->Sign-in logs.  Find the failed user sign-in withSign-in error code50053 and check theFailure reason.


## Troubleshooting Steps
Troubleshooting Guide for Error Code AADSTS50053:

**Initial Diagnostic Steps:**
1. Verify the exact error message and code to confirm it is AADSTS50053.
2. Check if the user has experienced repeated sign-in failures or if the sign-in attempt is blocked due to malicious activity.
3. Ensure you have admin access to the Microsoft Azure portal for troubleshooting.

**Common Issues that Cause this Error:**
1. IdsLocked: User account is locked due to repeated incorrect sign-in attempts.
2. Malicious Activity: Sign-in is blocked because it originated from an IP address associated with malicious behavior.

**Step-by-Step Resolution Strategies:**
1. Sign in to the Microsoft Azure Admin Center as at least a Cloud Application Administrator.
2. Navigate to your Microsoft Azure tenant and go to Monitoring & Health -> Sign-in Logs.
3. Find the failed user sign-in with the Sign-in error code 50053 and check the Failure reason.
4. If the Failure reason is IdsLocked, follow the steps to remediate risks and unblock the user. This might involve resetting the user's password or unlocking the account.
5. If the Failure reason is related to malicious activity from an IP address, take action to investigate and mitigate the threat. This may involve blocking the IP address or enabling additional security measures.

**Additional Notes or Considerations:**
- Regularly monitor sign-in logs and configure alerts for suspicious activities to prevent such errors in the future.
- Educate users on best practices for passwords and account security to avoid lockouts and malicious activities.

**Documentation for Guidance:**
For detailed step-by-step instructions and official documentation, refer to the Microsoft documentation on managing user accounts and security settings in the Azure portal. You can find specific guidance on handling AADSTS50053 errors in the Azure Active Directory documentation as well.

By following these troubleshooting steps and best practices, you can effectively address the AADSTS50053 error and ensure the security of your Azure tenant.