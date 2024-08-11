
# AADSTS90087: OrgIdWsFederationMessageCreationFromUriFailed - An error occurred while creating the WS-Federation message from the URI.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS90087: OrgIdWsFederationMessageCreationFromUriFailed

#### Initial Diagnostic Steps:
1. Confirm the specific circumstances under which this error occurs - note down any patterns or recent changes that might be relevant.
2. Check the error message for more details to understand the context of the issue.
3. Verify if other users in your organization are experiencing the same problem.

#### Common Issues that Cause this Error:
1. Incorrect configuration settings related to WS-Federation within the Identity Provider (IdP) or the relying party application.
2. Mismatch between the requested URI and the configured IdP settings.
3. Issues with the token signing or encryption keys.
4. Connectivity problems between the IdP and the relying party application.

#### Step-by-Step Resolution Strategies:
1. **Verify Configuration Settings:**
    - Review the WS-Federation configuration settings in both the IdP and the relying party application to ensure they match.
    - Check if the URI used for WS-Federation authentication is accurate and updated.

2. **Check Token Signing/Encryption Keys:**
    - Ensure that the token signing and encryption keys in both the IdP and the relying party application are valid and in sync.
    - If keys have expired or been rotated, update them accordingly.

3. **Troubleshoot Connectivity Issues:**
    - Verify the network connectivity between the IdP and the relying party application.
    - Check firewall settings and make sure the necessary ports are open for communication.

4. **Review Logs and Additional Information:**
    - Analyze log files or error details for more specific clues that might pinpoint the exact issue.
    - Look for any recent changes or updates that might have triggered the error.

#### Additional Notes or Considerations:
- It's essential to involve your IT team or system administrators if the issue involves configuration changes or access to the IdP settings.
- Keep a record of any changes made during the troubleshooting process to revert if needed.

#### Documentation for Guidance:
For detailed instructions on troubleshooting WS-Federation issues in Azure Active Directory, you can refer to the official Microsoft documentation:
- [Troubleshoot WS-Federation service provider integration issues in Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/hybrid/tshoot-nexcessity)
- [Troubleshoot SAML SSO integration issues in Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/troubleshoot-tenant-mismatch-error)

By following the steps outlined above and leveraging the provided resources, you should be able to diagnose and resolve the error code AADSTS90087 effectively. If you encounter any specific challenges during the process, feel free to seek further assistance from your organization's IT support team.