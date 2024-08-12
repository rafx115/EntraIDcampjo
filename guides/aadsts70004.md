
# AADSTS70004: InvalidRedirectUri - The app returned an invalid redirect URI. The redirect address specified by the client does not match any configured addresses or any addresses on the OIDC approve list.


## Troubleshooting Steps
Certainly! The error code **AADSTS70004** indicates that there is an issue with the redirect URI configured in Azure Active Directory (AAD) during the authentication process. Here’s a detailed troubleshooting guide to help diagnose and resolve the issue.

### Troubleshooting Guide for AADSTS70004 Error

#### Initial Diagnostic Steps:
1. **Identify the Application**: Determine which application is generating this error.
2. **Check the Redirect URI**: Inspect the redirect URI that your application is using in the authentication flow.
3. **Verify the Error Message**: Confirm the exact message associated with the error to ensure you are dealing with **AADSTS70004**.

#### Common Issues That Cause This Error:
1. **URI Mismatch**: The redirect URI provided during authentication does not match any of the URIs configured in Azure AD.
2. **Unregistered URI**: The redirect URI is not registered in the application registration in Azure AD.
3. **Trailing Slashes**: A trailing slash issue can cause URI mismatches, i.e., `https://example.com/callback/` vs. `https://example.com/callback`.
4. **HTTP vs. HTTPS**: If the application is using HTTP instead of HTTPS, it will be considered an invalid redirect URI.
5. **Port Number Issue**: Including a port number that isn't configured in AAD can lead to mismatches.

#### Step-by-Step Resolution Strategies:
1. **Check Application Registration**:
   - Go to the Azure portal.
   - Navigate to **Azure Active Directory** > **App registrations** > [Your App].
   - Select **Authentication** and verify the **Redirect URIs** listed here.

2. **Verify the Redirect URI Being Used**:
   - In your application code (often found in your authentication configuration), find the redirect URI you are requesting and ensure it is exactly as it is listed in Azure AD.

3. **Confirm Application Type**:
   - Ensure the correct application type is set (Web, Native, etc.) in the app registration. The redirect URI must correspond with the application type.

4. **Adjust URI for Exact Matches**:
   - Make sure that the URI matches exactly in terms of:
     - Schema (http/https)
     - Port (if applicable)
     - Path (exact path, including trailing slashes)

5. **Add Missing Redirect URIs**:
   - If the correct redirect URI is not present in the Azure AD app registration, add it in the **Redirect URIs** section.

6. **Test with Known Good URIs**:
   - If you're still having issues, try using a simple known good redirect URI that you have tested before.

#### Additional Notes or Considerations:
- Ensure that all environments (development, staging, production) have their redirect URIs properly registered in Azure AD.
- Be aware of single-page applications (SPAs) or mobile apps that may have specific redirect URI requirements.

#### Documentation for Guidance:
- Azure Active Directory App Registration: [Microsoft Docs - Register an app with the Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)
- Redirect URIs Overview: [Microsoft Docs - Authentication with Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/develop/authentication-scenarios)

#### Data Collection for Advanced Troubleshooting:
- Use **Event Viewer Logs**:
  - Check for any warnings or errors relevant to the application under Windows Logs > Application if on a Windows Server.
  
- **Network Tracing Tools**:
   - Use **Fiddler** or **Wireshark** to capture network traffic and see the exact redirect URI being called.
   - Check the returned error response from AAD.

- **Browser Developer Tools**:
   - Use Chrome Developer Tools or the equivalent in your browser to inspect requests and ensure that the correct redirect URI is being posted.

Collecting this data will be helpful in diagnosing complex issues or confirming that the redirect URI is indeed being advertised correctly. Always ensure to handle sensitive data according to your organization's security policies when performing diagnostic activities.