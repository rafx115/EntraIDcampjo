# AADSTS50079: UserStrongAuthEnrollmentRequired - Due to a configuration change made by the admin such as a Conditional Access policy, per-user enforcement, or because the user moved to a new location, the user is required to use multifactor authentication. Either a managed user needs to register security info to complete multifactor authentication, or a federated user needs to get the multifactor claim from the federated identity provider.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS50079

#### Error Description:
UserStrongAuthEnrollmentRequired - Due to a configuration change made by the admin such as a Conditional Access policy, per-user enforcement, or because the user moved to a new location, the user is required to use multifactor authentication. Either a managed user needs to register security info to complete multifactor authentication, or a federated user needs to get the multifactor claim from the federated identity provider.

#### Initial Diagnostic Steps:
1. **Confirm the Error**: Verify that the error code is indeed AADSTS50079, as described.
2. **Check User Details**: Identify if the user is a managed user or a federated user.
3. **Review Recent Changes**: Determine if any recent configuration changes or Conditional Access policies were implemented by the admin.

#### Common Issues:
1. **Unregistered Security Information**: Managed users may not have completed multifactor authentication enrollment.
2. **Federated Claim Missing**: Federated users may not be receiving the multifactor claim from the identity provider.

#### Step-by-Step Resolution Strategies:
1. **Managed User - Security Info Registration**:
   
   - Instruct managed users to log in to their account.
   - Prompt them to navigate to the security settings to register security information for multifactor authentication.
   - Once registered, the user should attempt to log in again.

2. **Federated User - Multifactor Claim**:

   - For federated users, contact the federated identity provider to ensure that the multifactor claim is being provided.
   - Confirm that the federated identity provider is correctly configured to issue the multifactor claim.
   - Advise the user to log in after confirming that the multifactor claim is being provided.

#### Additional Notes or Considerations:
- **User Communication**: Clear communication with the affected user is crucial to guide them through the resolution steps.
- **Admin Involvement**: Admin intervention may be necessary to adjust Conditional Access policies or settings as needed.

#### Documentation:
For detailed guidance on troubleshooting AADSTS50079 errors and configuring multifactor authentication in Azure Active Directory, refer to Microsoft's official documentation:
- [Azure Active Directory - Troubleshooting errors related to conditional access](https://docs.microsoft.com/en-us/azure/active-directory/conditional-access/plan-conditional-access-troubleshoot)
- [Azure Active Directory - Configure multifactor authentication settings](https://docs.microsoft.com/en-us/azure/active-directory/authentication/howto-mfa-mfasettings)

#### Note:
Always ensure that any changes made to authentication settings comply with security best practices and organizational policies. If the issue persists despite following the steps above, consider consulting with Azure Active Directory support for further assistance.