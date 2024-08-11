# AADSTS50079: UserStrongAuthEnrollmentRequired - Due to a configuration change made by the admin such as a Conditional Access policy, per-user enforcement, or because the user moved to a new location, the user is required to use multifactor authentication. Either a managed user needs to register security info to complete multifactor authentication, or a federated user needs to get the multifactor claim from the federated identity provider.

## Introduction
This guide will help resolve issues related to userstrongauthenrollmentrequired - due to a configuration change made by the admin such as a conditional access policy, per-user enforcement, or because the user moved to a new location, the user is required to use multifactor authentication. either a managed user needs to register security info to complete multifactor authentication, or a federated user needs to get the multifactor claim from the federated identity provider..

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
Here is a detailed troubleshooting guide for error code AADSTS50079 (UserStrongAuthEnrollmentRequired):

**Initial Diagnostic Steps:**
1. Verify the exact error message and error code received, which is AADSTS50079 in this case.
2. Confirm whether the user is a managed user (using Azure Active Directory) or a federated user (using a federated identity provider).
3. Check if the user has recently changed locations or if any new Conditional Access policies have been implemented by the admin.

**Common Issues that Cause this Error:**
1. Configuration changes by the admin, such as the implementation of Conditional Access policies requiring multifactor authentication.
2. Per-user enforcement where a specific user is required to complete multifactor authentication as per policy.
3. User's change in location triggering security policies for additional authentication.
4. Missing security information for managed users or failed multifactor authentication for federated users.

**Step-by-Step Resolution Strategies:**
1. For Managed Users:
   a. Instruct the user to sign in to the Azure portal (https://portal.azure.com).
   b. Navigate to "Security info" under their account settings.
   c. Prompt the user to add and verify additional security information for multifactor authentication.
   
2. For Federated Users:
   a. Contact the federated identity provider or IT admin responsible for managing federated services.
   b. Ensure that the federated identity provider is configured correctly to issue the multifactor claim.
   c. Instruct the user to authenticate with the federated identity provider and complete the multifactor authentication process.

**Additional Notes or Considerations:**
1. Admins may need to communicate the policy changes clearly to users affected by the multifactor authentication requirement.
2. Ensure that users follow the recommended security best practices while setting up additional security information for MFA.
3. Continuous monitoring of security policies and user compliance is essential to prevent authentication issues in the future.
4. If the issue persists, users can reach out to their organization's IT support for further assistance with completing the multifactor authentication process.

By following these troubleshooting steps, you should be able to address the UserStrongAuthEnrollmentRequired error caused by the requirement for multifactor authentication due to admin configuration changes or user location updates.