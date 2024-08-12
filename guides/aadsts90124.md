# AADSTS90124: V1ResourceV2GlobalEndpointNotSupported - The resource isn't supported over the/commonor/consumersendpoints. Use the/organizationsor tenant-specific endpoint instead.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS90124 Error

#### Overview
The error code AADSTS90124 indicates that the application is attempting to access a resource that is not supported for the "common" or "consumer" endpoints in Azure Active Directory (AAD). Instead, it requires the use of the "organizations" or tenant-specific endpoint.

#### Initial Diagnostic Steps

1. **Identify the AAD Endpoint Used**:
   - Check if the application is trying to authenticate against the `/common` or `/consumers` endpoint.
   - If you are using an AAD library, review the configuration to see which endpoint is specified.

2. **Verify Resource URL**:
   - Confirm the resource URL you are attempting to access. Verify if it should be accessed via the organizations endpoint.

3. **Platform/Service Check**:
   - Determine if the resources in question are intended for personal Microsoft accounts or Azure AD accounts.

4. **Review Application Permissions**:
   - Check if the application has the necessary permissions in Azure AD for the resource you're trying to access.

#### Common Issues that Cause this Error

- **Using Common Endpoint Incorrectly**:
  - Trying to use the `/common` endpoint when accessing resources that are specifically meant for Azure AD tenants.

- **Mismatched Resource Type**:
  - Attempting to access resources that are not available for consumers or personal accounts (such as certain enterprise-level APIs).

- **Incorrect Authentication Flow**:
  - Misconfiguring the OAuth flow; for instance, using the implicit grant flow where an authorization code flow is needed.

#### Step-by-Step Resolution Strategies

1. **Change the Endpoint**:
   - Update your application's endpoint from `/common` to `/organizations` if the resource is intended for Azure AD users.
   - If applicable, use tenant-specific endpoints (e.g., `https://login.microsoftonline.com/{tenant-id}`) for greater granularity.

2. **Modify the Resource Identifier**:
   - Ensure that the resource being accessed is compatible with the chosen endpoint.

3. **Review and Update Configuration**:
   - If using OAuth libraries (like MSAL or ADAL), ensure that the configuration options for the authority are set correctly.
   - Example: Changing from `https://login.microsoftonline.com/common` to `https://login.microsoftonline.com/{tenant-id}` resulting in a more specific request.

4. **Check App Registration**:
   - Go to the Azure Portal and navigate to `Azure Active Directory > App registrations`.
   - Review application settings, permissions, and redirect URIs to ensure they align with AAD requirements.

5. **User Account Type Verification**:
   - Ensure that the account type being used is appropriate for the resource being accessed; for instance, make sure the accounts are Azure AD accounts if required.

#### Additional Notes or Considerations

- **Testing Best Practices**:
  - When testing changes, use accounts known to work with the requested resource to isolate the problem.

- **Documentation Updates**:
  - Review Azure AD documentation regularly for any updates on endpoints and resources, as practices may evolve.

#### Documentation for Guidance

- [Microsoft Identity Platform Documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/)
- [Get tokens to access a web API](https://docs.microsoft.com/en-us/azure/active-directory/develop/scenario-desktop-acquire-token)
- [Understanding Azure Active Directory authentication](https://docs.microsoft.com/en-us/azure/active-directory/develop/authentication-scenarios)

#### Advice for Data Collection

1. **Event Viewer Logs**:
   - Check the Event Viewer logs on the client machine for any related authentication failures or warnings.
   - Look under `Applications and Services Logs` > `Microsoft` > `Windows` > `UserAccessLogging`.

2. **Network Traces (Nettrace)**:
   - Use NetCapture tools to capture network traffic if the application fails to connect. Monitor for the specific request made to AAD.

3. **Fiddler HTTP Debugging**:
   - Use Fiddler to diagnose HTTP traffic. Monitor the request made to Azure AD, check the URL being called, and the response body for detailed error messages.

By following the troubleshooting steps above, you should be able to effectively diagnose and resolve the AADSTS90124 error, leading to successful resource access.