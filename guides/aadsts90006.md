
# AADSTS90006: ExternalServerRetryableError - The service is temporarily unavailable.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS90006

**Description**: The error code **AADSTS90006** indicates an **ExternalServerRetryableError** meaning that the Azure Active Directory (AAD) service you are trying to access is temporarily unavailable. This could be due to service disruptions or specific issues within the Azure Active Directory infrastructure.

#### Initial Diagnostic Steps

1. **Check Azure Service Health**: 
   - Visit the [Azure Status](https://status.azure.com/en-us/status) page to check for any ongoing outages or issues with Azure Active Directory services.
   - Look for alerts or service interruptions that may affect the service.

2. **Reproduce the Error**:
   - Try to access the service using different networks and devices to determine if the error persists across environments. 

3. **Review Recent Changes**:
   - Identify any recent changes in the Azure Active Directory configuration, such as new policies, updates, or changes in connected applications that may correlate with the start of the issue.

#### Common Issues That Cause This Error

1. **Service Outages**: Temporary service outages affecting AAD or the associated Azure services.
2. **Network Connectivity Issues**: Problems with the internet connection or firewalls blocking access to Azure services.
3. **Configuration Errors**: Misconfigured applications or Azure AD settings that could lead to blocked access.
4. **Resource Limits**: Hitting quotas or limits set within Azure services, potentially causing temporary failures.

#### Step-by-step Resolution Strategies

1. **Verify Azure Service Status**:
   - Confirm that there are no ongoing incidents affecting Azure services that could be causing the error.

2. **Network Troubleshooting**:
   - Ensure that your network connection is stable, and run a network diagnostics to rule out issues.
   - Check firewall settings to ensure that they are not blocking Azure Active Directory endpoints.

3. **Retry the Operation**:
   - Since this is a retryable error, wait for a short period and attempt to re-access the service.
   - Note any patterns regarding how often the error appears (e.g., specific times of day).

4. **Review Application Configuration**:
   - Ensure that the application has the necessary permissions and is configured correctly in Azure AD.
   - Verify that the application is not misconfigured with incorrect redirect URIs, client IDs, or secrets.

5. **Check Logs and Monitor Usage**:
   - Collect logs from the Azure AD sign-in logs for insights related to the error.
   - Use monitoring solutions like Azure Monitor to watch for unusual metrics or spikes in requests leading up to the error.

#### Additional Notes or Considerations

- **Temporary Nature**: This error is likely temporary, so a pause and retry approach may resolve the issue without requiring extensive troubleshooting.
- **Support**: If the error persists after following the above steps, consider opening a support ticket with Microsoft Azure Support for help.

#### Documentation Where Steps Can Be Found for Guidance

1. **Azure Status Page**: [Azure Status](https://status.azure.com/en-us/status)
2. **Azure Active Directory Documentation**: [Azure Active Directory Documentation](https://docs.microsoft.com/en-us/azure/active-directory/)
3. **Troubleshoot Azure AD Sign-in Errors**: [Troubleshooting Azure AD sign-in errors](https://docs.microsoft.com/en-us/azure/active-directory/hybrid/tshoot-connect-issues)

#### Advice for Data Collection

- **Event Viewer Logs**:
  - Check the Windows Event Viewer for any errors related to application sign-ins or any issues occurring at the time of the error. Look for specific signs of authentication errors or service failures.
  
- **Nettrace**:
  - Use tools like `Wireshark` or `Network Monitor` to capture network activity, focusing specifically on requests to Azure endpoints. This can provide insights into network issues that could be causing the problem.

- **Fiddler**:
  - Use Fiddler to capture and analyze HTTP(s) requests and responses. This tool can reveal any issues in the requests sent to Azure AD and might help in identifying if there are any unexpected responses.

In any collection of logs and traces, ensure compliance with your organization’s data security and privacy policies.