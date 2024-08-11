
# AADSTS90090: GraphRetryableError - The service is temporarily unavailable.


## Introduction

This guide will help resolve issues related to graphretryableerror - the service

is temporarily unavailable..


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

Error Code: AADSTS90090 - GraphRetryableError - The service is temporarily

unavailable.

**Initial Diagnostic Steps:** 

1. **Verify the Error:** Confirm the error code AADSTS90090 and the associated

   message about the service being temporarily unavailable.

2. **Check Service Status:** Ensure that the Microsoft Azure Active Directory

   (AAD) service and associated services like Microsoft Graph API are
   operational by checking the service status page on the Azure Portal or
   Microsoft's official status page.

3. **Validate API Request:** Verify that the API requests being made to the

   Microsoft Graph API are correctly formatted and include the required
   authentication headers and parameters.

**Common Issues that Cause this Error:** 

1. **Network Connectivity Problems:** Temporary network issues on the

   client-side or server-side may result in the service being inaccessible.

2. **Server-Side Outages:** Microsoft Azure services occasionally experience

   outages or maintenance periods, leading to temporary unavailability.

3. **Throttling Limit Exceeded:** If the number of requests from your

   application exceeds the rate limits defined by Microsoft, you may encounter
   this error.

**Step-by-Step Resolution Strategies:** 

1. **Check Network Connection:**    * Ensure that your network connection is 
stable and not experiencing any

     issues. Retry the request on a different network if possible.

2. **Verify Service Status:** 

   * Check the Azure service status page for any ongoing incidents or outages

     affecting the services. Wait for the issue to be resolved by Microsoft if
     it is a server-side problem.

3. **Implement Retry Logic:** 

   * Incorporate retry logic in your application to handle temporary service

     unavailability. Implement exponential backoff strategies to avoid
     overwhelming the service.

4. **Respect API Rate Limits:**    * Review the Microsoft Graph API 
documentation to understand the rate limits

     and adjust your application's request rate accordingly to prevent hitting
     throttling limits.

**Additional Notes or Considerations:**


* **Contact Support:** If the issue persists even after following the

  troubleshooting steps, consider reaching out to Microsoft Azure support for
  further assistance.


* **Monitor Service Status:** Stay updated on service status updates provided by

  Microsoft to be informed about any ongoing issues that may impact your
  application.


* **Cache Responses:** Consider implementing caching mechanisms to reduce the

  frequency of calls to the Microsoft Graph API and lessen the impact of
  temporary service unavailability.

By following these detailed troubleshooting steps, you should be able to address
the AADSTS90090 error code related to the service being temporarily unavailable.