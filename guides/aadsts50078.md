
# AADSTS50078: UserStrongAuthExpired- Presented multifactor authentication has expired due to policies configured by your administrator. You must refresh your multifactor authentication to access '{resource}'.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS50078

#### Initial Diagnostic Steps:
1. **Confirm the Error Message**: Double-check the error message and ensure it matches the description provided.
2. **Verify Resource Access**: Note the resource mentioned in the error message that requires refreshed multifactor authentication.

#### Common Issues:
1. **Expired Multifactor Authentication:** The issue arises when the multifactor authentication has expired due to policies configured by the administrator.
2. **Policy Restrictions**: Administrator-defined policies might prevent access until multifactor authentication is refreshed.

#### Resolution Strategies:
1. **Navigate to Multi-Factor Authentication Portal**:
    - Visit the Multi-Factor Authentication portal for your organization.
    - Authenticate using your credentials.

2. **Refresh Multifactor Authentication**:
    - Follow the prompts to refresh your multifactor authentication.
    - Complete the MFA process as per the organization's policies.

3. **Retry Access**:
    - Once the multifactor authentication has been successfully refreshed, attempt to access the '{resource}' again.

#### Additional Notes or Considerations:
- **Contact Administrator**: If you face difficulties during the multifactor authentication process, reach out to your administrator for assistance.
- **Policy Compliance**: Ensure you comply with the organization's security policies while refreshing the multifactor authentication.

#### Documentation for Guidance:
- For detailed steps on how to refresh your multifactor authentication, refer to the official Microsoft documentation on [Azure Active Directory error codes](https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-logs#troubleshoot-aad-error-codes).

By following these steps and considerations, you should be able to resolve the AADSTS50078 error related to expired multifactor authentication efficiently. If you encounter any issues or need further assistance, don't hesitate to contact your organization's IT support team.