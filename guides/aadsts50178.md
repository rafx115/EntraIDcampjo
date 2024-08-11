
# AADSTS50178: SessionControlNotSupportedForPassthroughUsers - Session control isn't supported for passthrough users.


## Troubleshooting Steps
### Error Code: AADSTS50178
#### Description: SessionControlNotSupportedForPassthroughUsers - Session control isn't supported for passthrough users.

### Troubleshooting Guide:

#### Initial Diagnostic Steps:
1. Verify the user authentication process being used (e.g., Azure AD Passthrough Authentication).
2. Check the configuration settings related to session control in Azure AD.

#### Common Issues:
1. User is configured as a passthrough user in Azure AD.
2. Session control settings are misconfigured in Azure AD.

#### Step-by-Step Resolution Strategies:
1. Ensure that the user experiencing the issue is not configured as a passthrough user in Azure AD.
2. Check the session control settings in Azure AD and verify if they are appropriately configured for the user experiencing the error.
3. If the user needs to maintain the passthrough authentication, consider adjusting the session control settings accordingly.

#### Additional Notes or Considerations:
- Passthrough users do not support session control settings in Azure AD, which may lead to this error.
- Ensure proper communication with users about limitations and functionalities related to passthrough authentication in Azure AD.

#### Documentation:
- Microsoft Azure official documentation provides detailed guidance on Azure AD error codes and troubleshooting steps. Refer to the following link for more information: [Azure AD Error Codes](https://docs.microsoft.com/en-us/azure/active-directory/develop/reference-aadsts-error-codes)

If you encounter any issues while following the troubleshooting steps or have specific scenarios, feel free to provide more details for tailored assistance.