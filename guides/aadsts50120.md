
# AADSTS50120: ThresholdJwtInvalidJwtFormat - Issue with JWT header. Contact the tenant admin.


## Troubleshooting Steps
**Error Code: AADSTS50120 ThresholdJwtInvalidJwtFormat**

### Initial Diagnostic Steps:

1. **Check Tenant Configuration**: Ensure that the Azure Active Directory (AAD) tenant settings are configured correctly by the tenant admin.

2. **Verify JWT Format**: Validate the JWT (JSON Web Token) header format to identify any discrepancies or errors.

3. **Review Application Configuration**: Confirm that the application settings, permissions, and configurations are aligned with the AAD requirements.

### Common Issues causing this error:

1. **Invalid JWT Header**: The JWT header may have incorrect or missing information causing the issue.

2. **Misconfigured Application Settings**: Application settings related to tokens, authentication methods, or permissions may be set incorrectly.

3. **Tenant Admin Permissions**: Insufficient permissions for the tenant admin to validate or manage JWT configurations.

### Step-by-Step Resolution Strategies:

1. **Review JWT Header**: Check the JWT header for correct format, including the algorithm, type, and other necessary attributes.

2. **Update Application Settings**: Ensure that the application settings, such as token configurations, match the requirements set by the AAD.

3. **Contact Tenant Admin**: Reach out to the tenant admin or support team to address the JWT header issue and seek guidance on resolving it.

4. **Upgrade Library or SDK**: If using a library or SDK for handling JWT, update it to the latest version to potentially resolve any compatibility issues.

### Additional Notes or Considerations:

- **Logs and Error Details**: Collect detailed logs and error messages to provide insights into the specific cause of the JWT header issue.

- **Testing across Environments**: Verify the application behavior across different environments to ascertain if the issue is environment-specific.

- **Audit Trail**: Maintain a record of changes made to configurations and settings for future reference and troubleshooting.

### Documentation for Guidance:

- **Microsoft Documentation**: Visit the [Microsoft Azure AD Error Codes](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-error-codes) documentation for detailed insights on common error codes and resolution steps.

Following these troubleshooting steps should help in resolving the AADSTS50120 error related to JWT header issues. If the problem persists, consulting with the Azure AD support team or community forums can provide further assistance.