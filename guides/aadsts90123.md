
# AADSTS90123: IdentityProviderAccessDenied - The token can't be issued because the identity or claim issuance provider denied the request.


## Troubleshooting Steps
### Troubleshooting Guide: Error Code AADSTS90123

#### Initial Diagnostic Steps:
1. **Verify User Credentials**: Ensure that the user attempting to access the resource is using the correct identity provider credentials.
2. **Check Token Issuance**: Confirm that the token issuance provider is properly set up and not blocking the request.
3. **Review Application Configuration**: Check the application settings to ensure they are correctly configured with the identity provider.

#### Common Issues:
- **Misconfigured Identity Provider**: The identity provider settings may not be properly configured, leading to access denial.
- **Claim Issuance Policy Misalignment**: Misalignment in claim issuance policies between identity provider and relying party application can cause the error.
- **Expired Tokens**: Tokens may have expired, causing the denial of access.

#### Step-by-step Resolution Strategies:
1. **Check Identity Provider Settings**:
   - Verify the identity provider configuration and ensure it allows token issuance to the application.
2. **Review Claim Issuance Policies**:
   - Compare claim issuance policies between the identity provider and application settings to ensure they match.
3. **Refresh Tokens**:
   - If tokens have expired, have the user re-authenticate to generate new tokens.
4. **Check Access Control Policies**:
   - Verify that access control policies are not restricting the user's access.
5. **Monitor Logs**:
   - Check logs for more specific error messages that can provide insight into the root cause.

#### Additional Notes or Considerations:
- **API Permissions**: Ensure the application has the necessary API permissions to access the resource.
- **Token Configuration**: Check if token configurations are correctly set up for seamless issuance.
- **Network Connectivity**: Confirm that there are no network issues preventing communication between the identity provider and the application.

#### Documentation:
For detailed guidance, refer to the Microsoft Azure documentation on troubleshooting authentication issues, specifically related to the error code AADSTS90123:
- [Microsoft Azure Active Directory Error Codes](https://docs.microsoft.com/en-us/azure/active-directory/develop/reference-aadsts-error-codes)

By following the outlined diagnostic steps and resolution strategies, you should be able to address the IdentityProviderAccessDenied error (AADSTS90123) effectively. If the issue persists, consider reaching out to your IT support team or identity provider for further assistance.