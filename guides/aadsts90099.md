# AADSTS90099: The application '{appId}' ({appName}) has not been authorized in the tenant '{tenant}'. Applications must be authorized to access the external tenant before partner delegated administrators can use them. Provide pre-consent or execute the appropriate Partner Center API to authorize the application.


## Introduction

This guide will help resolve issues related to the application '{appid}'
({appname}) has not been authorized in the tenant '{tenant}'. applications must
be authorized to access the external tenant before partner delegated
administrators can use them. provide pre-consent or execute the appropriate
partner center api to authorize the application..


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


### Troubleshooting Guide for Error Code AADSTS90099


#### Initial Diagnostic Steps

1. **Confirm Error Code**: Verify that the error message matches AADSTS90099.
2. **Review Parameters**: Note down the values of '{appId}', '{appName}', and
   '{tenant}' mentioned in the error message.
3. **Check Application Consent Status**: Determine if the application has been
   previously authorized in the specified tenant.


#### Common Issues

1. **Missing Application Consent**: The application '{appId}' has not been
   granted consent to access the specified tenant.
2. **Incorrect Permissions**: The application may lack necessary permissions to
   access resources in the tenant.
3. **Partner Center API Not Executed**: The appropriate Partner Center API has
   not been called to authorize the application.


#### Step-by-Step Resolution

1. **Check Application Consent Status**:

   * Visit the Azure Portal and navigate to Azure Active Directory.

   * Go to "Enterprise applications" and search for the application '{appName}'

     using the '{appId}'.
   * Verify if the application has been granted permissions in the tenant.

2. **Grant Pre-Consent**:

   * If the application lacks consent, follow these steps to provide

     pre-consent:
     * Within the application permissions section, grant the required

       permissions.
     * Ensure that the consent is provided in the tenant specified in the error

       message.

3. **Execute Partner Center API**:

   * Utilize the appropriate Partner Center API to authorize the application for

     access:
     * Refer to the Microsoft Partner Center API documentation for the specific

       API needed to authorize the application.
     * Execute the API call with the correct parameters including the '{appId}',

       '{appName}', and '{tenant}'.

4. **Re-validate Access**:
   * After granting consent or executing the API, retest the functionality that

     was triggering the error to confirm the issue has been resolved.


#### Additional Notes or Considerations


* **API Authentication**: Ensure the user executing the API call has the

  necessary permissions to authorize applications in the specified tenant.

* **Partner Center Documentation**: Consult the official Microsoft Partner

  Center documentation for detailed guidance on using the APIs for application
  authorization.

* **Error Persistence**: If the error persists after following the steps,

  contact Microsoft support for further assistance in addressing the
  authorization issue.