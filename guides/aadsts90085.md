
# AADSTS90085: OrgIdWsFederationSltRedemptionFailed - The service is unable to issue a token because the company object hasn't been provisioned yet.


## Introduction

This guide will help resolve issues related to
orgidwsfederationsltredemptionfailed - the service is unable to issue a token

because the company object hasn't been provisioned yet..


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

**Troubleshooting Guide for Error Code AADSTS90085:
OrgIdWsFederationSltRedemptionFailed**

**Description:** The error message indicates that the service is unable to issue

a token due to the company object not being provisioned yet.

**Initial Diagnostic Steps:** 

1. **Verify the Error:** Check if the error code AADSTS90085 is consistently

   appearing during the authentication process.
2. **Access Logs:** Review any available log files from the identity provider or

   authentication system for more specific error details.
3. **Check Provisioning Status:** Confirm whether the company object has been

   provisioned and is accessible within the system.

**Common Issues:** 

1. **Delayed Provisioning:** The company object might not have been fully set up

   or provisioned in the identity provider service.
2. **Mismatched or Missing Attributes:** Incomplete or incorrect details related

   to the company object may be causing the error.
3. **Access Permission Settings:** Insufficient permissions or misconfigured

   access controls for the company object could lead to this issue.

**Step-by-Step Resolution Strategies:** 

1. **Confirm Provisioning:** Ensure the company object has been properly

   provisioned in the identity provider system.
2. **Validate Attributes:** Check and compare the attributes of the company

   object to the required information for successful token issuance.
3. **Update Attributes:** Make necessary updates to the company object's

   attributes if any discrepancies are found.
4. **Permission Review:** Verify that the necessary permissions are granted for

   the service to issue tokens related to the company object.
5. **Refresh Token Process:** If the error persists, consider revoking existing

   tokens and initiating the token issuance process again.

**Additional Notes or Considerations:**


* **Documentation Check:** Refer to the identity provider's documentation for

  specific guidance on provisioning and token issuance.

* **Support Channels:** Contact technical support for the identity provider or

  authentication system for further assistance if needed.

* **Testing and Monitoring:** Conduct thorough testing of the authentication

  flow post-resolution to ensure the error has been mitigated.

By following these steps and considering the common issues associated with error
code AADSTS90085, you should be able to troubleshoot and resolve the
OrgIdWsFederationSltRedemptionFailed issue effectively.