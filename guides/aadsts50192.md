
# AADSTS50192: Invalid Request - RawCredentialExpectedNotFound - No Credential was included in the sign-in request. Example: user is performing certificate-based authentication (CBA) and no certificate is sent (or Proxy removes) the user's certificate in the sign-in request.


## Troubleshooting Steps
Certainly! The error code AADSTS50192 indicates an issue with certificate-based authentication (CBA) where a required credential, typically a certificate, is not present in the sign-in request. Below is a detailed troubleshooting guide that includes diagnostic steps, common issues, resolution strategies, additional notes, relevant documentation, and advice for data collection.

### Troubleshooting Guide for AADSTS50192

#### Initial Diagnostic Steps
1. **Confirm the Error**: Verify that the error message AADSTS50192 is indeed being encountered during the sign-in process.
2. **Check Authentication Method**: Confirm that the user is attempting to use certificate-based authentication, as indicated in the error message.
3. **Review User Account Configuration**: Ensure that the user's account is properly configured for CBA in Azure AD.

#### Common Issues That Cause This Error
1. **Missing Client Certificate**: The most common cause is that the client certificate is not being sent with the authentication request.
2. **Proxy Interference**: A network proxy might be removing the client certificate from the sign-in request.
3. **Device Configuration Issues**: The machine may not be configured properly to present the necessary client certificate.
4. **Certificate Revocation**: The certificate being used might be revoked or expired.
5. **Certificate Store Issues**: The certificate might not be present in the appropriate store on the client machine.
6. **Browser Configuration**: Some browsers might not have the necessary configurations to send client certificates.

#### Step-by-Step Resolution Strategies
1. **Verify Client Certificate Installation**:
   - Check if the client certificate is installed in the appropriate certificate store (typically Personal store for the user).
   - **Windows**: Open the Certificate Manager (`certmgr.msc`) and navigate to `Personal -> Certificates` to ensure the certificate is present.

2. **Check Certificate Validity**:
   - Ensure that the client certificate is valid (not expired or revoked).
   - If necessary, obtain a new client certificate from the Certificate Authority (CA).

3. **Inspect Proxy Settings**:
   - If a proxy is in use, check the configuration to ensure that it allows the client certificate to pass through. Disable the proxy temporarily to see if authentication succeeds without it.

4. **Confirm Browser & Application Settings**:
   - If using a web browser, ensure that the browser is configured to present client certificates correctly.
   - Check that no extensions or settings are causing the rejection of client certificates.

5. **Review Authentication Logs**:
   - Check Azure AD sign-in logs in the Azure portal for more details. Navigate to Azure Active Directory > Security > Sign-in logs.
   - Look for any related logs that might indicate issues with the sign-in process.

6. **Perform a Test with Different Devices**:
   - Attempt to sign in from a different device that is known to have a working certificate to isolate the issue.

7. **Check Group Policies**:
   - Review any group policies that might impact certificate retrieval or network settings, especially regarding HTTP/HTTPS traffic.

#### Additional Notes or Considerations
- **User Education**: Ensure users understand the need for the client certificate and how to install it properly.
- **Network Environment**: Understand the network environment the client is in, including firewall settings that may affect the authentication process.
- **Antivirus/Firewall**: Sometimes, antivirus or firewall settings may block certificate auth-related traffic.

#### Documentation for Guidance
- Microsoft Documentation on Certificate-Based Authentication: [Certificate-Based Authentication Overview](https://learn.microsoft.com/en-us/azure/active-directory/develop/active-directory-certificate-based-authentication)
- Troubleshooting Azure AD sign-in issues: [Troubleshoot Azure AD Sign-In](https://learn.microsoft.com/en-us/azure/active-directory/authentication/howto-authentication-logs)

#### Advice for Data Collection
- **Event Viewer Logs**: Check the Security and Application logs for events related to authentication or certificate usage.
- **Network Tracing (nettrace)**: Use tools like Microsoft Message Analyzer or Wireshark to capture network traffic to diagnose whether the certificate is being sent.
- **Fiddler**: Use Fiddler to inspect the HTTP(S) traffic and check if the client certificate is being displayed and passed in the request headers.

By following these steps, you should be able to diagnose and resolve the issues related to error code AADSTS50192. If the issue persists after exhaustive troubleshooting, consider reaching out to Azure support for more dedicated assistance.