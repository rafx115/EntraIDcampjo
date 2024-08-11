
# AADSTS90114: InvalidExpiryDate - The bulk token expiration timestamp will cause an expired token to be issued.


## Troubleshooting Steps
Error code AADSTS90114 with the description "InvalidExpiryDate" indicates that the expiration timestamp for bulk token issuance is incorrect, which will result in issuing an expired token. To troubleshoot this issue, follow the detailed guide below:

### Initial Diagnostic Steps:
1. **Verify the Error Message**: Ensure that the error code received is indeed AADSTS90114 with the description "InvalidExpiryDate."
2. **Check the Token Expiry Configuration**: Review the configuration settings related to token expiration timestamps in the system or application.

### Common Issues:
- Incorrectly set or expired token expiration timestamps.
- Timezone discrepancies causing expiration timestamp errors.
- Issues with the refresh token setup.
- Backend system errors or limitations.

### Step-by-step Resolution Strategies:

1. **Check Token Expiry Settings**:
    - Review the token expiration settings in the Azure Active Directory (AAD) portal or the identity provider being used.
    - Ensure that the token expiry durations are correctly configured.
    - Adjust the expiration timestamps if necessary.

2. **Verify Timezone Configuration**:
    - Check the timezone settings on the server or system generating the tokens.
    - Make sure that the time configuration is accurate and aligned with the timezone settings in Azure AD.

3. **Refresh Token Handling**:
    - Ensure that refresh tokens are being managed properly.
    - Check for any issues related to refreshing expired tokens.

4. **Backend System Review**:
    - Investigate any potential errors or limitations within the backend system generating the tokens.
    - Address any issues that may be affecting token issuance.

### Additional Notes or Considerations:
- Keep track of any recent changes made to the token generation settings.
- Verify that the system clocks are synchronized and accurate across all relevant services.
- Review any recent updates or patches applied to the system that may have impacted token generation.

### Documentation:
- Microsoft Azure Active Directory documentation provides detailed steps for managing token lifetimes and expiration. You can refer to the official documentation for guidance:
  [Azure AD Token Lifetime Configuration](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-configurable-token-lifetimes)

By following these troubleshooting steps and considering the common issues, you should be able to identify and resolve the error code AADSTS90114 related to an InvalidExpiryDate effectively. If the issue persists after troubleshooting, consider reaching out to Azure AD support for further assistance.