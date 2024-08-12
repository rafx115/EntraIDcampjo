# AADSTS90072: PassThroughUserMfaError - The external account that the user signs in with doesn't exist on the tenant that they signed into; so the user can't satisfy the MFA requirements for the tenant. This error also might occur if the users are synced, but there is a mismatch in the ImmutableID (sourceAnchor) attribute between Active Directory and Microsoft Entra ID. The account must be added as an external user in the tenant first. Sign out and sign in with a different Microsoft Entra user account. For more information, please visitconfiguring external identities.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS90072 Error

**Error Description:**
AADSTS90072 indicates that a user is trying to authenticate with an external account that doesn't exist in the tenant they've signed into. This can occur due to a mismatch with the Multi-Factor Authentication (MFA) requirements or issues with user synchronization such as problems with the `ImmutableID`.

---

### 1. Initial Diagnostic Steps

- **Review the Error Message:** Verify the complete error message for specifics on the account involved.
- **Test User Sign-in:** Attempt to sign in with a different account within the same tenant to determine if the issue is user-specific or tenant-wide.
- **Check the User's Email:** Ensure the email used to sign in matches what is configured in the tenant.

---

### 2. Common Issues That Cause AADSTS90072

- The user account is not added as an external user in the tenant.
- The `ImmutableID` (sourceAnchor) attribute for synced users may have discrepancies between on-premises Active Directory and Azure Active Directory.
- The user may be attempting to access resources that require MFA without satisfying those requirements.
- The users' accounts may exist in some state of deletion or disablement in Azure AD.
- Network issues or misconfigurations may prevent proper authentication routing.

---

### 3. Step-by-Step Resolution Strategies

#### Step 1: Check User Accounts

- **External User Setup:** Confirm that the user has been added to the tenant as an external user.
  - Navigate to Azure portal > Azure Active Directory > Users > External users.

#### Step 2: Validate Synchronization

- **Check ImmutableID:**
  - If the user is synced from on-premises Active Directory, check the `ImmutableID` value in both environments.
  - Use the Azure AD PowerShell module to retrieve `ImmutableID`:
    ```powershell
    Get-AzureADUser -ObjectId user@domain.com | Select-Object ImmutableId
    ```
  - Verify that the `ImmutableID` matches the corresponding on-premises account.

#### Step 3: Review MFA Requirements

- Ensure that the user meets the MFA requirements configured for the tenant.
- If required, update the user’s MFA settings in Azure AD.

#### Step 4: Add the User as External User, If Needed

- To add a user as an external user:
  - Go to Azure Active Directory > Users > New guest user.
  - Input their email and send an invitation.

#### Step 5: Sign Out and Test

- After making any changes, sign out of any sessions and sign back in using the account you tested.

---

### 4. Additional Notes or Considerations

- **Azure AD Conditional Access Policies:** Review any conditional access policies that might be impacting MFA for users.
- **Tenant Settings:** Consider settings regarding external users and MFA as part of your organization's identity security strategy.

---

### 5. Documentation Where Steps Can Be Found

- Microsoft Documentation about [Azure AD user management](https://docs.microsoft.com/en-us/azure/active-directory/users/groups/manage-groups).
- Understanding [MFA in Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/authentication/howto-mfa-getstarted).
- Azure AD [Sync troubleshooting](https://docs.microsoft.com/en-us/azure/active-directory/hybrid/tshoot-sync-errors).

---

### 6. Advice for Data Collection

If you're still experiencing issues, collect the following data:

- **Event Viewer Logs:** Check the logs on the user’s device for any errors that may give context to the failure.
  - Look under Applications and Services Logs > Microsoft > Windows > ADAudit > Operational.

- **Network Traces:**
  - Use tools like Fiddler or Wireshark to capture the network traffic during the authentication attempt, looking for SSL/TLS issues or service unavailability.

- **Diagnostic Logs via Azure AD:**
  - Use Azure AD sign-in logs to look for any failure codes or problematic patterns surrounding the user's authentication attempts. 
  - You can access these logs in the Azure portal: Azure Active Directory > Sign-ins.

Collecting detailed logs and system events will assist in resolving any underlying issues and provide context for support teams if further escalation is required.