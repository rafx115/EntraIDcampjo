# AADSTS65005: MisconfiguredApplication - The app required resource access list doesn't contain apps discoverable by the resource, or the client app has requested access to resource, which wasn't specified in its required resource access list or Graph service returned bad request or resource not found. If the app supports SAML, you might have configured the app with the wrong Identifier (Entity). To learn more, see the troubleshooting article for errorAADSTS650056.


## Troubleshooting Steps
### Error Code: AADSTS65005 - MisconfiguredApplication

#### Initial Diagnostic Steps:
1. **Confirm Error Specifics**: Gather all available information about the error, including user actions leading to the error, timestamp of occurrence, affected user accounts, attempted operations, etc.
   
2. **Check Application Configuration**: Verify the settings and configurations of the application in Azure Active Directory (AAD), specifically related to resource access permissions.

3. **Review Requested Resource**: Determine the resource that the client app is trying to access and ensure it aligns with the required resource access list.

#### Common Issues:
1. **Missing Resource Permissions**: The application might not have the necessary permissions specified in its required resource access list to access the desired resources.

2. **Incorrect Identifier Configuration**: If SAML is used, the identifier (Entity) configured for the application may be incorrect, leading to resource access issues.

3. **Bad Request/Resource Not Found**: The Azure AD Graph service might be returning errors, such as bad requests or resource not found, impacting the application's functionality.

#### Step-by-Step Resolution Strategies:
1. **Verify Application Permissions**:
   - Access Azure Portal, navigate to Azure Active Directory > App registrations.
   - Locate and select the misconfigured application.
   - Check the required resource access list and ensure it includes all necessary resources.
   - Update the permissions if required and save the changes.

2. **Review SAML Configuration (If Applicable)**:
   - If the application supports SAML, double-check the Entity configuration in the app settings.
   - Update the Identifier (Entity) to the correct value if it is found to be misconfigured.

3. **Investigate Azure AD Graph Service Issues**:
   - Check the Azure service health status to ensure there are no ongoing issues with the Azure AD Graph service.
   - Review Azure AD logs and monitor for any specific errors related to the resource access requests.

#### Additional Notes or Considerations:
- **Permission Sync Delay**: Changes in application permissions may take some time to propagate across the Azure AD system. Allow time for sync if recent modifications have been made.
  
- **Logging and Monitoring**: Enable and utilize Azure AD logs and monitoring tools to track resource access requests and any related errors for troubleshooting.

#### Documentation for Guidance:
- Microsoft Azure Documentation:
  - For specific steps and detailed guidance on troubleshooting AADSTS65005 error, refer to [Troubleshooting AADSTS65005](https://docs.microsoft.com/en-us/troubleshoot/azure/active-directory/error-code-aadsts65005). 
  - Additional information on managing Azure AD App Registrations can be found [here](https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-app-registration).
  
By following the outlined diagnostics and resolution strategies, you can effectively address the AADSTS65005 MisconfiguredApplication error for the affected application.