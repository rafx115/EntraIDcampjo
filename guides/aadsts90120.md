# AADSTS90120: InvalidDeviceFlowRequest - The request was already authorized or declined.


## Introduction

This guide will help resolve issues related to invaliddeviceflowrequest - the

request was already authorized or declined..


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


### Troubleshooting Guide for Error Code AADSTS90120: InvalidDeviceFlowRequest


#### 1. Initial Diagnostic Steps:


* **Ensure Correct User Interaction**: Ensure that the user is following the

  correct authentication flow, especially in the context of device authorization
  flow.

* **Check User Authorization Status**: Verify if the user has already authorized

  or declined the request.

* **Review Application Configuration**: Confirm that the application settings

  are configured correctly for device authorization flow.


#### 2. Common Issues Causing the Error:


* **User Interaction**: The user may have previously authorized or declined the

  request.

* **Multiple Requests**: Multiple concurrent authorization requests can lead to

  conflicts.

* **Incorrect Application Configuration**: Improper configuration of the

  application settings for device flow authentication.


#### 3. Step-by-Step Resolution Strategies:

1. **Check Authorization Status**: Verify the authorization status of the user
   for the particular request to ensure it has not already been authorized or
   declined.
2. **Handle Multiple Requests**: If multiple requests are being made
   concurrently, handle them sequentially to avoid conflicts.
3. **Reset the Authorization**: If the user has previously responded to the
   request, consider resetting the authorization status for the user.
4. **Review Application Configuration**: Ensure that the application is
   correctly configured to handle device flow requests and responses.
5. **Log and Monitor**: Enable detailed logging to track the flow of requests
   and responses for better troubleshooting.


#### 4. Additional Notes or Considerations:


* **User Communication**: If the error persists, communicate with the user to

  clarify their actions regarding the authorization request.

* **Authentication Flow**: Understand the device flow authentication process

  thoroughly to identify any deviations causing the error.

* **API Documentation**: Refer to the API documentation for relevant details on

  handling device flow requests and errors like AADSTS90120.

* **Support**: Reach out to Azure Active Directory support for further

  assistance if the issue remains unresolved despite following the
  troubleshooting steps.