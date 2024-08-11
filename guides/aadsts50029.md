
# AADSTS50029: Invalid URI - domain name contains invalid characters. Contact the tenant admin.


## Troubleshooting Steps
## Troubleshooting Guide for AADSTS50029: Invalid URI - Domain Name Contains Invalid Characters

### Overview
The AADSTS50029 error occurs when there are invalid characters in the URI (Uniform Resource Identifier) that a user is trying to access, particularly when it involves Azure Active Directory (AAD) authentication. This can happen in scenarios involving Single Sign-On (SSO) or when applications or resources are configured incorrectly.

### Initial Diagnostic Steps
1. **Check the Error Message**: Note the exact wording of the error message, as it may provide hints about the invalid characters or misconfigured settings.
   
2. **Identify the URI**: Determine which URI triggered the error. This might be a redirect URI or the application’s resource identifier.

3. **Environment Context**: Identify if the error occurs in a specific environment (e.g., production vs. development) or for specific users.

4. **User Context**: Understand if the issue is affecting all users or just specific ones.

### Common Issues that Cause this Error
- **Invalid Characters**: The most common cause is the presence of symbols or characters in the domain name which are not allowed (e.g., spaces, special characters).
- **Misconfigured Redirect URIs**: If the redirect URI registered in the Azure portal does not match the one being requested.
- **Tenant-Specific Restrictions**: The Azure tenant may have specific restrictions on domain names or configurations.
- **Typo in the Domain**: Simple typographical errors such as incorrect casing or misplaced characters.

### Step-by-step Resolution Strategies
1. **Validate the Domain Name**:
   - Check the domain name for any invalid characters.
   - Ensure that the domain name adheres to standard domain naming conventions.

2. **Inspect the Redirect URIs**:
   - In the Azure portal, navigate to **Azure Active Directory** > **App registrations** > [Your Application].
   - Inspect the **Redirect URIs** section and ensure there are no invalid characters.
   - If the URI is incorrect, update it to use a valid format.

3. **Update Application Configuration**:
   - If the application uses code to define URIs, ensure the code is properly sanitizing and validating the URIs before sending them to Azure AD.

4. **Check Azure Portal Settings**:
   - Navigate to **Azure Active Directory** > **User settings** and ensure that the organizational settings do not impose restrictions that could affect domain names.

5. **Test the Validity of Updated URIs**:
   - Use a browser or Postman to try the updated URIs and see if the error persists.

6. **Consult with Tenant Admin**:
   - If issues persist, contact the Azure tenant administrator to gather more context and additional restrictions that may be in place.

### Additional Notes or Considerations
- Ensure all users and developers working with the application are aware of the correct format for URIs.
- Keep documentation for URI conventions handy to prevent future errors.
- Review any recent changes to the application or Azure AD configurations, as they may have introduced the error.

### Documentation References
- **Azure Active Directory Documentation** - [Redirect URIs in Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/develop/reply-url)
- **Domain Naming Conventions** - [RFC 1035 - Domain Names](https://tools.ietf.org/html/rfc1035)

### Test Documentation Reachability
Ensure that the above documentation links are accessible from your browser:
- Open your web browser.
- Enter the URLs provided above and verify the pages load correctly.

### Advice for Data Collection
If these troubleshooting steps do not resolve the issue:
1. **Collect Error Details**: Take screenshots of the error and note any steps that reproduce it.
2. **Gather Configuration Details**: Document your application’s configuration, especially the redirect URIs and service settings in Azure AD.
3. **User Reports**: Compile feedback from users experiencing the issue about the context in which it occurs (e.g., specific applications or actions).

By following this troubleshooting guide, you should be able to resolve the AADSTS50029 error effectively. If further assistance is necessary, consider raising a support ticket with Microsoft.