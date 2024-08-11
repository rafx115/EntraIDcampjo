
# AADSTS70007: UnsupportedResponseMode - The app returned an unsupported value ofresponse_modewhen requesting a token.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS70007 - UnsupportedResponseMode

#### Initial Diagnostic Steps:
1. **Confirm the Error Code**: Ensure that the error code being encountered is indeed AADSTS70007, which corresponds to the UnsupportedResponseMode error.
2. **Check Application Configuration**: Verify the configuration settings of the application that is requesting the token.

#### Common Issues Causing This Error:
1. **Incorrect Response Mode**: The application is using an unsupported response mode when requesting a token.
2. **Misconfigured Application**: The application settings in Azure Active Directory (AAD) may be misconfigured, leading to the error.

#### Step-by-Step Resolution Strategies:
1. **Review Application Code**:
   - Check the code of the application to ensure that the correct response mode is being used.
   - If the response mode is set programmatically, modify it to use a supported response mode (e.g., query, form_post).

2. **Check Application Settings in Azure AD**:
   - Access the Azure portal and navigate to the Azure Active Directory.
   - Locate and select the application causing the error.
   - Review the application settings, especially related to authentication and token requests.
   - Update the response mode setting to a supported value.

3. **Test and Validate**:
   - After making changes, test the application to verify that the error has been resolved.
   - Verify that the application can now successfully request a token without encountering the UnsupportedResponseMode error.

#### Additional Notes or Considerations:
- **Documentation**: Detailed documentation and guidance on configuring applications in Azure Active Directory can be found in the [Microsoft Azure Docs](https://docs.microsoft.com/en-us/azure/active-directory/).

- **Support Resources**: If further assistance is needed, consider reaching out to Microsoft Azure support or consulting Azure Active Directory forums for additional help.

By following these troubleshooting steps and addressing the common issues associated with the AADSTS70007 error (UnsupportedResponseMode), you should be able to resolve the problem and ensure that the application can successfully request tokens from Azure Active Directory.