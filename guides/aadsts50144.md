
# AADSTS50144: InvalidPasswordExpiredOnPremPassword - User's Active Directory password has expired. Generate a new password for the user or have the user use the self-service reset tool to reset their password.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS50144

**Error Description**: 
The AADSTS50144 error indicates that a user's Active Directory (AD) password has expired and needs to be reset. This can occur in environments that synchronize on-premises Active Directory accounts with Azure Active Directory (AAD).

---

### 1. Initial Diagnostic Steps

#### Step 1: Identify the Error
- Confirm the error code `AADSTS50144` and review the accompanying message regarding the expired password.
  
#### Step 2: User Verification
- Ensure the user affected is attempting to log in with an account that is synchronized from on-premises Active Directory.

#### Step 3: Check Password Expiration
- Review the user's account settings in the on-premises AD to verify if the password has indeed expired.

#### Step 4: Check Synchronization Status
- Use the Azure AD Connect Health portal (if applicable) to ensure that synchronization between on-prem AD and AAD is functioning properly.

---

### 2. Common Issues That Cause This Error

- User's password has expired per on-premises AD policy.
- The password is not updated in Azure AD due to synchronization issues.
- The user is trying to log in to a service that does not recognize the expired password status from on-premises AD.
- The account may be locked or disabled in AD.
  
---

### 3. Step-by-step Resolution Strategies

#### Step 1: Reset the Password
1. **For Admins**:
   - **Use Active Directory Users and Computers (ADUC)**:
     1. Open ADUC.
     2. Locate the user account.
     3. Right-click and select "Reset Password."
     4. Enter a new password and ensure the “User must change password at next logon” option is selected.

2. **For Users**:
   - **Self-Service Password Reset (SSPR)**:
     - Instruct the user to go to the SSPR portal if configured in your environment.
     - Have the user follow the prompts to reset their password.

#### Step 2: Confirm and Test
- After resetting the password, have the user attempt to log in again to the Azure service.
- Ensure the password change is reflected in Azure AD by checking Azure Active Directory > Users.

#### Step 3: Monitor Synchronization
- Make sure that Azure AD Connect is running smoothly and there are no synchronization errors.
- You can manually trigger a sync using the PowerShell command:
  ```powershell
  Start-ADSyncSyncCycle -PolicyType Delta
  ```

---

### 4. Additional Notes or Considerations

- If the user has not changed their password in a while, they may require a more comprehensive password policy.
- Ensure that users are trained to utilize self-service password reset tools to minimize future issues.
- Regularly review password expiration policies in Active Directory to avoid unexpected interruptions.

---

### 5. Documentation for Guidance

- Microsoft Documentation on [Self-Service Password Reset in Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/authentication/howto-reset-password)
- Microsoft Guidance on [Azure AD Connect](https://docs.microsoft.com/en-us/azure/active-directory/hybrid/deploy/whatis)
- Password Policy Management in [Active Directory](https://docs.microsoft.com/en-us/windows-server/security/windows-security-baselines/password-policy)

---

### 6. Advice for Data Collection (Event Viewer logs, NetTrace, Fiddler)

- **Event Viewer**:
  - Check the **Security** and **Application** logs on the Domain Controller for any authentication issues or related errors.
  - Look for event IDs related to account password changes or expirations.

- **Network Trace/NetTrace**:
  - Use tools like Wireshark or NetMon to trace the connections during the authentication attempt to monitor which requests are sent and any failures returned.

- **Fiddler**:
  - If applicable to a web application, capture requests and responses in Fiddler to view authentication attempts and any errors encountered.
  
By following this detailed troubleshooting guide, issues related to the AADSTS50144 error can be diagnosed and resolved efficiently.