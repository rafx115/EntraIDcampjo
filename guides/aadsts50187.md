
# AADSTS50187: DeviceInformationNotProvided - The service failed to perform device authentication.


## Introduction

This guide will help resolve issues related to deviceinformationnotprovided -
the service failed to perform device authentication..


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


### Troubleshooting Guide for Error Code AADSTS50187: DeviceInformationNotProvided


#### Initial Diagnostic Steps:

1. **Confirm the Issue:** Ensure that the error code AADSTS50187 is indeed being

   encountered during the authentication process.
2. **Check Device Information:** Verify if the device information is being

   correctly provided during the authentication process.
3. **Review Logs:** Examine any relevant logs or error messages to gather more

   context about the failure.
4. **Check Network Connectivity:** Ensure the device has stable internet

   connectivity.


#### Common Issues Causing This Error:

1. **Missing Device Information:** The required information about the device is

   not being sent during authentication.
2. **Incorrect Device Configuration:** Device settings or configurations are

   preventing the authentication process from completing.
3. **Network Issues:** Connectivity problems preventing the device from properly

   communicating with the authentication service.


#### Step-by-Step Resolution Strategies:

1. **Ensure Device Information is provided:**    * Check the authentication 
request payload to confirm that necessary device

     information like device ID, type, and OS version is included.
2. **Verify Device Configuration:**    * Review the device settings to ensure 
they are correctly configured to

     support the authentication process.
3. **Update Device Software:**    * Ensure that the device's operating system 
and any relevant software are up

     to date to avoid compatibility issues.
4. **Check Network Connection:**    * Verify that the device has a stable 
internet connection and can reach the

     authentication service without any restrictions.
5. **Try Another Device:**    * If possible, attempt the authentication process 
on a different device to

     isolate if the issue is specific to one device.
6. **Contact Support:**    * If the error persists, reach out to the support 
team of the service

     generating the error for further assistance.


#### Additional Notes or Considerations:


* **Device Compliance:** Some services require devices to comply with specific

  security standards for authentication.

* **Security Policies:** Ensure that any security policies enforced by the

  service are not blocking the device authentication.

* **Client Application:** The client application initiating the authentication

  process may need updates or modifications for successful device
  authentication.

By following these troubleshooting steps, you should be able to diagnose and
address the Error Code AADSTS50187 related to DeviceInformationNotProvided. If
you encounter any challenges during the resolution process, don't hesitate to
seek assistance from technical support for the specific service or platform
generating the error.