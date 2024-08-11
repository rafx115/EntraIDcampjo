# AADSTS50053: This error can result from two different reasons:IdsLocked - The account is locked because the user tried to sign in too many times with an incorrect user ID or password. The user is blocked due to repeated sign-in attempts. SeeRemediate risks and unblock users.Or, sign-in was blocked because it came from an IP address with malicious activity.To determine which failure reason caused this error, sign in to theMicrosoft Entra admin centeras at least aCloud Application Administrator.  Navigate to your Microsoft Entra tenant and thenMonitoring & health->Sign-in logs.  Find the failed user sign-in withSign-in error code50053 and check theFailure reason.

## Introduction
This guide will help resolve issues related to this error can result from two different reasons:idslocked - the account is locked because the user tried to sign in too many times with an incorrect user id or password. the user is blocked due to repeated sign-in attempts. seeremediate risks and unblock users.or, sign-in was blocked because it came from an ip address with malicious activity.to determine which failure reason caused this error, sign in to themicrosoft entra admin centeras at least acloud application administrator.  navigate to your microsoft entra tenant and thenmonitoring & health->sign-in logs.  find the failed user sign-in withsign-in error code50053 and check thefailure reason..

## Prerequisites
- Access to the Azure AD portal with administrator privileges.
- The user must have already set up MFA.

## Steps to Resolve

### Step 1: Initial Actions
1. Log in to the Azure AD portal.
2. Navigate to the "Users" section.
3. Select the affected user.
4. Perform necessary actions as described for the error.

### Step 2: Verify MFA Settings
1. Ensure that the user has MFA configured.
2. If necessary, guide the user through the MFA setup process.

## Troubleshooting
- Check for any Azure AD conditional access policies that might be affecting the MFA process.
- Consider any additional security measures that might be in place.

## Additional Notes
- Refer to the [Azure AD documentation](https://learn.microsoft.com/en-us/azure/active-directory/) for more details.


## Troubleshooting Steps
Troubleshooting steps could not be generated due to an error.

## Troubleshooting Steps
Troubleshooting steps could not be generated due to an error.

## Troubleshooting Steps
**Error Code: AADSTS50053 Troubleshooting Guide**

**Description:**
Error Code AADSTS50053 can occur due to two different reasons:
1. IdsLocked: The account is locked because the user tried to sign in too many times with an incorrect user ID or password. The user is blocked due to repeated sign-in attempts.
2. Sign-in was blocked because it came from an IP address with malicious activity.

**Initial Diagnostic Steps:**
1. Confirm the exact error message and error code received.
2. Verify if the error is consistent across multiple sign-in attempts or platforms.
3. Check if other users are experiencing similar issues.
4. Identify the user affected by the error.

**Common Issues that Cause this Error:**
1. Incorrect user ID or password input.
2. Repeated sign-in attempts with incorrect credentials.
3. Malicious activity from the user's IP address.
4. System misconfiguration impacting user sign-in.

**Step-by-Step Resolution Strategies:**

**1. Identify Failure Reason:**
- Sign in to the Microsoft admin center as a Cloud Application Administrator.
- Navigate to your Microsoft Entra tenant and go to Monitoring & health -> Sign-in logs.
- Find the failed user sign-in with the Sign-in error code 50053 and check the Failure Reason to determine if it's IdsLocked or IP related.

**2. Remediate Risks and Unblock Users:**
If the Failure Reason is IdsLocked:
- Follow Microsoft's guidelines to unblock the user due to repeated sign-in attempts.
- Guide the user to reset their password or verify their user ID to regain access.
- Implement security measures to prevent future lockouts.

**3. Address Malicious IP Activity:**
If the Failure Reason is a malicious IP address:
- Investigate the IP address activity and take necessary security actions.
- Implement IP blocking or access controls to prevent further malicious sign-in attempts.
- Consider enforcing multi-factor authentication for added security.

**4. System Configuration Review:**
- Check for any misconfigurations in your Microsoft Entra settings that may be affecting user sign-in.
- Ensure all settings are aligned with security best practices and policies.
- Test user sign-in after making any configuration changes to verify resolution.

**Additional Notes or Considerations:**
- Communicate with the affected user to provide guidance on resolving the sign-in issue.
- Educate users on secure sign-in practices and password management.
- Regularly monitor sign-in logs for suspicious activities and address them promptly.

By following these troubleshooting steps, you should be able to determine the root cause of the AADSTS50053 error and take appropriate actions to resolve it effectively.