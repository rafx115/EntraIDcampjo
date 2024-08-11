# AADSTS50005: DevicePolicyError - User tried to sign in to a device from a platform not currently supported through Conditional Access policy.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS50005 - DevicePolicyError

**Error Code**: AADSTS50005  
**Description**: User tried to sign in to a device from a platform not currently supported through Conditional Access policy.

This specific error indicates that the user is attempting to sign in from a device or platform that does not comply with the organization's Conditional Access policies set within Azure Active Directory (AAD).

---

### Initial Diagnostic Steps

1. **Verify User Context**: Confirm who is experiencing the error, the device they are using, and what platform (Windows, macOS, iOS, Android, etc.) they are attempting to sign in from.

2. **Review Conditional Access Policies**: Look into the Conditional Access policies configured in Azure AD to see what devices/platforms are permitted or denied.

3. **Check User Assignments**: Verify if the affected user is assigned to a Conditional Access policy that restricts access based on device type or platform.

---

### Common Issues that Cause this Error

1. **Unsupported Device or OS**: The user is attempting to access the service from a device or operating system that is excluded by the Conditional Access policies.

2. **Location-Based Policies**: Conditional Access policies may restrict access based on the user's geographic location or network.

3. **Unregistered Device**: The device being used might not be registered or compliant with the organization's device management policies.

4. **Browser Compatibility Issues**: Some policies apply only to specific browsers; using an unsupported browser could cause this error.

5. **User Account Status**: The user account may be disabled or not licensed correctly for the subscription.

---

### Step-by-Step Resolution Strategies

1. **Identify Device and Platform**:
   - Ask the user what type of device they are using.
   - Note the operating system version and browser being used.

2. **Check Azure AD Conditional Access Policies**:
   - Log in to the Azure portal.
   - Navigate to `Azure Active Directory` > `Security` > `Conditional Access`.
   - Review the policies for any restrictions on device platforms.

3. **Adjust Conditional Access Policies (if necessary)**:
   - If the current policy is too restrictive and allows for broader access, edit the policy to include the user's device type or platform.

4. **Test from a Different Device**:
   - Instruct the user to try signing in from a different, known compliant device or platform. If they succeed, it confirms the original device is not supported.

5. **Device Compliance Check**:
   - If using Intune for device management, ensure that the device is registered with Intune and meets compliance policies.

6. **Review and Update User Assignments**:
   - Go to `Azure Active Directory` > `Users` > Select the affected user > Check assigned groups and roles related to Conditional Access.

7. **Gather Diagnostic Data**:
   - Collect logs and error messages related to the sign-in attempts from Azure AD Sign-in logs.

---

### Additional Notes or Considerations

- **Policy Timing**: Newly created policies may take some time before fully applying. If a new policy was just created or modified, allow some time for changes to take effect.

- **Policy Conflicts**: Check for any overlapping Conditional Access policies which might be causing conflicting rules.

- **Review Documentation**: Ensure that users know and understand the Device Compliance standards required by your organization.

---

### Documentation Links for Further Guidance

- [Overview of Conditional Access in Azure Active Directory](https://docs.microsoft.com/en-us/azure/active-directory/conditional-access/overview)
- [Manage Conditional Access Policies](https://docs.microsoft.com/en-us/azure/active-directory/conditional-access/concepts/policy)
- [Monitoring Sign-ins in Azure Active Directory](https://docs.microsoft.com/en-us/azure/active-directory/reports-monitoring/concept-sign-ins)

*Note: Always verify that these links are accessible and relevant to the current state of Microsoft documentation.*

---

### Test Documentation Accessibility 

To ensure the documentation is reachable:
- Open a web browser.
- Visit each of the provided links to confirm they are alive and contain the necessary information.

---

### Advice for Data Collection

- Use Azure AD's `Sign-ins` logs to collect information about user sign-ins.
- Check for any other errors that may have occurred recently from the `Audit logs`.
- Document user details, timestamp of the issue, and device specifics (make, model, OS version).
- Collect network information, including whether the user is on a corporate network or a public Wi-Fi.

By following this troubleshooting guide, you can systematically approach the AADSTS50005 error and work through resolution steps effectively.