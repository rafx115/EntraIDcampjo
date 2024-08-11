# AADSTS75005: Saml2MessageInvalid - Microsoft Entra doesn�t support the SAML request sent by the app for SSO. To learn more, see the troubleshooting article for errorAADSTS75005.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS75005: Saml2MessageInvalid

#### Initial Diagnostic Steps:
1. Verify the error message received: **AADSTS75005 - Saml2MessageInvalid**
2. Determine the identity provider and the application involved in the SSO process.
3. Check if the SAML request is correctly formatted and compliant with Microsoft Entra's requirements.

#### Common Issues Causing the Error:
1. Incorrect SAML request structure or missing required attributes.
2. Mismatch in SAML protocol versions.
3. Invalid certificates or incorrect encryption methods.
4. Misconfigured or incompatible SAML settings between the identity provider and application.

#### Step-by-Step Resolution Strategies:
1. **Review SAML Request:**
    - Ensure the SAML request is correctly formatted and all required attributes are included.
    - Confirm that the SAML request is compliant with Microsoft Entra's SSO requirements.

2. **Check SAML Settings:**
    - Verify the SAML settings in both the identity provider and the application.
    - Ensure that the SAML protocol versions match and all configurations are accurate.

3. **Certificate Verification:**
    - Validate the certificates used for encryption and signing.
    - Make sure the certificates are correctly installed and updated.

4. **Update SAML Configuration:**
    - Adjust the SAML configuration settings based on the requirements of Microsoft Entra.
    - Ensure that the identity provider and the application are configured to support SAML properly.

5. **Test SSO Flow:**
    - Conduct a test SSO flow to check if the issue persists after the configuration changes.
    - Monitor the logs for any new error messages or warnings related to SAML interactions.

#### Additional Notes or Considerations:
- **Collaboration:** Coordinate with the IT team responsible for SSO configurations to troubleshoot and resolve the issue effectively.
- **Documentation:** Refer to the official Microsoft Entra documentation and SAML best practices for detailed guidance on configuring SAML settings.

#### Documentation for Guidance:
- Microsoft Entra Troubleshooting Article for **Error AADSTS75005**: [Link to Troubleshooting Article](https://docs.microsoft.com/en-us/troubleshoot/azure/active-directory/error-code-aadsts75005-saml2messageinvalid)

By following these steps and guidelines, you should be able to diagnose and resolve the **AADSTS75005 - Saml2MessageInvalid** error related to SSO with Microsoft Entra. If the issue persists, consider reaching out to Microsoft support for further assistance.