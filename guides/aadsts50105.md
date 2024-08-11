# AADSTS50105: EntitlementGrantsNotFound - The signed in user isn't assigned to a role for the signed in app. Assign the user to the app. To learn more, see the troubleshooting article for errorAADSTS50105.


## Introduction

This guide will help resolve issues related to entitlementgrantsnotfound - the

signed in user isn't assigned to a role for the signed in app. assign the user
to the app. to learn more, see the troubleshooting article for
erroraadsts50105..


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


### Troubleshooting Guide for Error Code AADSTS50105: EntitlementGrantsNotFound


#### Initial Diagnostic Steps:

1. **Confirm User Role Assignment:** Verify if the user is assigned a role for

   the specific application that is causing the error.
2. **Check Application Permissions:** Review the permissions and roles set up

   within the application that the user is trying to access.
3. **Review Recent Changes:** Check if any recent changes were made to user

   roles, application configurations, or permission settings that could have
   triggered the error.
4. **Check for Service Outages:** Verify if there are any ongoing service

   outages or disruptions affecting the authentication process.


#### Common Issues that Cause this Error:

1. **Role Assignment Issues:** The user may not be assigned the required role

   within the application.
2. **Permission Settings:** Incorrect or insufficient permissions granted to the

   user for the application.
3. **User Account Sync:** Delayed synchronization of user account roles and

   permissions with the application.
4. **Misconfigured Application Settings:** Incorrectly configured application

   roles or permissions causing access issues for the user.


#### Step-by-Step Resolution Strategies:

1. **Verify User Role Assignment:** 

   * Access the application's admin portal.

   * Locate the user's account and ensure they are assigned the necessary role.

   * If the user is missing a role, assign the appropriate role to the user.

2. **Check Application Permissions:** 

   * Review the application's permission settings to ensure the user has the

     required access.
   * Adjust permissions if necessary to align with the user's role and access

     needs.

3. **Trigger User Account Sync:** 

   * Force a synchronization of the user's account with the application.

   * This can often resolve issues related to delayed role assignments.

4. **Verify Application Configuration:** 

   * Cross-verify the application's role definitions and permissions.

   * Ensure that roles are correctly set up and linked to user entitlements.

5. **Reset User Authentication:**    * Have the user sign out of the application 
and sign back in to trigger a

     fresh authentication process.
   * This can sometimes refresh user entitlements and resolve access issues.


#### Additional Notes or Considerations:


* **Documentation and Support:** Refer to the troubleshooting article for error

  AADSTS50105 provided by the authentication service for specific guidance.

* **Collaborate with IT Admins:** Work closely with IT administrators or

  application owners to troubleshoot and resolve role assignment issues
  effectively.

* **Regular Monitoring:** Periodically review user roles and permissions to

  prevent future occurrence of this error.

* **Logging and Audit Trails:** Utilize logs and audit trails to track changes

  in user roles and permissions for better troubleshooting and monitoring.

By following these steps and considerations, you should be able to address the
error code AADSTS50105 related to EntitlementGrantsNotFound effectively. If the
issue persists, consider seeking assistance from the application's support or IT
team for further investigation.