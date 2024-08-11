
# AADSTS50014: GuestUserInPendingState - The user account doesn’t exist in the directory. An application likely chose the wrong tenant to sign into, and the currently logged in user was prevented from doing so since they didn't exist in your tenant. If this user should be able to sign in, add them as a guest. For further information, please visitadd B2B users.


## Introduction

This guide will help resolve issues related to guestuserinpendingstate - the

user account doesn’t exist in the directory. an application likely chose the
wrong tenant to sign into, and the currently logged in user was prevented from
doing so since they didn't exist in your tenant. if this user should be able to
sign in, add them as a guest. for further information, please visitadd b2b
users..


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

**Error Code: AADSTS50014 - GuestUserInPendingState**

**Description:** This error occurs when a user attempts to sign in to an

application, but their user account does not exist in the directory. This often
happens when the application selects the wrong tenant to sign into, or the user
has not been added as a guest in the tenant they are trying to access.

**Initial Diagnostic Steps:** 

1. Confirm the user's email address that is being used to sign in.
2. Verify the tenant or directory associated with the user's account.
3. Check if the user has been invited as a guest to the tenant they are
   attempting to sign in to.
4. Review the application configuration to ensure it is set up correctly for B2B
   (Business-to-Business) scenarios.

**Common Issues:** 

1. User account does not exist in the directory.
2. User has not been invited as a guest to the tenant.
3. Application configuration is not set up properly for B2B scenarios.
4. Incorrect tenant selected during sign-in.

**Step-by-Step Resolution Strategies:** 

1. **Confirm User Existence:**
   * Ensure that the user account actually exists in the directory.

2. **Add User as Guest:** 

   * If the user is an external user, invite them as a guest to the tenant they

     are trying to access.

3. **Verify Directory and Tenant:** 

   * Make sure the user is signing in to the correct tenant. Check if the

     application is configured to support B2B users.

4. **Application Configuration:** 

   * Review the application's configuration and settings to ensure it supports

     B2B scenarios and guest users.

5. **IT Admin Assistance:**    * If the issue persists, contact your IT 
administrator or Microsoft support

     for further assistance in troubleshooting the tenant configuration and user
     access.

**Additional Notes or Considerations:**


* Ensure that permissions and access policies are correctly set up for guest

  users in your tenant.

* Regularly review and manage guest accounts in your directory to prevent

  unauthorized access.

* Educate users about the correct tenant and the process of being added as a

  guest to access resources in other tenants.

* Keep the application's documentation and guides up to date to assist users in

  troubleshooting such issues on their own.