
# AADSTS50034: UserAccountNotFound - To sign into this application, the account must be added to the directory. This error can occur because the user mis-typed their username, or isn't in the tenant. An application might have chosen the wrong tenant to sign into, and the currently logged in user was prevented from doing so since they did not exist in your tenant. If this user should be able to log in, add them as a guest. See docs here:Add B2B users.

## Introduction
This guide will help resolve issues related to useraccountnotfound - to sign into this application, the account must be added to the directory. this error can occur because the user mis-typed their username, or isn't in the tenant. an application might have chosen the wrong tenant to sign into, and the currently logged in user was prevented from doing so since they did not exist in your tenant. if this user should be able to log in, add them as a guest. see docs here:add b2b users..

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
