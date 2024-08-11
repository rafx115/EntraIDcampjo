# AADSTS20012: WsFedMessageInvalid - There's an issue with your federated Identity Provider. Contact your IDP to resolve this issue.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS20012: WsFedMessageInvalid

When encountering the AADSTS20012 error with the description "WsFedMessageInvalid - There's an issue with your federated Identity Provider," it indicates a problem with the Identity Provider (IDP) configuration. Below is a detailed troubleshooting guide to resolve this issue:

#### Initial Diagnostic Steps:
1. **Review Error Message:** Carefully read the error message to identify the exact issue related to the federated Identity Provider.
2. **Check IDP Configuration:** Verify the settings and configurations of your IDP to ensure they are correctly configured.
3. **Review Recent Changes:** Determine if any recent changes were made to the IDP configuration or settings before the error started occurring.

#### Common Issues Causing the Error:
1. **Incorrect IDP Configuration:** Misconfigured settings or parameters on the Identity Provider's side can lead to this error.
2. **Expired Certificates:** Check if the certificates used for the IDP have expired or have become invalid.
3. **Mismatched Keys:** Ensure that the cryptographic keys used by the IDP and the relying party services match.
4. **IDP Server Unavailability:** The IDP server may be experiencing downtime or connectivity issues.

#### Step-by-Step Resolution Strategies:
1. **Check IDP Configurations:** Validate the settings on the IDP side to ensure they match the required configurations.
2. **Renew Certificates:** If certificates have expired, renew them and update them in the IDP configuration.
3. **Verify Key Matching:** Ensure that the keys and cryptographic algorithms used by both the IDP and relying party match.
4. **Monitor IDP Server Availability:** Ensure that the IDP server is up and running without any connectivity issues.

#### Additional Notes or Considerations:
- **Logs Analysis:** Check the logs on both the IDP and relying party sides for more detailed error information.
- **Collaboration:** Collaborate with your IDP support team to identify and resolve the issue efficiently.
- **Testing Environment:** Use a testing environment to validate changes before applying them to production.

#### Documentation for Guidance:
- **Microsoft Docs - Troubleshoot single sign-on (SSO) issues:** [Microsoft Docs](https://docs.microsoft.com/en-us/azure/active-directory/hybrid/tshoot-connect-federated-single-sign-on) provides comprehensive information on troubleshooting SSO issues, including error code AADSTS20012.

By following these steps and guidelines, you should be able to diagnose and resolve the AADSTS20012 error related to the federated Identity Provider effectively. If the issue persists, consider reaching out to your IDP support team for further assistance.