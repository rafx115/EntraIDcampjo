# AADSTS90055: TenantThrottlingError - There are too many incoming requests. This exception is thrown for blocked tenants.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS90055: TenantThrottlingError

#### Initial Diagnostic Steps:
1. **Confirm Error Details**: Note down the error message received, which is "TenantThrottlingError - There are too many incoming requests. This exception is thrown for blocked tenants."
2. **Check Tenant Status**: Determine if the tenant has been blocked or rate-limited due to excessive requests.

#### Common Issues Causing This Error:
1. **Excessive Requests**: The tenant might have exceeded the allowed limit for incoming requests.
2. **Abusive Behavior**: Continuous usage that violates Azure Active Directory's policies can trigger throttling.
3. **Malicious Activity**: If the tenant's activities are flagged as suspicious, it may lead to blocking.

#### Step-by-Step Resolution Strategies:
1. **Identify Root Cause**:
   - Review recent activity logs and request history to understand the pattern of usage that triggered the error.
2. **Check Azure AD Service Health**:
   - Verify if there are any ongoing issues or maintenance that could be affecting the tenant's access.
3. **Implement Rate Limiting**:
   - If the issue is due to excessive requests, throttle the requests from the tenant's end to stay within the limits.
4. **Review Azure AD Policies**:
   - Ensure that the tenant's activities comply with Azure AD's usage policies and guidelines.
5. **Contact Support**:
   - If the issue persists, reach out to Azure support for assistance in unblocking the tenant and resolving the throttling error.

#### Additional Notes or Considerations:
- **Monitoring**: Set up monitoring to proactively track usage patterns and avoid reaching threshold limits.
- **Educate Users**: Train tenants on best practices to prevent accidental triggering of throttling mechanisms.
- **Review Application Design**: Optimize applications to minimize the number of requests sent to Azure AD.

#### Documentation for Guidance:
- [Azure Active Directory Error Codes](https://docs.microsoft.com/en-us/azure/active-directory/develop/reference-aadsts-error-codes)
- [Azure Active Directory Throttling Guidance](https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-control-client-app-access#throttling)

By following these steps and considerations, you should be able to troubleshoot and resolve the AADSTS90055 TenantThrottlingError effectively.