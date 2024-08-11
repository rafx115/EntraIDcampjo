# AADSTS90124: V1ResourceV2GlobalEndpointNotSupported - The resource isn't supported over the/commonor/consumersendpoints. Use the/organizationsor tenant-specific endpoint instead.


## Troubleshooting Steps
Here is a detailed troubleshooting guide for the error code AADSTS90124 with the description: V1ResourceV2GlobalEndpointNotSupported - The resource isn't supported over the/commonor/consumersendpoints. Use the /organizations or tenant-specific endpoint instead.

Initial Diagnostic Steps:
1. Verify the complete error message and error code to identify the specific issue.
2. Check if the application is using the correct endpoints and authentication mechanisms.
3. Ensure that the resource being accessed is intended to be accessed via the /common or /consumers endpoint.

Common Issues:
1. Application using incorrect endpoint: The application may be using the global/common endpoint instead of the organization-specific endpoint.
2. Improper configuration: The application might be configured with outdated or incorrect settings causing authentication issues.
3. Permissions: Insufficient permissions granted to the application to access the resource.

Step-by-step Resolution Strategies:
1. Update Application Configuration:
   - Check the application settings to ensure it is configured to use the /organizations or tenant-specific endpoint instead of /common or /consumers.
   - Update the application configuration to use the correct endpoint based on the resource being accessed.

2. Check Permissions:
   - Ensure that the application has the necessary permissions granted to access the resource.
   - Verify that the permissions are correctly configured in Azure Active Directory.

3. Invoking the correct endpoint:
   - Update the code to call the appropriate /organizations or tenant-specific endpoint based on the resource being accessed.
   - Modify the authentication flow to comply with the supported endpoints.

Additional Notes or Considerations:
- It is important to understand the resource being accessed and the supported endpoints for it.
- Regularly review and update application configurations to align with any changes in the authentication mechanisms.

Documentation for Guidance:
- Microsoft Azure Active Directory documentation provides detailed information on configuring applications, authentication endpoints, and troubleshooting common issues related to authentication errors such as AADSTS90124.
  Link: [AADSTS error codes and troubleshooting guides](https://docs.microsoft.com/en-us/azure/active-directory/develop/reference-aadsts-error-codes)