# AADSTS50076: UserStrongAuthClientAuthNRequired - Due to a configuration change made by the admin such as a Conditional Access policy, per-user enforcement, or because you moved to a new location, the user must use multifactor authentication to access the resource. Retry with a new authorize request for the resource.

## Introduction

This guide will help resolve issues related to
userstrongauthclientauthnrequired - due to a configuration change made by the
admin such as a conditional access policy, per-user enforcement, or because you
moved to a new location, the user must use multifactor authentication to access
the resource. retry with a new authorize request for the resource..

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
  [Azure AD documentation](https://learn.microsoft.com/en-us/azure/active-directory/)
  for more details.

## Troubleshooting Steps

Troubleshooting steps could not be generated due to an error.

## Troubleshooting Steps

Troubleshooting steps could not be generated due to an error.

## Troubleshooting Steps

### Troubleshooting Guide for Error Code AADSTS50076: UserStrongAuthClientAuthNRequired

#### Initial Diagnostic Steps:

1. Confirm if the user is subject to a Conditional Access policy requiring
   multifactor authentication.
2. Verify user's current location and if they have moved to a new geographic
   region recently.
3. Check for any recent configuration changes by the admin that may have
   triggered the error.
4. Ensure the user's account is not locked or flagged for unusual activity.

#### Common Issues:

1. Conditional Access Policies: Policies requiring multifactor authentication
   for specific users or based on conditions might result in this error.
2. User's Location Change: Moving to a new location may trigger security
   measures that mandate multifactor authentication.
3. Recent Admin Changes: Modifications made by the admin, such as enabling
   per-user enforcement, can lead to this error.

#### Step-by-Step Resolution Strategies:

1. **Retry the Authorization Request:**
   * Request the user to retry accessing the resource to trigger the multifactor
     authentication prompt.
2. **Review Conditional Access Policies:**
   * Admin should review and adjust conditional access policies to ensure they
     align with the user's access requirements.
3. **User Location Verification:**
   * Confirm the user's current location and have them complete the multifactor
     authentication process accordingly.
4. **Admin Configuration Check:**
   * Admin should scrutinize recent changes and configurations to identify any
     settings conflicting with the user's access.
5. **User Communication:**
   * Communicate the situation clearly to the user, explaining the need for
     multifactor authentication and guiding them through the process.

#### Additional Notes:

* **User Training:** Provide users with training on multifactor authentication
  processes to facilitate smoother access in such scenarios.
* **Admin Monitoring:** Regularly monitor and review Conditional Access policies
  to ensure they meet the organization's security and access requirements.
* **Consider SSO:** If applicable, explore the use of Single Sign-On solutions
  that can streamline authentication processes for users.

By following these steps and considerations, you can effectively address and
resolve the AADSTS50076 error caused by the UserStrongAuthClientAuthNRequired
scenario.
