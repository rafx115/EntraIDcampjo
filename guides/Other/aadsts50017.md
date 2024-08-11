# AADSTS50017: CertificateValidationFailed - Certification validation failed, reasons for the following reasons:Cannot find issuing certificate in trusted certificates listUnable to find expected CrlSegmentCannot find issuing certificate in trusted certificates listDelta CRL distribution point is configured without a corresponding CRL distribution pointUnable to retrieve valid CRL segments because of a timeout issueUnable to download CRLContact the tenant admin.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS50017 - CertificateValidationFailed

The error code AADSTS50017 indicates that there were issues validating a certificate during authentication. Below is a detailed troubleshooting guide designed to help you diagnose and resolve this error.

#### Initial Diagnostic Steps

1. **Identify the Application**: Determine which application or service is producing the AADSTS50017 error.
  
2. **Gather Error Details**: Look for any additional error messages or logs that accompany the AADSTS50017 error to gain more context.

3. **Check the Certificate**:
   - Determine which certificate is being used.
   - Confirm it is present and correctly configured in Azure AD.

4. **Check Trust Chain**: Verify that the root and intermediate certificates are trusted and present in your environment.

#### Common Issues Causing This Error

1. **Missing Intermediate or Root Certificates**: The issuing certificate might not be in the trusted certificate store.
  
2. **CRL Access Issues**: There could be problems accessing the Certificate Revocation List (CRL), such as:
   - Timeout while trying to reach the CRL distribution point.
   - Lack of internet connectivity blocking access to the CRL.

3. **Configuration Errors**: Misconfigured CRL settings, such as Delta CRL distribution points that do not correspond to CRL distribution points.

4. **Firewall Restrictions**: Firewalls or proxies blocking access to the CRL distribution points.

#### Step-by-Step Resolution Strategies

##### 1. Validate the Certificate Chain
   - Check if the certificate used by your application is valid and has not expired.
     - **Action**: Use tools like **OpenSSL** or **certutil** to examine the certificate and ensure the root and intermediate certificates are installed.

##### 2. Ensure CRL Access
   - Confirm that you can reach the CRL endpoints.
     - **Action**: Use `curl` or `ping` commands to check the CRL distribution point URLs from the machine experiencing the error.
     ```
     curl <CRL_URL>
     ```
   - Check firewall/proxy settings to ensure they allow outbound HTTPS traffic to CRL URLs.

##### 3. Install Missing Certificates
   - If you identify any missing certificates:
     - **Action**: Download the required root and intermediate certificates from the CA or the issuer's website and install them into your trusted root and intermediate certification authorities.

##### 4. Configure Delta CRL Settings
   - If Delta CRL distribution points are configured, ensure they are correctly set up and reachable.
     - **Action**: Review CRL configuration settings in your certificate manager/enterprise CA settings.

##### 5. Network Diagnostics
   - Check your network to ensure connectivity issues are resolved.
   - **Action**: If using a corporate network, consult with your network administration team about potential restrictions.

#### Additional Notes or Considerations

- **Certificates Expiry**: Regularly monitor the expiry dates of certificates in your environment to avoid unexpected downtime.
- **Logging**: Enable certificate validation logging in your application to gather more detailed error information if the problem persists.
  
#### Documentation for Further Guidance

- Azure Active Directory Authentication Errors: [Microsoft Documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/authentication-scenarios)
- Managing Certificates in Azure AD: [Microsoft Docs - Manage certificates](https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-manage-certificates)
- CRL Distribution Point Configuration: [RFC 5280](https://tools.ietf.org/html/rfc5280)

#### Test Documentation Accessibility

Ensure you can reach the documentation links mentioned above. Open a browser and navigate to the URLs provided to check the accessibility of Microsoft Docs.

#### Advice for Data Collection

- Collect log files and error messages from the affected application.
- Gather network access logs, especially around the time of the error occurrence.
- Record the configuration details of involved certificates, such as paths to the certificates, CRL URLs, and any related settings.

By following these troubleshooting steps, you should be able to diagnose and resolve the AADSTS50017 error effectively. If issues persist, consider reaching out to Microsoft support for further assistance.

Category: Other