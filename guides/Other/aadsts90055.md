# AADSTS90055: TenantThrottlingError - There are too many incoming requests. This exception is thrown for blocked tenants.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS90055 (TenantThrottlingError)

The AADSTS90055 error indicates a TenantThrottlingError, meaning there are too many incoming requests to the Azure Active Directory (AAD) tenant, which leads to temporary blocking of requests. This error is typically encountered in scenarios with high request volumes to AAD. Below is a comprehensive troubleshooting guide.

#### Initial Diagnostic Steps
1. **Identify the Error Message**: Confirm that the error code is indeed AADSTS90055.
2. **Check Request Volume**: Review logs to determine if there has been an increase in the number of authentication requests to AAD.
3. **Identify Affected Applications**: Determine which applications or users are encountering this error and under what conditions.
4. **Consult Azure Service Health**: Check the Azure Service Health dashboard to see if there are any ongoing incidents or outages affecting Azure AD.

#### Common Issues That Cause This Error
- **High Volume of Authentication Requests**: Applications making too many requests in a short amount of time.
- **Burst Traffic**: Sudden spikes in traffic, possibly due to scheduled tasks or bulk operations.
- **Misconfigured Applications**: Applications that do not handle token caching efficiently or retry requests without implementing a backoff strategy.
- **Testing from Development Environments**: Frequent requests during testing/development may inadvertently flood the service.

#### Step-by-Step Resolution Strategies

1. **Rate Limiting Implementation**:
   - Implement rate limiting on your applications to control the number of requests sent to AAD. This can help prevent surpassing the threshold set by Azure AD.

2. **Optimize Authentication Flows**:
   - Review the authentication flow to ensure tokens are being cached and reused efficiently. Use refresh tokens instead of accessing the authentication endpoint repeatedly.

3. **Implement Exponential Backoff**:
   - When retrying requests after receiving a throttling error, implement exponential backoff in your retry logic. This can reduce the number of immediate follow-up requests.

4. **Analyze Application Usage Patterns**:
   - Use Azure Monitor and Application Insights to analyze usage patterns. Look for peak usage times and assess if requests can be redistributed.

5. **Increase Capacity or Scale**:
   - If your application consistently requires high volumes of authentication, consider architectural changes, such as distributing load across multiple tenants, if applicable.

6. **Contact Microsoft Support**:
   - If the issue persists and you believe it to be an error unrelated to your application’s request patterns, contact Microsoft Support for assistance and clarification of tenant-specific limits.

#### Additional Notes or Considerations
- **Throttling Limits**: Azure AD has certain built-in throttling policies which can differ by tenant size, type, and usage patterns. Familiarize yourself with these policies.
- **Monitoring and Alerts**: Implement monitoring to alert you when nearing throttling limits to prepare in advance for mitigating actions.
- **User Experience**: Ensure users are informed when their requests are being throttled, and provide clear communication on how long they may need to wait for subsequent requests.

#### Documentation and Resources
- [Azure AD Throttling Limits](https://docs.microsoft.com/en-us/azure/active-directory/develop/access-tokens#how-to-troubleshoot-token-issues)
- [Implementing Rate Limiting in Azure AD Applications](https://docs.microsoft.com/en-us/azure/active-directory/develop/architecture-identity)
- [Application Insights and Monitoring](https://docs.microsoft.com/en-us/azure/monitoring/app-insights/)

#### Testing Documentation Accessibility
To ensure that the documentation is reachable, visit:
- [Azure AD Throttling Limits](https://docs.microsoft.com/en-us/azure/active-directory/develop/access-tokens#how-to-troubleshoot-token-issues)
- [Implementing Rate Limiting](https://docs.microsoft.com/en-us/azure/active-directory/develop/architecture-identity)
- [Application Insights](https://docs.microsoft.com/en-us/azure/monitoring/app-insights/)
Make sure you can navigate, read, and search for required information.

#### Advice for Data Collection
- **Log Data**: Collect and log all errors including timestamp, user identifier, application identifier, and request frequency.
- **Request Analysis**: Analyze request patterns over time to get a clearer picture of what is triggering the throttling.
- **Performance Metrics**: Monitor performance metrics such as average response times and authentication success rates to correlate with the errors being encountered.

By following these guidelines, you will be better positioned to understand, diagnose, and resolve issues related to AADSTS90055 and improve the overall stability and performance of your applications interfacing with Azure AD.

Category: Other