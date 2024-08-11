
# AADSTS50170: MissingExternalClaimsProviderMapping - The external controls mapping is missing.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS50170: MissingExternalClaimsProviderMapping

#### Initial Diagnostic Steps:
1. **Check Azure Active Directory Logs**: Look for detailed error messages and any relevant information.
2. **Verify External Mapping Configuration**: Ensure that the external claims provider mapping is correctly set up in your Azure AD.

#### Common Issues:
- Incorrect or missing external control mappings.
- Issues with the configuration of the claims provider.
- Permission or access problems associated with the external claims provider.

#### Step-by-Step Resolution Strategies:
1. **Verify External Claims Provider Mapping**:
   - Navigate to Azure portal > Azure Active Directory > External Claims Providers.
   - Check if the required external claims provider mapping is correctly configured.
  
2. **Update or Create External Claims Provider Mapping**:
   - If the mapping is missing, create a new mapping by selecting the external provider and providing the necessary mapping details.

3. **Check Permissions**:
   - Ensure that the account associated with the external claims provider has the necessary permissions to be used in Azure AD.

4. **Perform a SAML Metadata Update**:
   - If using a SAML-based provider, update the SAML metadata in Azure AD to ensure correct configuration.

5. **Review Error Details**:
   - Analyze the error message in Azure AD logs to get more information on the specific issue.

#### Additional Notes or Considerations:
- It is crucial to understand the external claims provider's requirements and specifications for the mapping configuration.
- Regularly monitoring logs and maintaining up-to-date configurations can prevent this issue from reoccurring.

#### Documentation for Guidance:
- Official Microsoft Documentation: [Azure Active Directory External Claims Providers](https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/external-claims-provider)
- Azure AD Help Center: [Troubleshooting Azure AD Single Sign-On](https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/troubleshoot-single-sign-on)

Following these steps and guidelines should help you diagnose and address the "MissingExternalClaimsProviderMapping" error code AADSTS50170 effectively.