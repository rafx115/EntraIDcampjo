# AADSTS20033: FedMetadataInvalidTenantName - There's an issue with your federated Identity Provider. Contact your IDP to resolve this issue.


## Troubleshooting Steps
Certainly! The error code **AADSTS20033** is typically encountered when there is an issue with the federated identity provider setup in Azure Active Directory (Azure AD). Below is a detailed troubleshooting guide for addressing this error.

### Troubleshooting Guide for AADSTS20033

#### Initial Diagnostic Steps
1. **Replication of the Error**: Confirm the error message by attempting to access the application that prompted the error. Note the exact wording and context in which the error appears.

2. **User Context**: Identify if the issue is affecting all users or just specific ones. This will help narrow down the problem.

3. **Review User Credentials**: Ask affected users to verify their credentials, ensuring they are using the correct username and password.

4. **Check the Application Registration**: Log into the Azure portal and verify the application registration's configuration, ensuring it’s correctly set up to use the federated identity provider.

#### Common Issues that Cause This Error
1. **Incorrect Tenant Name**: The tenant name in the federation metadata might not match the tenant associated with Azure AD.

2. **Incorrectly Configured Identity Provider**: There may be misconfigurations in the settings of the federated identity provider, such as metadata URLs or certificates.

3. **Service Principal Issues**: The service principal for the application might not have adequate permissions or may not exist for the federated identity provider.

4. **Expired or Invalid Certificates**: The certificates used for signing or encryption in the federation setup could be expired or invalid.

5. **DNS Issues**: There may be DNS resolution issues that prevent Azure AD from reaching the identity provider.

#### Step-by-Step Resolution Strategies
1. **Verify Tenant Name**:
   - Go to the Azure portal.
   - Navigate to Azure Active Directory > Properties and check the Primary Domain Name.
   - Ensure that the tenant name in the federation metadata matches this name.

2. **Check Federation Metadata**:
   - Access the federation metadata URL configured for the identity provider. Ensure that the content is available and correctly represents the configuration.
   - Compare it to the expected configuration provided by your identity provider.

3. **Review Identity Provider Configuration**:
   - Navigate to Azure Active Directory > Enterprise Applications.
   - Select the application reporting the error and review the settings under "Single sign-on". Correct any discrepancies in the setup.
   - Ensure that the correct application identifier (Client ID/Domain) is being used.

4. **Inspect Certificates**:
   - Navigate to Azure Active Directory > Enterprise Applications > [Your Application] > Single sign-on > Certificates & secrets.
   - Check if the signing certificates are valid and not expired. Replace expired certificates if necessary.

5. **Check Application Permissions**:
   - Ensure the application has been granted the right permissions to access Azure AD.
   - Review the enterprise application permissions and consent settings.

6. **Test Connectivity**:
   - Perform a DNS lookup to check if the identity provider’s URL is resolvable.
   - Use tools like `nslookup` or `curl` to test the reachability of the federation metadata URL.

#### Additional Notes or Considerations
- **Support Contact**: If the issue persists after your checks, contact your Identity Provider (IDP) for assistance. They may have specific configurations or updates that need to be made on their side.
- **Azure Logs**: Consider looking into Azure AD logs for additional information regarding authentication failures. You can find logs under Azure Active Directory > Sign-ins.

#### Documentation and Resources
- [Azure Active Directory Docs](https://docs.microsoft.com/en-us/azure/active-directory/)
- [Configure SAML-based single sign-on](https://docs.microsoft.com/en-us/azure/active-directory/develop/enterprise-apps-saml-sso)
- [Troubleshooting SSO](https://docs.microsoft.com/en-us/azure/active-directory/develop/troubleshoot-sso)

#### Test Accessibility of Documentation
- Ensure the above documentation links can be opened in a browser to confirm their accessibility.

#### Advice for Data Collection
1. **Gather Logs**: Collect sign-in logs from Azure AD related to the authentication attempts, including timestamps and user identifiers.
2. **Record Metadata URLs**: Document the federation metadata URLs and their responses.
3. **Configuration Snapshots**: Take screenshots of the relevant Azure portal settings for comparison.
4. **User Feedback**: Collect feedback from affected users about their experience and if they notice any patterns (e.g., specific times of access, devices, etc.).

By following these steps, you should be able to diagnose and resolve the **AADSTS20033** error effectively.