# AADSTS50178: SessionControlNotSupportedForPassthroughUsers - Session control isn't supported for passthrough users.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS50178

#### Understanding the Issue
**Error Code:** AADSTS50178  
**Description:** "SessionControlNotSupportedForPassthroughUsers - Session control isn't supported for passthrough users."

This error typically occurs in Azure Active Directory (Azure AD) when a user is identified as a passthrough user, and there are attempts to apply session controls that are incompatible with passthrough authentication. 

#### Initial Diagnostic Steps
1. **Verify User Type:**
   - Determine if the affected user is a passthrough user. This can be done by checking the user's authentication method in the Azure AD portal.

2. **Check Conditional Access Policies:**
   - Review any Conditional Access policies applied to the user, particularly those that involve session controls.

3. **Review Authentication Methods:**
   - Ensure that the authentication method configured for the user allows for the intended session control.

#### Common Issues that Cause This Error
1. **User Identification as Passthrough:**
   - The user is set up to use passthrough authentication, which may not support certain session control settings.

2. **Incompatible Conditional Access Policies:**
   - Policies containing session control features (like "Sign-in frequency" or “Application enforced restrictions”) that are not applicable to passthrough users.

3. **Configuration Errors:**
   - Incorrect configuration of session controls or authentication mechanisms in the Azure AD portal.

#### Step-by-Step Resolution Strategies

**Step 1: Assess User Authentication Method**
- Go to the Azure AD portal.
- Navigate to **Users** > **Select the User** > **Authentication methods**.
- Confirm that the user is using passthrough authentication.

**Step 2: Review Conditional Access Policy**
- Go to **Azure AD** > **Security** > **Conditional Access**.
- Review the policies applied to the user. Check for policies with session controls that may be conflicting with passthrough authentication.
- If any policy conflicts, consider modifying it to exclude passthrough authentication users or altering the session control settings.

**Step 3: Adjust Authentication Settings**
- If session control is necessary for compliance or security, consider switching the user or application to another authentication method that supports session controls (e.g., using Azure AD password-based sign-in).

**Step 4: Test and Validate**
- After making changes, ask the affected user to retry their login.
- Monitor the logs for any recurrence of the error.

#### Additional Notes or Considerations
- Ensure that the session controls you wish to apply are compatible with the authentication methods used by your users.
- Consider creating an internal documentation or FAQ for users regarding authentication methods and their implications.

#### Documentation for Guidance
- [Azure Active Directory Conditional Access](https://docs.microsoft.com/en-us/azure/active-directory/conditional-access/)
- [Understand authentication methods in Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/authentication/authentication-methods)
- [Session control in Conditional Access](https://docs.microsoft.com/en-us/azure/active-directory/conditional-access/concepts/session-control)

#### Advice for Data Collection
- **Event Viewer Logs:**
  - Check for any authentication-related logs in the Event Viewer under `Windows Logs > Security`.
- **Network Trace:**
  - Use tools like Microsoft Network Monitor or Wireshark to capture and analyze network traffic when the error occurs; this helps track any underlying issues with communication between the client and Azure AD.
- **Fiddler:**
  - Use Fiddler to inspect HTTP requests and responses. Look for any failed requests with error details that might give more insight into what part of the session control failed.

Collecting this data will aid in pinpointing the specific cause and help when seeking further technical support if necessary.