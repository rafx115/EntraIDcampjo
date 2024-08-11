
# AADSTS90002: InvalidTenantName - The tenant name wasn't found in the data store. Check to make sure you have the correct tenant ID. The application developer will receive this error if their app attempts to sign into a tenant that we cannot find. Often, this is because a cross-cloud app was used against the wrong cloud, or the developer attempted to sign in to a tenant derived from an email address, but the domain isn't registered.


## Troubleshooting Steps
## Troubleshooting Guide for Error Code AADSTS90002

### Initial Diagnostic Steps:
1. **Verify the Tenant ID:** Double-check the Tenant ID being used by the application developer.
  
### Common Issues:
1. **Incorrect Tenant ID:** The provided Tenant ID is invalid or not recognized.
2. **Using Wrong Cloud:** Cross-cloud applications being used against the wrong cloud.
3. **Unregistered Domain:** Attempting to sign in to a tenant derived from an email address, but the domain isn't registered.

### Step-by-Step Resolution Strategies:
1. **Confirm Tenant ID**: Ensure that the Tenant ID being used is correct. You can verify this by checking the Azure Active Directory portal.
  
2. **Check Application Configuration**:
    - Verify that the application is correctly configured with the appropriate Tenant ID.
  
3. **Verify Cloud Environment**:
    - Ensure that the application is targeting the correct cloud environment.
  
4. **Validate Domain Registration**:
    - Check if the domain associated with the tenant is registered and properly configured.
  
5. **Recheck Email Domain**:
    - Ensure that the tenant derived from the email address is valid and correctly linked to the domain.

### Additional Notes or Considerations:
- The error AADSTS90002 with the description "InvalidTenantName" usually occurs when there is a problem with the Tenant ID or the cloud environment configuration.
- Encourage developers to carefully review their application configurations and inputs when encountering this error.

### Documentation for Guidance:
- For further guidance on resolving AADSTS90002 errors, developers can refer to the official Microsoft documentation on troubleshooting Azure AD error codes: [Azure AD error codes troubleshooting](https://docs.microsoft.com/en-us/azure/active-directory/develop/troubleshoot-error-codes).

By following these troubleshooting steps and considerations, you can help resolve the error AADSTS90002 with the "InvalidTenantName" description, ensuring a smoother experience for developers interacting with Azure Active Directory.