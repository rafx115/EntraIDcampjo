# AADSTS90095: AdminConsentRequiredRequestAccess- In the Admin Consent Workflow experience, an interrupt that appears when the user is told they need to ask the admin for consent.

## Introduction

This guide will help resolve issues related to
adminconsentrequiredrequestaccess- in the admin consent workflow experience, an
interrupt that appears when the user is told they need to ask the admin for
consent..

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

**Troubleshooting Guide for AADSTS90095 Error Code:**

**Description:** The AADSTS90095 error code indicates that the user needs to
request admin consent in the Admin Consent Workflow experience. This error
occurs when a user attempts to access resources that require admin consent, and
the system prompts the user to ask the admin for permission.

**Initial Diagnostic Steps:**

1. Verify if the user has permissions to access the resource.
2. Check the application settings in Azure AD to see if admin consent is
   required.
3. Confirm if the user is a global admin or has the necessary permissions to
   grant admin consent.
4. Check if the application permissions have been configured correctly.

**Common Issues that Cause this Error:**

1. User lacks the necessary permissions to access the resource that requires
   admin consent.
2. Application settings in Azure AD are misconfigured, triggering the need for
   admin consent.
3. User attempting to access the resource is not an admin or does not have the
   appropriate role to grant consent.
4. Application permissions are not correctly configured, leading to the error
   prompt.

**Step-by-Step Resolution Strategies:**

1. **Ensure User Permissions:**

   * Confirm if the user has the necessary permissions to access the resource.
     If not, contact the admin to grant access or request admin consent.

2. **Check Azure AD Application Settings:**

   * Review the application settings in Azure AD to ensure that admin consent is
     configured correctly. Modify the settings if needed.

3. **Grant Admin Consent:**

   * If the user is not an admin, they need to request admin consent. The user
     should ask the admin to grant the necessary permissions.

4. **Verify Application Permissions:**

   * Check the application permissions to ensure they are correctly configured.
     Adjust the permissions as required to resolve the error.

5. **Clear Browser Cache and Cookies:**
   * Sometimes, cache issues can cause authentication problems. Clear the
     browser cache and cookies, then try accessing the resource again.

**Additional Notes or Considerations:**

* Ensure that the admin understands the request for consent and is aware of the
  implications.
* Encourage users to follow security best practices and only request admin
  consent when necessary.
* If the issue persists, consider reaching out to Microsoft support or the
  application developer for further assistance.

By following these troubleshooting steps, you should be able to address the
AADSTS90095 error code related to AdminConsentRequiredRequestAccess effectively.
