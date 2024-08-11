
# AADSTS50199: CmsiInterrupt - For security reasons, user confirmation is required for this request. Interrupt is shown for all scheme redirects in mobile browsers.No action required. The user was asked to confirm that this app is the application they intended to sign into.This is a security feature that helps prevent spoofing attacks. This occurs because a system webview has been used to request a token for a native application.To avoid this prompt, the redirect URI should be part of the following safe list:http://https://chrome-extension:// (desktop Chrome browser only)


## Introduction

This guide will help resolve issues related to cmsiinterrupt - for security

reasons, user confirmation is required for this request. interrupt is shown for
all scheme redirects in mobile browsers.no action required. the user was asked
to confirm that this app is the application they intended to sign into.this is a
security feature that helps prevent spoofing attacks. this occurs because a
system webview has been used to request a token for a native application.to
avoid this prompt, the redirect uri should be part of the following safe
list:http://https://chrome-extension:// (desktop chrome browser only).


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

Here is a detailed troubleshooting guide for the error code AADSTS50199 with the
CmsiInterrupt description:


### Initial Diagnostic Steps:

1. **Check URL Configuration**: Ensure that the redirect URI is configured
   correctly in the application's settings.
2. **Browser Compatibility**: Verify if the issue is specific to mobile browsers
   or if it occurs on other devices as well.
3. **Review App Permissions**: Confirm that the app requesting access is the one
   intended.
4. **Review Azure AD Settings**: Check if the redirect URI is correctly
   specified and part of the safe list.
5. **Check for Spoofing Indicators**: Look for any signs of malicious activity
   or unauthorized attempts.


### Common Issues Causing the Error:


* **Incorrect Redirect URI Configuration**: Redirect URI not matching or not

  included in the safe list.

* **Use of System WebView**: Using a system webview to request a token for a

  native application can trigger the security confirmation.

* **Spoofing Attempt**: Suspicious activity detected that may indicate a

  spoofing attack.


### Step-by-Step Resolution Strategies:

1. **Review Redirect URI Configuration**:

   * Ensure the redirect URIs are correctly configured in the Azure AD

     application settings.
   * Add the necessary redirect URI to the safe list if required.

2. **Check Browser Compatibility**:

   * Verify if the issue is specific to mobile browsers and if any specific

     configurations are needed.

3. **User Confirmation**:

   * If the interruption is due to a security feature, inform users that this is

     a standard procedure to prevent spoofing attacks.

4. **Avoid System WebView**:

   * If possible, avoid using system webviews for requesting tokens and opt for

     browser-based flows instead.

5. **Additional Considerations**:
   * Consider the use of secure browser extensions for desktop Chrome browsers

     to avoid interruptions.
   * Educate users on recognizing spoofing attempts to enhance security

     awareness.


### Additional Notes or Considerations:


* If the error persists despite following the steps, contact Azure AD support

  for further assistance.

* Regularly review and update the application settings to maintain security and

  prevent unauthorized access.

* Encourage users to report any suspicious activity or prompts for user

  confirmation that seem out of the ordinary.

By following these steps and considering the mentioned factors, you can
troubleshoot and address the AADSTS50199 error with the CmsiInterrupt
description effectively.