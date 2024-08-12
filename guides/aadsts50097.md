
# AADSTS50097: DeviceAuthenticationRequired - Device authentication is required.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS50097: DeviceAuthenticationRequired

#### Overview
The error code AADSTS50097 indicates that device authentication is required for the user to access the requested resources. This is commonly encountered in environments that utilize Azure Active Directory (Azure AD) alongside Conditional Access policies or where device compliance is enforced.

---

#### Initial Diagnostic Steps
1. **Verify the User Account**: Ensure that the account experiencing the issue is correct and has the appropriate permissions.
2. **Check Azure AD Conditional Access Policies**: Review any Conditional Access policies that may require device compliance or specific authentication methods.
3. **Review Device Compliance Policies**: Ensure that the device being used complies with organizational policies.
4. **Assess Network Connection**: Confirm that the user has a stable and secure network connection.
5. **Identify Device Type**: Note whether the device is a Windows PC, Mac, mobile device, etc. Different operating systems may have different compliance requirements.

---

#### Common Issues That Cause This Error
1. **Non-Compliant Devices**: The device does not meet the security posture required by the organization's policies.
2. **Unregistered or Unenrolled Devices**: The device must be registered with Azure AD or enrolled in Mobile Device Management (MDM).
3. **Outdated OS or Software**: Ensure that the operating system and applications are up to date, as old versions may not comply with security policies.
4. **Inadiquate Authentication Methods**: The user may not have the necessary multi-factor or modern authentication methods set up.
5. **Location of Access**: Accessing from a non-trusted location could trigger device authentication requirements.

---

#### Step-by-Step Resolution Strategies
1. **Check Compliance Status**:
   - **Intune/Mobile Device Management**: Verify that the device is enrolled in Intune or another MDM solution. Check for compliance status via the Intune portal or equivalent management interface.

2. **Register the Device**:
   - **Join the Device to Azure AD**: Ensure that the user's device is joined to Azure AD. Go to Settings > Accounts > Access Work or School > Connect, and sign in with work or school account.

3. **Update Device**:
   - **Software Update**: Make sure the operating system and security software are fully updated. Instructions for Updates:
     - **Windows**: Settings > Update & Security > Windows Update.
     - **macOS**: System Preferences > Software Update.
     - **Mobile Devices**: Settings > General > Software Update.

4. **Ensure Proper Authentication Setup**:
   - **Multi-factor Authentication (MFA)**: Ensure MFA is set up if required. Navigate to Azure AD > Users > User > Authentication Methods, then verify the settings for the user.

5. **Review Conditional Access Policies**:
   - Login to the Azure portal and navigate to Azure AD > Security > Conditional Access. Review policies that might be enforcing device-based conditions.
   
6. **Mobile Device Registration**:
   - If using a mobile device, ensure it is registered in Azure AD and complies with the set policies.

7. **Testing with an Alternative Device**:
   - As a test, try accessing the application with a different device that is known to be compliant.

8. **User Support and Documentation**:
   - Refer the user to IT support if they need assistance in providing device compliance. Provide documentation for them to follow.

---

#### Additional Notes or Considerations
- Ensure that the user is aware of their organizational policies regarding device compliance and authentication.
- Emphasize the importance of keeping devices synchronized with organizational policies for seamless access.

---

#### Documentation for Guidance
- [Azure AD Conditional Access Documentation](https://docs.microsoft.com/en-us/azure/active-directory/conditional-access/)
- [Manage device compliance in Intune](https://learn.microsoft.com/en-us/mem/intune/protect/compliance-policy-monitor)

---

#### Advice for Data Collection
Gather the following logs if the issue persists:

1. **Event Viewer Logs**:
   - Navigate to **Windows Logs > Application** and **Windows Logs > Security** for any related events.

2. **Nettrace**:
   - Use **Netsh trace** to capture network traffic. Command: `netsh trace start capture=yes` and `netsh trace stop`.

3. **Fiddler**:
   - Install Fiddler to capture request/response data when accessing the application. Look for any 401 or 403 status codes.
   
4. **Azure AD Sign-In Logs**:
   - Azure AD Portal > Monitoring > Sign-in logs. Filter for the user and the specific error code for additional insight.

By following the recommendations above, you will likely resolve the AADSTS50097 error and restore access to the affected user.