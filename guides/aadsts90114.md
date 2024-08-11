# AADSTS90114: InvalidExpiryDate - The bulk token expiration timestamp will cause an expired token to be issued.


## Introduction

This guide will help resolve issues related to invalidexpirydate - the bulk

token expiration timestamp will cause an expired token to be issued..


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

Error Code: AADSTS90114 - InvalidExpiryDate

**Initial Diagnostic Steps:** 

1. Verify the exact error message and error code to ensure it is "AADSTS90114 -    
InvalidExpiryDate".

2. Determine if the error is specific to a particular application or across
   multiple applications.
3. Check if the issue occurs consistently or sporadically.
4. Review recent changes made to the Azure Active Directory (AAD) configuration
   or any relevant settings.

**Common Issues that Cause this Error:** 

1. Incorrectly configured token expiration settings in Azure Active Directory.
2. Invalid or outdated token expiration timestamp configuration.
3. Time synchronization issues between different components of the system.
4. Issues with the application's handling of token expiration.

**Step-by-Step Resolution Strategies:** 

1. **Verify Token Expiration Settings**:

   * Go to the Azure Portal and navigate to Azure Active Directory.

   * Check the token configurations, especially the expiration timestamp

     settings.
   * Ensure the token expiration timestamp is set correctly and is not causing

     tokens to be issued as expired.

2. **Adjust Token Expiry Settings**:

   * If the expiration timestamp is incorrect, adjust it to a valid future

     date/time.
   * Ensure the token expiration settings align with the requirements of your

     application.

3. **Check Time Synchronization**:

   * Make sure that all components (Azure AD, servers, applications) have

     synchronized time settings.
   * Any time drift could cause tokens to be considered expired prematurely.

4. **Refresh Tokens or Reauthenticate**:
   * If users are experiencing issues, advise them to try refreshing their

     tokens or reauthenticating to get a new valid token.
   * For applications experiencing this issue, make necessary updates to handle

     token expiration gracefully.

**Additional Notes or Considerations:**


* It's important to monitor token expiration settings regularly and ensure they

  align with your application's requirements.

* Time synchronization across systems is crucial for avoiding token expiry

  issues.

* If the issue persists after following the above steps, consider reaching out

  to Microsoft Azure Support for further assistance.

* Conduct thorough testing after making any changes to ensure the issue has been

  resolved.