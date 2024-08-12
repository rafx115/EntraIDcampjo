
# AADSTS90087: OrgIdWsFederationMessageCreationFromUriFailed - An error occurred while creating the WS-Federation message from the URI.


## Troubleshooting Steps
Certainly! The AADSTS90087 error, indicating that an issue occurred during the creation of a WS-Federation message, can impede authentication processes. Below is a comprehensive troubleshooting guide detailing diagnostic steps, common issues, resolution strategies, and information for data collection.

### Troubleshooting Guide for AADSTS90087

#### 1. Initial Diagnostic Steps
- **Check Error Context**: Identify the context in which the error occurs. Is it related to a specific application, user, or event?
- **Reproduce the Issue**: Attempt to reproduce the error to confirm its persistence. Document any steps that lead to the error.
- **Review User Feedback**: Collect feedback from users experiencing the issue, including their environment (browser type/version, network conditions, etc.).

#### 2. Common Issues that Cause This Error
- **Incorrect Configuration**: The most common cause is misconfiguration of the WS-Federation settings in Azure or the relying party application.
- **Invalid URI**: The URI used to initiate the authentication may not be correctly formatted or may not match the trusted URIs configured in Azure AD.
- **Certificate Issues**: Expired or misconfigured certificates used in the WS-Federation setup can cause failures.
- **Audience URI Mismatch**: The audience element in the security token may not match what the application is expecting.
- **Network Issues**: Firewalls or proxy settings may interfere with the communication between the user and Azure AD.

#### 3. Step-by-Step Resolution Strategies
1. **Verify WS-Federation Settings**:
   - Log into the Azure portal.
   - Navigate to Azure Active Directory → Enterprise applications → [Your Application].
   - Go to "Single sign-on" and review the WS-Federation settings. Ensure all URIs are correctly configured.

2. **Check the Relying Party (RP) Assertion**:
   - Ensure that the RP’s configuration (especially the "wreply" parameter) matches the reply URL registered in Azure AD.
   - Validate that the application is capable of accepting the token issued by Azure AD.

3. **Examine Certificates**:
   - Ensure that all certificates used for signing and encryption are valid.
   - Check for certificate expiration or misconfiguration. This can be managed under "Enterprise applications" in the Azure portal.

4. **Test URL Encoding**:
   - Ensure that the URLs in the WS-Federation request are URL-encoded appropriately.
   - Invalid characters in the URI can lead to improper request formation.

5. **Inspect Audience URI**:
   - Validate that the audience defined in the security token matches what the application expects. Adjust the application settings if necessary.

6. **Network Examination**:
   - Review network configurations to ensure the application can reach Azure AD without impediments.

#### 4. Additional Notes or Considerations
- **Logs and Traces**: Consider enabling diagnostic logs in the Azure portal for the application. This can provide more insight into authentication issues.
- **Application Updates**: Ensure that the application is up-to-date and compliant with any changes in Azure AD protocols.
- **Custom Application Logic**: If the application implements custom authentication logic, ensure that it correctly handles the WS-Federation protocols.

#### 5. Documentation for Guidance
- **Azure AD WS-Federation**: [WS-Federation with Azure Active Directory](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-ws-federation)
- **Application Configuration Guide**: [Integrate your web application with Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/develop/scenario-web-app-sign-in)

#### 6. Advice for Data Collection
- **Event Viewer Logs**: Check the Application and System logs for any relevant errors or warnings related to authentication services. Look for entries from the AD FS service, if applicable.
- **Network Traces**: Use tools like **Wireshark** or **Fiddler** to capture traffic during the WS-Federation flow. Look for anomalies in the requests or responses.
- **NetTrace**: If applicable, run a .NET network trace to monitor the authentication calls and log outputs that might point to where the failure occurs.

By following this structured approach, you can identify and resolve issues related to AADSTS90087 efficiently, ensuring a smoother authentication experience for users.