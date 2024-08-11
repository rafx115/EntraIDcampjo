
# AADSTS50086: SasNonRetryableError


## Introduction

This guide will help resolve issues related to sasnonretryableerror.


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

Error code AADSTS50086 with the description SasNonRetryableError typically
occurs in Microsoft Azure Active Directory when there is an issue with the
authentication process. This error can be quite frustrating, but with the
following troubleshooting guide, you will be able to resolve it effectively:


### Initial Diagnostic Steps:

1. **Confirm the Error Details**: Take note of the full error message, including
   any specific details or error codes provided.

2. **Check the Azure AD Portal**: Login to the Azure AD portal to see if any
   relevant notifications or alerts are present that might shed light on the
   issue.

3. **Review Recent Changes**: Identify any recent changes made to the Azure AD
   configuration, application settings, or user permissions that may have
   triggered the error.


### Common Issues Causing AADSTS50086:

1. **Incorrect Tenant Configuration**: Misconfigurations in the Azure AD tenant
   properties can lead to this error.
2. **Expired Access Token**: If the user's access token has expired, it can
   result in an authentication error.
3. **Missing or Incorrect Redirect URIs**: Incorrectly configured redirect URIs
   can cause authentication failures during the sign-in process.


### Step-by-Step Resolution Strategies:

1. **Check Tenant Configuration**:
   * Verify the Azure AD tenant properties and ensure they are correctly set up.

2. **Refresh Access Token**:
   * Check if the user's access token is expired and refresh it to establish a

     new authentication session.

3. **Verify Redirect URIs**:

   * Confirm that the redirect URIs in your application settings match the ones

     set in the Azure AD portal.

4. **Clear Browser Cache**:

   * Sometimes, browser cache or cookies can cause authentication issues. Clear

     the cache and attempt the sign-in process again.

5. **Review Application Permissions**:

   * Ensure that the required permissions are granted to the application in

     Azure AD to access the necessary resources.

6. **Test Using Different Browsers or Devices**:
   * Attempt signing in using different browsers or devices to rule out any

     client-specific issues.


### Additional Notes or Considerations:


* **Logging and Monitoring**: Enable logging and monitoring in Azure AD to track

  authentication events and identify potential issues.

* **Support**: If you're still facing difficulties after following these steps,

  consider reaching out to Microsoft Azure support for further assistance.

By following these steps and strategies, you should be able to troubleshoot and
resolve the AADSTS50086 SasNonRetryableError in Azure Active Directory
effectively.