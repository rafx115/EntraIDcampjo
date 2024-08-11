# AADSTS50126: InvalidUserNameOrPassword - Error validating credentials due to invalid username or password. The user didn't enter the right credentials. Expect to see some number of these errors in your logs due to users making mistakes.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS50126

#### Initial Diagnostic Steps:
1. Confirm with the user that they are entering the correct username and password.
2. Check if there are any recent changes to the user's account or the authentication system.
3. Verify if the user account is still active and not locked out.
4. Ensure there are no authentication-related network issues that could be causing the error.

#### Common Issues:
1. **Incorrect Credentials:** The user is entering the wrong username or password.
2. **Expired Password:** The user's password may have expired.
3. **Locked Account:** The account may be locked due to multiple failed login attempts.
4. **Network Connectivity:** Network issues preventing successful authentication.

#### Step-by-Step Resolution Strategies:
1. **Confirm Correct Credentials:**
   - Ask the user to double-check the username and password they are entering.
  
2. **Reset Password:**
   - If the password is expired or suspected to be incorrect, guide the user to reset their password following the provided password reset process.
  
3. **Unlock Account:**
   - If the account is locked, an administrator may need to unlock the account or guide the user on the process to unlock it.
  
4. **Check Network Connectivity:**
   - Ensure the device has a stable internet connection and there are no network issues impacting the authentication process.

#### Additional Notes:
- Encourage users to follow best practices for secure password management (e.g., creating complex passwords, not sharing passwords, enabling multi-factor authentication).
- Admins can monitor authentication logs to identify patterns or potential security threats related to failed login attempts.

#### Documentation:
- Refer to the Azure Active Directory documentation on troubleshooting common errors like AADSTS50126 for detailed guidance and steps: [Azure AD Error Codes Reference](https://docs.microsoft.com/en-us/azure/active-directory/develop/reference-aadsts-error-codes).

By following these steps and considerations, you should be able to diagnose and resolve the Error Code AADSTS50126 related to InvalidUserNameOrPassword effectively.