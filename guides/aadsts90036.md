
# AADSTS90036: MsodsServiceUnretryableFailure - An unexpected, non-retryable error from the WCF service hosted by MSODS has occurred.Open a support ticketto get more details on the error.


## Introduction

This guide will help resolve issues related to msodsserviceunretryablefailure - 
an unexpected, non-retryable error from the wcf service hosted by msods has

occurred.open a support ticketto get more details on the error..


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

**Troubleshooting Guide for Error Code AADSTS90036:
MsodsServiceUnretryableFailure**

**Initial Diagnostic Steps:** 

1. **Confirm Error Code**: Make sure the error code is indeed AADSTS90036 with
   the specific description "MsodsServiceUnretryableFailure."

2. **Check Service Status**: Verify the status of the WCF service hosted by
   MSODS to rule out any service-related issues.

3. **Review Documentation**: Consult Microsoft's official documentation for the
   error code to understand potential causes and solutions.

**Common Issues Causing This Error:** 

1. **Service Outage**: The WCF service hosted by MSODS might be experiencing
   downtime or issues, leading to the non-retryable error.

2. **Authentication Problems**: Issues with token validation or authentication
   processes can also trigger this error.

3. **Configuration Errors**: Incorrect configuration settings, permissions, or
   network settings might result in the unexpected error.

**Step-by-Step Resolution Strategies:** 

1. **Open a Support Ticket**: As suggested in the error message, reach out to
   Microsoft support to get more details on the specific error and for
   assistance in resolving it.

2. **Check Service Health**: Monitor the service health dashboard or contact the
   service provider to ensure that the WCF service is operational and running
   without any disruptions.

3. **Review Logs**: Examine the logs for additional error details or stack
   traces that can shed light on what exactly went wrong while communicating
   with the MSODS service.

4. **Update Dependencies**: Verify that all dependencies, libraries, and SDKs
   used in the application are up-to-date and compatible with the MSODS service.

5. **Review Authentication Settings**: Ensure that the authentication
   mechanisms, like Azure AD configurations, are correctly set up and that there
   are no issues with tokens or user credentials.

**Additional Notes or Considerations:**


* **Network Connectivity**: Check if there are any network issues or firewalls

  blocking the communication with the MSODS service.


* **Retry Mechanism**: If possible, implement a retry mechanism in your

  application for transient errors, but in the case of
  "MsodsServiceUnretryableFailure," it's crucial to address the root cause.


* **Microsoft Updates**: Stay updated with Microsoft announcements or updates

  related to the MSODS service, as there might be known issues or fixes provided
  by the service provider.

By following these steps and considering the common causes, you can troubleshoot
and hopefully resolve the error code AADSTS90036 with the description
"MsodsServiceUnretryableFailure." If the issue persists, contact Microsoft
support for further assistance.