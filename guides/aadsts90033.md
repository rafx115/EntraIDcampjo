
# AADSTS90033: MsodsServiceUnavailable - The Microsoft Online Directory Service (MSODS) isn't available.


## Troubleshooting Steps
Certainly! The error code **AADSTS90033** indicating **MsodsServiceUnavailable - The Microsoft Online Directory Service (MSODS) isn't available** suggests there may be issues on the Microsoft side with the online directory service, or there could be network-related issues from the client side. Here’s a detailed troubleshooting guide that provides steps to diagnose and resolve this error.

### **Initial Diagnostic Steps**

1. **Verify the Error Message:**
   - Confirm the exact error message and context in which it occurs (e.g., when logging into a service, during a particular operation).

2. **Check Service Status:**
   - Visit the [Microsoft 365 Service Health status page](https://portal.office.com/servicestatus) to check if there are any reported outages or service disruptions related to Microsoft Online Services.

3. **Network Connectivity:**
   - Ensure that there is stable internet connectivity from the client side.
   - Test accessing other Microsoft services to rule out broader connectivity issues.

4. **Browser and Session:**
   - Clear the browser cache or try a different browser or incognito mode to rule out any cookie/session issues.
   - Ensure that no browser extensions are interfering with the authentication process.

### **Common Issues That Cause This Error**

- **Microsoft Service Outage:** Microsoft may be experiencing a temporary outage or service degradation for the directory services.
- **Network Issues:** Local network issues that are blocking access to Microsoft services.
- **Expired or Incorrect Credentials:** If the credentials being used to access the service are incorrect or have expired.
- **Firewall or Proxy Settings:** Local firewall or proxy settings may be blocking the connection to the directory services.
- **Service Configuration Issues:** Issues with the Azure Active Directory configuration on the client's end.

### **Step-by-Step Resolution Strategies**

1. **Check Microsoft Service Health:**
   - Wait for a few minutes and refresh the service status page to see if the issue is resolved or updates are provided.

2. **Troubleshoot Network Issues:**
   - Verify that you can reach Microsoft Online Directory URLs (like graph.microsoft.com).
   - If on the corporate network, check with IT if there have been changes to firewall or proxy configurations.

3. **Review User Account Status:**
   - Log into the Azure portal using an admin account and check the status of the user account facing the issue.
   - Ensure the account is not disabled or locked out.

4. **Verify Credentials:**
   - If applicable, reset the password for the account experiencing the issue.
   - Ensure Multi-Factor Authentication (MFA) requirements are fulfilled if enabled.

5. **Test Alternate Authentication Methods:**
   - If available, try using OAuth tokens, or check if the application supports alternate login flows.

6. **Try from Different Clients:**
   - Attempt the same operation from a different network, different device, or a different browser to see if the issue persists.

7. **Contact Support:**
   - If the problem remains unresolved, collect error logs, account details, and other relevant information and contact Microsoft Support for assistance.

### **Additional Notes or Considerations**

- **Temporary Nature:** This error can be temporary; if you encounter it, it’s worth waiting a short period before retrying.
- **Documentation Updates:** Microsoft continually updates their services; checking their documentation regularly can provide insights into changes that could affect connectivity.

### **Documentation for Guidance**

- [Azure Active Directory - Troubleshooting Common Errors](https://learn.microsoft.com/en-us/azure/active-directory/develop/active-directory-authentication-scenarios)
- [Microsoft Online Service Status](https://portal.office.com/servicestatus)
- [Azure Support](https://azure.microsoft.com/en-us/support/contact/)

### **Test Access to Documentation**

- Verify the accessibility of the documentation pages:
   - [Azure Active Directory troubleshooting guide](https://learn.microsoft.com/en-us/azure/active-directory/develop/active-directory-authentication-scenarios) – Ensure the page loads successfully.
   - Check the status page by visiting [Microsoft 365 Service Health](https://portal.office.com/servicestatus).

### **Advice for Data Collection**

- Keep a log of the actions taken leading up to the error.
- Capture screenshots of the error message and status code.
- Collect browser console logs to identify any potential client-side issues.
- Document any changes made to configuration or network settings that correlate with the onset of the issue.
- If contacting support, be prepared with information such as:
  - Timestamp of issue occurrence.
  - User account affected.
  - Steps to reproduce the issue.
  
By following these steps, you should be able to diagnose and resolve the AADSTS90033 error effectively.