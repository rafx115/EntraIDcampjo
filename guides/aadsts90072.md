# AADSTS90072: PassThroughUserMfaError - The external account that the user signs in with doesn't exist on the tenant that they signed into; so the user can't satisfy the MFA requirements for the tenant. This error also might occur if the users are synced, but there is a mismatch in the ImmutableID (sourceAnchor) attribute between Active Directory and Microsoft Entra ID. The account must be added as an external user in the tenant first. Sign out and sign in with a different Microsoft Entra user account. For more information, please visitconfiguring external identities.


## Troubleshooting Steps
**Troubleshooting Guide for Error Code AADSTS90072 - PassThroughUserMfaError:**

**Initial Diagnostic Steps:**
1. Confirm the error code AADSTS90072 with the specific description provided - PassThroughUserMfaError.
2. Verify the user's external account sign-in details.
3. Check if the user exists in the tenant they are trying to sign into.
4. Ensure the ImmutableID attribute in Active Directory matches the Microsoft Entra ID.
5. Verify if the user needs to be added as an external user in the tenant.

**Common Issues that Cause this Error:**
1. User does not exist in the tenant they are trying to sign into.
2. Mismatch in the ImmutableID (sourceAnchor) attribute between Active Directory and Microsoft Entra ID.
3. User account needs to be added as an external user in the tenant.

**Step-by-step Resolution Strategies:**
1. **Verify User Existence:**
   - Check if the user exists in the target tenant.
   - If not, add the user as an external user in the tenant.

2. **Sync ImmutableID Attributes:**
   - Ensure the ImmutableID (sourceAnchor) attribute matches between Active Directory and Microsoft Entra ID.
   - Resolve any mismatches in the attribute.

3. **Add User as External User:**
   - If the user needs to be added as an external user, follow the steps to add them to the tenant.

4. **Sign Out and Sign In with Different Account:**
   - Sign out of the current account.
   - Try signing in with a different Microsoft Entra user account that meets the requirements.

**Additional Notes or Considerations:**
- Make sure you have the necessary permissions to modify user accounts in Active Directory and the tenant.
- Double-check all user details and attributes for accuracy before making changes.
- Test the sign-in process with the corrected information to ensure the error is resolved.

**Documentation for Guidance:**
For more detailed steps and guidance on configuring external identities and resolving issues with error code AADSTS90072, refer to the official Microsoft documentation on [configuring external identities](https://docs.microsoft.com/en-us/azure/active-directory/external-identities/). This resource provides in-depth information on managing external users, syncing attributes, and troubleshooting common errors.