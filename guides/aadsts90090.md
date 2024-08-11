# AADSTS90090: GraphRetryableError - The service is temporarily unavailable.


## Troubleshooting Steps
### Troubleshooting Guide: Error Code AADSTS90090 - GraphRetryableError

#### Initial Diagnostic Steps:
1. **Confirm the Error Details**: Understand the error message and code. In this case, AADSTS90090 indicates a GraphRetryableError stating that the service is temporarily unavailable.
2. **Check Service Status**: Verify if the Microsoft Graph service is experiencing any outages or maintenance by visiting the Microsoft 365 Service Status page.
3. **Review Recent Changes**: If applicable, check for any recent changes made to user permissions, app registrations, or configurations that could have triggered this error.

#### Common Issues:
- **Temporary Service Outages**: Microsoft Graph may face temporary service disruptions or maintenance activities causing the unavailability.
- **Network Connectivity Issues**: Slow or unreliable internet connections can lead to connectivity problems with the service.
- **Authentication Token Expiry**: Access tokens used for authentication may have expired, requiring new tokens to be generated.
- **API Rate Limiting**: Exceeding the API rate limit for your application can result in temporary unavailability.

#### Step-by-Step Resolution Strategies:
1. **Check Service Status**:
   - If Microsoft Graph is experiencing issues, wait for the service to be restored as these errors are usually transient.
2. **Refresh Tokens**:
   - Generate new access tokens if existing tokens have expired. Ensure the tokens have the necessary permissions.
3. **Verify Connectivity**:
   - Test your network connection to ensure stable and sufficient internet connectivity.
4. **Check API Rate Limits**:
   - Review your application's API usage and ensure it complies with Microsoft Graph's rate limits.
5. **Retry Operation**:
   - Implement retry logic in your application to handle transient errors like this. This can involve waiting and retrying the operation after a short interval.

#### Additional Notes or Considerations:
- **Error Retries**: GraphRetryableErrors are often transient, so retrying the operation after a delay can often resolve the issue without intervention.
- **Token Management**: Proper token management and ensuring their validity is crucial to prevent authentication-related errors like this.

#### Documentation:
- Microsoft Graph API Reference: [Microsoft Graph REST API documentation](https://docs.microsoft.com/en-us/graph/api/overview?view=graph-rest-1.0)
- Azure Active Directory Authentication Error Codes: [AADSTS error codes documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/reference-aadsts-error-codes)

By following these steps and considering the potential causes outlined above, you should be able to troubleshoot and resolve the AADSTS90090 error with the GraphRetryableError effectively.