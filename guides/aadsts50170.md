# AADSTS50170: MissingExternalClaimsProviderMapping - The external controls mapping is missing.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS50170: "MissingExternalClaimsProviderMapping"

The error code AADSTS50170 indicates that there is a mapping issue with external claims providers in Azure Active Directory (Azure AD). This usually occurs when there is a problem with the configuration of identity providers or the claims mapping used in your authentication flow.

#### Initial Diagnostic Steps

1. **Understand Context**: Determine the scenario in which the error occurs. Is it happening during sign-in for users from an external identity provider or during some specific integration?

2. **Verify User Information**: Gather details about the user encountering the error. Specifically, check if they are associated with an external identity provider that your application supports.

3. **Check Azure AD Configuration**: Log in to the Azure portal and review the configuration of the Azure AD tenant to ensure that external claims providers are correctly set up.

4. **Review Recent Changes**: Look for any recent updates or changes made to the Azure AD configuration that may have impacted external identity provider setups.

#### Common Issues that Cause this Error

1. **Missing or Incorrect Claims Mapping**: The most common cause is that the necessary claims mapping for the external identity providers is either missing or incorrectly configured in the Azure AD application manifest.

2. **Misconfiguration of Identity Providers**: Issues with how an external identity provider (like Google, Facebook, etc.) is set up can lead to this error if claims aren’t correctly defined.

3. **Policy or Rule Changes**: Changes to Azure AD policies or application-specific authorization rules can impact how claims are processed.

4. **Missing Middleware/Integration Components**: If you are using middlewares, such as OpenID Connect or OAuth, make sure they are correctly set up to handle claims.

#### Step-by-Step Resolution Strategies

1. **Verify External Identity Provider Configuration**:
   - Go to **Azure Active Directory > External Identities > External Identities settings**.
   - Ensure that all external identity providers are correctly configured.

2. **Check Claims Mapping in Azure AD**:
   - Open the Azure portal and navigate to **Azure Active Directory > App registrations**.
   - Select the app registration that experiences the error.
   - Navigate to the **Token configuration** tab and review the claims mapping. Ensure that the necessary claims are present and correctly defined.

3. **Update Application Manifest**:
   - In the application registration, click on **Manifest**.
   - Look for the `"externalIdentities"` section, or any claim mapping definition. Ensure that a mapping for the external claims provider is correctly defined and matches the expected format.

4. **Test with Different Users**:
   - Attempt signing in with users from different external identity providers to isolate the issue. Check if only specific providers are causing problems.

5. **Review Registered Applications**:
   - Confirm that other applications utilizing the same identity providers are functioning correctly. If they are not, the issue might be systemic.

6. **Check Documentation**: Refer to Microsoft's official documentation for setting up and troubleshooting external identity providers:
   - [Azure AD B2C - External Identity Providers](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-identityproviders)
   - [Azure AD - Claims Mapping](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-claims-mapping)

#### Additional Notes or Considerations

- Ensure that all applications that consume Azure AD tokens are correctly expecting the claims being passed and handling them appropriately.

- If the application uses custom claims transformations or logic, ensure those haven't changed or are still aligned with expected outcomes.

- For enterprise applications, it may be necessary to work with your Azure AD admin to get detailed logs and diagnostics.

#### Documentation for Guidance

- [Azure Active Directory documentation](https://docs.microsoft.com/en-us/azure/active-directory/)
- [Azure Active Directory B2C documentation](https://docs.microsoft.com/en-us/azure/active-directory-b2c/)
- [Claims mapping guide](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-claims-mapping)

#### Advice for Data Collection and Diagnostics

- **Event Viewer Logs**: Review logs on the server hosting the application for any related authentication errors. Look specifically for logs related to Azure AD or federated authentication.

- **Network Traces**: Use **NetTrace** and **Fiddler** to capture traffic to and from Azure endpoints during the sign-in process. Look for any unusual HTTP response codes or error messages.

- **Azure AD Sign-In Logs**: Use the Azure portal to access **Azure Active Directory > Sign-ins** to check for specific entries related to the failed authentication. This will provide details on what claims were present during the authentication attempt.

By following these steps, you should be able to troubleshoot and resolve the AADSTS50170 error and ensure proper integration with external claims providers.