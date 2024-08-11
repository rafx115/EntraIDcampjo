# AADSTS53002: ApplicationUsedIsNotAnApprovedApp - The app used isn't an approved app for Conditional Access. User needs to use one of the apps from the list of approved apps to use in order to get access.


## Introduction

This guide will help resolve issues related to
applicationusedisnotanapprovedapp - the app used isn't an approved app for

conditional access. user needs to use one of the apps from the list of approved
apps to use in order to get access..


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

Troubleshooting Guide for Error Code AADSTS53002 -
ApplicationUsedIsNotAnApprovedApp:

Initial Diagnostic Steps:

1. Verify the error message: Confirm that the error message you are receiving is
   indeed AADSTS53002 - ApplicationUsedIsNotAnApprovedApp.

2. Check the user account: Ensure that the user account being used for the
   application has the correct permissions and licenses.
3. Review Conditional Access policies: Check the Conditional Access policies in
   Azure AD to determine if the application you are trying to access is
   restricted.

Common Issues that Cause this Error:

1. Unauthorized application: The application being used is not on the list of
   approved apps configured in the Conditional Access policies.
2. Incorrect user permissions: The user does not have the required permissions
   to access the application.
3. Conditional Access misconfiguration: The Conditional Access policies are not
   correctly configured to allow access to the application.

Step-by-Step Resolution Strategies:

1. Review Conditional Access Policies:

   * Log in to the Azure portal and navigate to Azure Active Directory.

   * Go to Security > Conditional Access.

   * Review the Conditional Access policies to identify if the application is

     restricted.
   * Update the policy to include the application or create a new policy if

     needed.

2. Verify Application Approval:

   * Check with your IT administrator to confirm if the application you are

     using needs to be approved.
   * If the application needs approval, submit a request to have the app added

     to the list of approved apps in the Conditional Access policies.

3. Validate User Permissions:

   * Ensure that the user attempting to access the application has the correct

     permissions assigned.
   * Check the user's group memberships and licenses to verify they have the

     necessary access privileges.

4. Clear Browser Cache and Cookies:
   * Sometimes, clearing the browser cache and cookies can resolve

     authentication issues. Instruct the user to clear their browser cache and
     cookies and attempt to log in again.

Additional Notes or Considerations:


* Ensure that the application being used is accounted for in the Conditional

  Access policies to prevent unauthorized access.

* Communicate with your IT department or Azure AD administrator to understand

  the approval process for applications and to address any policy
  misconfigurations.

* Regularly review and update Conditional Access policies to align with

  organizational security requirements.

If you are unable to resolve the error after following these troubleshooting
steps, consider reaching out to your IT support team or Microsoft support for
further assistance.