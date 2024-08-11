# AADSTS50003: MissingSigningKey - Sign-in failed because of a missing signing key or certificate. This might be because there was no signing key configured in the app. To learn more, see the troubleshooting article for errorAADSTS50003. If you still see issues, contact the app owner or an app admin.


## Troubleshooting Steps
Troubleshooting Guide for Error Code AADSTS50003: MissingSigningKey

1. Initial Diagnostic Steps:
- Verify the error code AADSTS50003 to confirm that it is indeed related to a MissingSigningKey issue.
- Check the configuration settings of the app to see if a signing key or certificate is missing.
- Review any recent changes made to the app or its configuration that may have led to the error.

2. Common Issues that Cause this Error:
- Incorrect or missing configuration of signing keys in the app settings.
- Expired, revoked, or invalid signing key or certificate.
- Incorrect permissions or roles assigned to the app causing issues with accessing signing keys.
- Changes made to the app configuration without updating corresponding signing key settings.

3. Step-by-step Resolution Strategies:
a. Check App Configuration:
   - Sign in to the Azure portal and navigate to the app's settings.
   - Verify that the correct signing key or certificate is configured.
   - If no signing key is configured, follow the steps to add a new signing key.

b. Generate a New Signing Key:
   - If a signing key is missing, follow the steps to generate a new key.
   - Ensure that the new key is securely stored and updated in the app's configuration.

c. Check Key Expiry:
   - If the signing key has expired, generate a new key and update the app's configuration with the new key.
   - Remove any expired or revoked keys from the configuration settings.

d. Permissions and Roles:
   - Ensure that the app has the necessary permissions to access the signing key.
   - Review the app's roles and permissions settings in Azure AD to ensure proper access to keys.

4. Additional Notes or Considerations:
- Regularly monitor the expiration dates of signing keys and certificates to prevent issues.
- Keep backup copies of signing keys in secure locations to avoid loss of access.

5. Documentation:
- For detailed guidance on configuring signing keys in Azure AD and troubleshooting AADSTS50003 errors, refer to the Microsoft documentation:
   [Troubleshoot AADSTS50003: MissingSigningKey](https://docs.microsoft.com/en-us/azure/active-directory/develop/reply-url-protection#error-aadsts5000304)
   [Azure AD documentation](https://docs.microsoft.com/en-us/azure/active-directory/)

By following these steps and ensuring the correct configuration of signing keys, you can resolve the AADSTS50003 error related to a MissingSigningKey issue in your Azure AD app.