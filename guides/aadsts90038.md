# AADSTS90038: NationalCloudTenantRedirection - The specified tenant 'Y' belongs to the National Cloud 'X'. Current cloud instance 'Z' does not federate with X. A cloud redirect error is returned.


## Troubleshooting Steps
The error code AADSTS90038 indicates a situation where there's a mismatch between the cloud instance you are trying to access and the national cloud your tenant belongs to. Here’s a detailed troubleshooting guide to help you diagnose and resolve this error.

### 1. Initial Diagnostic Steps

1. **Identify the Tenant Information:**
   - Confirm the tenant ID or domain (e.g., your organization’s name). This will involve checking the Azure portal or utilizing Azure CLI commands.
   - Verify if this tenant is part of a National Cloud (such as Azure Government, Azure China, etc.).

2. **Check Current Cloud Instance:**
   - Confirm which cloud instance you are currently connected to (commercial, government, etc.). You can check this by looking at the endpoint URLs when signing into Azure.

3. **Sign-In Attempts:**
   - Attempt to sign in using the Azure Portal to see if the issue persists when accessing different resources or services.

### 2. Common Issues that Cause this Error

- **Cloud Mismatch:** The specified tenant is in a different cloud instance than the one being accessed.
- **Configuration Issues:** Misconfigurations in Azure AD, particularly with tenant settings or application registrations.
- **Legacy Links:** Applications or services that are hard-coded to point to a specific cloud endpoint.

### 3. Step-by-Step Resolution Strategies

#### Step 1: Check Tenant and Current Cloud Configuration
- Use the Azure AD Portal to review your tenant information.
- Verify the resource URLs and ensure they match the cloud you are in. Example:
  - Azure Government: `*.usgovcloudapi.net`
  - Azure Germany: `*.azure.de`
  - Azure China: `*.chinacloudapi.cn`

#### Step 2: Determine Application Registration Configuration
- If you are using an app or service, ensure the application registration is correctly configured for the intended cloud.
- Consult the Azure AD documentation that outlines how to register applications in national clouds:
  - Sample documentation: [App registration](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)
  
#### Step 3: Plan a Cloud Redirection 
- If necessary, update the relevant identifiers for applications (application id, secret, etc.) to point to the appropriate resources.
- Utilize Azure CLI or PowerShell commands to adjust or check your setup.

#### Step 4: Contact Support if Needed
- If you still cannot resolve the issue, consider contacting Microsoft Support for further assistance. Gather details such as error codes, timestamps, and your account information.

### 4. Additional Notes or Considerations

- This error often indicates a need to reassess your IT architecture with respect to national cloud compliance (especially for government entities).
- Regular audits of application registrations and cloud configurations can help prevent such issues.
- Be aware of changes in compliance and regulations governing the use of national clouds.

### 5. Documentation References

- To check Azure AD documentation: 
  - [Azure Active Directory Documentation](https://docs.microsoft.com/en-us/azure/active-directory/)
- For guidance on national clouds: 
  - [National Cloud Information](https://docs.microsoft.com/en-us/azure/government/gov-overview)
  
### 6. Testing Documentation Accessibility

Ensure the documentation links work by accessing them directly in a browser. 
- Open each link provided above.
- Check for any errors or issues in loading the content.

### 7. Advice for Data Collection

- Collect logs and relevant error messages:
  - Use Azure AD sign-in logs to gather pertinent data around the errors encountered.
  - Enable diagnostics logging on your applications to capture events leading to sign-in attempts.
  
By following these detailed steps, you should be able to diagnose and resolve the AADSTS90038 error effectively. Always ensure your configurations align with best practices for your specific national cloud environment.