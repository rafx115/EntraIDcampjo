# AADSTS50168: ChromeBrowserSsoInterruptRequired - The client is capable of obtaining an SSO token through the Windows 10 Accounts extension, but the token was not found in the request or the supplied token was expired.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS50168 Error

The AADSTS50168 error indicates that there is an issue with obtaining a Single Sign-On (SSO) token. Below is a comprehensive troubleshooting guide that outlines steps to diagnose and resolve the issue, as well as additional considerations.

#### 1. Initial Diagnostic Steps

- **Check the User's Network Connectivity:**
  Ensure that the device has stable access to the internet and can reach the Azure Active Directory endpoints.
  
- **Verify User Credentials:**
  Confirm that the user is entering valid credentials and that their account is in good standing (not locked, expired, etc.).

- **Check Browser and OS Compatibility:**
  Ensure that the user is using a compatible version of Chrome and that Windows 10 is fully updated.

- **Review Session Requirements:**
  Make sure the user is attempting to access the resource while logged into their Azure AD account and that they haven't logged out or timed out.

#### 2. Common Issues that Cause this Error

- **Expired or Absent Token:**
  The SSO token may not be present or may have expired. This often occurs due to session timing issues.

- **Misconfigured Azure AD Settings:**
  The Azure AD configuration for applications may be incorrect, preventing the correct retrieval of the token.

- **Browser Configuration Issues:**
  Browser settings such as cookies being disabled or unauthorized HTTP requests can block the token from being obtained or validated.

- **Cache and Cookies Corruption:**
  Corrupted browser cache or cookies can cause conflicts in retrieving proper authentication tokens.

- **Environment Restrictions:**
  Group policy configurations or security settings in the organization can prevent access to Azure AD services.

#### 3. Step-by-Step Resolution Strategies

1. **Clear Browser Cache and Cookies:**
   - In Chrome, go to `Settings` → `Privacy and Security` → `Clear browsing data`.
   - Clear cookies and cached images/files.

2. **Check Windows 10 Accounts Settings:**
   - Open the **Settings** app on Windows.
   - Navigate to **Accounts** → **Access work or school**.
   - Ensure that the Azure AD account is connected properly. If not, disconnect and reconnect it.

3. **Token Expiry Check:**
   - Use Fiddler or a network trace to check if the token is being sent with the request from the browser.
   - If there is an expired token, guide the user to re-authenticate, thereby obtaining a new token.

4. **Configuration in Azure AD:**
   - Review the application's configuration in the Azure portal.
   - Ensure that the required permissions are granted and that the application is properly registered in Azure AD.

5. **Adjust Browser Settings:**
   - Ensure the browser settings allow cookies and third-party cookies.
   - Disable any extensions that may block scripts or tracking, such as ad blockers.

6. **Network Configuration Review:**
   - Investigate any firewall or proxy configurations that might block access to Azure AD.

7. **Reconfigure SSO Settings:**
   - If necessary, reconfigure SSO settings in both Azure AD and on the local machine to ensure compatibility.

8. **Site-Specific Issues:**
   - If the site has specific SSO requirements, check their documentation or support for any particular configurations required.

#### 4. Additional Notes or Considerations

- **Testing in Incognito Mode:**
  Sometimes, browser extensions can interfere with authentication. Testing the login process in Incognito mode can help determine if extensions are causing issues.

- **Different Browsers:**
  If possible, test the functionality in different browsers (Edge, Firefox) to determine if the issue is browser-specific.

- **User Support Requests:**
  If issues persist, gather detailed user reports and escalate them to the IT support team or Azure AD administrators.

#### 5. Documentation Where Steps Can Be Found for Guidance

- **Azure AD Documentation:**
  You can find detailed documentation on Azure Active Directory and troubleshooting here:
  - [Azure AD Authentication Issues](https://docs.microsoft.com/en-us/azure/active-directory/develop/authentication-scenarios)

- **Single Sign-On (SSO) Information:**
  - [Understanding EAS SSO](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-authentication-scenarios)

#### 6. Advice for Data Collection (Event Viewer Logs, NetTrace, Fiddler)

- **Event Viewer Logs:**
  - Check for errors related to authentication under **Windows Logs** → **Application** scripts for any authentication-related entries during the error time.
  
- **Network Traces:**
  - Use `NetTrace` with the Windows Performance Toolkit to capture network performance and issues related to token retrieval.

- **Fiddler Usage:**
  - Capture HTTP/HTTPS traffic by running Fiddler and analyzing requests to see if the authentication tokens are being sent correctly or if any error responses are returned.
  
By following these strategies, you should be able to isolate and resolve the issues related to the AADSTS50168 error and restore normal Single Sign-On functionality.