# AADSTS70016: AuthorizationPending - OAuth 2.0 device flow error. Authorization is pending. The device will retry polling the request.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS70016: AuthorizationPending

**Description:**  
The error code AADSTS70016 occurs in the context of the OAuth 2.0 device flow when authorization is pending. This means that a device is waiting for user consent or approval on another device, and there is no completed authorization yet.

---

### Initial Diagnostic Steps

1. **Identify the Device Flow Context**
   - Confirm if the error occurred while using a device flow application and ensure that this is the expected behavior for your application architecture.

2. **Review the Error Message**
   - Look at the full message accompanying the AADSTS70016 error for additional context or parameters that may provide insight into what the device is polling for.

3. **Check User Notifications**
   - Make sure the user is checking the authorization URL on their browser or mobile device. Users need to accept or deny the prompt for authorization.

4. **Verify User Status**
   - Ensure that the user receiving the authorization request has access to use the application and is properly signed in.

---

### Common Issues that Cause This Error

1. **User Not Responding**
   - The user receiving the authorization prompt hasn’t interacted with the prompt yet or may have missed the notification.

2. **Incorrect Redirect URI**
   - The device might be using an incorrect or stale redirect URI which is not recognized by the Azure AD application.

3. **Short Polling Interval**
   - The device is polling too quickly, resulting in excessive requests, which may not be behavior as expected.

4. **User Consent Policies**
   - The organization may have conditional access policies that require additional actions before a user can grant permissions.

5. **Network Latency Issues**
   - High network latency can cause delays in user authorization response being registered.

---

### Step-by-Step Resolution Strategies

1. **User Interaction**
   - Instruct the user to check their device(s) where the authorization request was sent. They need to accept the request to proceed. Often, the solution is simply awaiting user action.

2. **Review and Confirm Redirect URIs**
   - Check the application registration in Azure AD for the correct redirect URI settings:
     - Go to Azure Portal → Azure Active Directory → App registrations → Your App → Authentication.
     - Ensure the list of Redirect URIs includes the one your device is trying to use.

3. **Adjust Polling Interval**
   - If you have control over the device code polling frequency, consider adjusting it to avoid overwhelming Azure AD. A common practice is to use a polling interval of about 5 seconds.

4. **Check User Consent Requirements**
   - Ensure the user has the appropriate permissions and understand any consent prompts or policies that need to be addressed:
     - Review your organization's sign-in and security policies.

5. **Monitor Network Conditions**
   - Verify network connectivity and ensure that there are no latency issues affecting the connection to Azure AD. Conduct tests with different networks if necessary.

---

### Additional Notes or Considerations

- **Timeout Settings:** Be aware that in some applications, the polling takes time. If a user is taking too long, the authorization request may time out, and the application should handle this gracefully.

- **User Education:** Provide clear instructions for users on how they should interact with the device flow authorization requests. 

- **Application Log Review:** Check application logs for any additional debugging information that could indicate what's happening when the device is polling.

---

### Documentation for Guidance

- [Azure Active Directory Device Code Flow Documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth-device-code)
- [Error Codes Reference for Azure Active Directory](https://docs.microsoft.com/en-us/azure/active-directory/develop/reference-aad-error-codes)

**Testing Documentation Accessibility:**
- Ensure that the documentation linked can be accessed through your organization’s network and is not behind a firewall or requiring additional permissions.

---

### Advice for Data Collection

- **Capture Logs:** If possible, capture logs from your application when the error occurs. This can include timestamps, the user’s action (or inaction), and the state of the application at the time.
  
- **User Feedback:** Collect information from users experiencing the issue to identify if there are common patterns or if specific devices/browsers are encountering this error.

- **Monitoring Authorization Requests:** You may want to monitor the authorization requests being sent to see their statuses and understand how many are pending.

By following the guide above, you should be able to diagnose and resolve the AADSTS70016 error effectively.