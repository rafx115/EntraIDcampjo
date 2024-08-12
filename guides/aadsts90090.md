
# AADSTS90090: GraphRetryableError - The service is temporarily unavailable.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS90090: "GraphRetryableError - The service is temporarily unavailable"

**Error Summary**:  
Error code **AADSTS90090** indicates that the Microsoft Graph service is temporarily unavailable. This is a retryable error, suggesting that the service may be experiencing transient issues. 

---

### Initial Diagnostic Steps

1. **Check Service Status**:
   - Visit the Azure Service Health Dashboard or Microsoft 365 Service Status pages to check if there are any known outages or issues with the Graph API.
   - Check the status page for updates regarding service availability.

2. **Verify Network Connectivity**:
   - Ensure that your application can access the internet and that you do not have firewall or proxy settings interfering with your connection to the Microsoft Graph service.

3. **Examine Error Logs**:
   - If available, review application logs that may contain more information about the request that resulted in the error. Look for patterns in the errors reported.

4. **Reproduce the Issue**:
   - Attempt to replicate the error under similar conditions to gather more information on when the error occurs.

---

### Common Issues That Cause This Error

1. **Service Outages**: 
   - Temporary unavailability of the Microsoft Graph service or specific endpoints due to outages.

2. **Rate Limiting**: 
   - Your application may be making too many requests in a short period, leading to temporary unavailability due to rate limiting.

3. **Network Issues**: 
   - Network interruptions or connectivity issues can impair access to the Azure services.

4. **Heavy Load or DDoS Protection**:
   - The service may be under heavy load or experiencing denial-of-service prevention mechanisms that temporarily restrict connections.

---

### Step-by-Step Resolution Strategies

1. **Retry the Request**:
   - Implement an exponential backoff strategy, where the application waits for a short period before retrying the request, increasing the wait time on each subsequent failure.
   - Example: 
     - 1st retry: Wait 1 second
     - 2nd retry: Wait 2 seconds 
     - 3rd retry: Wait 4 seconds, etc.

2. **Optimize API Calls**:
   - Review your application’s API usage and optimize it by reducing the number of calls made to the Graph API. Consider batching API requests if applicable.

3. **Implement Caching**:
   - If possible, cache responses from the Graph API to reduce the number of repeated requests for frequently accessed data.

4. **Check Application Configuration**:
   - Ensure correct permissions are set up for accessing Microsoft Graph and that your application is properly configured to handle authentication.

5. **Monitoring and Alerts**:
   - Set up monitoring for the application to get notified of the error when it occurs, allowing for quicker remediation.

---

### Additional Notes or Considerations

- This error is often transient, so it’s important not to panic on the first occurrence. Implementing robust error handling is essential.
- If the error persists over an extended period, further investigation is warranted to rule out persistent service issues.

---

### Documentation for Guidance

- **Azure Active Directory Authentication Errors Documentation**:
  [Microsoft Docs - Azure AD Error Codes](https://docs.microsoft.com/en-us/azure/active-directory/develop/reference-aad-error-codes)
  
- **Best Practices for Microsoft Graph API**:
  [Microsoft Graph - Best practices](https://docs.microsoft.com/en-us/graph/best-practices-overview)

- **Implementing Exponential Backoff with HTTP APIs**:
  [Google's Exponential Backoff Algorithm](https://cloud.google.com/storage/docs/exponential-backoff)

---

### Advice for Data Collection (Event Viewer Logs, NetTrace, Fiddler)

1. **Event Viewer Logs**:
   - Check Windows Event Logs for any application-specific entries at the time the error occurred, particularly in the Application logs.

2. **NetTrace**:
   - Use tools like **Network Monitor** or **Wireshark** to capture packets and analyze network activity to understand if requests are getting dropped or if there are delays.

3. **Fiddler**:
   - Capture web traffic using Fiddler to see the requests and responses sent to the Microsoft Graph API when the error occurs. Look for error details in the response and any correlation with request headers or payload format.

---

By following this guide, you should be able to effectively troubleshoot and resolve the AADSTS90090 error, ensuring a smoother experience with the Microsoft Graph API.