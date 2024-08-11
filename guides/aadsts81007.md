# AADSTS81007: DesktopSsoTenantIsNotOptIn - The tenant isn't enabled for Seamless SSO.


## Troubleshooting Steps
Error Code: AADSTS81007
Description: DesktopSsoTenantIsNotOptIn - The tenant isn't enabled for Seamless SSO.

Troubleshooting Guide:

Initial Diagnostic Steps:
1. Verify that the error code received is AADSTS81007, indicating an issue with Seamless Single Sign-On (SSO).
2. Confirm that your tenant is expected to support Seamless SSO.
3. Check if the Seamless SSO feature has been correctly configured within your Azure AD tenant.

Common Issues:
1. Azure AD tenant not properly configured for Seamless SSO.
2. Misconfiguration of domain in Azure AD.
3. Incorrect settings or missing configuration in Azure AD.

Resolution Strategies:

Step 1: Verify Seamless SSO Configuration Settings
1. Log in to the Azure portal using administrator credentials.
2. Navigate to Azure Active Directory > Azure AD Connect.
3. Check if Seamless SSO is enabled and configured correctly.
4. If not enabled, follow the on-screen instructions to enable Seamless SSO.
5. Save the changes and wait for the configuration to replicate.

Step 2: Check Domain Configuration
1. Go to Azure Active Directory > Custom domain names.
2. Ensure that the domain used for Seamless SSO is added and verified in Azure AD.
3. Check if the domain is set up for Seamless SSO by enabling the required settings.
4. Save any changes made to the domain settings.

Step 3: Verify User Sign-In Experience
1. Have a user attempt to sign in using the Seamless SSO feature.
2. Monitor for any errors and confirm if the issue persists.
3. If the error reoccurs, review the configuration settings and make necessary adjustments.

Additional Notes or Considerations:
- Ensure that you have the necessary administrator permissions to configure Seamless SSO in Azure AD.
- Review any recent changes made to the Azure AD tenant that might have affected Seamless SSO.
- Check for any service advisories or updates from Microsoft related to Seamless SSO.

Documentation for Guidance:
For detailed steps on configuring Seamless SSO in Azure AD, refer to the official Microsoft documentation:
- Microsoft Docs: Configure seamless single sign-on for Azure AD Connect: https://docs.microsoft.com/en-us/azure/active-directory/hybrid/how-to-connect-sso-quick-start

By following the outlined troubleshooting guide and verifying the Seamless SSO configuration in your Azure AD tenant, you should be able to address the error code AADSTS81007 (DesktopSsoTenantIsNotOptIn) related to Seamless SSO. If the issue persists, consider reaching out to Microsoft support for further assistance.