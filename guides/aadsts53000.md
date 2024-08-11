# AADSTS53000: DeviceNotCompliant - Conditional Access policy requires a compliant device, and the device isn't compliant. The user must enroll their device with an approved MDM provider like Intune. For additional information, please visitConditional Access device remediation.


## Troubleshooting Steps
**Troubleshooting Guide for AADSTS53000 Error Code**

**Initial Diagnostic Steps:**
1. Confirm that the user's device is non-compliant and not enrolled in an approved MDM provider like Intune.
2. Ensure that the user is accessing a resource protected by Conditional Access policies that require device compliance.
3. Verify any specific policy requirements set by your organization regarding device compliance.

**Common Issues Leading to AADSTS53000 Error:**
1. Device is not compliant with organization's security policies.
2. User's device is not enrolled in an approved MDM provider.
3. Incorrect Conditional Access policy settings or configurations.

**Step-by-Step Resolution Strategies:**
1. **Enroll Device with Intune:**
   - Instruct the user to enroll their device with Intune or another approved MDM provider as per your organization's policy.
   - Provide guidance on the enrollment process and any specific requirements.
   
2. **Check Device Compliance:**
   - Have the user verify if their device meets the organization's security standards and is marked as compliant in Intune.
   - Guide them on how to check device compliance status on their device or through Intune dashboard.
   
3. **Review Conditional Access Policies:**
   - Check the specific Conditional Access policies that are in place and ensure that they require compliant devices.
   - Review and adjust the policy settings if necessary to align with the user's device compliance status.
   
**Additional Notes or Considerations:**
- It's essential to communicate the importance of device compliance to users and provide assistance in the enrollment process.
- Regularly review and update your organization's Conditional Access policies to adapt to changing security requirements.
  
**Documentation for Guidance:**
- Microsoft official documentation on Conditional Access policies and device compliance: [Conditional Access Documentation](https://docs.microsoft.com/en-us/azure/active-directory/conditional-access/)
- Microsoft Intune documentation for device enrollment and compliance: [Intune Documentation](https://docs.microsoft.com/en-us/mem/intune/)
  
By following these detailed troubleshooting steps, you can help users resolve the AADSTS53000 error related to device compliance issues effectively.