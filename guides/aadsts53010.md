
# AADSTS53010: ProofUpBlockedDueToSecurityInfoAcr - Cannot configure multifactor authentication methods because the organization requires this information to be set from specific locations or devices.


## Introduction

This guide will help resolve issues related to
proofupblockedduetosecurityinfoacr - cannot configure multifactor authentication

methods because the organization requires this information to be set from
specific locations or devices..


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


### Error Code: AADSTS53010 - ProofUpBlockedDueToSecurityInfoAcr


#### Initial Diagnostic Steps:

1. **Verify the Error:** Ensure that the error code is indeed AADSTS53010 with

   the specified description.
2. **Check Authentication Settings:** Confirm if multifactor authentication

   methods have been configured for the user account.
3. **Review Security Policies:** Determine if the organization has specific

   requirements for setting up security information.


#### Common Issues Causing this Error:

1. **Restrictive Security Policies:** Organization policies may limit the setup

   of multifactor authentication to specific locations or devices.
2. **Device Restrictions:** User accounts may be restricted to configure

   security info from particular devices.
3. **Configuration Errors:** Incorrect setup of security information or

   misconfigured authentication settings.


#### Step-by-Step Resolution Strategies:

1. **Contact IT Support:** If possible, contact the organization's IT support

   team for guidance and clarification regarding the specific requirements for
   setting up multifactor authentication.

2. **Check Security Policies:** Review the organization's security policies or

   documentation to understand the restrictions placed on setting up security
   information.

3. **Use Allowed Locations/Devices:** If the organization requires specific

   locations or devices for configuring security info, ensure you are complying
   with these requirements. Access the authentication setup from the specified
   location or device.

4. **Reset Security Info:** If allowed, try resetting the security information

   from a permitted location or device. Proceed with setting up multifactor
   authentication as per the organization's guidelines.

5. **Verify Account Permissions:** Ensure that your account has the necessary

   permissions to configure security information. Check if any roles or access
   restrictions are affecting the process.

6. **Clear Cache and Cookies:** Sometimes, clearing the cache and cookies of the

   browser might resolve authentication issues and allow you to proceed with the
   setup.


#### Additional Notes or Considerations:


* **Organization Guidance:** Follow any specific instructions or guidance

  provided by your organization's IT team or security policies.

* **Test in a Controlled Environment:** If the setup cannot be done from your

  current location or device, attempt the configuration from an approved
  environment.

* **Stay Informed:** Keep yourself informed about any updates or changes in the

  organization's security policies that may impact authentication methods.

By following the outlined troubleshooting guide, you should be able to address
the AADSTS53010 error related to multifactor authentication configuration
restrictions effectively. If the issue persists, contact your organization's
support for further assistance.