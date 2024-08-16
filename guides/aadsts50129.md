# AADSTS50129: DeviceIsNotWorkplaceJoined - Workplace join is required to register the device.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS50129

**Error Code:** AADSTS50129  
**Description:** DeviceIsNotWorkplaceJoined - Workplace join is required to register the device.

### 1. Initial Diagnostic Steps

- **Identify User and Device**: Collect information about the user encountering the error and the device being used.
- **Check Intune or Azure AD**: Verify whether the user is expected to register the device with Workplace Join.
- **Operating System Version**: Ensure that the device is running a supported operating system (Windows 10/11, for example).
- **Internet Connectivity**: Confirm that the device has a stable internet connection.
- **Check Organization Policies**: Understand if there are specific organizational policies regarding device registration.

### 2. Common Issues That Cause This Error

- **Device Not Joined to Azure AD**: The device does not meet the requirements to be considered 'workplace joined'.
- **Group Policy Restrictions**: Existing Group Policy settings may restrict the device registration.
- **User Account Issues**: The user account might not have the permissions needed to join devices to Azure AD.
- **Network Issues**: Firewalls or network restrictions could be blocking necessary Azure AD services.
- **Windows Updates**: The device might need updates that facilitate the joining or registration with Azure AD.

### 3. Step-by-Step Resolution Strategies

#### Step 1: Check Device Join Status
- **Windows Settings**:
  1. Go to **Settings → Accounts → Access work or school**.
  2. Check if the account is listed as a connected account; if not, proceed to join.

#### Step 2: Join Device to Azure AD
- **Joining Process**:
  1. Navigate to **Settings → Accounts → Access work or school**.
  2. Click on **Connect**.
  3. Enter your work or school email address when prompted.
  4. Follow the prompts to complete the joining process.

#### Step 3: Resolve Group Policy Restrictions
- **Group Policy Management** (if applicable):
  1. Open the Group Policy Management Console.
  2. Check for policies that affect Azure AD Join. Specifically, ensure policies such as `Allow users to connect remotely using NLA` are correctly configured.

#### Step 4: Permissions Verification
- Ensure that the user account being used has the necessary permissions to register devices with Azure AD. If not, update the account status in Azure AD.

#### Step 5: Check and Update the Device
- **Windows Update**: Go to **Settings → Update & Security → Windows Update**. Install any pending updates.
  
#### Step 6: Validate Network Configuration
- Ensure that DNS and network configurations allow connections to Azure AD services. Test by pinging `login.microsoftonline.com`.

### 4. Additional Notes or Considerations

- **Device Compliance**: Ensure that the device meets all compliance requirements set out by the organization.
- **Manual Workaround**: If automatic registration fails, explore manual registration options with IT support.
- **Documentation Review**: Reference Microsoft documentation for Workplace Join and Azure AD Setup.

### 5. Documentation for Steps

1. [Join a Windows 10 or Windows 11 Device to Azure Active Directory](https://docs.microsoft.com/en-us/azure/active-directory/devices/azure-ad-join-windows)
2. [Workplace Join Overview](https://docs.microsoft.com/en-us/enterprise/desktop-deployment/update/windows-workplace-join)
3. [Device Registration for Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/devices/overview)

### 6. Advice for Data Collection

If further troubleshooting is necessary:

- **Event Viewer Logs**:
  - Navigate to `Event Viewer → Applications and Services Logs → Microsoft → Windows → User Device Registration`.
  - Look for relevant errors or warnings around the time the error occurs.

- **NetTrace**:
  - Use the built-in Windows tool to capture network traffic during the registration attempt. Helpful for analyzing connectivity issues.

- **Fiddler**:
  - Capture HTTP/HTTPS traffic to observe the requests and responses from the Azure AD endpoints. This can help identify unexpected behavior or failures in API calls.

#### Note on Security:
Always ensure that logs and traces do not contain sensitive information before sharing them for troubleshooting.

### Conclusion

By following the above steps and utilizing the provided resources, you should be able to diagnose and resolve the AADSTS50129 error effectively.