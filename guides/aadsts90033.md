
# AADSTS90033: MsodsServiceUnavailable - The Microsoft Online Directory Service (MSODS) isn't available.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS90033 Error Code: MsodsServiceUnavailable

#### Initial Diagnostic Steps:
1. **Check Microsoft Service Status**: Verify the availability status of Microsoft Online Directory Service (MSODS) by visiting the Microsoft Service Health Dashboard or Service Status page.
   
2. **Confirm Other User Reports**: See if other users are experiencing the same issue by checking community forums or Microsoft Support channels.

#### Common Issues:
- Network issues preventing the authentication service from connecting to the Microsoft Online Directory Service.
- Incorrect DNS configurations that prevent the service from resolving the MSODS domain.
- Service disruption or maintenance on the Microsoft side causing the unavailability of MSODS.

#### Step-by-Step Resolution Strategies:
1. **Network Connectivity Check**:
   - Ensure that there are no network issues affecting the connection between your system and Microsoft's services.
   - Check firewall settings and ensure that there are no restrictions blocking the communication with MSODS servers.

2. **DNS Configuration Verification**:
   - Validate the DNS settings on your network to guarantee that the MSODS domain can be resolved successfully.
   - Consider using public DNS servers like Google DNS (8.8.8.8, 8.8.4.4) to rule out any local DNS issues.

3. **Service Health and Status**:
   - Monitor the Microsoft Service Health Dashboard for any reported incidents or outages affecting the MSODS service.
   - Wait for the service to resume normal operations if the unavailability is due to maintenance activities.

4. **Contact Support**:
   - If the issue persists and is not resolved by the above steps, reach out to Microsoft Support for further assistance and escalations.

#### Additional Notes or Considerations:
- Clearing browser cache and cookies can sometimes resolve authentication issues due to cached credentials.
- Consider the impact of any recent changes in your organization's Azure AD configuration that might have contributed to this error.

#### Documentation:
You can refer to Microsoft's official documentation for specific guidance on troubleshooting AADSTS errors:
- [Azure AD error codes and resolutions](https://docs.microsoft.com/en-us/azure/active-directory/develop/reference-aadsts-error-codes)

Following the above steps and considerations should help in addressing and resolving the AADSTS90033 error related to MsodsServiceUnavailable effectively.