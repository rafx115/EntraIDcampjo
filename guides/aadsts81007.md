
# AADSTS81007: DesktopSsoTenantIsNotOptIn - The tenant isn't enabled for Seamless SSO.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS81007: DesktopSsoTenantIsNotOptIn

The error code AADSTS81007 indicates that a particular tenant is not enabled for Seamless Single Sign-On (Seamless SSO). This guide provides steps for diagnosing and resolving the error.

#### Initial Diagnostic Steps

1. **Verify Tenant Settings:**
   - Confirm that you are using the correct Azure Active Directory (AAD) tenant.
   - Check if Seamless SSO is indeed desired for your user experience.

2. **Check User Environment:**
   - Confirm that the user experiencing the error is attempting to access the correct application or resource.
   - Verify that the user is using a supported Windows version and browser for Seamless SSO.

3. **Review Logs:**
   - Use Azure AD sign-in logs to find additional context around the error. This can provide clues on what might be going wrong during the sign-in process.

#### Common Issues that Cause AADSTS81007

- **Seamless SSO Not Configured:**
  - The most common cause is that Seamless SSO has not been enabled for the tenant.
  
- **Incompatible Authentication Settings:**
  - If Kerberos or other authentication methods are misconfigured, this can prevent Seamless SSO from functioning.

- **Group Policies not Applied:**
  - A missing or misconfigured Group Policy that enables Seamless SSO can lead to authentication errors.

- **Network Configuration:**
  - Issues with DNS resolution or network connectivity that prevent access to necessary Azure AD endpoints.

#### Step-by-Step Resolution Strategies

1. **Enable Seamless SSO:**
   - Navigate to the **Azure portal**: [Azure Portal](https://portal.azure.com).
   - Go to **Azure Active Directory > Enterprise applications**.
   - Select the application you are having issues with.
   - Under **Single sign-on**, ensure that the Seamless SSO option is enabled. If not, enable it following the prompts.

2. **Validate Azure AD Connect Configuration:**
   - Open the Azure AD Connect tool on the server where it's installed.
   - Check if Seamless SSO is configured. If it is not, you can run through the configuration wizard to enable it:
     - Click on **Configure** and select **Configure device options**.
     - Select **Enable single sign-on** and follow the steps in the wizard.

3. **Check User Permissions and Group Policy:**
   - Ensure that users are assigned the necessary roles that allow them to use Seamless SSO in Azure AD.
   - Verify that Group Policies required for SSO are correctly applied to the user’s machine. This may involve checking:
     - Windows Group Policies (gpedit.msc).
     - Registry settings related to Azure AD.

4. **Test Network Connectivity:**
   - Ensure that the client machine can reach Azure AD endpoints. This may involve:
     - Pinging necessary Azure infrastructure.
     - Checking firewall rules that could be blocking access.

5. **Review Conditional Access Policies:**
   - Check if any Conditional Access policies are impeding the sign-in process. Adjust or disable policies temporarily to test.

#### Additional Notes or Considerations

- **User Training:** Users should be educated about the dual factor authentication process and how it interacts with Seamless SSO.
- **Multi-Factor Authentication (MFA):** If MFA is enforced, Seamless SSO may have certain limitations; verify configuration according to your organizational policy.
- **Browser Compatibility:** Ensure that users are utilizing supported browsers for the best experience with Seamless SSO.

#### Documentation for Guidance

- [Seamless SSO for Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/hybrid/how-to-connect-sso)
- [Troubleshoot Seamless SSO](https://docs.microsoft.com/en-us/azure/active-directory/hybrid/tshoot-sso)

#### Testing Documentation Accessibility

You can visit the links provided in the Documentation for Guidance section to ensure they're reachable. 

1. Open your web browser.
2. Enter the URL for Seamless SSO documentation.
3. Verify the page loads correctly.

#### Advice for Data Collection

- **Gather Diagnostic Logs:** Collect logs from Azure AD, Azure AD Connect, and the affected user’s machine.
- **User Feedback:** Have users provide a screenshot of the error if possible and a description of their actions before encountering the issue.
- **Environment Details:** Document the Windows version, browser type, and any policies that may be relevant to the problem.

This comprehensive troubleshooting guide should assist in resolving the error code AADSTS81007 effectively. Make sure to follow through each step methodically to isolate and correct the issue.