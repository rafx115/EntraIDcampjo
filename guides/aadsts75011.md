
# AADSTS75011: NoMatchedAuthnContextInOutputClaims - The authentication method by which the user authenticated with the service doesn't match requested authentication method. To learn more, see the troubleshooting article for errorAADSTS75011.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS75011 Error

Error code **AADSTS75011** indicates a mismatch between the authentication method the user has used and the method required by the application. Below is a structured troubleshooting guide to help resolve this issue.

#### Initial Diagnostic Steps

1. **Identify the User and Context**:
   - Confirm which user is experiencing the issue.
   - Gather information about the context of the authentication (e.g., device, location).

2. **Review Error Message**: 
   - Carefully read the error message to comprehend the authentication context that was requested versus what was received.

3. **Check Authentication Methods**:
   - Verify which authentication methods are currently configured for the application in Azure AD.

4. **Confirm Application Permissions**:
   - Ensure that the application permissions are correctly set for the requested authentication scenario.

#### Common Issues That Cause This Error

1. **Mismatched Authentication Protocols**:
   - The application may be requesting a specific authentication method (e.g., MFA, passwordless) that the user is not able to satisfy.

2. **Conditional Access Policies**:
   - Conditional access policies may restrict methods based on user attributes, location, or device risk.

3. **Misconfigured Application Registration**:
   - The application registration in Azure Active Directory may not align with the authentication methods users are attempting to use.

4. **User Authentication Group Membership**:
   - Users may not belong to any security group that grants access to the required authentication methods.

5. **Device Compliance Issues**:
   - User devices may not meet compliance or security requirements set in Azure AD policies.

#### Step-by-Step Resolution Strategies

1. **Review Application Authentication Settings**:
   - Go to the Azure portal > Azure Active Directory > App registrations > [Your App] > Authentication.
   - Verify the authentication methods configured (e.g., OAuth, OpenID Connect).

2. **Check Conditional Access Policies**:
   - Navigate to Azure Active Directory > Security > Conditional Access.
   - Review the policies applied to the user and the application to ensure they allow the authentication method being used.

3. **Update Authentication Methods per User/Group**:
   - Confirm that users have access to the required authentication methods under Azure AD > Users > [User] > Authentication methods.
   - Enable or modify the authentication methods as needed.

4. **Test with Different Users**:
   - Attempt authentication with a different user account that should have access. This can provide insight into whether it is a user-specific issue.

5. **Review User Group Memberships**:
   - Ensure that the user is part of any necessary Azure AD security groups that have access to authentication methods.

6. **User Device Compliance Check**:
   - Verify that the user's device complies with any device policies. Non-compliant devices may be blocked from certain authentication methods.

7. **Logs Review**:
   - Collect and analyze logs to identify where the authentication strategy is failing.

#### Additional Notes or Considerations

- If the application is integrated with ADFS or any other identity provider, check how authentication flows are configured.
- Consider any recent changes to the Azure AD configuration or application settings that may have led to the mismatch.

#### Documentation for Guidance

Microsoft provides extensive documentation on troubleshooting Azure AD errors. For AADSTS75011 specifically, reference the following links:
- [Azure Active Directory Error Codes](https://docs.microsoft.com/en-us/azure/active-directory/develop/reference-aad-error-codes)
- [Troubleshoot Authentication Issues](https://docs.microsoft.com/en-us/azure/active-directory/develop/troubleshoot-authentication-issues)

#### Advice for Data Collection

When troubleshooting, you might need to collect the following data:

1. **Event Viewer Logs**:
   - On the client machine, open the Event Viewer and check logs under "Applications and Services Logs" > "Microsoft" > "Windows" > "AzureAd" for relevant error logs.

2. **Network Traces**:
   - Use network tracing tools like **NetTrace** or **Wireshark** to collect packets during authentication attempts to analyze the requests and responses.

3. **Fiddler**:
   - If using Fiddler, capture HTTPS traffic to monitor the HTTP requests sent to Azure AD during the authentication process.

Collect these logs before trying to troubleshoot or make changes, as they can provide insights into the authentication workflow and where exactly the issue is occurring.

Following these steps should help you diagnose and resolve the AADSTS75011 error efficiently.