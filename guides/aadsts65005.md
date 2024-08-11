
# AADSTS65005: MisconfiguredApplication - The app required resource access list doesn't contain apps discoverable by the resource, or the client app has requested access to resource, which wasn't specified in its required resource access list or Graph service returned bad request or resource not found. If the app supports SAML, you might have configured the app with the wrong Identifier (Entity). To learn more, see the troubleshooting article for errorAADSTS650056.


## Introduction

This guide will help resolve issues related to misconfiguredapplication - the

app required resource access list doesn't contain apps discoverable by the
resource, or the client app has requested access to resource, which wasn't
specified in its required resource access list or graph service returned bad
request or resource not found. if the app supports saml, you might have
configured the app with the wrong identifier (entity). to learn more, see the
troubleshooting article for erroraadsts650056..


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


### Troubleshooting Guide for Error Code AADSTS65005: Misconfigured Application


#### Initial Diagnostic Steps:

1. **Confirm Error Description**: Start by verifying that the error is indeed
   AADSTS65005 with the specific description relating to a Misconfigured
   Application.

2. **Check App Configuration**: Ensure the configuration settings of the
   application in question, especially concerning resource access, client app
   permissions, and any SAML configurations.

3. **Review Service Requests**: If applicable, review the requests made by the
   client app to identify any discrepancies with the expected resource access
   list or requested permissions.


#### Common Issues:

1. **Missing Resource Access**: The app's required resource access list may not
   include apps discoverable by the resource it is trying to access.

2. **Incorrect Permissions Request**: The client app may be requesting access to
   a resource that is not specified in its required resource access list.

3. **SAML Misconfiguration**: If SAML is supported, the app might have the wrong
   Identifier (Entity) configured, leading to authentication issues.

4. **Bad Request/Resource Not Found**: Issues with the Graph service can also
   cause this error.


#### Step-by-Step Resolution Strategies:

1. **Review App Configuration**:

   * Check the app's resource access list and ensure it includes all necessary

     resources.
   * Verify that the client app's permissions align with the resources it needs

     to access.

2. **Validate SAML Configuration** (if applicable):

   * Double-check the Identifier (Entity) configuration in the app if SAML is

     being used.
   * Ensure that the SAML settings match the requirements of the authentication

     provider.

3. **Investigate Graph Service Errors**:

   * If the error involves bad requests or resource not found from the Graph

     service, investigate and address those specific issues.

4. **Update Permissions and Resource Access**:
   * Adjust the permissions requested by the client app to match the required

     resource access list.
   * Update the app configuration to include all the necessary resources.


#### Additional Notes or Considerations:


* **Documentation**: Refer to Microsoft's documentation or the specific service

  provider's documentation for detailed guidance on resolving AADSTS65005
  errors.


* **Testing**: After making any changes, thoroughly test the application to

  ensure that the error has been resolved and that the desired resource access
  is functioning correctly.


* **Consultation**: If the issue persists despite troubleshooting efforts,

  consider reaching out to support resources provided by Microsoft or the
  service provider for further assistance.

By following these steps and considerations, you should be able to diagnose and
resolve the AADSTS65005 error related to a Misconfigured Application
effectively.