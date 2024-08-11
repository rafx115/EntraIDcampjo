# AADSTS90002: InvalidTenantName - The tenant name wasn't found in the data store. Check to make sure you have the correct tenant ID. The application developer will receive this error if their app attempts to sign into a tenant that we cannot find. Often, this is because a cross-cloud app was used against the wrong cloud, or the developer attempted to sign in to a tenant derived from an email address, but the domain isn't registered.


## Troubleshooting Steps
# Troubleshooting Guide for AADSTS90002: InvalidTenantName

## Overview
AADSTS90002 indicates an invalid tenant name, meaning Azure Active Directory (AAD) could not find the specified tenant. This typically occurs due to misspecified tenant identifiers, domain registration issues, or attempting cross-cloud operations with the wrong configurations.

### Initial Diagnostic Steps
1. **Check the Tenant Identifier Used**:
   - Verify the tenant ID or tenant name that is being used in the application. Ensure that it is correct.

2. **Validate Application Registration**:
   - Ensure the application is correctly registered in the Azure portal under the appropriate tenant.

3. **Test Authentication with Direct URLs**:
   - Attempt to sign in directly to the Azure Portal or any relevant services using the identified tenant name or domain.

### Common Issues That Cause This Error
- **Typographical Errors**: Mistakes in the tenant ID or name.
- **Incorrect Domain**: Attempting to sign in with a domain that isn't registered in the tenant.
- **Cross-Cloud Applications**: Trying to access a tenant from a wrong Azure cloud (e.g., trying to access an Asia tenant from the US cloud).
- **Deleted or Not Provisioned Tenants**: If the tenant was deleted or not provisioned, it will not be found.

### Step-by-Step Resolution Strategies

#### Step 1: Verify Tenant Name/ID
- Go to the Azure Portal and check under **Azure Active Directory > Properties** to confirm the tenant name and ID.
- Check if you are using the correct format (e.g., for example.com use `example.onmicrosoft.com` or the custom domain).

#### Step 2: Verify Domain Registration
- Access Azure Active Directory in the Azure Portal.
- Click on **Custom domain names** and check if the domain used is listed there.
- If the domain isn’t present, add it and finalize verification steps.

#### Step 3: Reconfigure the Application
- Check your application's configuration and ensure it is set to the correct tenant ID.
- If using a cross-cloud application, verify the deployment settings reflect the correct cloud service provider.

#### Step 4: Review Application Permissions
- Check if the application has been granted the appropriate permissions in Azure AD to access the resources it is trying to reach.
  
#### Step 5: Re-attempt Authentication
- After confirming that the tenant name and application settings are correct, re-attempt the authentication process.

### Additional Notes or Considerations
- Consider regional constraints for Azure AD—some features or tenants may not yet be fully supported for all regions.
- If using tenant identifier in the format of an email or custom domain, ensure it has been correctly set up and associated with AAD.

### Documentation for Guidance
1. [Microsoft Documentation on Azure AD Error Codes](https://docs.microsoft.com/en-us/azure/active-directory/develop/reference-tenant-ids)
2. [How to Verify and Add Custom Domains in Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/add-custom-domain)
3. [Register an Application in Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)

### Test Documentation Reachability
Ensure these links are operational by visiting them in a web browser. They should redirect to the current guidance provided by Microsoft Azure.

### Advice for Data Collection
- **Collect Client Request Information**: Log the exact request made to the AAD service when the error occurs.
- **Response Codes and Messages**: Capture the full response returned, including timestamp, request ID, and error codes/messages.
- **Environment Details**: Include details about the environment (tenant, application name, configurations).
- **Versioning**: Note the version of libraries or frameworks being used (if applicable) to troubleshoot compatibility issues.

By following these structured steps, you should be able to effectively diagnose and resolve issues related to AADSTS90002. If the issue persists after following the troubleshooting steps, consider reaching out to Microsoft Support with the collected data for further assistance.