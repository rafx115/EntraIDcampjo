# AADSTS50049: NoSuchInstanceForDiscovery - Unknown or invalid instance.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS50049 Error Code: NoSuchInstanceForDiscovery

#### Initial Diagnostic Steps:
1. Verify that the error code is indeed AADSTS50049 with the description "NoSuchInstanceForDiscovery - Unknown or invalid instance."
2. Check if you are trying to access Microsoft Azure resources, such as Azure Active Directory (AAD) or Microsoft 365.
3. Ensure your browser is not blocking any necessary scripts or cookies required for authentication.

#### Common Issues that Cause this Error:
1. Incorrect URL or instance specified during authentication.
2. Network connectivity issues preventing discovery of the instance.
3. Missing or invalid configuration settings in Azure AD configuration.
4. Incorrect permissions or configurations on the application registration in Azure AD.

#### Step-by-Step Resolution Strategies:
1. **Check the URL**: 
   - Ensure the URL you are using for authentication is correct and includes the valid instance details.
  
2. **Verify Network Connectivity**:
   - Check if your network connection is stable and not blocking any necessary requests to discover the instance.
   
3. **Review Azure AD Configuration**:
   - Verify the Azure AD configuration settings, including the registered endpoints and URLs in the Azure portal.
   
4. **Validate Application Registration**:
   - Make sure that the application registration in Azure AD has the correct permissions and configurations set up.
   
5. **Clear Browser Cache**:
   - Clear your browser's cache and cookies to ensure a clean authentication flow without any stored incorrect data.
   
6. **Try from a Different Network**:
   - If possible, test the authentication from a different network to rule out any network-specific issues.

#### Additional Notes or Considerations:
- In some cases, the error might be due to temporary outages in Microsoft Azure services. Check for any service health notifications from Microsoft.
- Ensure that you have the necessary permissions to make configuration changes in Azure AD.

#### Documentation for Guidance: 
- Microsoft Azure AD troubleshooting documentation: [Azure AD troubleshooting](https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-access-troubleshooting-common-causes-aadsts-errors)

By following the steps outlined above and referring to the Azure AD troubleshooting documentation, you should be able to diagnose and resolve the AADSTS50049 error related to NoSuchInstanceForDiscovery effectively. If the issue persists, consider reaching out to Microsoft support for further assistance.