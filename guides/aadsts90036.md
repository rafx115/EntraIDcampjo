
# AADSTS90036: MsodsServiceUnretryableFailure - An unexpected, non-retryable error from the WCF service hosted by MSODS has occurred.Open a support ticketto get more details on the error.


## Troubleshooting Steps
**Troubleshooting Guide for Error Code AADSTS90036**

**Error Description:**
AADSTS90036 (MsodsServiceUnretryableFailure) indicates an unexpected, non-retryable error from the Windows Communication Foundation (WCF) service that is hosted by Microsoft Online Directory Services (MSODS). The error suggests that there is a significant issue that cannot be automatically resolved and requires assistance from Microsoft support.

---

### Initial Diagnostic Steps

1. **Understanding the Context:**
   - Identify the operation being performed when the error occurred (e.g., user sign-in, service provisioning).

2. **Check Service Status:**
   - Visit the [Microsoft 365 Service Health Status](https://portal.office.com/adminportal/home#/servicehealth) page to see if there are any ongoing outages or incidents affecting Microsoft services that could cause this error.

3. **Monitor Logs:**
   - Examine logs for any preceding errors or warnings that could give insight into the underlying issue leading to the AADSTS90036 error.

---

### Common Issues that Cause This Error

1. **Configuration Issues:**
   - Incorrect application settings or misconfigurations in Azure Active Directory (AAD) can lead to this error.

2. **User Account Issues:**
   - The user account experiencing the error may be in a non-intended state (e.g., disabled, deleted, or not properly synchronized).

3. **Service Availability:**
   - Temporary outages or issues with the MSODS service can cause unexpected failures.

4. **Intermittent Network Problems:**
   - Network connectivity issues between the client application and Azure services may lead to unexpected errors.

---

### Step-by-Step Resolution Strategies

1. **Review Configuration:**
   - Go to the Azure portal and confirm your application's registration settings, including redirect URIs, permission scopes, and other configurations.
   - Ensure that there are no erroneous settings for Identity Provider configurations if applicable.

2. **Check User Account Status:**
   - Navigate to Azure Active Directory > Users.
   - Search for the affected user and verify their account status. Make sure the account is enabled and properly licensed.

3. **Try a Different User or App:**
   - Test with another user account or application to determine if the issue is isolated to a specific configuration or account.

4. **Engage Support:**
   - If no configuration issues are found and the error persists, open a support ticket with Microsoft. Provide detailed logs, reproduction steps, and any other relevant information. 

5. **Monitor Service Health:**
   - Keep an eye on the Service Health dashboard to see if there are updates regarding the status of the MSODS service.

---

### Additional Notes or Considerations

- **Rate Limiting:** Be aware that excessive requests can sometimes lead to throttling errors. Ensure your application is within Azure AD's thresholds for the number of API calls.
  
- **Timing:** If the issue appears to be intermittent, it may relate to service availability during heavy usage times.

- **Authentication Flows:** Ensure that the authentication flow (authorization code, implicit, etc.) is implemented correctly as per Microsoft guidelines.

---

### Documentation for Guidance

For further details and step-by-step guidance, refer to the following Microsoft documentation:
- [Azure Active Directory Authentication](https://docs.microsoft.com/en-us/azure/active-directory/develop/)
- [Troubleshooting Sign-in Issues](https://docs.microsoft.com/en-us/azure/active-directory/user-help/troubleshoot-sign-in-issues)
- [Microsoft 365 Service Health](https://portal.office.com/adminportal/home#/servicehealth)

**Testing Accessibility of Documentation:**
You can check the above links in your browser to ensure they are reachable and provide the necessary information to resolve the error.

---

### Advice for Data Collection

When preparing to troubleshoot or to open a support ticket, collect the following data:
- Detailed logs around the time the error occurred.
- Steps to reproduce the error, including exact user actions.
- Any relevant configurations/settings from the Azure portal.
- Screenshots of errors or the context in which the error appears.
- User account details (not sensitive data) such as state, license status, and roles.

By following the structured troubleshooting steps and guidelines outlined above, you should be able to diagnose and resolve the AADSTS90036 error or gather the necessary information for Microsoft support to assist you further.