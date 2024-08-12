
# AADSTS50005: DevicePolicyError - User tried to sign in to a device from a platform not currently supported through Conditional Access policy.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS50005

The error code AADSTS50005 indicates that a user is attempting to sign in to a device from an unsupported platform under the Conditional Access policy configured in Azure Active Directory (AAD). This guide will provide you with detailed steps to troubleshoot and resolve the issue.

#### Initial Diagnostic Steps

1. **Confirm User Identity**: Verify that the user receiving the error is attempting to sign in with the correct username and password.

2. **Check the Device**: Determine the type of device (Windows, macOS, Linux, iOS, Android) that the user is attempting to sign in from.

3. **Review Conditional Access Policies**:
   - Log in to the Azure portal and navigate to **Azure Active Directory > Security > Conditional Access**.
   - Review the policies that apply to the user and the device being used.

#### Common Issues That Cause This Error

1. **Device Platform Restrictions**: Conditional Access policies may restrict certain platforms. For instance, if a policy applies only to Windows devices, and the user is trying to sign in from a macOS device, this error may occur.

2. **Device Compliance**: The device may not comply with security requirements defined in the Conditional Access policy (e.g., not registering with Intune or not being marked as compliant).

3. **User License Issues**: The user may not have the necessary licenses for the features enabled by the Conditional Access policy.

4. **Browser or App Versions**: Some older browsers or applications might not be supported as per Conditional Access policies.

5. **Multiple Policies Conflicting**: There could be overlapping Conditional Access policies leading to unexpected results.

#### Step-by-Step Resolution Strategies

1. **Review the Current Conditional Access Policies**:
   - Identify which policies are currently active and who they apply to.
   - Check if there are any restrictions based on operating system or device management status.

2. **Modify or Create a Policy**:
   - If appropriate, modify existing policies or create a new policy that supports the required device type. For example, if the policy restricts access to Windows devices only, you may want to allow macOS or mobile devices, based on your organizational needs.

3. **Ensure Device Compliance**:
   - Check if the device being used is marked as compliant in your Intune or device management solutions.
   - If it is not compliant, address any compliance issues before re-attempting the sign-in.

4. **Test Access from a Different Device**:
   - If possible, have the user attempt to sign in from a device that is known to be compliant with existing policies to isolate whether the issue is device-specific.

5. **Check User Licenses**:
   - Verify that the user has the necessary licenses assigned in the Azure portal that grants access to the services controlled by the Conditional Access policy.

6. **Browser/App Compatibility**:
   - Ensure the user is using an up-to-date browser or application that is supported by your Conditional Access policies.

7. **Logging and Analysis**:
   - Utilize Azure AD sign-in logs to monitor the sign-in attempts and identify patterns or specific policy blocks.
   - If necessary, collect logs from applications and devices as outlined below.

#### Additional Notes or Considerations

- **User Notifications**: Ensure users are aware of which devices are permitted under the Conditional Access policies, which can help reduce confusion.
- **Training and Documentation**: Provide documentation or training sessions on Conditional Access policies and supported devices.

#### Documentation for Further Guidance

- Azure Active Directory Conditional Access: [Microsoft Docs](https://docs.microsoft.com/en-us/azure/active-directory/conditional-access/overview)
- Managing Devices in Azure AD: [Microsoft Docs](https://docs.microsoft.com/en-us/azure/active-directory/devices/)

#### Advice for Data Collection

- **Event Viewer Logs**: 
  1. On the device, access the Event Viewer by typing `eventvwr` in the Run dialog (Windows + R).
  2. Look under **Applications and Services Logs > Microsoft > Windows > User Device Registration** for relevant logs.
  
- **Network Tracing (Nettrace)**: 
  1. Run `netsh trace start capture=yes` in an elevated command prompt.
  2. Attempt to reproduce the error, then stop the trace with `netsh trace stop`.

- **Fiddler**: 
  1. Install Fiddler and configure it to capture HTTP/HTTPS traffic.
  2. Capture logs while the user attempts to sign in to investigate the requests/responses related to authentication.

Collecting this information will help in deeper analysis and in providing precise guidance to support teams or Microsoft support if the issue persists.