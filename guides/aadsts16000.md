
# AADSTS16000: InteractionRequired - User account '{EmailHidden}' from identity provider '{idp}' doesn't exist in tenant '{tenant}' and can't access the application '{appid}'({appName}) in that tenant. This account needs to be added as an external user in the tenant first. Sign out and sign in again with a different Microsoft Entra user account. This error is fairly common when you try to sign in to Microsoft Entra admin center by using personal Microsoft Account and no directory associated with it.


## Introduction

This guide will help resolve issues related to interactionrequired - user

account '{emailhidden}' from identity provider '{idp}' doesn't exist in tenant
'{tenant}' and can't access the application '{appid}'({appname}) in that tenant.
this account needs to be added as an external user in the tenant first. sign out
and sign in again with a different microsoft entra user account. this error is
fairly common when you try to sign in to microsoft entra admin center by using
personal microsoft account and no directory associated with it..


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


### Troubleshooting Guide for Error Code AADSTS16000


#### Initial Diagnostic Steps:

1. **Confirm Error Description**: Ensure that the error message received matches
   the provided description for AADSTS16000.
2. **Check Sign-in Context**: Identify the context in which the error occurs
   (e.g., trying to sign in to a specific application or admin center).
3. **Verify the User Account**: Confirm the email address and identity provider
   associated with the user account mentioned in the error message.


#### Common Issues that Cause this Error:

1. **User Account Not Added**: The user account mentioned in the error message
   does not exist in the specified tenant or is not added as an external user.
2. **Personal Microsoft Account**: Attempting to sign in using a personal
   Microsoft Account that is not associated with any tenant.
3. **Incorrect Application Access**: The application specified in the error
   message may not have been properly configured or accessible to the user
   account.


#### Step-by-Step Resolution Strategies:

1. **Ensure Account Existence**:

   * If the user account mentioned in the error message is valid, ensure it is

     added as an external user in the tenant.

2. **Use a Work or School Account**:

   * Sign out of the current session and sign in again using a different

     Microsoft Entra user account associated with the specific tenant.
   * Avoid using personal Microsoft Accounts to access admin centers or

     applications that require organizational credentials.

3. **Verify Application Access**:

   * Check the application '{appName}' (identified by '{appid}') settings to

     verify that the user account has the necessary access permissions.

4. **Contact Administrator**:
   * If you are unable to resolve the issue, contact the admin of the tenant to

     assist in adding the user account or troubleshooting the access problem.


#### Additional Notes or Considerations:


* **Use Organization Credentials**: Always use organizational accounts provided

  by the company or organization to access business-related tools and
  applications.

* **Permissions and Directory Association**: Ensure that the user account has

  the necessary permissions within the tenant to access the specific
  application.

* **Keep Directory Information Updated**: Regularly update and manage user

  accounts and their association with directories to prevent similar errors in
  the future.

Following these steps should help in diagnosing and resolving the AADSTS16000
error related to account existence and application access issues.