
# AADSTS90130: NonConvergedAppV2GlobalEndpointNotSupported - The application isn't supported over the/commonor/consumersendpoints. Use the/organizationsor tenant-specific endpoint instead.


## Troubleshooting Steps
Error Code: AADSTS90130
Description: NonConvergedAppV2GlobalEndpointNotSupported - The application isn't supported over the /common or /consumers endpoints. Use the /organizations or tenant-specific endpoint instead.

Initial Diagnostic Steps:
1. Verify the application registration in Azure Active Directory (Azure AD).
2. Check if the application is configured to use the correct endpoint.
3. Ensure the tenant-specific endpoint is accessible and properly configured.

Common Issues:
1. Incorrect application configuration settings.
2. Accessing the application using the /common or /consumers endpoint instead of the /organizations or tenant-specific endpoint.
3. Misconfigured permissions or access policies.
4. Outdated or missing configurations in the Azure AD application registration.

Step-by-Step Resolution Strategies:

1. Application Registration Check:
   a. Sign in to the Azure portal.
   b. Navigate to Azure Active Directory > App registrations.
   c. Locate the application causing the issue and check its settings.
   d. Verify the Reply URLs and Redirect URIs are correctly configured.

2. Update Endpoint:
   a. Update the application code or configuration to use the /organizations or tenant-specific endpoint.
   b. Check the authentication flow to ensure it is directing to the correct endpoint.

3. Check Permissions:
   a. Review the permissions assigned to the application in Azure AD.
   b. Ensure the application has the necessary permissions and scopes to access the required resources.

4. Verify Tenant-Specific Endpoint:
   a. Update the application to use the tenant-specific endpoint, such as https://login.microsoftonline.com/{tenant_id}.
   b. Test the application using the updated endpoint to confirm the issue is resolved.

Additional Notes or Considerations:
- Ensure that the application registration is up-to-date with the latest settings and configurations.
- Verify that the Azure AD settings align with the requirements of the application and its usage scenario.

Documentation:
For detailed guidance on troubleshooting Azure AD errors and managing application registrations, refer to the following Microsoft documentation:
- Azure AD error codes and messages: https://docs.microsoft.com/en-us/azure/active-directory/develop/msal-error-handling
- Managing application registrations in Azure AD: https://docs.microsoft.com/en-us/azure/active-directory/develop/manage-apps/permissions-and-consent