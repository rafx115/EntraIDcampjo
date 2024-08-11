# AADSTS90072: PassThroughUserMfaError - The external account that the user signs in with doesn't exist on the tenant that they signed into; so the user can't satisfy the MFA requirements for the tenant. This error also might occur if the users are synced, but there is a mismatch in the ImmutableID (sourceAnchor) attribute between Active Directory and Microsoft Entra ID. The account must be added as an external user in the tenant first. Sign out and sign in with a different Microsoft Entra user account. For more information, please visitconfiguring external identities.

## Introduction
This guide will help resolve issues related to passthroughusermfaerror - the external account that the user signs in with doesn't exist on the tenant that they signed into; so the user can't satisfy the mfa requirements for the tenant. this error also might occur if the users are synced, but there is a mismatch in the immutableid (sourceanchor) attribute between active directory and microsoft entra id. the account must be added as an external user in the tenant first. sign out and sign in with a different microsoft entra user account. for more information, please visitconfiguring external identities..

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
### Troubleshooting Guide for Error Code AADSTS90072: PassThroughUserMfaError

#### Initial Diagnostic Steps:
1. **Confirm Error Code:** Verify that the error code displayed is AADSTS90072 with the specific message mentioning PassThroughUserMfaError.
2. **User Account Verification:** Determine which external account the user is trying to sign in with and ensure it exists in the tenant they are attempting to access.
3. **Check Synchronization:** If users are synced, investigate whether there is an issue with the ImmutableID (sourceAnchor) attribute between Active Directory and Microsoft Entra ID.

#### Common Issues:
1. **Non-existent External Account:** The user's external account does not exist in the tenant they are trying to sign into, leading to MFA requirements being unsatisfiable.
2. **Mismatch in ImmutableID:** If user accounts are synced, a discrepancy in the value of the ImmutableID attribute between Active Directory and Microsoft Entra ID can trigger the error.

#### Step-by-Step Resolution Strategies:
1. **Verify External Account Existence:**
    - Ensure the external account the user is trying to sign in with is added as an external user in the tenant.
    - If not added, follow the process to add the external account as a user in the tenant.

2. **Check ImmutableID Matching:**
    - Compare the ImmutableID (sourceAnchor) attribute value between the user's account in Active Directory and their corresponding account in Microsoft Entra ID.
    - If there is a mismatch, correct the ImmutableID attribute to match between both sources.

3. **Sign Out and Sign In with Different Account:**
    - Instruct the user to sign out of their current Microsoft Entra user account.
    - Have them sign back in with a different Microsoft Entra account that is properly set up and exists in the tenant.

#### Additional Notes or Considerations:
- **External Identity Configuration:** If dealing with external identities, refer to the documentation on configuring external identities for detailed instructions on setting up and managing external accounts within the tenant.
- **Support Channels:** If further assistance is required, the user can reach out to their organization's IT support team or Microsoft support for help in resolving the AADSTS90072 error.
- **Regular Verification:** Periodically check and ensure that external accounts are correctly set up and synced with Active Directory to prevent potential synchronization issues that could trigger errors like PassThroughUserMfaError.

By following these steps and understanding the common causes of the AADSTS90072 error with the PassThroughUserMfaError description, users can effectively troubleshoot and resolve the issue related to external account sign-ins and MFA requirements within their tenant environment.