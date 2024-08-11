
# AADSTS50177: ExternalChallengeNotSupportedForPassthroughUsers - External challenge isn't supported for passthrough users.


## Introduction

This guide will help resolve issues related to
externalchallengenotsupportedforpassthroughusers - external challenge isn't

supported for passthrough users..


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

Here is a detailed troubleshooting guide for the error code AADSTS50177 with the
description "ExternalChallengeNotSupportedForPassthroughUsers - External

challenge isn't supported for passthrough users":

**Initial Diagnostic Steps:** 

1. Verify the specific scenario or actions that trigger the error. Determine the
   sequence of events leading up to the error.

2. Check the Azure Active Directory logs or diagnostic reports for more detailed
   information related to the error.

3. Confirm if the affected user accounts are configured as "passthrough users"
   in Azure Active Directory.

**Common Issues that Cause this Error:** 

1. **Incorrect User Configuration**: If the user is configured as a "passthrough
   user," they may not be able to use external challenges for certain
   operations.

2. **Misconfiguration of Conditional Access Policies**: Conditional Access
   policies in Azure AD may not be correctly set up to handle passthrough users
   and external challenges.

3. **Permission Settings**: Insufficient permissions or misconfigured security
   settings can sometimes lead to this error.

**Step-by-Step Resolution Strategies:** 

1. **Review User Settings**:

   * Navigate to the Azure Active Directory portal.

   * Locate the affected user account and check if it is indeed configured as a

     "passthrough user."
   * Consider changing the user's configuration if external challenges are

     required.

2. **Review Conditional Access Policies**:

   * Check the Conditional Access policies that may affect the affected users.

   * Ensure that the policies are correctly set up to accommodate passthrough

     users and external challenges.

3. **Verify User Permissions**:

   * Confirm if the affected users have the necessary permissions to complete

     the operation that triggers the error.
   * Adjust permissions or security settings if needed.

4. **Test Access**:
   * Attempt the action that previously resulted in the error to see if the

     issue persists.
   * If the error continues, review the Azure AD logs for more insights into the

     problem.

**Additional Notes or Considerations:**


* **User Training**: Provide training to users on how to handle operations that

  may not support external challenges for passthrough users.

* **Azure Support**: If the issue persists and troubleshooting steps do not

  resolve the error, consider reaching out to Microsoft Azure support for
  further assistance.

By following these steps, you should be able to troubleshoot and address the
error code AADSTS50177 related to the issue of external challenges not supported
for passthrough users.