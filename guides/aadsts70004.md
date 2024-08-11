# AADSTS70004: InvalidRedirectUri - The app returned an invalid redirect URI. The redirect address specified by the client does not match any configured addresses or any addresses on the OIDC approve list.


## Troubleshooting Steps
**Troubleshooting Guide for Error Code AADSTS70004 - InvalidRedirectUri:**

**Initial Diagnostic Steps:**
1. Verify the redirect URI in the application registration.
2. Check if the redirect URI being used in the application matches the one configured in the Azure Active Directory.
3. Confirm if the redirect URI is correctly formatted and includes the correct protocol (http:// or https://).

**Common Issues that Cause this Error:**
1. **Misconfigured Redirect URI:** The redirect URI specified by the client in their application does not match what is configured in the Azure Active Directory app registration.
2. **Protocol Mismatch:** Ensure that the protocol (http:// or https://) in the redirect URI is consistent between the application and Azure AD configuration.
3. **Dynamic Redirect URIs:** Some applications may dynamically generate redirect URIs, which may not match the configured ones.
4. **Unapproved Redirect URIs:** The redirect URI used by the client application must be explicitly approved in the Azure AD app registration configuration.

**Step-by-Step Resolution Strategies:**
1. **Check and Update Redirect URI:**
   - Navigate to the Azure Portal and locate the application registration for your app.
   - Update the Redirect URI in the Application Registration to match the one specified by the client.
   - Save the changes and test the application to see if the issue is resolved.

2. **Verify URI Protocol:**
   - Ensure that the protocol (http:// or https://) in the redirect URI matches on both the client application and Azure AD configuration.
   - Update the URI if there is a mismatch and test the application again.

3. **Request Approval for New Redirect URIs:**
   - If the client is using a new redirect URI that is not yet approved, add it to the list of Redirect URIs in the Azure AD app registration.
   - Once added, test the application to verify if the issue is resolved.

**Additional Notes or Considerations:**
- The Redirect URI is crucial for securely handling authentication flows. It must be correctly configured to ensure proper authentication and authorization.
- Make sure to communicate with the client or development team responsible for the application to gather accurate information about the Redirect URI being used.

**Documentation for Guidance:**
- You can find detailed steps and documentation on managing Redirect URIs in Azure Active Directory in the official Microsoft documentation:
  [Azure AD Redirect URIs](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-protocols-oauth-code#redirect-uri-redirection-endpoint)

Follow these steps diligently to resolve the AADSTS70004 error related to the InvalidRedirectUri, ensuring a successful authentication and authorization flow for your application.