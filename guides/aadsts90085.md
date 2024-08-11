# AADSTS90085: OrgIdWsFederationSltRedemptionFailed - The service is unable to issue a token because the company object hasn't been provisioned yet.


## Troubleshooting Steps
**Troubleshooting Guide for Error Code AADSTS90085 - OrgIdWsFederationSltRedemptionFailed**

**Initial Diagnostic Steps:**
1. Verify the identity provider (IdP) configuration.
2. Check if the company object has been provisioned in the directory.
3. Review the federation settings for any misconfigurations.
4. Validate the token issuance process.
5. Confirm the user's access rights and permissions.

**Common Issues that Cause this Error:**
1. Misconfigured federation settings between the identity provider and Azure AD.
2. Incomplete provisioning of the company object in the directory.
3. Incorrect user permissions or roles assigned within the Azure AD.
4. Token issuance failure due to a mismatch in the signing keys.
5. Network connectivity issues affecting the token redemption process.

**Step-by-Step Resolution Strategies:**
1. **Verify IdP Configuration:**
   - Ensure the IdP settings match the configuration required by Azure AD.
   
2. **Provision Company Object:**
   - Check if the company object has been created and provisioned in the Azure AD directory.

3. **Review Federation Settings:**
   - Validate the federation settings between the IdP and Azure AD for accuracy.
   
4. **Confirm Token Issuance:**
   - Troubleshoot and resolve any token issuance failures in the authentication flow.
   
5. **Check User Permissions:**
   - Ensure that the user attempting to access has the necessary roles and permissions in Azure AD.

**Additional Notes or Considerations:**
- Consider checking the logs for more detailed error messages to pinpoint the root cause.
- Ensure that the Azure AD Connect configuration is up to date and functioning correctly for identity synchronization.

**Documentation for Guidance:**
- Microsoft provides detailed documentation on Azure AD error codes and troubleshooting steps. You can refer to the official documentation [here](https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/errors-listing#:~:text=AADSTS90085%20%2D%20OrgIdWsFederationSltRedemptionFailed%20%2D%20The%20service%20is%20unable%20to,made%20for%20the%20company%20object.&text=The%20application%20is%20seeking%20a,user%20consent%20for%20an%20application.).