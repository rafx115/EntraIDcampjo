
# AADSTS53001: DeviceNotDomainJoined - Conditional Access policy requires a domain joined device, and the device isn't domain joined. Have the user use a domain joined device.


## Troubleshooting Steps
## Troubleshooting Guide for Error Code AADSTS53001

### Description
The error code AADSTS53001 indicates that a Conditional Access policy in Azure Active Directory (AAD) requires a device to be domain-joined, but the device trying to access the resource is not domain-joined. This often occurs in environments where security compliance is enforced via device management policies.

---

### Initial Diagnostic Steps
1. **Identify the User**: Confirm which user is encountering the error and the specific resource they are trying to access.
2. **Review Conditional Access Policies**: Check the specific Conditional Access policy that is triggering this error to determine if it includes a requirement for domain-joined devices.
3. **Check Device Status**: Verify the status of the device the user is accessing from:
   - Is the device part of the corporate domain?
   - Is the device properly joined to the domain?
4. **Device Information**: Gather information about the device:
   - Operating System version
   - Device type (PC, Mobile, etc.)
   - Network configuration
5. **Connect with User**: Have a conversation with the user to ascertain what they were doing at the time of receiving the error, and if any recent changes were made to their device or configuration.

---

### Common Issues That Cause This Error
- **Device Not Joined to Domain**: The primary cause of this error is that the device the user is using is not joined to the required domain.
- **Outdated Device Status**: The device may have been domain-joined prior but was removed from the domain or unable to recognize its domain status due to various reasons.
- **Network Issues**: The device may not have a reliable connection to the network; hence, it cannot authenticate to the domain.
- **Conditional Access Policy Configuration**: The policy may have been recently modified to enforce domain join requirements.
- **Intune/MDM Settings**: If the organization utilizes mobile device management (MDM) solutions, the device may not be compliant.

---

### Step-by-Step Resolution Strategies
1. **Verify Device Domain Join Status**:
   - On the device, go to **Settings > System > About** and check the "Domain" section to see if it's listed as being joined to the correct domain.
   - Alternatively, you can check using PowerShell:
     ```powershell
     Get-ComputerInfo | Select-Object CsDomain
     ```

2. **Join Device to Domain** (If not joined):
   - Ensure you have the right credentials to join the device to the domain.
   - Right-click on **This PC > Properties > Change settings > Change...** and specify the domain to join.

3. **Verify Network Connection**:
   - Check that the device is connected to the corporate network or VPN.
   - Use commands such as `ping` or `nslookup` to check domain connectivity.

4. **Check Conditional Access Policy**:
   - Sign into the Azure Active Directory Admin Center.
   - Navigate to **Security > Conditional Access** and review the policies affecting your user/group.
   - Ensure that the policy correctly reflects your organization’s requirements.

5. **Device Compliance**:
   - If applicable, check if the device is enrolled in Intune or another MDM, and verify compliance status.
   - Enforce compliance policies if you manage devices using MDM.

6. **Retry Access**: After making the necessary changes, have the user reattempt access to the resource.

---

### Additional Notes or Considerations
- If the user does not have access to a domain-joined device, consider alternative access methods configured by your organization (e.g., guest access, secure portals).
- Ensure that all changes are documented for IT audits and compliance purposes.
- Regularly review and update Conditional Access policies as necessary to align with organizational needs and security compliance.
  
---

### Documentation for Guidance
- [Microsoft Azure AD Conditional Access](https://docs.microsoft.com/en-us/azure/active-directory/conditional-access/overview)
- [Join a Windows 10 Device to a Domain](https://docs.microsoft.com/en-us/windows/security/identity-protection/active-directory-domain-services)
- [Troubleshoot Intune Device Compliance](https://docs.microsoft.com/en-us/mem/intune/protect/devices-compliance-troubleshoot)

---

### Advice for Data Collection
- **Event Viewer Logs**: Check the Event Viewer on the affected device:
  - Type `eventvwr.msc` in the Run dialog.
  - Look under "Windows Logs" > "Application" and "Security" for any relevant logs related to domain joins or authentication failures.
  
- **Network Tracing**: Use tools like Netsh or Wireshark to collect network traces if needed for deeper troubleshooting.
  
- **Fiddler**: If the issue involves web access, gather Fiddler traces to analyze HTTP requests being made and their responses.

**Note**: Always ensure you have proper permission and authority before gathering event logs or conducting network analyses in a corporate environment.