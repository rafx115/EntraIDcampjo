
# AADSTS90086: OrgIdWsTrustDaTokenExpired - The user DA token is expired.


## Introduction

This guide will help resolve issues related to orgidwstrustdatokenexpired - the

user da token is expired..


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


### Troubleshooting Guide for Error Code AADSTS90086: OrgIdWsTrustDaTokenExpired


#### Initial Diagnostic Steps:

1. **Verify User Credentials**: Ensure that the user attempting to authenticate
   is using the correct username and password. Check for any typos or password
   changes that may have occurred.

2. **Check Token Expiration Time**: Confirm the validity period of the DA
   (Device Administrator) token that is being used for the authentication
   process.

3. **Review Authentication Logs**: Check the authentication logs or error logs
   to identify any specific details or patterns related to this error.


#### Common Issues Causing the Error:

1. **Token Expiration**: The DA token used for authentication has expired.

2. **Token Renewal Failure**: Issues during the renewal process of the DA token.


#### Step-by-Step Resolution Strategies:

1. **Generate a New DA Token**:
   * In the case of token expiration, the user needs to generate a new DA token.

2. **Clear Browser Cache and Cookies**:

   * Sometimes, session data stored in the browser cache can cause

     authentication issues. Clearing cache and cookies might resolve the
     problem.

3. **Check Token Renewal Processes**:

   * Review the token renewal settings and processes to ensure that tokens are

     being renewed in a timely manner.

4. **Check Device Time and Date**:

   * Ensure that the device's time and date are accurate. Inaccurate time

     settings can cause token expiration issues.

5. **Review Token Expiration Time**:
   * Adjust the token validity period if necessary to prevent premature

     expiration.


#### Additional Notes or Considerations:


* **Token Rotation Policy**: Implement a token rotation policy to automatically

  renew tokens before they expire to prevent such errors in the future.


* **User Education**: Educate users on the importance of timely renewal of

  authentication tokens and provide guidance on troubleshooting common issues.


* **Monitoring and Alerts**: Set up monitoring systems to alert administrators

  when tokens are close to expiration or when authentication errors occur.

By following these troubleshooting steps and strategies, you should be able to
address the Error Code AADSTS90086 related to the expiration of the
OrgIdWsTrustDaToken successfully.