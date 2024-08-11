
# AADSTS50131: ConditionalAccessFailed - Indicates various Conditional Access errors such as bad Windows device state, request blocked due to suspicious activity, access policy, or security policy decisions.


## Introduction

This guide will help resolve issues related to conditionalaccessfailed - 
indicates various conditional access errors such as bad windows device state,

request blocked due to suspicious activity, access policy, or security policy
decisions..


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


### Troubleshooting Guide for Error Code AADSTS50131 - ConditionalAccessFailed


#### Initial Diagnostic Steps:

1. **Confirm Error Code**: Ensure that the error code displayed is indeed
   AADSTS50131.
2. **Check User Activity**: Verify the recent activities of the user
   encountering the error.
3. **Review Conditional Access Policies**: Check the Conditional Access policies
   that are in place.


#### Common Issues:

1. **Bad Windows Device State**: This can occur if the user's device does not
   meet the security requirements.
2. **Request Blocked Due to Suspicious Activity**: If there have been recent
   suspicious activities from the user or device.
3. **Access Policy Decisions**: Errors may arise due to conflicts with
   established access policies.
4. **Security Policy Decisions**: Non-compliance with security policies can
   trigger this error.


#### Step-by-Step Resolution Strategies:

1. **Check User Device**: Ensure that the user's Windows device meets the
   security requirements stipulated in the Conditional Access policies.
2. **Review Suspicious Activity**: Investigate and address any suspicious
   activities associated with the user and device.
3. **Evaluate Access Policies**: Review and update any conflicting access
   policies to align with the current requirements.
4. **Adjust Security Policies**: Make necessary adjustments to the security
   policies for compliance.


#### Additional Notes or Considerations:

1. **User Communication**: Inform the user of the error and any actions required
   from their end.
2. **Policy Review**: Regularly review and update Conditional Access policies to
   prevent such errors.
3. **Admin Support**: Seek assistance from administrators or IT support if
   needed for policy adjustments or device evaluations.

By following these steps and strategies, you should be able to diagnose and
resolve the AADSTS50131 error related to Conditional Access issues effectively.