
# AADSTS90126: DebugModeEnrollTenantNotInferred - The user type isn't supported on this endpoint. The system can't infer the user's tenant from the user name.


## Introduction

This guide will help resolve issues related to
debugmodeenrolltenantnotinferred - the user type isn't supported on this

endpoint. the system can't infer the user's tenant from the user name..


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


### Troubleshooting Guide: AADSTS90126 - DebugModeEnrollTenantNotInferred


#### Initial Diagnostic Steps:

1. **Confirm the Error Code**: Verify that the error code is indeed
   AADSTS90126 - DebugModeEnrollTenantNotInferred.

2. **User Type Confirmation**: Identify the user type and pay attention to the
   tenant information related to the user.
3. **Check Endpoint**: Ensure that the endpoint being used is correct and
   supports the user type.


#### Common Issues:

1. **Invalid User Type**: Attempting to use an unsupported user type on the
   endpoint.
2. **Tenant Inference**: Inability to determine the user's tenant based on the
   provided user name.
3. **DebugMode Enroll**: Issues related to debug mode enrollment not being
   inferred or processed correctly.


#### Step-by-Step Resolution Strategies:

1. **Review User Type**:
   * Check the user type being used and ensure it is supported by the endpoint.

2. **Explicit Tenant Information**:

   * If the system cannot infer the user's tenant from the username, ensure that

     the tenant information is explicitly provided.
   * Add the tenant ID or tenant domain to make sure the system can identify the

     correct tenant.

3. **DebugMode Enroll Adjustment**:

   * Make sure that the enrollment process in debug mode is correctly configured

     and that the necessary information is being provided.

4. **Endpoint Verification**:

   * Verify that you are using the correct endpoint that supports the user type

     and allows for tenant inference based on the information provided.

5. **Clear Cache and Cookies**:
   * Sometimes issues related to authentication errors can be resolved by

     clearing cache and cookies from the browser.


#### Additional Notes or Considerations:


* **User Type Support**: Ensure that the user type being used is compatible with

  the endpoint where the error is occurring.

* **Azure AD Configuration**: Check the Azure AD configuration to ensure that

  the tenant inference mechanisms are properly set up.

* **Documentation Reference**: Refer to official documentation or contact

  Microsoft support for specific troubleshooting related to Azure AD error
  codes.

By following these steps and considering the common issues related to the
AADSTS90126 error code, you should be able to troubleshoot and resolve the
"DebugModeEnrollTenantNotInferred" issue effectively.