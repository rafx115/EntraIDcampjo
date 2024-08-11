# AADSTS90091: GraphServiceUnreachable

## Introduction

This guide will help resolve issues related to graphserviceunreachable.

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
  [Azure AD documentation](https://learn.microsoft.com/en-us/azure/active-directory/)
  for more details.

## Troubleshooting Steps

Troubleshooting steps could not be generated due to an error.

## Troubleshooting Steps

Troubleshooting steps could not be generated due to an error.

## Troubleshooting Steps

**Troubleshooting Guide for Error Code AADSTS90091 (GraphServiceUnreachable)**

**Initial Diagnostic Steps:**

1. **Confirm the Error:** Ensure that the error code AADSTS90091 with the
   description GraphServiceUnreachable is consistently occurring.
2. **Check Network Connection:** Verify that your device has a stable internet
   connection to access the Microsoft Graph service.
3. **Review Service Status:** Check the official Microsoft Azure status page to
   see if there are any ongoing service disruptions that could be impacting the
   Graph service.
4. **Check Permissions:** Ensure that the user or application trying to access
   the Microsoft Graph service has the appropriate permissions and consent
   granted.

**Common Issues Leading to Error AADSTS90091:**

1. **Network Connectivity Issues:** Unstable internet connection, firewall
   restrictions, or proxy settings preventing communication with the Microsoft
   Graph service.
2. **Permission Misconfiguration:** Insufficient permissions granted to the user
   or application trying to access the Graph service.
3. **Service Outages:** Microsoft Graph service may be experiencing downtime or
   issues impacting its availability.

**Step-by-Step Resolution Strategies:**

1. **Network Troubleshooting:**

   * Restart your network hardware and reconnect to the internet.
   * Disable any VPN or proxy settings temporarily to check if they are causing
     the issue.
   * Whitelist necessary URLs or IPs related to the Microsoft Graph service in
     your firewall settings.

2. **Permission Verification:**

   * Ensure that the user or application has the required permissions to access
     the Graph service.
   * Review the Azure Active Directory settings to verify if the necessary
     consent has been granted.

3. **Service Status Check:**
   * Monitor the Microsoft Azure status page for any updates regarding the Graph
     service.
   * Consider reaching out to Microsoft support if there are known service
     disruptions that are causing the issue.

**Additional Notes or Considerations:**

* Ensure that the client application has been properly configured to interact
  with the Microsoft Graph API.
* It might be helpful to review the Azure AD logs or diagnostic reports for more
  detailed information on the error.
* Consider testing the Graph service access with a different network or device
  to isolate the issue further.

By following these troubleshooting steps, you should be able to diagnose and
resolve the AADSTS90091 error code with the description of
GraphServiceUnreachable effectively. If the issue persists, don't hesitate to
reach out to Microsoft support for further assistance.
