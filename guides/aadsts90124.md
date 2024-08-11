
# AADSTS90124: V1ResourceV2GlobalEndpointNotSupported - The resource isn't supported over the/commonor/consumersendpoints. Use the/organizationsor tenant-specific endpoint instead.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS90124

**Error Description:**
The error code AADSTS90124 indicates that the requested resource is not supported on the `/common` or consumer endpoints and suggests using the `/organizations` or tenant-specific endpoint instead.

### Initial Diagnostic Steps

1. **Check the Error Message**: Review the full error message to ensure it corresponds to AADSTS90124.
2. **Identify the Resource**: Determine which resource (API or service) is being accessed and what the expected endpoint is (common vs. organizations).
3. **Establish Context**: Identify whether the request is coming from an application configured for Azure AD (or other identity providers) that uses the resources in question.
4. **Inspect URL Patterns**: Check the URL patterns you're using in your code or application settings.

### Common Issues That Cause This Error

1. **Misconfigured Application**: The application is pointing to the `/common` endpoint when it should point to the `/organizations` endpoint.
2. **Resource Type**: The requested resource is specific to either organizational accounts (work/school accounts) vs. personal Microsoft accounts (MSA).
3. **Scope Settings**: Incorrect or missing scopes in your authorization setup can lead to this error.
4. **Token Requests**: The configuration for token requests may be improperly set up for multi-tenant access.
5. **Require Administrative Consent**: The application might require admin consent from the organization's user, and without it, access will fail.

### Step-by-Step Resolution Strategies

**Step 1: Update the Endpoint URL**
- If your application is configured to use the `/common` endpoint, change it to the `/organizations` endpoint.
- For example, replace `https://login.microsoftonline.com/common/oauth2/v2.0/token` with `https://login.microsoftonline.com/organizations/oauth2/v2.0/token`.

**Step 2: Check Application ID and Permissions**
- Ensure that the Application ID (Client ID) is correctly configured in the Azure portal.
- Check the API permissions in Azure AD to ensure that they are set correctly, according to the resource you are trying to access.

**Step 3: Admin Consent**
- If your application requires admin consent for certain permissions, make sure that it has been granted.
- This can be done via the Azure portal under "Enterprise applications" > Your Application > Permissions.

**Step 4: Use Tenant-Specific Endpoint**
- If your organization has a tenant-specific endpoint, use it. The format is:
  `https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token`
- Replace `{tenant_id}` with your actual Azure AD Tenant ID.

**Step 5: Code Review**
- If applicable, review the code that makes the API calls to ensure that the endpoint and scope configuration is as per the guidelines outlined above.

**Step 6: Test the Configuration**
- After making the above changes, re-test your application by initiating the authentication flow again.

### Additional Notes or Considerations

- Ensure that the user trying to access the resource is part of the directory if using the `/organizations` endpoint.
- Some resources are specifically limited to use either MSA or organizational accounts; understanding the distinctions can prevent confusion.

### Documentation for Guidance

- Official Microsoft documentation related to Azure AD authentication and token requests:
  1. [Authentication Scenarios in Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/develop/authentication-scenarios)
  2. [Azure Active Directory Token Reference](https://docs.microsoft.com/en-us/azure/active-directory/develop/access-tokens)

**Test Documentation Reachability**:  
You can check the links provided above in your browser to ensure that they are reachable. 

### Advice for Data Collection

- **Log Information**: Collect and log detailed information about the requests being made, including URLs, request headers, and any payloads.
- **Error Logs**: Review and save any server-side error logs that can provide context around the failure (e.g., API call failure).
- **Authentication Flow Trace**: If possible, trace the authentication flow to pinpoint exactly where the failure is occurring.
- **User Context**: Capture user information (with consent) to ensure that the right accounts are being used.

This troubleshooting guide provides a comprehensive approach to understanding and resolving the AADSTS90124 error code. Following each step methodically should help in identifying and correcting the issue.