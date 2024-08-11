# AADSTS90123: IdentityProviderAccessDenied - The token can't be issued because the identity or claim issuance provider denied the request.


## Troubleshooting Steps
## Troubleshooting Guide for Error Code AADSTS90123

### Overview
The error code AADSTS90123 indicates that the request for a token cannot be fulfilled due to denial from the identity or claim issuance provider. This error is often encountered in scenarios involving Azure Active Directory (AAD) and may occur during authentication processes.

### Initial Diagnostic Steps

1. **Check the Error Message**: Read the complete error message carefully. It often provides context that can direct your troubleshooting efforts.
   
2. **Verify User Identity**:
   - Validate that the user account attempting to authenticate is active and not disabled/deleted.
   - Ensure that the user belongs to the correct Azure AD tenant.

3. **Identify Authentication Method**: Determine if the user is trying to authenticate through a third-party identity provider (e.g., Google, Facebook) or an Azure AD B2C interaction.

4. **Review Logs**: If you have logging enabled:
   - Go to the Azure portal and check sign-in logs under Azure Active Directory > Sign-ins.
   - Look for failed sign-in attempts that correlate with the time of the error and examine the details.

### Common Issues That Cause This Error

1. **Denied Permissions**: The user may not have necessary permissions or roles assigned to perform the requested operation.

2. **Conditional Access Policies**: Azure AD Conditional Access policies may be denying access based on user conditions (e.g., location, device compliance).

3. **Multi-Factor Authentication Requirement**: The authentication method requested may require multi-factor authentication that is not being satisfied.

4. **Identity Provider Configuration**: Issues with the configuration of the identity provider may lead to denial of token issuance.

5. **Claim Modifications**: The requested claims for token issuance may not conform to the requirements set by the identity provider.

### Step-by-Step Resolution Strategies

1. **Check User Permissions**:
   - Go to Azure Active Directory > Users > [Select User].
   - Review roles and group memberships.
   - Assign necessary roles if needed.

2. **Review Conditional Access Policies**:
   - Go to Azure Active Directory > Security > Conditional Access.
   - Identify any policies that might block the user based on device, location, or user state.
   - Adjust or exclude the user to allow access, if applicable.

3. **Review Multi-Factor Authentication Settings**:
   - Go to Azure Active Directory > Security > Multi-Factor Authentication.
   - Ensure the user is enrolled and the MFA requirements are met.

4. **Inspect Identity Provider Settings**:
   - If using a third-party identity provider, review its configurations.
   - Ensure the integrations and redirect URIs are properly set.

5. **Claims Issuance Rules**:
   - Go to Azure Active Directory > App Registrations > [Select Application].
   - Review and modify claim issuance rules if needed. Ensure the claims being requested by your application are valid and allowed by the identity provider settings.

6. **Use Azure AD Graph/ Microsoft Graph API**:
   - Use APIs to automate reviews of the configuration and status of users and policies, especially for systems with many users or complex policies.

### Additional Notes or Considerations

- **Self-Service Restoration**: Encourage users to initiate a password reset or self-service actions where applicable, as this might resolve access issues linked to credential problems.
- **Testing in Non-Production**: Always test changes in a non-production environment first if possible to avoid unexpected outages.
- **Documentation**: Familiarize yourself with Azure’s documentation on identity management. This can provide a foundation for understanding additional authentication flows.

### Documentation for Guidance

- **Azure Active Directory**: [Learn about Azure Active Directory](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-overview)
- **Conditional Access**: [Conditional Access in Azure AD](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/overview)
- **Multi-Factor Authentication**: [What is Azure AD Multi-Factor Authentication?](https://learn.microsoft.com/en-us/azure/active-directory/authentication/concept-mfa-howitworks)
- **Claims-based Authentication**: [What is Claims-based Identity?](https://learn.microsoft.com/en-us/azure/active-directory/develop/claims-based-authentication)

### Test the Documentation Reachability

To ensure that the documentation links are reachable, simply navigate to each URL in a web browser. Confirm the pages load without errors. 

### Advice for Data Collection

- **Gather Logs**: Collect logs from Azure Active Directory regarding sign-in attempts. Export these logs if necessary for deeper analysis.
- **User Session Information**: Gather details on the user session, including the timestamp, IP address, and device information.
- **Configuration Settings**: Document the configurations for user roles, groups, conditional access policies, and identity providers.

By following this structured troubleshooting guide, you can proactively address and resolve the AADSTS90123 error, providing smoother authentication experiences for users in your Azure environment.