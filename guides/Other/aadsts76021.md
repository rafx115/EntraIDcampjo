# AADSTS76021: ApplicationRequiresSignedRequests - The request sent by client is not signed while the application requires signed requests


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS76021: ApplicationRequiresSignedRequests

**Error Description:**
AADSTS76021 indicates that the application you are trying to access requires signed requests, but the request sent from the client is not signed. This often occurs in scenarios involving Azure Active Directory (AAD) authentication where certain applications implement additional security measures by enforcing signed requests.

---

#### Initial Diagnostic Steps

1. **Understand the Context:**
   - Determine if this error occurs during a specific action (login, API call, etc.) and document the steps preceding the error.

2. **Identify the Client Configuration:**
   - Confirm the client application type (e.g., web app, mobile app) and the authentication methods used (e.g., OAuth2, OpenID Connect).

3. **Review Application Settings:**
   - Review the application registration settings in Azure AD to confirm whether signed requests are enforced.

4. **Check Azure AD Logs:**
   - Access Azure AD sign-in logs to identify any detailed logs for the failed request that can provide more context on the error.

---

#### Common Issues that Cause This Error

1. **Misconfiguration of the Client Application:**
   - The client may not be set up to sign requests properly, either due to missing libraries, incorrect settings, or misconfigured SDKs.

2. **Missing or Incorrect Signing Keys:**
   - If your application uses JWT tokens, ensure the signing keys are correctly configured on both the client and server.

3. **Outdated SDK or Library:**
   - The client SDK or library being used for authentication may be outdated and not support the required signing of requests.

4. **Policy Enforcement:**
   - The application’s Azure AD policies might enforce signed requests without the client being configured to comply.

---

#### Step-by-Step Resolution Strategies

1. **Configure Client Application for Signed Requests:**
   - Ensure that your client is configured to sign requests. Depending on the protocol used (OAuth2/OpenID Connect), follow these steps:
     - For OAuth2, ensure you use appropriate libraries that support signed requests (e.g., Microsoft Authentication Library).
     - Check if the request includes the necessary fields for signing, like a nonce or signature.

2. **Implement the Appropriate Signing Algorithm:**
   - Understand which signing algorithm your application requires (like HMAC, RSA, etc.).
   - Make sure the key used for signing corresponds to the application's expected key.

3. **Update SDK or Libraries:**
   - Upgrade the SDK or libraries used in your application to the latest versions which may include support for the necessary request signing.

4. **Manually Sign Requests:**
   - If your application does not use a library to handle signing, implement a manual signing process that adheres to Azure AD requirements.

5. **Test with Sample Application:**
   - Set up a sample application that successfully signs requests to validate your configuration against working examples.

6. **Review Azure AD Conditional Access Policies:**
   - If your organization uses Conditional Access policies, ensure they don’t unintentionally enforce signed requests outside expected scenarios.

---

#### Additional Notes or Considerations

- **End-to-End Security:**
  Ensure that you consider the overall security of your application. Enabling signed requests can help mitigate certain security risks.

- **Cross-Platform Considerations:**
  If the application is cross-platform, ensure that all clients maintain consistent signing logic and configuration to avoid discrepancies.

---

#### Documentation References

1. **Azure Active Directory Documentation**: [Azure AD Overview and Quickstarts](https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-v2-aspnet)
2. **Microsoft Authentication Library**: [MSAL documentation](https://learn.microsoft.com/en-us/azure/active-directory/develop/msal-overview)
3. **Common scenarios for Azure AD**: [Common scenarios with Azure AD](https://learn.microsoft.com/en-us/azure/active-directory/develop/scenario-desktop-setup)

**Test the Documentation:**
Attempt to navigate to the documentation links provided above to ensure they are accessible and up-to-date.

---

#### Advice for Data Collection

- **Collect Request Logs:**
  Capture logs for the requests made before the error occurs, including headers, payload, and error messages.

- **Azure AD Sign-In Logs:**
  Pull relevant logs from Azure AD for the corresponding application and times to compare details.

- **Gather SDK Version Information:**
  Document the versions of libraries or SDKs being used during the error to understand if you need to upgrade.

- **Environment Configuration:**
  Note the configuration settings of both the Azure AD application registration and the client application to verify they correspond to expected values.

---

By following these strategies and recommendations, you should be able to address the AADSTS76021 error effectively.

Category: Other