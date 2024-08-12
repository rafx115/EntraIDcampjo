
# AADSTS50017: CertificateValidationFailed - Certification validation failed, reasons for the following reasons:Cannot find issuing certificate in trusted certificates listUnable to find expected CrlSegmentCannot find issuing certificate in trusted certificates listDelta CRL distribution point is configured without a corresponding CRL distribution pointUnable to retrieve valid CRL segments because of a timeout issueUnable to download CRLContact the tenant admin.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS50017: Certificate Validation Failed

The error code `AADSTS50017` indicates that there are issues with certificate validation. This can occur due to multiple factors, including problems with the certificate itself or issues accessing Certificate Revocation Lists (CRLs). Below is a comprehensive troubleshooting guide.

---

### Initial Diagnostic Steps

1. **Event Viewer Check**:
   - Open Windows Event Viewer (`eventvwr.msc`) on the client or server experiencing the issue.
   - Navigate to `Windows Logs` -> `Application` and look for any logged errors related to Certificate Services or Active Directory Authentication.

2. **Network Connectivity**:
   - Test network connectivity to ensure the device can reach the required URLs for CRLs.
   - You can use commands like `ping` or `tracert` to check the connectivity to the CRL distribution point.

3. **Check Certificate Validity**:
   - Use `certutil -verify` on the server/client in question to diagnose any issues with the certificate’s status.
   - Ensure the certificate chain is intact and that each certificate is trusted.

4. **Inspect Certificate Store**:
   - Validate the presence of the issuing certificate in the Trusted Root Certification Authorities store.
   - Open `certmgr.msc`, navigate to `Trusted Root Certification Authorities`, and check if the correct root certificate is present.

---

### Common Issues That Cause This Error

1. **Missing Issuing Certificate**:
   - The certificate chain is incomplete or the issuer’s certificate is not found in the Trusted Root Certification Authorities.

2. **CRL Access Issues**:
   - The application is unable to access the CRL distribution points due to firewall settings, network issues, or incorrect CRL URLs.

3. **Delta CRL Configuration**:
   - Issues arise when Delta CRLs are configured without a proper distribution point for the base CRL, or if the necessary segments are unavailable.

4. **Timeout Issues**:
   - Timeout while trying to retrieve the CRL could occur due to high network latency or server unavailability.

---

### Step-by-Step Resolution Strategies

#### Step 1: Verify Certificate Chain

- Check if the loading application has access to the full certificate chain (including intermediate and root).
- Validate that the certificate is not expired or revoked.

#### Step 2: Check Trusted Root Certificates

- Open `certmgr.msc`, navigate to:
  - **Trusted Root Certification Authorities**: Make sure the root certificate is present and has not been deleted or expired.
  - **Intermediate Certification Authorities**: Ensure that any intermediate certificates are present.

#### Step 3: Assess Network Connectivity to CRLs

- Attempt to access the CRL distribution points using a web browser or `curl` command.
- Check your network settings, ensuring that firewalls or proxies are not blocking access to these endpoints.

#### Step 4: Validate CRL Distribution Points

- Check the certificate properties for the CRL distribution point URIs.
- Make sure the CRL Distribution Points are reachable.
- If you cannot reach the points, consider working with your network team to unblock the URLs.

#### Step 5: Reconfigure Delta CRLs

- If Delta CRLs are used, ensure that appropriate configuration exists for base CRLs as well.
- Verify in your CA settings to ensure both types of CRLs are properly published.

#### Step 6: Test Under Different Conditions

- If possible, try using a different network or device to validate whether the issue is local to a particular setup.
  
---

### Additional Notes or Considerations

- **DNS Issues**: If CRL URLs depend on DNS resolution, ensure DNS is functioning correctly.
- **Group Policy Settings**: Verify if there are any configured group policies that could be affecting certificate trust.
- **Update System Time**: Ensure the system’s date and time settings are synchronized; discrepancies can affect certificate validation.

---

### Documentation for Further Guidance

- Microsoft Docs on [Certificate Services](https://docs.microsoft.com/en-us/windows-server/identity/ad-certificate-services).
- Microsoft Docs on [Managing Certificate Revocation List](https://docs.microsoft.com/en-us/windows-server/identity/ad-certificate-services/manage/manage-crl).

---

### Advice for Data Collection

1. **Event Viewer Logs**:
   - Export relevant logs from Event Viewer, particularly focusing on events related to `Certificate Services`.

2. **NetTrace**:
   - Use the `netsh trace` command to collect network tracing data while trying to access the CRL.

3. **Fiddler**:
   - Use Fiddler to capture HTTP/HTTPS requests to the CRL distribution URLs, analyzing the responses for errors or timeouts.

4. **Network Logs**:
   - Document any relevant network logs, especially if using protocols like LDAP or HTTP for certificate retrievals.

---

By following this guide, you should be able to diagnose and possibly resolve the `AADSTS50017` error. If the issue persists, further assistance from your organization's IT support or Microsoft support may be necessary.