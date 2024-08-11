
# AADSTS50124: ClaimsTransformationInvalidInputParameter - Claims Transformation contains invalid input parameter. Contact the tenant admin to update the policy.


## Introduction

This guide will help resolve issues related to
claimstransformationinvalidinputparameter - claims transformation contains

invalid input parameter. contact the tenant admin to update the policy..


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

Troubleshooting Guide for Error Code AADSTS50124 -
ClaimsTransformationInvalidInputParameter:

Initial Diagnostic Steps:

1. Verify the exact error message and error code (AADSTS50124) to accurately
   identify the issue.
2. Check the Azure Active Directory (AAD) logs for any additional information
   related to the error.
3. Confirm if the issue is user-specific or affecting multiple users.
4. Ensure that the claims transformation policy is configured correctly.

Common Issues that Cause this Error:

1. Incorrect input parameter in the claims transformation policy.
2. Missing or invalid attribute mappings in the policy.
3. Improper configuration of the claims transformation rules.
4. Outdated or conflicting policies affecting the transformation.
5. Lack of permissions for the tenant admin to update the policy.

Step-by-Step Resolution Strategies:

1. Contact the Tenant Admin: Reach out to the tenant admin or the Azure AD
   administrator to update the claims transformation policy. The admin will need
   to review and modify the policy with the correct input parameters.
2. Validate Input Parameters: Verify the input parameters specified in the
   claims transformation policy. Ensure that the parameters are correctly
   formatted and match the expected values.
3. Review Attribute Mappings: Check the attribute mappings in the transformation
   rules. Make sure that the mappings are accurate and align with the claim
   input requirements.
4. Test Policy Changes: After updating the policy, test the changes to ensure
   that the error has been resolved. Use test users or accounts to validate the
   functionality of the claims transformation.
5. Monitor and Audit: Regularly monitor the Azure AD logs and audit the claims
   transformation process to detect any potential issues or errors in real-time.

Additional Notes or Considerations:


* It's crucial to have a clear understanding of how claims transformation

  policies work in Azure AD to troubleshoot effectively.

* Document any policy changes made and the resolution steps taken for future

  reference.

* Stay up to date with Microsoft Azure AD documentation and resources for any

  updates or best practices related to claims transformation policies.

* Consider engaging Microsoft Support for further assistance if the issue

  persists despite following the resolution steps.

By following these steps and considerations, you should be able to effectively
troubleshoot and resolve the AADSTS50124 error related to
ClaimsTransformationInvalidInputParameter in Azure AD.