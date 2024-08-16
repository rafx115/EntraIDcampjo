# AADSTS50034: UserAccountNotFound - To sign into this application, the account must be added to the directory. This error can occur because the user mis-typed their username, or isn't in the tenant. An application might have chosen the wrong tenant to sign into, and the currently logged in user was prevented from doing so since they did not exist in your tenant. If this user should be able to log in, add them as a guest. See docs here:Add B2B users.


## Troubleshooting Steps
Sure! Below is a detailed troubleshooting guide specifically for the AADSTS50034 error code, along with diagnostics, common issues, and resolution strategies.

### AADSTS50034 Troubleshooting Guide

#### Initial Diagnostic Steps
1. **Confirm Account Details:**
   - Verify that the user’s email or username is correct. A simple typo can lead to this error.

2. **Check Tenant Configuration:**
   - Determine whether the user is part of the Azure Active Directory (AAD) tenant that hosts the application. If not, they may need to be invited as a guest user.

3. **Identify the Application:**
   - Ensure you are working with the correct application. Applications can be registered in multiple tenants, and the user account must be present in the same tenant that the application is trying to authenticate against.

4. **Logs and Event Viewer:**
   - Check logs in Azure AD for sign-in attempts. Go to the Azure portal, navigate to Azure Active Directory > Sign-ins, and look for any failed sign-in attempts associated with that user.

#### Common Issues Causing AADSTS50034
1. **User Not in Tenant:**
   - The user account is not registered in the Azure AD tenant that the application is trying to access.

2. **Application Configuration:**
   - The application is misconfigured and is trying to authenticate against the wrong tenant.

3. **Licensing Issues:**
   - The user might require a specific license to access the application.

4. **Multiple Tenants:**
   - If the user has accounts in multiple tenants, they may be attempting to log into the incorrect tenant.

5. **Mis-typed Username:**
   - The user may have entered their username or email incorrectly.

#### Step-by-Step Resolution Strategies
1. **Verify User Existence in Directory:**
   - Navigate to the Azure portal and check if the user is listed under Azure Active Directory > Users.
   - If the user is not listed, proceed to add them as a guest user.

2. **Add the User as a B2B Guest:**
   - Go to Azure Active Directory > Users > New guest user.
   - Fill in the user information (email address, optional personal message, etc.) and select "Invite".

3. **Check Application Registration:**
   - Ensure the application is correctly registered in the directory and that the API permissions are configured properly.
   - Go to Azure Active Directory > App registrations and check the application in question.

4. **Check User’s Email Domain:**
   - Verify if the user's email domain is allowed within the tenant's domain settings.

5. **Reconfirm Login URL:**
   - Ensure that the login URL being used points to the correct AAD tenant. This means checking that the sign-in URL is using the correct tenant identifier.

6. **Attempt User Sign-in:**
   - After adding the user, ask them to sign-in again to confirm that they no longer see the AADSTS50034 error.

#### Additional Notes or Considerations
- **External Identities:**
  If the application is intended for external users, ensure that external identities are enabled on the Azure AD tenant.

- **Conditional Access Policies:**
  Check if there are any conditional access policies that might be affecting guest users’ access.

- **Sign-in Activity:**
  Regularly monitor sign-in activities to identify patterns or repeated issues concerning user sign-ins.

#### Documentation for Guidance
- [Add B2B users](https://docs.microsoft.com/en-us/azure/active-directory/external-identities/what-is-b2b)
- [Azure Active Directory User Management Documentation](https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/add-users-azure-active-directory)
- [Troubleshoot Sign-in Issues](https://docs.microsoft.com/en-us/azure/active-directory/authentication/troubleshoot-sign-in-issues)

#### Advice for Data Collection
- **Event Viewer Logs:**
  - Review the application’s logs and any relevant event viewer logs on the client machine to identify errors connected to authentication.

- **Network Traces:**
  - Utilize tools like Fiddler or NetTrace to capture and analyze the authentication requests and responses for further insights into potential issues.

- **Azure AD Logs:**
  - Collect logs from the Azure AD sign-in events to monitor user activities and pinpoint anomalies.

By following this troubleshooting guide, you should be able to effectively resolve the AADSTS50034 error and assist users in accessing their required applications.