# AADSTS50017: CertificateValidationFailed - Certification validation failed, reasons for the following reasons:Cannot find issuing certificate in trusted certificates listUnable to find expected CrlSegmentCannot find issuing certificate in trusted certificates listDelta CRL distribution point is configured without a corresponding CRL distribution pointUnable to retrieve valid CRL segments because of a timeout issueUnable to download CRLContact the tenant admin.

## Troubleshooting Steps

### Troubleshooting Guide for Error Code AADSTS50017: CertificateValidationFailed

#### **Initial Diagnostic Steps:**

1. **Confirm the Error:** Make sure the error code AADSTS50017 with the
   description "CertificateValidationFailed" appears consistently.
2. **Check Certificate Configuration:** Verify the certificate used for
   authentication and its configuration in the troubled service.

#### **Common Issues:**

1. **Missing Issuing Certificate:** The certificate required for validation is
   not included in the trusted certificates.
2. **CRL Issues:** Problems with Certificate Revocation Lists (CRL) like missing
   segments or timeout issues.
3. **Misconfigured CRL Distribution Points:** Issues with the delta CRL
   distribution point or incorrect configuration.
4. **Network Connectivity:** Timeout issues while downloading CRL due to network
   problems.

#### **Step-by-Step Resolution Strategies:**

1. **Check Trusted Certificates:**
   - Ensure the issuing certificate is added to the trusted certificates list.
2. **Verify CRL Configuration:**

   - Ensure CRL distribution points are correctly configured and accessible.
   - Check that delta CRL distribution points are correctly configured.

3. **Resolve CRL Downloading Issues:**

   - Confirm the network connectivity and timeout settings for downloading CRL.
   - Troubleshoot any network-related issues causing CRL download failures.

4. **Contact Tenant Admin:**
   - If the issue persists, contact the admin of the tenant for further
     assistance or to validate the certificate configurations.

#### **Additional Notes or Considerations:**

- **Certificate Renewal:** Check if the certificate in use has expired or if a
  newer certificate is available.
- **Network Security:** Verify if any security measures are blocking the CRL
  download or if a proxy server is causing issues.

#### **Documentation for Guidance:**

- Microsoft Azure Active Directory documentation provides extensive resources on
  Azure AD error codes and troubleshooting. Navigate to
  [Azure AD Error Codes](https://docs.microsoft.com/en-us/azure/active-directory/develop/reference-aadsts-error-codes)
  for detailed information on troubleshooting common errors.

By following the outlined steps and considering the common issues, you should be
able to diagnose and resolve the AADSTS50017 error related to
CertificateValidationFailed effectively.
