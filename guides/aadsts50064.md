# AADSTS50064: CredentialAuthenticationError - Credential validation on username or password has failed.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS50064 Error

The error code **AADSTS50064** typically indicates that there was a failure in validating an account's username or password during credential authentication via Azure Active Directory (AAD). This can happen for several reasons, including incorrect credentials, account lockouts, or issues with the identity provider configuration.

#### Initial Diagnostic Steps

1. **Verify the Username and Password:**
   - Ensure that the username and password entered are correct. Pay attention to case sensitivity.
   - If the username contains an email format (user@domain.com), ensure that it is entered correctly.

2. **Account Status Check:**
   - Verify if the account is active and not locked out or disabled in Azure AD.
   - Check for any password expiration or reset policies that may apply to the account.

3. **Multi-Factor Authentication (MFA):**
   - If MFA is enabled, ensure that any required second-factor authentication step is completed.

4. **Service Health:**
   - Check the Azure Service Health Dashboard to see if there are any ongoing incidents or outages that may affect authentication services.

#### Common Issues that Cause AADSTS50064

1. **Incorrect Credentials:**
   - Users often enter their credentials incorrectly. Confirm the correct login credentials outside of the application where the error is occurring.

2. **Account Lockout:**
   - If a user has been locked out due to multiple failed sign-in attempts, they may encounter this error.

3. **Password Expiry:**
   - The user's password may have expired, requiring a reset.

4. **Unregistered Device:**
   - If the sign-in is from an unregistered device that needs to be registered with Azure AD.

5. **Configuration Issues:**
   - Problems with the application registration in Azure AD, such as incorrect redirect URIs or API permissions not granted.

#### Step-by-Step Resolution Strategies

1. **Confirm Credentials:**
   - Log in directly to the Azure portal or corresponding service to validate credentials.

2. **Reset Password:**
   - If credentials are not working, consider resetting the password using the self-service password reset option (if enabled).

3. **Check Account State:**
   - Use Azure Active Directory admin center or PowerShell to verify the account status:
     ```powershell
     Get-AzureADUser -ObjectId <userId> | Select-Object AccountEnabled
     ```

4. **Verify Account Lockout:**
   - Reset the account lockout through the Azure AD portal if applicable.

5. **Review User Settings:**
   - Check user settings for MFA requirements and ensure the MFA methods are accessible from the user's device.

6. **Application Configuration Review:**
   - Ensure the application is registered correctly:
     - Check application ID and redirect URIs in Azure AD.
     - Confirm required API permissions are granted and admin consent is obtained.

7. **Audit Logs:**
   - Review the Azure AD sign-in logs to gather more information about the error. This may give clues about the nature of the authentication failure.

#### Additional Notes or Considerations

- Different applications integrated with Azure AD may have varied authentication work flows (e.g., native apps vs. web apps). Ensure you adapt practices based on specific requirements.
- Educate users on the importance of password management and MFA to avoid common pitfalls.

#### Documentation for Guidance

- Azure AD Sign-in errors documentation (Microsoft):
  - [Azure AD Sign-in Errors](https://docs.microsoft.com/en-us/azure/active-directory/human-resources/active-directory-sign-in-errors)

- Self-service password reset:
  - [Self-service Password Reset Overview](https://docs.microsoft.com/en-us/azure/active-directory/authentication/howto-sspr-user)

- Manage user accounts in Azure AD:
  - [Manage Users in Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-users)

#### Advice for Data Collection (Event Viewer Logs, NetTrace, Fiddler)

- **Event Viewer Logs:**
  - Check the Application Logs under Windows Logs for errors related to your application. Look for event IDs (e.g., 4625 for failed logon attempts) that correlate with the time of the issue.

- **NetTrace:**
  - Use `nettrace` to capture network traffic during the authentication process. Analyze the trace file for failed requests to Azure AD.

- **Fiddler:**
  - Capture HTTP(s) traffic with [Fiddler](https://www.telerik.com/fiddler), which can expose failed requests and their responses. Look for HTTP status codes related to the AADSTS error.

By following this structured approach, you should be able to pinpoint the cause of the AADSTS50064 error and implement the appropriate resolution.