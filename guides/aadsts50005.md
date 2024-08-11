
# AADSTS50005: DevicePolicyError - User tried to sign in to a device from a platform not currently supported through Conditional Access policy.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS50005: DevicePolicyError

#### Initial Diagnostic Steps:
1. **Identify the User**: Verify the user who is experiencing the issue and note the specific device or platform they are trying to sign in with.
2. **Review Conditional Access Policies**: Check the Conditional Access policies applied in your Azure AD to see if the platform they are using is indeed not supported.
3. **Check Recent Changes**: Determine if any recent changes to Conditional Access policies, device management settings, or user configurations might have triggered the error.

#### Common Issues Causing the Error:
- Incorrect Conditional Access Policy configuration.
- User attempting to sign in from a platform not compliant with current policies.
- Recent policy updates restricting access to certain devices or platforms.

#### Step-by-Step Resolution Strategies:
1. **Review and Update Conditional Access Policies**:
   - Navigate to Azure Active Directory portal > Security > Conditional Access.
   - Check the existing policies to ensure they do not block the platform the user is attempting to sign in from.
   - Modify the policy or create new policies to allow access from the specific platform if needed.
2. **Check Device Compliance**:
   - Ensure the device being used meets the compliance requirements set in the Conditional Access policies.
   - If the device is non-compliant, work on bringing it into compliance before attempting to sign in again.
3. **User Communication and Assistance**:
   - Communicate with the user experiencing the issue to gather more details about the device and platform they are using.
   - Provide guidance on acceptable platforms for sign-in as per organizational policies.

#### Additional Notes or Considerations:
- **User Training**: Educate users on the supported platforms for signing in to enhance compliance with policies.
- **Regular Policy Review**: Regularly review and update Conditional Access policies to align with organizational needs and changing requirements.

#### Documentation for Guidance:
- [Azure Active Directory Conditional Access documentation](https://docs.microsoft.com/en-us/azure/active-directory/conditional-access/overview)
- [Troubleshoot Conditional Access policies in Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/conditional-access/howto-conditional-access-policy-common-problems)

By following these troubleshooting steps, you can effectively address the error code AADSTS50005 (DevicePolicyError) and help users sign in securely while ensuring compliance with your organization's Conditional Access policies.