# AADSTS90094: AdminConsentRequired - Administrator consent is required.

## Introduction
This guide will help resolve issues related to adminconsentrequired - administrator consent is required..

## Prerequisites
- Access to the Azure AD portal with administrator privileges.
- The user must have already set up MFA.

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
- Check for any Azure AD conditional access policies that might be affecting the MFA process.
- Consider any additional security measures that might be in place.

## Additional Notes
- Refer to the [Azure AD documentation](https://learn.microsoft.com/en-us/azure/active-directory/) for more details.


## Troubleshooting Steps
Troubleshooting steps could not be generated due to an error.

## Troubleshooting Steps
Troubleshooting steps could not be generated due to an error.

## Troubleshooting Steps
**Troubleshooting Guide for Error Code AADSTS90094 - AdminConsentRequired**

**Initial Diagnostic Steps:**
1. Verify the nature of the application or service attempting to access resources requiring admin consent.
2. Confirm the roles and permissions of the user encountering the error.
3. Check the Azure Active Directory logs for more detailed error information.
4. Ensure that the app registration and permissions are correctly configured in Azure AD.

**Common Issues Causing This Error:**
1. Insufficient permissions granted to the application in Azure AD.
2. User attempting to access resources does not have required administrative privileges.
3. Misconfigured Azure AD app registration settings.
4. Missing or incorrect consent requirements defined within the app registration.

**Step-by-step Resolution Strategies:**
1. **Request Administrator Consent:**
   - An administrator needs to provide consent for the application to access resources. The admin can go to the provided consent URL in the error message and grant the necessary permissions.
  
2. **Check Application Manifest:**
   - Ensure that the required permissions are correctly listed in the application manifest file. Update the manifest if necessary and save the changes.

3. **Upgrade Permissions:**
   - Update the application permissions to include the required admin consent if they were missing. Save the changes and retry the access.

4. **Verify User Privileges:**
   - Ensure that the user attempting to access the resources has necessary administrative privileges.

**Additional Notes or Considerations:**
- If multiple applications or services are interacting, ensure that all are configured with the correct permissions and consent requirements.
- Regularly review and update the permissions granted to applications in Azure AD to prevent permission-related errors.
- Encourage administrators to regularly check and monitor consent requests for potential security risks.

Remember to test the application after applying the troubleshooting steps to confirm that the error has been resolved successfully.