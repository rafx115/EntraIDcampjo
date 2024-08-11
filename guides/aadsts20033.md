# AADSTS20033: FedMetadataInvalidTenantName - There's an issue with your federated Identity Provider. Contact your IDP to resolve this issue.


## Troubleshooting Steps
### Troubleshooting Guide: Error Code AADSTS20033 (FedMetadataInvalidTenantName)

#### Initial Diagnostic Steps:
1. **Confirm Error Description:** Ensure that the error message specifically states "FedMetadataInvalidTenantName."
2. **Check Federation Settings:** Look into the federated identity provider (IDP) settings for any misconfigurations.
3. **Review Recent Changes:** Identify any recent changes made to the federated setup that may have triggered the error.
4. **Test Other Federated Applications:** Check if other federated applications are working correctly to isolate the issue.

#### Common Issues:
1. **Incorrect Tenant Name:** The IDP's tenant name configured in Azure Active Directory (AAD) doesn't match the actual tenant name.
2. **Outdated Metadata:** The IDP's metadata may be outdated or invalid, causing authentication failures.
3. **Misconfigured Trust Relationship:** Issues in the trust relationship between Azure AD and the IDP can lead to this error.

#### Step-by-Step Resolution Strategies:
1. **Verification of Tenant Name:**
   - Reach out to the IDP to validate the correct tenant name.
   - Update the tenant name on Azure AD with the correct information.
   
2. **Metadata Update:**
   - Request the IDP to update and share the latest metadata.
   - Update the metadata on Azure AD to reflect the changes.
   
3. **Trust Relationship Checks:**
   - Review the trust relationship settings both on Azure AD and the IDP.
   - Ensure there are no discrepancies in trust settings or certificates.

#### Additional Notes or Considerations:
- Regularly monitor the federated setup to catch any issues early on.
- Have proper communication channels with the IDP for quick issue resolution.
- Check for any Azure service advisories related to federation issues.

#### Documentation for Guidance:
- Microsoft Azure AD Troubleshooting Guide: [Troubleshoot federated single sign-on errors in Azure Active Directory](https://docs.microsoft.com/en-us/azure/active-directory/hybrid/tshoot-sso)

By following these steps and suggestions, you can effectively troubleshoot and resolve the AADSTS20033 error with the FedMetadataInvalidTenantName description.