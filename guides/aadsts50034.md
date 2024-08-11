# AADSTS50034: UserAccountNotFound - To sign into this application, the account must be added to the directory. This error can occur because the user mis-typed their username, or isn't in the tenant. An application might have chosen the wrong tenant to sign into, and the currently logged in user was prevented from doing so since they did not exist in your tenant. If this user should be able to log in, add them as a guest. See docs here:Add B2B users.


## Troubleshooting Steps
Certainly! Here is a comprehensive troubleshooting guide for the error code AADSTS50034 - UserAccountNotFound.

### Troubleshooting Guide for AADSTS50034

#### Initial Diagnostic Steps
1. **Verify User Credentials**:
   - Ensure that the user is entering the correct username (email address) and password. 
   - Confirm that there are no typos.

2. **Check the Application Configuration**:
   - Verify that the application is configured to point to the correct Azure Active Directory (Azure AD) tenant.
   - Confirm that the correct redirect URI is set for the application.

3. **User Existence**:
   - Check if the user exists in Azure AD. You can do this by searching for the user in the Azure portal:
     - Go to `Azure Active Directory` > `Users`.

4. **Consult Tenant Configuration**:
   - Ensure that the signed-in user is attempting to access the correct tenant. If the user has multiple accounts, they may be logged into a different tenant.

#### Common Issues That Cause This Error
- **User Not in Tenant**: The user�s account does not exist in the Azure AD tenant associated with the application.
- **Mis-typed Email**: The user might have entered an incorrect email address or username.
- **Application Misconfiguration**: The application might be configured to use the wrong tenant.
- **Tenant Restrictions**: The tenant may restrict the sign-in for users who are not part of the directory.

#### Step-by-Step Resolution Strategies
1. **Correct User Input**:
   - Confirm username and password. Suggest users to check for typing errors.

2. **Add User to Tenant**:
   - If the user is not listed in the Azure AD:
     - Log into the Azure portal.
     - Navigate to `Azure Active Directory` > `Users` > `+ New guest user`.
     - Fill in the email address of the user and send an invitation.

3. **Check Application Permissions**:
   - Ensure that the application has the necessary permissions granted in Azure AD:
     - Go to `Azure Active Directory` > `App registrations` > Select your application > `API permissions`.
     - Ensure the permissions required for the application are granted and not set to 'Pending'.

4. **Check Authentication Method**:
   - Confirm the authentication methods and policies configured for the tenant by navigating to Azure Active Directory > Security > Authentication methods.

5. **Tenant Configuration Verification**:
   - Ensure the tenant that hosts the application corresponds with the directory the user is trying to access. 

#### Additional Notes or Considerations
- **Guest User Limitations**: Be aware that guest accounts have certain limitations in Azure AD, such as the inability to access all resources depending on settings configured by the administrator.
- **User License Requirement**: In some cases, if your Azure AD tenant requires licenses for specific services, make sure the user has the necessary licenses assigned.

#### Documentation
- **Microsoft Documentation**: 
    - [Add B2B users](https://docs.microsoft.com/en-us/azure/active-directory/external-identities/what-is-b2b)
    - [Microsoft Identity Platform documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/)
    
*Ensure to test that the documentation is accessible by clicking the links to make certain that the resources are available.*

#### Advice for Data Collection
1. **Gather User Information**:
   - Collect the exact user email or username attempting to sign in.
   - Note the error message details for specific troubleshooting.

2. **Application Logs**:
   - Check application logs to identify any patterns or additional error details that might be associated with sign-in attempts.

3. **Directory Audit Logs**:
   - Review the Azure AD audit logs to see if there were any recent changes to the user account or the application settings that might explain the error.

By following the guide above, you should be able to systematically identify and resolve issues leading to the error code AADSTS50034.