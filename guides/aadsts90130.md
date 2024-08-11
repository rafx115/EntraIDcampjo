
# AADSTS90130: NonConvergedAppV2GlobalEndpointNotSupported - The application isn't supported over the/commonor/consumersendpoints. Use the/organizationsor tenant-specific endpoint instead.


## Introduction

This guide will help resolve issues related to
nonconvergedappv2globalendpointnotsupported - the application isn't supported

over the/commonor/consumersendpoints. use the/organizationsor tenant-specific
endpoint instead..


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

Here is a detailed troubleshooting guide for the error code AADSTS90130 with the
description NonConvergedAppV2GlobalEndpointNotSupported:

Initial Diagnostic Steps:

1. Verify the application configuration in Azure Active Directory (Azure AD)
   portal.
2. Check if the application was created using the correct Azure AD endpoint.
3. Confirm the relevant OAuth/OpenID Connect endpoints being used by the
   application.
4. Review the permissions and authentication settings for the application.
5. Ensure that the appropriate permissions are granted for the application in
   Azure AD.

Common Issues that Cause this Error:

1. The application is configured to use global endpoints (/common or
   /consumers), which are not supported for certain types of applications.
2. The application's configuration is incorrect, leading to a mismatch in
   endpoint usage.
3. The application may not have proper permissions or scopes configured in Azure
   AD.
4. Tenant-specific settings are required for the application, but global
   endpoints are being used.
5. The application may be attempting to access resources that are restricted to
   specific endpoints or tenants.

Step-by-Step Resolution Strategies:

1. Update the application configuration in the Azure AD portal to use the
   tenant-specific endpoint instead of global endpoints.
2. Ensure that the correct authentication endpoints (/organizationsor) are used
   based on the application's requirements.
3. Update the application code or configuration to use the appropriate Azure AD
   endpoints for authentication and authorization.
4. Verify the permissions and consent required for the application to access
   Azure AD resources.
5. If the application needs to support multiple tenants, consider implementing
   multi-tenant support using tenant-specific endpoints.

Additional Notes or Considerations:

1. Review the Azure AD documentation and guidelines for configuring applications
   to ensure compliance with best practices.
2. Test the application with different authentication scenarios to ensure that
   the issue is resolved.
3. Keep track of any changes made to the application configuration for future
   reference and troubleshooting.

By following these steps and considerations, you should be able to resolve the
error code AADSTS90130 related to the
NonConvergedAppV2GlobalEndpointNotSupported issue effectively.