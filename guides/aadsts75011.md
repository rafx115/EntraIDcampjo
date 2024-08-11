# AADSTS75011: NoMatchedAuthnContextInOutputClaims - The authentication method by which the user authenticated with the service doesn't match requested authentication method. To learn more, see the troubleshooting article for errorAADSTS75011.


## Troubleshooting Steps
Below is a detailed troubleshooting guide for the error code AADSTS75011, specifically for the NoMatchedAuthnContextInOutputClaims scenario:

### Initial Diagnostic Steps:
1. **Verify User Authentication Method:** Confirm how the user authenticated with the service. Check if the method aligns with the requested authentication method.
   
2. **Review Application Configuration:** Examine the Azure AD application configuration and settings related to authentication methods.

### Common Issues:
1. **Mismatched Authentication Methods:** This error typically occurs when the user authentication method doesn't match the one requested by the application.

### Step-by-Step Resolution Strategies:
1. **Ensure Consistency in Authentication Methods:**
   - Cross-validate the authentication method used by the user with the one configured in the Azure AD application.
   - Update the application configuration to align with the authentication method the user is using.

2. **Check Claims Issuance Rules:**
   - Review the claims issuance rules for the Azure AD application to ensure that the correct authentication method claims are being provided.

3. **Verify Application Manifest:**
   - Check the application manifest in Azure AD to confirm that the correct authentication methods are specified.

4. **User Re-Authentication:**
   - Request the user to re-authenticate using the appropriate authentication method.

5. **Investigate Conditional Access Policies:**
   - Review any Conditional Access Policies that may be affecting the authentication flow.

### Additional Notes or Considerations:
- It's important to communicate with the user about the authentication method they used and any potential issues they faced during the authentication process.
- Periodic review and updates of application configurations in Azure AD can help prevent authentication-related errors.

### Documentation for Guidance:
- Microsoft Azure AD documentation offers detailed information on troubleshooting various error codes, including AADSTS75011. Refer to this [Troubleshooting guide for error AADSTS75011](https://docs.microsoft.com/en-us/azure/active-directory/develop/troubleshoot-errors-no-matched-authn-context#in-output-claims) for more specific guidance on resolving this error.

By following these steps and guidelines, you should be able to diagnose and resolve the AADSTS75011 error with the NoMatchedAuthnContextInOutputClaims message effectively. If further assistance is needed, consider reaching out to Azure AD support for personalized help.