# AADSTS20012: WsFedMessageInvalid - There's an issue with your federated Identity Provider. Contact your IDP to resolve this issue.


## Troubleshooting Steps
Certainly! The error code **AADSTS20012**, with the description "WsFedMessageInvalid - There's an issue with your federated Identity Provider. Contact your IDP to resolve this issue," generally indicates a problem with the communication between Azure Active Directory (AAD) and the federated identity provider (IdP). Here’s a detailed troubleshooting guide to help you diagnose and resolve this error.

### 1. Initial Diagnostic Steps

- **Confirm the Error:** Ensure that the error is reproducible and occurs consistently.
- **Check User Details:** Validate the user account attempting to authenticate, ensuring that it exists in AAD and is properly configured.
- **Verify Browser/Network Conditions:** Attempt the sign-in using different browsers or devices, and check if the issue persists.

### 2. Common Issues That Cause This Error

- **Invalid Tokens:** The tokens received from the federated IdP may be malformed or invalid.
- **Issues with Federation Metadata:** Changes in the IdP configuration may not be reflected correctly in the federation metadata.
- **Certificate Issues:** The signing certificate used by the IdP may be expired or mismatched.
- **Clock Skew:** Time synchronization issues between AAD and the IdP can lead to token validation failures.
- **Misconfiguration of Relying Party Trust:** Issues in the settings for the relying party trust in the IdP.

### 3. Step-by-Step Resolution Strategies

- **Check Federation Metadata:**
  1. Access the federation metadata URL configured for your AAD.
  2. Ensure that it's accessible and returns the correct XML metadata.
  3. Compare this with the settings in your IdP to ensure consistency.

- **Validate Certificates:**
  1. Check the signing certificate used by your IdP for expiration.
  2. If needed, update the certificate in AAD with the new public key.

- **Confirm User Configuration:**
  1. Ensure that the user account is properly set up within the IdP.
  2. Verify that the account is not locked or disabled.
  3. Ensure that the user is associated with the correct claims.

- **Inspect Claims and Token Structure:**
  1. Use tools like Fiddler or Postman to capture the token being sent.
  2. Inspect the structure to ensure it conforms to expected formats, like WS-Federation.

- **Time Synchronization:**
  1. Confirm that both the IdP and AAD servers are synchronized to an accurate time source. Use NTP for synchronization.
  2. Check the expiration times of tokens to ensure they are valid at the time of verification.

- **Check Logs:**
  1. Review the event logs on the server that hosts the federated IdP.
  2. Look for errors related to token generation or user authentication.

### 4. Additional Notes or Considerations

- **Service Provider Logs:** If you are using a custom application, also check the logs for the application to see if any additional information related to the error is logged.
- **Identity Provider Support:** If you continue having issues, consider contacting the support team of your federated IdP for assistance.

### 5. Documentation for Further Guidance

- **Azure Active Directory Documentation**: 
  - [Integrate your app with Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-v2-aspnet)
  - [WS-Federation authentication](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-ws-fed-protocol)

### 6. Advice for Data Collection

- **Event Viewer Logs:**
  1. On the server running your IdP, open the Event Viewer and check for any relevant logs under "Applications and Services Logs."
  2. Look for Event ID that might provide additional error messages about token issues.

- **Network Trace:**
  1. Use *NetTrace* to capture packets while reproducing the issue. Filter by the protocol (e.g., HTTPS) to focus on relevant traffic.
  2. Analyze any failed requests or unusual response codes.

- **Using Fiddler:**
  1. Set up Fiddler to capture HTTP(S) traffic while the error is reproduced.
  2. Inspect the requests to the IdP, and check the response payload for hints on what's going wrong.

Utilizing these steps should help you effectively diagnose and resolve the AADSTS20012 error. If you require further assistance, consider working with your Identity Provider's support or consulting Microsoft's support directly.