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


## Troubleshooting Steps
Troubleshooting steps could not be generated due to an error.

## Troubleshooting Steps
Troubleshooting steps could not be generated due to an error.

## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS50034: UserAccountNotFound

#### Initial Diagnostic Steps:
1. **Verify Account Details:**
   - Confirm that the user has entered the correct username. Typos or incorrect usernames can lead to this error.
   
2. **Check Tenant Membership:**
   - Ensure that the user account is part of the correct directory or tenant required to access the application.
   
3. **Application Tenant Configuration:**
   - Check if the application has been configured to the correct tenant for user sign-in.
   
4. **Identify the User as Internal or Guest:**
   - Determine if the user should be added as a guest to access the application.

#### Common Issues:
- Incorrect username input.
- User not added to the correct directory or tenant.
- Application configured with the wrong tenant.
- User status is not set to guest when required.

#### Step-by-Step Resolution Strategies:
1. **Correct Username Entry:**
   - Ensure that the user inputs the correct username.
   
2. **Add User to the Tenant:**
   - If the user is not part of the tenant, add them as a guest user using the following steps:
     - Go to Azure Active Directory portal.
     - Select "Users" and then choose "New guest user."
     - Follow the prompts to add the user as a guest in the tenant.
     
3. **Check Application Tenant Settings:**
   - Verify that the application is set up with the correct tenant for user sign-in.
   
4. **User Account Validation:**
   - Confirm with the user if they should have access to the application and adjust their status accordingly.

#### Additional Notes or Considerations:
- Some applications require users to be added as guests to access them from external directories.
- Ensure that the user account is active and does not have any restrictions that prevent access.
- Review the application's documentation for specific instructions on handling user accounts and tenants.
- Regularly monitor and update user access rights to prevent similar issues in the future.