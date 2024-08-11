# AADSTS90099: The application '{appId}' ({appName}) has not been authorized in the tenant '{tenant}'. Applications must be authorized to access the external tenant before partner delegated administrators can use them. Provide pre-consent or execute the appropriate Partner Center API to authorize the application.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS90099:

#### Initial Diagnostic Steps:
1. Verify the exact error message and error code (AADSTS90099) you are receiving.
2. Identify the application '{appId}' and tenant '{tenant}' mentioned in the error message.
3. Check if the application '{appId}' has been granted proper permissions in the specified tenant '{tenant}'.
4. Confirm if any Partner Center API calls have been made to authorize the application.

#### Common Issues Causing Error AADSTS90099:
1. **Missing Consent**: The application '{appId}' has not been pre-consented or authorized in the tenant '{tenant}'.
2. **Lack of Permissions**: The application may not have the necessary permissions to access the external tenant.
3. **Misconfiguration**: Improper setup or configuration settings within the application.
4. **Partner Center API Not Executed**: Failure to execute the appropriate Partner Center API to authorize the application.

#### Step-by-Step Resolution Strategies:
1. **Pre-Consent the Application**:
   - Utilize Azure AD Admin Consent workflow to grant necessary permissions for the application in the tenant.
  
2. **Execute Partner Center API**:
   - Follow the documentation provided by Microsoft for executing the required Partner Center API to authorize the application in the external tenant.

3. **Verify Permissions**:
   - Ensure the application has all the required permissions to access the specified tenant.

4. **Check Application Configuration**:
   - Review the configuration of the application to ensure it aligns with the requirements for accessing the external tenant.

#### Additional Notes or Considerations:
- It's crucial to understand the permissions required by the application and ensure they are properly configured.
- Collaborate with the Azure AD Admin of the tenant '{tenant}' to grant the necessary consents or permissions.

#### Documentation for Reference:
- [Microsoft Azure Active Directory documentation](https://docs.microsoft.com/en-us/azure/active-directory/)

This troubleshooting guide should help you navigate and resolve the error code AADSTS90099 effectively. If you encounter any challenges, consider seeking assistance from Azure support or relevant forums for further guidance.