# AADSTS53010: ProofUpBlockedDueToSecurityInfoAcr - Cannot configure multifactor authentication methods because the organization requires this information to be set from specific locations or devices.


## Troubleshooting Steps
## Troubleshooting Guide for AADSTS53010 Error

### Error Description
**AADSTS53010**: This error indicates that the multifactor authentication (MFA) methods cannot be configured because the organization has set restrictions on where or from which devices this information can be set.

---

### Initial Diagnostic Steps
1. **Verify User Permissions**:
   - Ensure that the user attempting to set up MFA has the proper permissions assigned.
   - Check if the user is part of a security group that allows MFA settings.

2. **Check Organizational Policies**:
   - Review the organization's policy settings related to MFA, conditional access, and user security.
   - Confirm if there are any restrictions in place that limit MFA configuration from specific locations or devices.

3. **Identify Location/Device**: 
   - Determine the device and network location from which the user is attempting to configure MFA.
   - Check if it falls within the permitted locations/devices specified by the organization.

---

### Common Issues that Cause this Error
1. **Security Restrictions**:
   - The organization has configured conditional access policies that restrict access based on location or device compliance.

2. **Device Compliance**:
   - The device being used might not meet the required compliance policies enforced by the organization.

3. **User Configuration Limitations**:
   - The user account may have limitations configured that prevent changes to MFA settings from certain locations.

4. **Identity Protection Settings**:
   - Any settings configured under Azure AD Identity Protection that restrict MFA may also be contributing to this error.

---

### Step-by-Step Resolution Strategies

#### Step 1: Validate Security Policies
- Access Azure Portal > Azure Active Directory > Security > Conditional Access.
- Review the policies to see if there are restrictions based on location or device compliance.
- Identify any relevant policies that may be blocking MFA setup.

#### Step 2: Configure Allowed Locations/Devices
- If needed, modify the conditional access policy to allow the user's location or device to configure MFA.
- Ensure that the policy aligns with the organization's security posture.

#### Step 3: Review User Account Settings
- Go to Azure Active Directory > Users > Select the affected user.
- Review their settings and group memberships to ensure they have the rights needed.

#### Step 4: Compliance Policies
- Ensure that the device attempting to configure MFA meets compliance requirements.
- For devices, check MDM (Mobile Device Management) compliance status if applicable.

#### Step 5: Dynamic Location Check
- If the user's current location is dynamic, it may be worthwhile to review network IP whitelist configurations in conditional access.

#### Step 6: User Instruction
- Instruct the user to attempt the configuration from a previously registered or compliant device/location if applicable.

---

### Additional Notes or Considerations
- Depending on the organization’s policies, employees are often required to register devices or submit requests to IT for access modifications.
- The organization’s IT Security team should be involved if policy modifications could have broader implications.

---

### Documentation for Guidance
- Microsoft Documentation on [Conditional Access](https://docs.microsoft.com/en-us/azure/active-directory/conditional-access/overview)
- Azure AD [Multi-Factor Authentication](https://docs.microsoft.com/en-us/azure/active-directory/authentication/howto-mfa-userstates).
- [Manage Authentication Methods](https://docs.microsoft.com/en-us/azure/active-directory/authentication/authentication-methods)

---

### Advice for Data Collection

#### Event Viewer Logs
- Check the Event Viewer on the user’s device for any log entries related to Azure AD sign-in failures or MFA setup.
   - Look under **Windows Logs > Application** or **Security** logs for relevant Error/Warn events.

#### Network Tracing
- Use **NetTrace** for capturing the network activity when attempting to configure MFA. This can help identify failures in network communications.

#### Fiddler
- Run Fiddler to capture HTTP/HTTPS calls during the MFA setup. Look for responses from Azure that mimic the AADSTS53010 error code. Analyze the the payload for additional context.

#### Review and Analyze Captured Data
- Look for patterns that indicate network or configuration issues related to specific locations or device context.

---

This troubleshooting guide should help diagnose and resolve the AADSTS53010 error effectively.