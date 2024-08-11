
# AADSTS90125: DebugModeEnrollTenantNotFound - The user isn't in the system. Make sure you entered the user name correctly.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS90125: DebugModeEnrollTenantNotFound

**Error Description**:  
The user isn't in the system. Make sure you entered the username correctly.

---

### Initial Diagnostic Steps

1. **Verify User Input**:
   - Double-check the username input for typos, incorrect characters, or formatting errors.
   - Ensure that the domain is included if applicable (e.g., user@domain.com).

2. **Previous Authentication Attempts**:
   - Check if the user has previously tried to authenticate and encountered issues. Confirm if the error persists.

3. **Service Status**:
   - Confirm that Azure Active Directory (AAD) services are operational by visiting the Azure status page: [Azure Status](https://status.azure.com/en-us/status).

---

### Common Issues That Cause This Error

1. **User Does Not Exist**: The user trying to log in is not registered in the Azure Active Directory (AAD).

2. **Wrong Tenant**: The user may be trying to access a tenant where they are not listed. The input must match the correct tenant domain.

3. **Deleted or Disabled Account**: The account may have been deleted or disabled in Azure Active Directory.

4. **Licensing Issues**: The user must have an appropriate license assigned to access specific resources.

5. **Synchronization Issues**: For organizations using Azure AD Connect, there may be issues with synchronization between on-premises Active Directory and Azure AD.

---

### Step-by-Step Resolution Strategies

#### Step 1: Verify User Existence

- **Azure Portal**: 
  1. Log in to the Azure Portal as an admin.
  2. Navigate to **Azure Active Directory** > **Users**.
  3. Search for the user by their username or email.

- If the user does not exist:
  - Add the user to the directory if they need access.

#### Step 2: Check User Status

- If the user exists but cannot log in:
  1. Check if the account is enabled or disabled.
  2. Verify that the user's license is set up correctly under **Users** > **User licenses**.

#### Step 3: Tenant Check

- Ensure that the user is attempting to log in to the correct tenant.
  - Confirm the user’s tenant through their user details in the Azure Portal or contact the user directly.

#### Step 4: Re-synchronize (If Applicable)

- If using Azure AD Connect:
  - Ensure synchronization status is healthy. Check for recent errors and mend any issues.
  - Force a sync if necessary.

#### Step 5: Troubleshooting Details

- Review the Azure AD sign-in logs:
  1. Navigate to **Azure Active Directory** > **Sign-ins**.
  2. Filter for entries related to the user and check for additional error details.

---

### Additional Notes or Considerations

- **Multi-Factor Authentication**: Ensure that multi-factor authentication is not the problem by checking if the user’s settings are configured properly.
  
- **Account Type**: Ensure the account type (e.g., personal Microsoft accounts vs. organization accounts) matches the requirements for signing into the application or service.

---

### Documentation for Guidance

- Azure AD User Management: [Manage Users in Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/user-help/usersignin-howto)
- Azure AD Connect: [Azure AD Connect Documentation](https://docs.microsoft.com/en-us/azure/active-directory/hybrid/concepts/active-directory-aadconnect)
- Troubleshoot Sign-in Issues: [Troubleshoot Sign-ins with Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/user-help/user-sign-in-troubleshoot)

**Testable Documentation Link**:  
You can verify reachability of the documentation and resources by clicking the links mentioned above.

---

### Advice for Data Collection

- Collect the following information prior to reaching out for support or further assistance:
  - Exact username being used.
  - Timestamp of the failed sign-in attempt.
  - Error messages or codes displayed during the error.
  - User account status from the Azure Portal.
  - Any recent changes made to the user account or Azure AD settings.

By following this guide, you should be able to diagnose and resolve the AADSTS90125 error effectively. If issues persist, consider reaching out to your Azure support team for additional assistance.