# AADSTS50002: NotAllowedTenant - Sign-in failed because of a restricted proxy access on the tenant. If it's your own tenant policy, you can change your restricted tenant settings to fix this issue.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS50002: NotAllowedTenant

The AADSTS50002 error typically indicates that the tenant's settings have restricted access, preventing users from signing in. This issue often arises from tenant configurations related to security protocols or proxy access.

#### Initial Diagnostic Steps
1. **Identify the User and Tenant**: Gather information about the user experiencing the issue. Confirm which Azure Active Directory (AAD) tenant they are trying to access.
   
2. **Check Access Policies**: Review the tenant's access policies to determine if there are restrictions impacting sign-ins. This includes verifying Conditional Access Policies and any IP address restrictions.

3. **Review the Application Settings**: Ensure that the application the user is attempting to access is properly registered within the AAD tenant.

4. **Assess Proxy Configuration**: If using a corporate network, check for any proxy configurations that might be limiting access.

#### Common Issues That Cause This Error
- **Restricted Tenant Access**: Specific Azure AD tenant policies are set that prevent access from certain conditions (e.g., unknown locations, devices).
- **Expired or Misconfigured Applications**: The Azure AD application used for authentication may have expired credentials, incorrect redirect URIs, or other configuration issues.
- **Geographic Restrictions**: Conditions set to deny access from certain geographic locations.
- **IP Restrictions**: Conditional Access Policies that block access from unfamiliar or unrecognized IP addresses.

#### Step-by-Step Resolution Strategies
1. **Check Tenant Settings**:
    - Log into the Azure portal using admin credentials.
    - Navigate to **Azure Active Directory > Properties**.
    - Check settings related to “User consent settings” and ensure they are correctly configured.

2. **Review Conditional Access Policies**:
    - Go to **Azure Active Directory > Security > Conditional Access**.
    - Assess policies to ensure they do not unintentionally block access for the user or location.

3. **Inspect Application Registration**:
    - Check the application registration in **Azure Active Directory > App registrations**.
    - Confirm that all settings, such as **Reply URLs** and **API permissions**, are correct.

4. **Update Proxy Settings**:
    - If accessing via a proxy, ensure that the IP address is allowed through the tenant’s configurations.
    - Test access directly without proxy to identify if this is the cause.

5. **User Authentication Flow**:
    - Confirm that the user is entering the correct credentials.
    - Check if Multi-Factor Authentication (MFA) is required and troubleshoot accordingly.

6. **Audit Logs**:
    - Utilize **Azure AD Audit logs** and sign-in logs to identify any error messages or alerts associated with the problem.
    - Filtering logs by user can help isolate specific error details.

#### Additional Notes or Considerations
- If the tenant is managed by a different organization or is a personal account, ensure that you have the right permissions to access tenant settings.
- Be cautious when modifying security settings and access policies as they can affect other users.

#### Documentation
- Azure AD Error Codes: [AADSTS Error Codes](https://docs.microsoft.com/en-us/azure/active-directory/develop/reference-aadsts-error-codes)
- Manage Conditional Access: [Manage Conditional Access in Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/conditional-access/)
- Application Registration in Azure AD: [Register an application with Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)

#### Advice for Data Collection
- **Event Viewer Logs**: Collect logs from the Event Viewer on the client's machine, especially under **Applications and Services Logs > Microsoft > Windows > AzureAD** for relevant entries.
  
- **Network Trace**: Use tools like **NetTrace** (Windows built-in) to capture network activity when the sign-in occurs. This can highlight blocked responses or error codes returned from the server.
  
- **Fiddler**: If applicable, running Fiddler to monitor HTTP/HTTPS traffic can help capture and analyze the requests and responses during authentication attempts, providing more context around the AADSTS50002 error.

By following these troubleshooting steps and utilizing the documentation, you can identify the cause of the AADSTS50002 error and effectively resolve it.