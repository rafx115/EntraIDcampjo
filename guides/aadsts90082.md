
# AADSTS90082: OrgIdWsFederationNotSupported - The selected authentication policy for the request isn't currently supported.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS90082: OrgIdWsFederationNotSupported

#### Initial Diagnostic Steps:
1. Verify the specific scenario in which the error occurs - authentication flow, application integration, etc.
2. Check the Azure AD logs to gather more detailed information about the error.
3. Confirm the authentication policy and settings configured for the application.

#### Common Issues Causing the Error:
1. Outdated or misconfigured authentication policies in Azure AD.
2. Unsupported security protocols or configurations in the application or integration process.
3. Incompatible application configuration with the selected authentication policy.
4. Misconfigured trust relationships between the relying party and the identity provider.

#### Step-by-Step Resolution Strategies:
1. **Review Authentication Policies**:
    - Check the Azure AD policies applied to the application and ensure they are up to date.
    - Verify that the selected policy aligns with the supported authentication methods.

2. **Adjust Application Settings**:
    - Update the application settings to match the supported authentication policies.
    - Ensure the application configuration is compatible with the specified policy.

3. **Check Security Protocols**:
    - Confirm that the application supports the required security protocols (e.g., WS-Federation) as specified in the policy.
    - Make necessary adjustments to enable the supported protocols.

4. **Verify Trust Relationships**:
    - Review the trust setup between the application and the identity provider.
    - Ensure that the relying party configurations are correctly aligned with the authentication policy requirements.

5. **Test and Monitor**:
    - Test the authentication flow post-adjustments to validate the resolution.
    - Monitor the Azure AD logs for any recurring errors or warnings.

#### Additional Notes or Considerations:
- Keep track of any changes made during the troubleshooting process for future reference.
- Ensure that all stakeholders are informed about the resolution steps taken.
- Regularly review and update the authentication policies and application settings to prevent similar issues.

#### Documentation for Guidance:
- For detailed information and step-by-step guides on Azure AD authentication policies and configurations, refer to the official Microsoft documentation: [Azure AD Authentication Documentation](https://docs.microsoft.com/en-us/azure/active-directory/)
  
By following the outlined troubleshooting steps and considering the common issues causing the error, you should be able to address the AADSTS90082 error effectively. If the issue persists, consider reaching out to Microsoft support for further assistance.