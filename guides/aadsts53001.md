
# AADSTS53001: DeviceNotDomainJoined - Conditional Access policy requires a domain joined device, and the device isn't domain joined. Have the user use a domain joined device.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS53001 (DeviceNotDomainJoined)

#### Initial Diagnostic Steps:
1. **Confirm the error**: Make sure the user has received the error code AADSTS53001: DeviceNotDomainJoined.
   
2. **Check Device Domain Join Status**: Verify that the device in use is not domain joined. This can typically be checked under the device settings or system information.

3. **Understand Conditional Access Policy Requirements**: Ensure the user is aware that the specific Conditional Access policy being enforced requires a domain joined device for access.

#### Common Issues that Cause this Error:
- User is using a personal device that is not joined to the domain.
- Presence of conflicting or incorrectly configured Conditional Access policies.
- Device registration issues within the Azure AD portal.

#### Step-by-Step Resolution Strategies:

1. **Use a Domain Joined Device**: Ask the user to switch to a device that is part of the domain if possible, to comply with the requirements of the Conditional Access policy.

2. **Verify Device Registration**: Ensure that the affected device is properly registered in Azure AD. The user may need assistance with this process.

3. **Review Conditional Access Policies**: Check the Azure AD portal for any conflicting or misconfigured Conditional Access policies that might be causing the issue. Modify or remove the conflicting policies as needed.

4. **Educate the User**: Explain the importance of using a domain joined device to access resources protected by specific Conditional Access policies. Provide guidance on proper device setup if necessary.

#### Additional Notes or Considerations:
- IT administration may need to review the device registration and Conditional Access policies to ensure compliance with organization's security policies.
- Encourage users to adhere to IT guidelines regarding device usage for work-related tasks.

#### Documentation for Further Guidance:
For detailed information on Conditional Access policies and best practices, refer to the [Microsoft documentation on Conditional Access](https://docs.microsoft.com/en-us/azure/active-directory/conditional-access/overview).

By following these steps and considerations, you can help resolve the error code AADSTS53001 (DeviceNotDomainJoined) effectively and ensure secure access to resources within your organization.