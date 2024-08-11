
# AADSTS20012: WsFedMessageInvalid - There's an issue with your federated Identity Provider. Contact your IDP to resolve this issue.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS20012 (WsFedMessageInvalid)

**Description:** AADSTS20012 is an error related to issues with the federated Identity Provider (IdP). It indicates that the service received a WS-Federation message that could not be processed correctly.

---

### Initial Diagnostic Steps
1. **Check the Error Message:**
   - Carefully read the error message to see if it provides more context or additional error codes.
   
2. **Review Logs:**
   - Check the application logs and any relevant security logs to find more details related to authentication attempts.

3. **Identify Recent Changes:**
   - Determine if there have been recent changes to the federated settings, including certificate updates, IdP configurations, or related network configurations.

4. **Recreate the Issue:**
   - Try to reproduce the error in a controlled environment to determine consistency and specifics of the failure.

---

### Common Issues that Cause AADSTS20012
1. **Expired or Invalid Signing Certificates:**
   - The signing certificates on the IdP may have expired or been revoked.

2. **Metadata Configuration Issues:**
   - Problems with WS-Federation metadata that the service relies on.

3. **Incorrect or Missing Claims:**
   - Missing or incorrectly formatted claims in the security token issued by the IdP.

4. **Network Communication Problems:**
   - Firewall or network issues that prevent communication between the service and the IdP.

5. **Configuration Drift:**
   - Changes in configuration settings that have not been propagated across systems.

---

### Step-by-Step Resolution Strategies
1. **Check Certificate Validity:**
   - Verify that the signing certificate from the IdP has not expired or been revoked.
   - Renew the certificate if necessary.

2. **Update WS-Federation Metadata:**
   - Ensure that the WS-Federation metadata endpoint is correctly configured and accessible.
   - If updates have been made to the IdP, refresh or reconfigure the metadata settings on your application.

3. **Validate Claims:**
   - Check the claims that are being sent with the token from the IdP. Ensure that all expected claims are included and formatted correctly.
   - If required claims are missing, update the IdP configuration to include them.

4. **Test Network Connectivity:**
   - Use tools like `ping`, `telnet`, or `curl` to verify that the application can reach the IdP endpoint.
   - Check firewall and proxy settings to ensure they do not block the required communication.

5. **Review and Synchronize Configurations:**
   - Compare configurations between environments (development, testing, production) to ensure consistency.
   - Apply any necessary changes to align configurations across environments.

6. **Engage with the Identity Provider:**
   - If the issue persists, contact your Identity Provider's support team for assistance.
   - Provide them with all relevant logs and error messages.

---

### Additional Notes or Considerations
- **Time Synchronization:** Ensure that both the application and the IdP are synchronized to the same time source. Time discrepancies can lead to token validation failures.
- **Browser Cache/Cookies:** Clear browser cache or cookies in case of session-related issues.
- **Token Signing Algorithms:** Ensure that the token signing algorithms used are acceptable for both the application and IdP.

---

### Documentation and Guidance
- **Microsoft Documentation on WS-Federation:**
  [Microsoft WS-Federation Documentation](https://docs.microsoft.com/en-us/windows-server/identity/ad-fs/overview)
  
- **Azure Active Directory Error Codes:**
  [Azure AD Error Codes Documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/reference-aadsts-error-codes)

- **Configuration Guide:**
  [Setting up Federation with Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/hybrid/how-to-connect-fed-whatis)

**Make sure you can reach the provided documentation links for accurate guidance.**

---

### Advice for Data Collection
1. **Log Files:** Collect relevant logs from both the application and the Identity Provider.
2. **Token Information:** If possible, capture the security token being sent by the IdP and analyze its claims.
3. **Network Traces:** Use tools like Wireshark or Fiddler to capture network traffic between the application and the IdP for deeper analysis.
4. **Error Details:** Document specific error messages, timestamps, user identifiers, and any actions performed leading up to the issue.

By following this troubleshooting guide, you can systematically identify and resolve the AADSTS20012 error.