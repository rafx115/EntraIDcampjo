# AADSTS52004: DelegationDoesNotExistForLinkedIn - The user has not provided consent for access to LinkedIn resources.


## Introduction

This guide will help resolve issues related to
delegationdoesnotexistforlinkedin - the user has not provided consent for access

to linkedin resources..


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

**Troubleshooting Guide for Error Code AADSTS52004:
DelegationDoesNotExistForLinkedIn**

**Description:** The error code AADSTS52004 indicates that the user has not

provided consent for access to LinkedIn resources.

**Initial Diagnostic Steps:** 

1. Verify the user's access permissions to LinkedIn resources.
2. Confirm if the user has previously granted consent for accessing LinkedIn
   resources.
3. Check the API permissions configuration for the application trying to access
   LinkedIn resources.
4. Ensure that there are no restrictions or issues with the LinkedIn integration
   setup.

**Common Issues Causing This Error:** 

1. User has not granted consent for LinkedIn resources.
2. API permissions are incorrectly configured or missing for LinkedIn resources.
3. Issues with the application's authentication process when trying to access
   LinkedIn resources.

**Step-by-Step Resolution Strategies:** 

1. **User Consent Verification:** 

   * Instruct the user to log in and grant consent for accessing LinkedIn

     resources.
   * Provide clear instructions on how to grant consent within the application.

2. **API Permissions Configuration:** 

   * Check the API permissions assigned to the application in the Azure portal.

   * Ensure the necessary permissions for LinkedIn resources are correctly

     configured.
   * Add or update the required permissions for LinkedIn resources as needed.

3. **Authentication Troubleshooting:**    * Check if the authentication flow is 
correctly handling consent requests for

     LinkedIn resources.
   * Verify that the correct scopes and permissions are being requested during

     the authentication process.
   * Ensure that the authentication tokens are being passed correctly for

     accessing LinkedIn resources.

**Additional Notes or Considerations:**


* It is essential to communicate clearly with the user about the need to grant

  consent for accessing LinkedIn resources.

* Monitor the Azure portal for any additional error logs or details that could

  provide insights into the issue.

* Test the authentication and access to LinkedIn resources thoroughly after

  making any configuration changes.

By following these troubleshooting steps, you should be able to resolve the
error code AADSTS52004 related to delegation not existing for LinkedIn
resources. If the issue persists, consider reviewing the specific implementation
details and seeking assistance from Microsoft support or relevant documentation.