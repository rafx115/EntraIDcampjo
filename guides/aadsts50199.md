
# AADSTS50199: CmsiInterrupt - For security reasons, user confirmation is required for this request. Interrupt is shown for all scheme redirects in mobile browsers.No action required. The user was asked to confirm that this app is the application they intended to sign into.This is a security feature that helps prevent spoofing attacks. This occurs because a system webview has been used to request a token for a native application.To avoid this prompt, the redirect URI should be part of the following safe list:http://https://chrome-extension:// (desktop Chrome browser only)

## Introduction
This guide will help resolve issues related to cmsiinterrupt - for security reasons, user confirmation is required for this request. interrupt is shown for all scheme redirects in mobile browsers.no action required. the user was asked to confirm that this app is the application they intended to sign into.this is a security feature that helps prevent spoofing attacks. this occurs because a system webview has been used to request a token for a native application.to avoid this prompt, the redirect uri should be part of the following safe list:http://https://chrome-extension:// (desktop chrome browser only).

## Prerequisites
- Access to the Azure AD portal with administrator privileges.
- The user must have already set up MFA.

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
- Check for any Azure AD conditional access policies that might be affecting the MFA process.
- Consider any additional security measures that might be in place.

## Additional Notes
- Refer to the [Azure AD documentation](https://learn.microsoft.com/en-us/azure/active-directory/) for more details.
