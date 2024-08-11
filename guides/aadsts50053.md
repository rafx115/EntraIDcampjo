
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
