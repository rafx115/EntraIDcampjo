# AADSTS81005: DesktopSsoAuthenticationPackageNotSupported - The authentication package isn't supported.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS81005: DesktopSsoAuthenticationPackageNotSupported

**Error Code:** AADSTS81005  
**Description:** DesktopSsoAuthenticationPackageNotSupported - The authentication package isn't supported.  

#### Initial Diagnostic Steps

1. **Check the Error Context:** 
   - Note the circumstances under which the error occurred. Was it during login? Was a specific application involved?

2. **Verify Date and Time Settings:**
   - Ensure that the device’s date and time settings are correct. Incorrect settings can cause authentication issues.

3. **Network Connectivity Check:**
   - Confirm that the device has a stable internet connection. Restart the router if necessary.

4. **Review User Account Details:**
   - Ensure the user attempting to authenticate is part of an Azure AD tenant and has the correct permissions.

5. **Determine the Authenticator:**
   - Identify whether the error occurred with Windows, macOS, or a specific application/service.

#### Common Issues Causing This Error

1. **Outdated system packages:**
   - The authentication methods may become outdated and unsupported if the OS or relevant applications aren't updated.

2. **Mismatched authentication methods:**
   - The device may be configured to use an authentication method that is not supported.

3. **Local Group Policy Restrictions:**
   - Group Policy settings may restrict the use of certain authentication packages.

4. **Unsupported Configuration:**
   - Unsupported Windows or Azure AD configurations can lead to this error.

5. **Interference from security software:**
   - Antivirus or firewall settings may block authentication processes or required packages.

#### Step-by-Step Resolution Strategies

1. **Update Your System:**
   - Ensure that the operating system is fully updated. This includes both system updates and application updates.

   **Windows:**
   - Go to **Settings** > **Update & Security** > **Windows Update** and check for updates.

   **macOS:**
   - Go to the **Apple menu** > **System Preferences** > **Software Update**.

2. **Check Group Policy Settings:**
   - For systems part of a domain, the Group Policy might restrict the authentication method.
   - Access the Group Policy Editor: `gpedit.msc`, and navigate to **Computer Configuration** > **Windows Settings** > **Security Settings** > **Local Policies** > **Security Options**. Check settings related to authentication.

3. **Review and Modify Authentication Methods in Azure AD:**
   - Log in to Azure portal, navigate to **Azure Active Directory** > **Security** > **Authentication methods**. Check if the methods set are compatible with your clients.

4. **Check Security Software Configuration:**
   - Temporarily disable any third-party antivirus or firewall on the client. Test authentication again.

5. **Consider Device Registration/Join:**
   - Ensure that the device is correctly registered or joined to Azure AD. Misconfigurations here can cause issues.

6. **Verify Local Authentication Methods:**
   - Ensure that the appropriate authentication packages (like NTLM, Kerberos) are installed and configured correctly as per your organization's needs.

#### Additional Notes or Considerations

- If testing in a non-production environment, always ensure proper backups are in place.
- Some legacy systems or outdated software may not fully support current authentication methods and could require an upgrade or replacement.

#### Documentation for Guidance

- [Azure Active Directory Documentation](https://docs.microsoft.com/en-us/azure/active-directory/)
- [Managing Authentication Methods in Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/authentication/authentication-methods)
- [Troubleshooting Azure AD Errors](https://docs.microsoft.com/en-us/azure/active-directory/develop/troubleshoot-authentication)

#### Test Document Accessibility

- The above documentation links can be verified for accessibility by navigating to the URLs in a web browser.

#### Advice for Data Collection

1. **Document Error Details:**
   - Take screenshots of error messages, timestamps, and any relevant logs.

2. **Collect System Logs:**
   - Gather Windows Event logs related to authentication (`Event Viewer > Windows Logs > Application/Security`).
   - Use Azure AD logs within the Azure portal for any corresponding entries.

3. **User Feedback:**
   - Collect input from the user encountering the error regarding the steps attempted and any changes made prior to the issue arising.

4. **Network Logs:**
   - If possible, collect network logs to identify any potential blocks or issues in the authentication flow.

By following this guide, you should be able to diagnose and resolve the AADSTS81005 error effectively. If the issue persists after trying the above steps, it may be worthwhile to reach out to Microsoft Support for further assistance.