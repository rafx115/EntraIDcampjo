# AADSTS90085: OrgIdWsFederationSltRedemptionFailed - The service is unable to issue a token because the company object hasn't been provisioned yet.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS90085: OrgIdWsFederationSltRedemptionFailed

The error code **AADSTS90085** indicates that the Azure Active Directory (AAD) is unable to issue a token due to the company object (i.e., the tenant or organization) not being properly provisioned. This can be a significant issue for applications relying on Azure AD for authentication. Below is a detailed troubleshooting guide to help diagnose and resolve this error.

#### Initial Diagnostic Steps

1. **Verify the Error Context**:
   - Understand the context in which the error occurs. Is it during application sign-in or when making API requests?
   - Collect detailed error messages and correlation IDs if available.

2. **Check Azure AD Status**:
   - Go to the Azure Service Health page to check for any ongoing issues affecting Azure AD in your region.

3. **Inspect Azure AD Configuration**:
   - Review the Azure AD settings in the Azure portal. Ensure the tenant is correctly set up.

4. **Review Application Registration**:
   - Ensure that the application that is trying to authenticate is registered properly in Azure AD.

#### Common Issues that Cause This Error
1. **Tenant Not Provisioned**: The tenant is not fully set up in Azure AD.
2. **Incorrect or Missing Federation Settings**: Issues with the federation configuration may prevent valid tokens from being issued.
3. **Domain Verification Issues**: The domain for the organization might not be properly verified or configured.
4. **Service Principal Problem**: The service principal for the application might not exist, or it could be misconfigured.

#### Step-by-Step Resolution Strategies

1. **Confirm Tenant Provisioning**:
   - Log in to the [Azure portal](https://portal.azure.com).
   - Go to **Azure Active Directory** > **Properties**.
   - Check if you can see all expected configurations for the tenant.

2. **Verify Application Configuration**:
   - Navigate to **Azure Active Directory** > **App registrations**.
   - Select the application and check the settings:
     - Ensure **Redirect URIs** are correct.
     - Inspect the **API permissions** and ensure they’re granted.
     - Check the **Manifest** for any discrepancies.

3. **Examine and Update Federation Settings**:
   - If using federated authentication, go to **Azure Active Directory** > **Enterprise applications** > Select your application > **Federation** settings.
   - Ensure all settings are configured according to your federation service.

4. **Check Domain Status**:
   - Under **Azure Active Directory** > **Custom domain names**, check if your domain is listed and verified.
   - If the domain isn’t verified, follow guiding documentation to complete this process.

5. **Examine Service Principal**:
   - Go to **Azure Active Directory** > **Enterprise applications**.
   - Search for your application to ensure the service principal exists.
   - If it’s missing, re-register the application.

6. **Review User Accounts**:
   - Ensure that the user account trying to log in is valid and exists in your Azure AD.

7. **Retry the Authentication**:
   - After making corrections, have the user try to authenticate again.

#### Additional Notes or Considerations

- **Test Different Accounts**: If possible, test with different accounts to verify if the issue is user-specific or tenant-wide.
- **Environment Separation**: Remember to check if the app is being tested in the correct environment (e.g., Development, Staging, Production).
- **Logs and Monitoring**: Utilize Azure AD sign-in logs to gather insights on the failed requests for further analysis.

#### Documentation and Resources
- **Azure AD Documentation**: [Azure Active Directory documentation](https://docs.microsoft.com/en-us/azure/active-directory/)
- **Register an Application**: [How to register an application in Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)

#### Test the Documentation Reachability
You can check the links above to ensure they are reachable. You can do this by simply clicking on the links or copy-pasting them into your browser.

#### Advice for Data Collection
- **Collect Logs**: Prior to making changes, gather logs related to the authentication attempts. Look for specific timestamps where the error occurred.
- **Note Configuration Changes**: Document each change you make to configurations for future reference or rollback if necessary.
- **User Feedback**: Collect feedback from impacted users on the specific error encountered to assist in troubleshooting.

By following these steps and considerations, you should be able to effectively diagnose and resolve the AADSTS90085 error in your Azure AD environment.

Category: Other