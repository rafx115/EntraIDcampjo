# AADSTS80012: OnPremisePasswordValidationAccountLogonInvalidHours - The users attempted to log on outside of the allowed hours (this is specified in AD).


## Introduction

This guide will help resolve issues related to
onpremisepasswordvalidationaccountlogoninvalidhours - the users attempted to log

on outside of the allowed hours (this is specified in ad)..


## Prerequisites


* Access to the Azure AD portal with administrator privileges.

* The user must have already set up MFA.


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


* Check for any Azure AD conditional access policies that might be affecting the

  MFA process.

* Consider any additional security measures that might be in place.


## Additional Notes


* Refer to the

  [Azure AD 
documentation](https://learn.microsoft.com/en-us/azure/active-directory/)
  for more details.


## Troubleshooting Steps

Troubleshooting steps could not be generated due to an error.


## Troubleshooting Steps

Troubleshooting steps could not be generated due to an error.


## Troubleshooting Steps


### Troubleshooting Guide for Error Code AADSTS80012: OnPremisePasswordValidationAccountLogonInvalidHours


#### Initial Diagnostic Steps:

1. **Verify User Logon Attempt**: Confirm that the user has indeed attempted to
   log on during restricted hours and received the error message.
2. **Check Active Directory**: Ensure that the allowed logon hours for the user
   are correctly configured in Active Directory.


#### Common Issues:

1. **Incorrect Logon Hours Configuration**: The user's logon hours in Active
   Directory may not be set up correctly.
2. **Timezone Mismatch**: The timezone of the user's device may not be
   synchronized with the Active Directory server.
3. **Daylight Saving Time**: Changes in daylight saving time can affect the
   allowed logon hours.


#### Step-by-Step Resolution Strategies:

1. **Verify Logon Hours**:

   * In Active Directory Users and Computers, locate the affected user.

   * Right-click on the user and select Properties.

   * Go to the Account tab and check the Logon Hours settings to ensure they

     align with the user's intended logon hours.

2. **Check Timezone Settings**:

   * Ensure that the user's device timezone matches the timezone settings in

     Active Directory.
   * Adjust the device's time, date, and timezone settings if necessary.

3. **Review Daylight Saving Time Changes**:

   * Verify if the user's logon hours need to be adjusted due to daylight saving

     time changes.
   * Update the logon hours accordingly in Active Directory.

4. **Reset Logon Hours**:
   * Temporarily remove logon hour restrictions in Active Directory to allow the

     user to log in and troubleshoot the issue further.
   * Reset the logon hours to the correct settings once the issue is resolved.


#### Additional Notes or Considerations:


* **Group Policy**: Check if any Group Policies are overriding the logon hours

  settings configured in Active Directory.

* **User Communication**: Inform the user about the restricted logon hours and

  provide guidance on when they can access the system.

* **Logon Restrictions**: Enforce logon hours policies consistently across all

  users to maintain security and compliance.

By following these troubleshooting steps and strategies, you should be able to
address the error code AADSTS80012 related to
OnPremisePasswordValidationAccountLogonInvalidHours effectively.