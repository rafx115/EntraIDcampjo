
# AADSTS50144: InvalidPasswordExpiredOnPremPassword - User's Active Directory password has expired. Generate a new password for the user or have the user use the self-service reset tool to reset their password.


## Troubleshooting Steps
Troubleshooting Guide for Error Code AADSTS50144: InvalidPasswordExpiredOnPremPassword

**Initial Diagnostic Steps:**
1. Confirm the specific error message: "InvalidPasswordExpiredOnPremPassword - User's Active Directory password has expired."
2. Verify the user impacted by this issue and determine if the password has indeed expired.
3. Check if the user has previously been notified about password expiration or if there are any relevant alerts or logs in the system.

**Common Issues that Cause this Error:**
1. User neglects to change password despite multiple notifications.
2. User is unaware of password expiration policies.
3. Server-side synchronization issues between on-premises Active Directory and Azure AD.
4. Incorrect configuration settings that do not trigger password expiration notifications.

**Step-by-Step Resolution Strategies:**
1. Inform the user: Notify the affected user that their Active Directory password has expired and needs to be reset.
2. Generate a new password: Admins can generate a new password for the user in Active Directory and communicate the new credentials securely.
3. Password reset tool: Instruct the user to use the self-service password reset tool if available to reset their password.
4. Verify synchronization: Ensure that synchronization between on-premises Active Directory and Azure AD is functioning correctly to prevent future occurrences.
5. Update policies: Review password expiration policies and user notifications to enhance users' awareness and compliance with password renewal requirements.

**Additional Notes or Considerations:**
- Encourage users to create strong and unique passwords to enhance security.
- Provide users with resources on how to change and manage their passwords securely.
- Regularly monitor password expiration status and promptly address any issues that arise.

**Documentation:**
- Microsoft Azure Active Directory documentation provides detailed steps and best practices for managing user passwords, including password expiration policies and self-service password reset tools. You can refer to the official documentation for guidance on resolving password-related issues: [Azure Active Directory Documentation - Managing User Passwords](https://docs.microsoft.com/en-us/azure/active-directory/authentication/concept-sspr-manage)