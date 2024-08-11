
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
