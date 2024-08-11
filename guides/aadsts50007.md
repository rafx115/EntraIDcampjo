# AADSTS50007: PartnerEncryptionCertificateMissing - The partner encryption certificate wasn't found for this app.Open a support ticketwith Microsoft to get this fixed.

## Troubleshooting Steps

### Troubleshooting Guide for Error Code AADSTS50007: PartnerEncryptionCertificateMissing

#### Initial Diagnostic Steps:

1. Confirm the exact error message and error code received (AADSTS50007).
2. Identify the application or service where the error is occurring.
3. Verify if the application is integrated with Azure Active Directory (AAD).

#### Common Issues that Cause this Error:

- Missing partner encryption certificate for the application or service in Azure
  AD.
- Incorrect configuration of encryption certificates in the Azure portal.
- Expired or revoked encryption certificate.
- Incorrect permissions or access rights assigned to the application.

#### Step-by-Step Resolution Strategies:

1. **Check Azure AD Application Settings**:

   - Log in to your Azure portal and navigate to the Azure AD.
   - Go to the application's settings and verify the encryption certificate
     details.

2. **Generate and Upload Encryption Certificate**:

   - If the partner encryption certificate is missing, generate a new encryption
     certificate.
   - Upload the new certificate to the Azure AD application settings.

3. **Verify Certificate Expiry and Revocation**:

   - Check if the encryption certificate used by the application has expired or
     been revoked.
   - Renew or reissue the encryption certificate if necessary.

4. **Assign Correct Permissions**:

   - Ensure that the application has the necessary permissions and access rights
     in Azure AD.
   - Grant the required permissions for the application to function properly.

5. **Contact Microsoft Support**:
   - Open a support ticket with Microsoft for further assistance in resolving
     the PartnerEncryptionCertificateMissing error.
   - Provide detailed information about the issue and steps you have already
     taken.

#### Additional Notes or Considerations:

- Regularly monitor and update encryption certificates to prevent such errors.
- Review Azure AD application configurations periodically for any discrepancies.
- Keep records of encryption certificates and their expiration dates.

#### Documentation for Guidance:

For detailed guidance and step-by-step instructions on managing Azure AD
applications and certificates, refer to the official Azure AD documentation:

- [Azure Active Directory documentation](https://docs.microsoft.com/en-us/azure/active-directory/)
- [Azure AD Application and Service Principal Objects](https://docs.microsoft.com/en-us/azure/active-directory/develop/app-objects-and-service-principals)
- [Managing Certificates in Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-self-signed-certificate)

Following these steps should help you troubleshoot and resolve the
PartnerEncryptionCertificateMissing error code AADSTS50007 effectively. If the
issue persists, Microsoft Support will be able to provide further assistance.
