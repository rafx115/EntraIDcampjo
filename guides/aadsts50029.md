# AADSTS50029: Invalid URI - domain name contains invalid characters. Contact the tenant admin.


## Introduction

This guide will help resolve issues related to invalid uri - domain name

contains invalid characters. contact the tenant admin..


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


### Troubleshooting Guide for AADSTS50029 Error Code: Invalid URI - Domain Name Contains Invalid Characters


#### Initial Diagnostic Steps:

1. **Confirm Error Code**: Verify that the error code displayed is AADSTS50029.
2. **Check Domain Name**: Ensure the domain name being used does not contain any
   special characters or invalid characters.
3. **Verify Permissions**: Check if the user has the necessary permissions to
   access the resource.


#### Common Issues That Cause This Error:

1. **Special Characters in Domain Name**: Invalid characters like spaces,
   special symbols, or non-ASCII characters in the domain name can trigger this
   error.
2. **Misconfigured Application Settings**: Incorrect settings within the
   application or Azure Active Directory can lead to this issue.


#### Step-by-Step Resolution Strategies:

1. **Check Domain Name Format**:

   * Verify that the domain name being used conforms to standard domain name

     format rules.
   * Ensure it contains only alphanumeric characters, hyphens, and dots.

2. **Update Domain Name**:
   * If the domain name is found to have invalid characters, contact the tenant

     admin to update the domain name.

3. **Review Application Configuration**:

   * Inspect the configuration settings of the application in Azure portal.

   * Ensure the redirect URI and any references to the domain name are correctly

     formatted.

4. **Check Azure Active Directory Configuration**:

   * Review the Azure Active Directory settings related to the application.

   * Confirm that the domain name is correctly specified in the configurations.

5. **Grant Correct Permissions**:
   * Ensure that the user has the appropriate permissions assigned in Azure

     Active Directory.
   * Grant necessary permissions to access the resource associated with the

     domain.


#### Additional Notes or Considerations:


* **Tenant Admin Assistance**: If unable to resolve the issue locally, contact

  the tenant admin for further assistance.

* **Update Documentation**: Document any changes made to the domain name or

  configuration settings for future reference.

* **Test Access**: After resolving the error, test access to ensure the issue is

  fully resolved.

By following these steps, you should be able to troubleshoot and resolve the
AADSTS50029 error related to an invalid URI due to domain name containing
invalid characters.