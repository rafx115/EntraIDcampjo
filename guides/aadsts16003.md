# AADSTS16003: SsoUserAccountNotFoundInResourceTenant - Indicates that the user hasn't been explicitly added to the tenant.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS16003 Error

**Error Code:** AADSTS16003  
**Description:** SsoUserAccountNotFoundInResourceTenant - Indicates that the user hasn't been explicitly added to the tenant.

---

### Initial Diagnostic Steps

1. **Identify User and Tenant Information:**
   - Confirm the identity of the user who encountered the error.
   - Identify which Azure Active Directory (AAD) tenant the user is trying to access.

2. **Review Error Context:**
   - Determine if the error occurred during a single sign-on (SSO) process, and if so, check the specific application and endpoint being accessed.

3. **Check Federation and SSO Settings:**
   - Confirm if federated authentication or third-party identity providers are involved.

4. **User Credentials Verification:**
   - Verify the user's login credentials and ensure they are using the correct account.

---

### Common Issues That Cause This Error

1. **User Not Added to the Tenant:**
   - The most common cause is that the user's account does not exist in the target Azure AD tenant.

2. **Incorrect Domain:**
   - Users may be attempting to log in using a domain that is not linked to the resource tenant.

3. **Licensing Issues:**
   - If the application requires specific licenses, ensure the user has the necessary licenses assigned.

4. **Inactive or Disabled Accounts:**
   - The user may have an inactive or disabled account in the tenant.

5. **Timing Issues:**
   - New users may need some time for account synchronization if the account was recently created.

---

### Step-by-Step Resolution Strategies

**Step 1: Verify User Existence in Tenant**
- Go to the Azure Portal:
  - Navigate to **Azure Active Directory** > **Users**.
  - Search for the user by their email address or user principal name.
  - If the user is not listed, they need to be added to the tenant.

**Step 2: Add User to Tenant**
- If the user is not found:
  - In the **Users** section, click **New User**.
  - Fill in the user details, ensuring to set the correct roles and permissions.
  - Click **Create**.

**Step 3: Check User Domain**
- Ensure the domain associated with the user's account is verified and added to the AAD tenant:
  - Go to **Azure Active Directory** > **Custom domain names**.
  - Verify that the user's email domain is listed and verified.

**Step 4: Review Service Principal and App Registration**
- Verify the application/service principal associated with the user's login and ensure it's correctly configured:
  - Go to **Azure Active Directory** > **App registrations**.
  - Check that the application is registered in the tenant and review its permissions.

**Step 5: Log Review and Analyze**
- Check Azure Active Directory sign-in logs:
  - Go to **Azure Active Directory** > **Sign-ins**.
  - Look for the sign-in attempt issued by the user to find additional error details.

---

### Additional Notes or Considerations

- Make sure multi-factor authentication (MFA) policies are not affecting access for the user.
- Check if there are any conditional access policies that could be blocking the user's access.
- New accounts may need time for propagation, especially in larger organizations where synchronization delays occur.

---

### Documentation for Guidance

- Microsoft Documentation on [Azure Active Directory User Management](https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/add-users-azure-active-directory)
- Overview of [Azure Active Directory Authentication Error Codes](https://docs.microsoft.com/en-us/azure/active-directory/develop/reference-aadsts-error-codes)
- Understanding [How to troubleshoot single sign-on](https://docs.microsoft.com/en-us/azure/active-directory/hybrid/tshoot-sso)

---

### Advice for Data Collection

If the issue persists, consider gathering logs for deeper troubleshooting:

1. **Event Viewer:**
   - Check local Windows Event Viewer for application logs related to the error (Application and System logs).

2. **Network Trace (nettrace):**
   - Use `netsh trace start capture` command or equivalent to capture network packets during the sign-in attempt.

3. **Fiddler:**
   - Use Fiddler to inspect HTTP(S) requests to Azure services. Set it up to decrypt HTTPS, and analyze the traffic for authorization headers and error messages.

Collecting this data can provide further insights into the underlying issue and assist in troubleshooting effectively.

---

Utilizing these strategies will help you systematically address the AADSTS16003 error and facilitate appropriate access for users within your Azure Active Directory tenant.