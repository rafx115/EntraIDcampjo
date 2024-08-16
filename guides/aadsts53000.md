# AADSTS53000: DeviceNotCompliant - Conditional Access policy requires a compliant device, and the device isn't compliant. The user must enroll their device with an approved MDM provider like Intune. For additional information, please visitConditional Access device remediation.


## Troubleshooting Steps
## Troubleshooting Guide for AADSTS53000: DeviceNotCompliant

### Overview
The AADSTS53000 error indicates that a user's device does not meet the compliance requirements set forth by the organization's Conditional Access policies, typically enforced through an MDM (Mobile Device Management) provider like Intune. Users must enroll their devices with the appropriate MDM solution to comply with these policies.

### Initial Diagnostic Steps
1. **User Notification**: Confirm the user who encountered the error and note the device they were using.
2. **Check Conditional Access Policies**: Review the Conditional Access policies applied to the user's account and the group to which they belong.
3. **User Location and Device Type**: Confirm if the user is trying to access resources either remotely or on a company-managed device.

### Common Issues that Cause This Error
1. **Not Enrolled in MDM**: The device is either not enrolled in the organization's MDM, or the enrollment is incomplete.
2. **Device Compliance Status**: The device may be enrolled but is not compliant with the organization's security policies (e.g., lacking updates, required settings).
3. **Intune/MDM Misconfiguration**: Errors in Intune policies that do not align with user/group and device settings.
4. **Network Issues**: Network configurations or firewalls that may block communication with the MDM services.
5. **Expired Compliance Settings**: Changes in the compliance settings at the organization level (e.g., a new policy applies but the device hasn’t been updated).

### Step-by-Step Resolution Strategies
1. **Check Device Enrollment**:
   - Verify that the device is enrolled in Intune.
   - Go to the Intune portal: [Microsoft Intune](https://endpoint.microsoft.com/) and check the user's device enrollment status.

2. **Compliance Status Check**:
   - In the Intune portal, check the device's compliance status.
   - Ensure the device meets all specified requirements (operating system version, security settings, etc.).

3. **Re-enroll the Device**:
   - If the device is not compliant, advise the user to re-enroll the device:
     - For Windows: Go to `Settings > Accounts > Access work or school`, select the account and choose `Disconnect`, and then re-connect.
     - For mobile devices: Follow the procedures in respective app stores.

4. **Update Device Configuration**:
   - Ensure the device has the latest operating system updates.
   - Check compliance policies for the required settings that may need to be configured (e.g., encryption, password policies).

5. **Reset Compliance Status**:
   - In rare scenarios, the compliance state may not reflect the actual usage. Remediating the device (removing and re-adding the MDM profiles) can help.

6. **Check Network Connectivity**:
   - If using a proxy or VPN, ensure these do not interfere with the MDM endpoints.
   - Verify that there are no DNS or routing issues preventing the device from reaching the MDM services.

### Additional Notes or Considerations
- Encourage users to follow up with IT support if issues persist after following the above steps.
- Ensure regular training and updates for users about compliance requirements and how to meet them.

### Documentation for Guidance
- **Microsoft Intune Documentation**: [Microsoft Intune Documentation](https://docs.microsoft.com/en-us/mem/intune/)
- **Azure Active Directory Conditional Access**: [Conditional Access Overview](https://docs.microsoft.com/en-us/azure/active-directory/conditional-access/overview)

### Advice for Data Collection
If issues are not resolved, collect logs for further investigation:

1. **Event Viewer Logs**:
   - Open the Event Viewer (eventvwr.msc).
   - Check under "Applications and Services Logs > Microsoft > Windows > DeviceManagement-Enterprise-Diagnostics-Provider" for errors related to enrollment or compliance.

2. **Network Trace (NetTrace)**:
   - Utilize `Microsoft Network Monitor` or `Wireshark` to capture traffic to and from the device to check for network issues or blocked connections to MDM services.

3. **Fiddler for HTTP/S Traffic**:
   - Use Fiddler to inspect HTTP/S traffic between the client device and the MDM server to trace any failed requests or response issues.

By following these steps and addressing the common causes of the AADSTS53000 error, users should be able to rectify compliance issues and access necessary resources.