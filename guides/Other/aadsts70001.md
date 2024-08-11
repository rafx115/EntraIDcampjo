# AADSTS70001: UnauthorizedClient - The application is disabled. To learn more, see the troubleshooting article for errorAADSTS70001.


## Troubleshooting Steps
Certainly! Here's a detailed troubleshooting guide for the AADSTS70001 error code, specifically with the description: "UnauthorizedClient - The application is disabled." 

### AADSTS70001 Error Code Troubleshooting Guide

#### 1. Initial Diagnostic Steps
   - **Check the Error Message**: Ensure that the error really states "UnauthorizedClient" and specifies that "The application is disabled".
   - **Identify the Application**: Determine which application is causing the error. This may involve checking logs or identifying which client is attempting to authenticate.
   - ** Review Application Registration**: Go to the Azure Portal and check the application registration that corresponds to the client application experiencing the error.

#### 2. Common Issues that Cause this Error
   - **Application Disabled**: The application is disabled in Azure Active Directory (AAD).
   - **Misconfigured Authentication Settings**: The application may have incorrect or missing authentication settings.
   - **Permissions Not Granted**: The application may not have sufficient permissions assigned in AAD.
   - **Wrong Tenant**: The application might be configured for a different tenant than the one where it's being used.
   - **Expired or Missing Client Secret**: If the application uses a client secret, it may have expired or not be set correctly.

#### 3. Step-by-Step Resolution Strategies
   Here’s how to resolve the AADSTS70001 error:

   **Step 1: Check Application Registration Status**
   - Log in to the [Azure Portal](https://portal.azure.com).
   - Go to **Azure Active Directory** > **App registrations**.
   - Search for and select the application causing the error.
   - Check if the application status is “Enabled.” If not, enable it.

   **Step 2: Review Authentication Settings**
   - While still in the application registration page, verify the **Authentication** settings.
   - Ensure that the redirect URIs are correctly configured and match what the client application is trying to use.

   **Step 3: Check API Permissions**
   - Under the selected application, navigate to **API permissions**.
   - Ensure that the required permissions are granted and that there are no permission errors.
   - If permissions were changed, make sure to **Grant admin consent** if required.

   **Step 4: Verify Client Secret**
   - Go to **Certificates & secrets** in the application registration.
   - Check if a valid client secret exists. If it has expired, create a new client secret and update your client application configuration.

   **Step 5: Confirm Tenant Configuration**
   - Ensure that the application has been registered in the correct Azure AD tenant.
   - If the application is intended to be multi-tenant, ensure it is configured correctly in the **Authentication** section.

   **Step 6: Check Service Principal**
   - Go to **Enterprise applications** in Azure AD.
   - Search for the application's service principal and check its status. If it is disabled, enable it.

#### 4. Additional Notes or Considerations
   - **Permissions Issues**: Sometimes permissions in AAD can take time to propagate or may require an administrator’s help to resolve.
   - **Azure AD Conditional Access Policies**: Check if there are any Conditional Access policies that may impact application access.
   - **Support**: If you can’t resolve the issue, consider reaching out to Microsoft support for assistance.

#### 5. Documentation
   For further guidance and reference, here are some helpful documentation links:
   - [Microsoft Azure Active Directory Documentation](https://docs.microsoft.com/en-us/azure/active-directory/)
   - [Troubleshooting Azure AD Authentication Issues](https://docs.microsoft.com/en-us/azure/active-directory/develop/troubleshoot-authentication)
   - [Register an application with the Microsoft identity platform](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)

   Make sure these links work and are reachable. You can simply paste them in your web browser to confirm they load.

#### 6. Advice for Data Collection
   - **Logs**: Gather logs from the client application to understand when and where the error is thrown.
   - **Application ID and Tenant ID**: Collect information about the Application ID, Client ID, and Tenant ID.
   - **Tenant Admin Support**: Engage with your Azure AD admin for insights on application permissions and configurations that may not be visible to you as a developer.

### Conclusion
By following the steps listed in this guide, you should be able to diagnose and resolve the AADSTS70001 error. Make sure to verify each component related to the application registration, ensure permissions are correctly set, and that no relevant settings are misconfigured.

Category: Other