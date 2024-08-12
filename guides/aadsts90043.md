
# AADSTS90043: NationalCloudAuthCodeRedirection - The feature is disabled.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS90043

#### Error Description
**Error Code:** AADSTS90043  
**Description:** NationalCloudAuthCodeRedirection - The feature is disabled.

This error typically arises when a request is made to Azure Active Directory (AAD) involving national cloud authentication features that are currently disabled for the tenant.

### Initial Diagnostic Steps

1. **Identify Your Environment:**
   - Confirm whether you are using Azure public cloud or any of the national clouds (like Azure Government, Azure Germany, or Azure China).

2. **Check Tenant Configuration:**
   - Review the configuration settings of your Azure AD tenant to verify if national cloud features are enabled.

3. **Review the Application Registration:**
   - Ensure that the application registration is correctly configured to support the required authentication flows and scopes.

4. **Check User Account:**
   - Confirm that the user account attempting to authenticate is valid and has appropriate permissions in the Azure AD environment.

### Common Issues that Cause This Error

1. **Feature Not Enabled:**
   - The National Cloud Authentication Code Redirection feature is disabled in your tenant settings.

2. **Incorrect Application Configuration:**
   - The application may not be set up to use national cloud environments or the associated endpoints.

3. **Mismatched Permissions:**
   - Users may not have the required permissions or roles assigned in Azure AD.

4. **Outdated Tokens:**
   - If tokens are being cached, they may not reflect recent configuration changes.

### Step-by-Step Resolution Strategies

#### Step 1: Review Tenant Configuration
- Log into the Azure portal and check if your tenant is set up for a national cloud environment:
  - Navigate to **Azure Active Directory** > **Properties**.
  - Review the Tenant ID and domain settings to confirm the active cloud environment.

#### Step 2: Enable National Cloud Features
- If your tenant requires national cloud features:
  - Contact Microsoft support or your Azure AD administrator to confirm the current feature status.
  - If the feature needs to be enabled, provide the necessary details to Microsoft support as they may help enable it on the backend.

#### Step 3: Application Registration
- Ensure that the application is registered correctly.
  - Go to **Azure Active Directory** > **App registrations** and select your application.
  - Review the authentication settings to verify URL and redirect URIs are correct and aligned with your national cloud.

#### Step 4: Permissions Review
- Check the assigned roles and permissions for the user:
  - From the Azure portal, navigate to **Azure Active Directory** > **Users** and select the user.
  - Review the assigned roles and ensure they have adequate permissions to access the application.

#### Step 5: Token Management
- If issues persist:
  - Clear any cached tokens in the application and re-authenticate to ensure you are using valid credentials.

### Additional Notes or Considerations

- Ensure that any changes made to the application or tenant configurations are properly documented, and all stakeholders are informed.
- Consider potential impacts on existing users when enabling or changing configurations.

### Documentation for Guidance

- [Understand the Azure Active Directory national cloud](https://docs.microsoft.com/en-us/azure/active-directory/develop/authentication-scenarios)
- [Azure Active Directory App Registration Guide](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)
- [Troubleshooting Azure AD B2C](https://docs.microsoft.com/en-us/azure/active-directory-b2c/troubleshoot)

### Advice for Data Collection
If troubleshooting does not resolve the issue, consider collecting logs for deeper analysis:

1. **Event Viewer Logs:**
   - Review the event logs under Windows Logs > Applications and Services logs > Microsoft > Windows > AAD for any related signs to the error.

2. **NetTrace:**
   - Use `netsh trace start capture=yes` to capture network traces while reproducing the error.
   - Stop the trace with `netsh trace stop` and analyze the collected .etl file.

3. **Fiddler:**
   - Use Fiddler to capture HTTP(S) traffic:
     - Ensure Fiddler is configured to decrypt HTTPS traffic.
     - Observe the request and response cycle involved in the AAD authentication process to spot any irregularities.

By following this guide, you should be able to effectively troubleshoot and resolve the AADSTS90043 error in your Azure Active Directory environment.