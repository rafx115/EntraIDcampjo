# AADSTS70001: UnauthorizedClient - The application is disabled. To learn more, see the troubleshooting article for errorAADSTS70001.


## Introduction

This guide will help resolve issues related to unauthorizedclient - the

application is disabled. to learn more, see the troubleshooting article for
erroraadsts70001..


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


### Troubleshooting Guide for Error Code AADSTS70001: UnauthorizedClient - The application is disabled


#### Initial Diagnostic Steps:

1. **Verify Application Status**: Ensure that the application you are trying to
   access is enabled in the identity provider's (such as Azure Active Directory)
   settings.

2. **Check Application Permissions**: Confirm that the application has the
   necessary permissions to access the resource or APIs it is trying to connect
   to.

3. **Review Recent Changes**: Check if there have been any recent changes to the
   application configuration or permissions settings that might have caused it
   to be disabled.


#### Common Issues that Cause this Error:

1. **Application Disabled**: The application in question may have been
   intentionally disabled in the identity provider's admin portal.

2. **Expired or Revoked Credentials**: The app's credentials (such as client
   secret or certificate) may have expired or been revoked, leading to the
   application being disabled.

3. **Incorrect Application Configuration**: Incorrect configuration settings
   within the application itself or in the identity provider's configuration can
   also trigger this error.


#### Step-by-Step Resolution Strategies:

1. **Check Application Status**:
   * Log in to the identity provider's admin portal.

   * Navigate to the list of registered applications.

   * Locate the application in question and ensure that its status is set to

     "Enabled."

2. **Verify Application Permissions**:
   * Review the permissions assigned to the application.

   * Make sure the application has the necessary permissions to access the

     required resources.

3. **Renew Credentials**:
   * If credentials have expired, generate new ones and update the application

     configuration.

4. **Correct Configuration Settings**:

   * Double-check the application's configuration settings to ensure they are

     accurate.
   * Verify that the redirect URLs, client IDs, and secrets are correctly set in

     both the application and identity provider configurations.

5. **Re-enable the Application**:
   * If the application was inadvertently disabled, re-enable it in the admin

     portal of the identity provider.


#### Additional Notes or Considerations:


* **Documentation Review**: Consult the official documentation provided by the

  identity provider for specific guidance on resolving AADSTS70001 errors.

* **Testing and Monitoring**: After making changes, thoroughly test the

  application to ensure the error has been resolved. Monitor the application for
  any further issues.

* **Reach Out for Support**: If you encounter difficulties resolving the error,

  consider reaching out to the identity provider's support team for assistance.

By following these troubleshooting steps, you should be able to address the
AADSTS70001 UnauthorizedClient error and successfully enable the application for
use.