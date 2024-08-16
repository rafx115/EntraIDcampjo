# AADSTS90125: DebugModeEnrollTenantNotFound - The user isn't in the system. Make sure you entered the user name correctly.


## Troubleshooting Steps
Certainly! Here's a detailed troubleshooting guide for the error code AADSTS90125 with its accompanying description "DebugModeEnrollTenantNotFound - The user isn't in the system. Make sure you entered the user name correctly."

### Troubleshooting Guide for AADSTS90125

#### 1. Initial Diagnostic Steps
   - **Verify User Input**: Double-check the user account being used. Ensure there are no typos in the email address or username.
   - **Check Online Status**: Confirm that the Azure Active Directory service is online and functioning correctly by checking the [Azure status page](https://status.azure.com/en-us/status).
   - **Check User Existence**:
     - Log into the Azure portal and navigate to Azure Active Directory > Users. Confirm that the user exists in the directory.
   - **Confirm Tenant ID**: Ensure that you are in the correct Azure AD tenant for that user. The user must be added to the appropriate tenant in which you're trying to authenticate.

#### 2. Common Issues that Cause this Error
   - **Incorrect Tenant**: You might be trying to authenticate against the wrong Azure Active Directory (AAD) tenant where the user does not exist.
   - **User Not Registered**: The user may not be registered in the Azure AD directory or has been deleted.
   - **Misconfigured Application**: The application trying to authenticate may not have permissions set correctly in AAD.
   - **User License Issues**: The user's license may have expired, which could affect their account status.

#### 3. Step-by-Step Resolution Strategies
   - **Step 1: Verify User Account**
     1. Go to Azure Portal.
     2. Navigate to "Azure Active Directory" > "Users".
     3. Search for the user's login or email. If not found, they will need to be invited or registered.
   
   - **Step 2: Check User Status**
     - If the user exists, check if the account is enabled and not locked.
     - Ensure that the user is assigned to the proper roles and scopes necessary for the application.

   - **Step 3: Check Tenant Settings**
     1. In the Azure Portal, navigate to "Azure Active Directory".
     2. Verify the directory (tenant) settings to ensure that the user belongs to the needed directory.

   - **Step 4: Application Registration Checks**
     1. In the Azure Portal, go to "Azure Active Directory" > "App registrations".
     2. Find the application attempting the authentication and ensure it is set up correctly (permissions and API permissions).
     3. Verify that the user has access to this application within the Tenant.
  
   - **Step 5: Update Application Settings**: If changes are made to the user account or the application permissions, attempt to authenticate again.
  
   - **Step 6: Re-Invite Users**: If the user does not exist, you may need to invite them if they are external (B2B) users.

#### 4. Additional Notes or Considerations
   - Ensure that you’re working in the right Azure region, as tenant settings can sometimes vary across different regions.
   - If the issue persists after making changes, wait a few minutes as changes may take some time to propagate.
   - For users from organizations with stricter security policies, contact their IT department to verify that they are allowed to use the application.

#### 5. Documentation for Further Guidance
   - [Azure Active Directory Documentation](https://docs.microsoft.com/en-us/azure/active-directory/)
   - [Manage users in Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/users)
   - [App Registration in Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)

#### 6. Advice for Data Collection
   - **Event Viewer Logs**:
     - Apply filters for credential use or AAD login failures. Look under Application and Services Logs > Microsoft > Windows > AAD.
  
   - **Nettrace**:
     - Use tools like `netsh trace start capture` to capture logs during the login attempts. Process with `netsh trace stop` after capturing.
  
   - **Fiddler**: 
     - Use Fiddler to capture HTTP requests during the authentication process. This can help identify issues with redirects or error responses.
     - Make sure to set up Fiddler to decrypt HTTPS traffic for better visibility into requests made to AAD.

This troubleshooting guide should help you identify and resolve the AADSTS90125 error efficiently.