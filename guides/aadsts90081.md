
# AADSTS90081: OrgIdWsFederationMessageInvalid - An error occurred when the service tried to process a WS-Federation message. The message isn't valid.


## Troubleshooting Steps
Certainly! The AADSTS90081 error indicates that there was an issue processing a WS-Federation message in an Azure Active Directory (AAD) setup. This error often occurs when there are misconfigurations or issues related to federation setups, authentication, and application configurations. Here’s a structured troubleshooting guide for this error code:

## AADSTS90081 Troubleshooting Guide

### Initial Diagnostic Steps

1. **Check Azure Status**:
   - Visit the Azure status page ([Azure Status](https://status.azure.com/)) to see if there are any ongoing outages or service issues related to Azure Active Directory.

2. **Verify the User Account**:
   - Ensure that the user account facing the issue is active and not locked out.
   - Confirm that the account exists in the directory.

3. **Review the WS-Federation Configuration**:
   - Check the configuration settings within Azure AD and the application regarding WS-Federation. Look for any typos or incorrect URIs.

4. **Review Logs**:
   - If logs are available, review them for any additional error messages that might provide more context.

### Common Issues that Cause this Error

1. **Incorrect WS-Federation Gateway URL**:
   - The WS-Federation endpoint might be misconfigured in the application settings.

2. **Expired or Invalid Certificates**:
   - WS-Federation relies on certificates for secure communication. Expired or invalid certificates can lead to this error.

3. **Claims Configuration Issues**:
   - Misconfiguration in the claims configuration can cause the federation message to be invalid.

4. **Mismatch between Relying Party Identifier**:
   - Ensure that the relying party identifier configured in Azure matches what the application is sending.

5. **Network Issues**:
   - Network issues preventing a successful connection between the Identity Provider (IdP) and the Service Provider (SP).

### Step-by-Step Resolution Strategies

1. **Verify URIs and Endpoints**:
   - Go to Azure AD -> Enterprise Applications -> [Your Application] -> Single Sign-On.
   - Check the WS-Federation settings, ensure a correct Relay State and WS-Federation URL.

2. **Check Certificate Validity**:
   - Under Azure AD -> App registrations -> [Your Application] -> Certificates and secrets.
   - Ensure certificates are valid and not expired. If necessary, upload a new certificate.

3. **Inspect Claims Mapping**:
   - Navigate to Azure AD -> Enterprise Applications -> [Your Application] -> Users and groups.
   - Review claim settings and ensure they match expected claims in your application.

4. **Monitor and Test the Identity Provider Configuration**:
   - If using a custom IdP, ensure its configuration matches Azure AD requirements.
   - Utilize tools like Fiddler or Postman to send a sample WS-Federation request to diagnose issues.

5. **Network Diagnostics**:
   - Test connectivity via command line tools (ping, tracert) to ensure network paths are correct. Check firewalls for any restrictions on HTTP/S traffic related to federated services.

### Additional Notes or Considerations

- **Logging Levels**: Increase logging levels on the application (if possible) to capture more detailed diagnostic information.
- **Test Different Browsers**: Sometimes browser extensions/settings can affect authentication; test the login in incognito mode or using another browser.
- **Check Time Synchronization**: Ensure that both the client and server are synchronized in terms of time, as discrepancies can lead to authentication issues.

### Documentation for Guidance

- Microsoft Documentation on WS-Federation:
  - [Introduction to WS-Federation](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-ws-fed)
  - [Configure WS-Federation in Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-ws-fed-tutorial)

### Test Documentation Accessibility

- Test the given links directly in your browser to ensure they are up-to-date and reachable.

### Advice for Data Collection

- When gathering data for troubleshooting, consider the following:
  - **Error messages**: Record the exact error message and any accompanying codes.
  - **Logs**: Collect logs from the application and Azure AD for the period when the error occurred.
  - **Network Trace**: If applicable, gather network traces (using tools like Fiddler) to analyze communication between the application and Azure AD.
  - **Configuration Snapshots**: Take screenshots or exports of current configuration settings in Azure and the application for comparison after changes.

By following these steps and gathering the appropriate data, you should be able to identify and resolve the underlying cause of the AADSTS90081 error. If issues persist, consider reaching out to Microsoft Support for further assistance.