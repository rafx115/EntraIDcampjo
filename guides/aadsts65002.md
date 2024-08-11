# AADSTS65002: Consent between first party application '{applicationId}' and first party resource '{resourceId}' must be configured via preauthorization - applications owned and operated by Microsoft must get approval from the API owner before requesting tokens for that API. A developer in your tenant might be attempting to reuse an App ID owned by Microsoft. This error prevents them from impersonating a Microsoft application to call other APIs. They must move to another app ID they register.

## Introduction

This guide will help resolve issues related to consent between first party
application '{applicationid}' and first party resource '{resourceid}' must be
configured via preauthorization - applications owned and operated by microsoft
must get approval from the api owner before requesting tokens for that api. a
developer in your tenant might be attempting to reuse an app id owned by
microsoft. this error prevents them from impersonating a microsoft application
to call other apis. they must move to another app id they register..

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

### Error Code: AADSTS65002 Troubleshooting Guide

#### Description:

The error code AADSTS65002 indicates that consent between a first-party
application and first-party resource must be configured via preauthorization.
This typically occurs when a developer within your tenant attempts to reuse an
App ID owned by Microsoft, which prevents them from impersonating a Microsoft
application to call other APIs.

#### Initial Diagnostic Steps:

1. Verify the specific applications and resources involved in the error message.
2. Confirm the ownership and permissions associated with the App ID and resource
   ID.
3. Check if any recent changes or configurations have been made that may have
   triggered this error.

#### Common Issues:

1. Attempting to use a Microsoft-owned App ID without proper authorization.
2. Misconfiguration of permissions between the application and resource.
3. Changes in APIs or permissions that were not properly managed.

#### Step-by-Step Resolution Strategies:

1. **Identify the Issue:**

   * Confirm the specific App ID and resource ID causing the error.
   * Determine if the developer is attempting to use a Microsoft-owned App ID.

2. **Register a New App ID:**
   * Advise the developer to register a new App ID that they can use for the
     application.

3. **Configure Consent:**
   * Ensure that proper consent and permissions are set between the new App ID
     and the required resources.

4. **Update Application Settings:**
   * Instruct the developer to update the application settings to use the newly
     registered App ID.

5. **Testing and Verification:**
   * Test the application to ensure that the error is resolved and that the new
     App ID is working correctly.

6. **Monitor for Recurrence:**
   * Keep an eye on the application to verify that the error does not reoccur.

#### Additional Notes or Considerations:

* Verify that the permissions and configurations are aligned with Microsoft's
  policies and guidelines.
* Communicate clearly with the developer to ensure they understand the reasons
  behind the error and the steps taken to resolve it.
* Regularly review and update permissions and configurations to prevent similar
  issues in the future.

By following these steps, you should be able to address the AADSTS65002 error
and allow the developer to continue using the application with the appropriate
permissions and configurations.
