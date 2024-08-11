# AADSTS50017: CertificateValidationFailed - Certification validation failed, reasons for the following reasons:Cannot find issuing certificate in trusted certificates listUnable to find expected CrlSegmentCannot find issuing certificate in trusted certificates listDelta CRL distribution point is configured without a corresponding CRL distribution pointUnable to retrieve valid CRL segments because of a timeout issueUnable to download CRLContact the tenant admin.

## Introduction
This guide will help resolve issues related to certificatevalidationfailed - certification validation failed, reasons for the following reasons:cannot find issuing certificate in trusted certificates listunable to find expected crlsegmentcannot find issuing certificate in trusted certificates listdelta crl distribution point is configured without a corresponding crl distribution pointunable to retrieve valid crl segments because of a timeout issueunable to download crlcontact the tenant admin..

## Prerequisites
- Access to the Azure AD portal with administrator privileges.
- The user must have already set up MFA.

## Steps to Resolve

### Step 1: Initial Actions
1. Log in to the Azure AD portal.
2. Navigate to the "Users" section.
3. Select the affected user.
4. Perform necessary actions as described for the error.

### Step 2: Verify MFA Settings
1. Ensure that the user has MFA configured.
2. If necessary, guide the user through the MFA setup process.

## Troubleshooting
- Check for any Azure AD conditional access policies that might be affecting the MFA process.
- Consider any additional security measures that might be in place.

## Additional Notes
- Refer to the [Azure AD documentation](https://learn.microsoft.com/en-us/azure/active-directory/) for more details.


## Troubleshooting Steps
Troubleshooting steps could not be generated due to an error.

## Troubleshooting Steps
Troubleshooting steps could not be generated due to an error.

## Troubleshooting Steps
Error code AADSTS50017 with the description "CertificateValidationFailed" indicates that there are issues with certificate validation during authentication. This error can occur due to various reasons as mentioned in the description. Here is a detailed troubleshooting guide to address this error:

### Initial Diagnostic Steps:
1. **Check the Error Message Details**: Understand the specific reasons for the certificate validation failure provided in the error description.
2. **Review Certificate Configuration**: Ensure that the certificates used for authentication are valid, not expired, and correctly configured.
3. **Communicate with Tenant Admin**: If the error persists, contact the tenant admin for assistance and provide them with the error details.

### Common Issues Causing the Error:
1. **Missing Issuing Certificate**: The certificate used for authentication is not present in the trusted certificates list.
2. **CRL Segments Issues**: Problems related to the Certificate Revocation List (CRL) segments like not finding the expected CRL segment or a timeout issue.
3. **Delta CRL Configuration**: Delta CRL distribution point may be configured without a corresponding CRL distribution point.
4. **Network Issues**: Connection timeout or inability to download the CRL due to network-related problems.

### Step-by-Step Resolution Strategies:
1. **Add Issuing Certificate to Trusted List**:
   - Obtain the issuing certificate from the certificate authority.
   - Add the issuing certificate to the trusted certificates list on the server or client where authentication is being performed.
  
2. **Ensure CRL Configuration**:
   - Check the CRL distribution points in the certificates and ensure they are valid and accessible.
   - Verify that the expected CRL segments are present and can be retrieved without any timeout issues.
  
3. **Review Delta CRL Configuration**:
   - If delta CRL is used, ensure that it is configured correctly with corresponding CRL distribution points.
  
4. **Resolve Network Issues**:
   - Check network connectivity to the CRL distribution points.
   - Confirm that there are no firewall restrictions blocking the download of CRL segments.
  
5. **Contact Tenant Admin**:
   - If the issue persists after performing the above steps, contact the tenant admin for further assistance and troubleshooting.

### Additional Notes or Considerations:
- **Certificate Expiry**: Regularly monitor the validity of certificates and renew them before expiration.
- **Network Configuration**: Ensure that the server or client can access the network resources required for CRL retrieval.
- **Logging and Monitoring**: Enable detailed logging to track certificate validation errors and monitor the authentication process for any issues.

By following these steps and considering the common causes of the error, you should be able to troubleshoot and resolve the AADSTS50017 error related to CertificateValidationFailed.