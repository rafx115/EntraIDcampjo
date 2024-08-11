# AADSTS70001: UnauthorizedClient - The application is disabled. To learn more, see the troubleshooting article for errorAADSTS70001.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS70001

**Description:** UnauthorizedClient - The application is disabled.

#### Initial Diagnostic Steps:
1. **Check Application Status:** Verify that the application status is not disabled within the Azure Active Directory (Azure AD) tenant.
2. **Verify API Permissions:** Ensure that the necessary API permissions for the application are correctly configured.

#### Common Issues:
- **Application Disabled**: The application might be disabled in Azure AD.
- **Expired Credentials**: Authentication tokens or client secrets have expired.
- **Incorrect Permissions**: The application doesn't have the necessary permissions to access the required resources.

#### Step-by-Step Resolution Strategies:
1. **Check Application Status:**
   - Go to the Azure Portal and navigate to Azure Active Directory.
   - Select "App registrations" and search for your application.
   - Ensure that the application status is set to enabled.

2. **Verify API Permissions:**
   - In the Azure Portal, navigate to the application's API permissions.
   - Make sure that the required permissions are granted.
   - If necessary permissions are missing, add them and grant admin consent.

3. **Check Expiry of Credentials:**
   - Verify if any client secrets or tokens used for authentication have expired.
   - Generate new client secrets if needed and update them in the application configurations.

#### Additional Notes or Considerations:
- **Admin Consent:** Some changes may require admin consent to take effect, so make sure to have the necessary permissions to perform these actions.
- **Log and Monitor:** Enable logging and monitoring to track any changes or issues with the application's status and permissions.

#### Documentation:
- **Microsoft Documentation:** You can find detailed troubleshooting steps and documentation related to Azure AD error codes on the [Microsoft documentation site](https://docs.microsoft.com/en-us/azure/active-directory/errors/aadsts70001).

By following these steps and considering the common issues, you should be able to resolve the AADSTS70001 error related to UnauthorizedClient - The application is disabled. If the issue persists, you may need to further investigate the application configurations and permissions.