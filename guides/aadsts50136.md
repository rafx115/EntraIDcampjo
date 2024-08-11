
# AADSTS50136: RedirectMsaSessionToApp - Single MSA session detected.


## Troubleshooting Steps
**Troubleshooting Guide for AADSTS50136 Error Code**

**Description**: RedirectMsaSessionToApp - Single MSA session detected.

**Initial Diagnostic Steps**:
1. Verify the error code AADSTS50136 and the specific error description.
2. Check if users are experiencing login issues.
3. Determine the affected application or service.
4. Review the user's authentication logs for more details.

**Common Issues Causing this Error**:
1. Microsoft account (MSA) single session conflict.
2. Incorrect authentication settings in the application configuration.
3. User's account has issues or is not properly linked to Microsoft account services.
4. MSA session conflict due to multiple logins on different devices.

**Step-by-Step Resolution Strategies**:
1. **Force Sign-Out from Microsoft Account**:
    - Instruct the affected user to sign out from all Microsoft account sessions.
    - Have the user try to login again to see if the issue persists.

2. **Check Application Configuration**:
    - Review the authentication settings in the application portal.
    - Ensure that the correct identity provider (Microsoft account) is configured.
    - Verify if there are any conflicting settings causing the error.

3. **Clear Browser Cache and Cookies**:
    - Instruct the user to clear their browser cache and cookies.
    - Ask them to try logging in again after clearing the cache.

4. **Reconnect Microsoft Account Services**:
    - Have the user navigate to their Microsoft account settings.
    - Check if there are any issues with the linked accounts or services.
    - Reconnect any necessary services to ensure proper authentication.

5. **Contact Microsoft Support**:
    - If the issue persists, it may require further investigation by Microsoft support.
    - Provide them with detailed information about the error code and steps taken for troubleshooting.

**Additional Notes or Considerations**:
- This error code typically indicates a conflict with single Microsoft account sessions.
- Educate users on the importance of managing their account sessions to prevent such errors.
- Monitor for any recurring instances of the error to identify potential systemic issues.

**Documentation for Guidance**:
- Microsoft Azure Active Directory documentation provides detailed guidance on troubleshooting various authentication errors including AADSTS50136.
- Refer to the Microsoft Azure portal documentation or support resources for detailed steps and best practices.

Following these troubleshooting steps should help resolve the AADSTS50136 error code related to RedirectMsaSessionToApp. If the issue persists, involving the support team or referring to official documentation can provide further assistance.