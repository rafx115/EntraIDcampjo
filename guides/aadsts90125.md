# AADSTS90125: DebugModeEnrollTenantNotFound - The user isn't in the system. Make sure you entered the user name correctly.


## Troubleshooting Steps
When encountering the error code AADSTS90125 with the description DebugModeEnrollTenantNotFound, it indicates that the user is not found in the system. This error usually occurs during authentication processes in Azure Active Directory (Azure AD) or other Microsoft services. Here is a detailed troubleshooting guide to help resolve this issue:

### Initial Diagnostic Steps:
1. **Verify User Information**: Check if the user name entered is correct and matches the user's actual account information.
  
2. **User Existence Confirmation**: Ensure that the user exists in the system and is active.

3. **Check Permissions**: Verify that the user has the necessary permissions and access rights based on the application or service they are trying to access.

### Common Issues causing this error:
1. **Typographical Errors**: Incorrectly entering the user name can trigger this error.
  
2. **Disabled User Account**: The user account may be disabled or blocked for some reason.

3. **User Not Added**: If the user has not been correctly added to the system or directory, this error may occur.

### Step-by-step resolution strategies:
1. **Check User Information**:
   - Correctly enter the user name and re-verify the spelling to ensure accuracy.

2. **Verify User Account Status**:
   - Check if the user account is active and not disabled. You can do this by a system administrator or through Azure AD portal.

3. **Re-Enroll User**:
   - If the user is not found, re-enroll them into the system with the correct details.

4. **Review Permissions**:
   - Ensure the user has the necessary permissions to access the application or service. Adjust permissions accordingly.

### Additional Notes or Considerations:
- **Permissions and Roles**: Ensure that users have been assigned the correct permissions and roles within the Azure AD setup.
- **Logging and Monitoring**: Maintaining logs and monitoring user activities can help identify potential issues that lead to user not found errors.

### Documentation for further guidance:
- Azure Active Directory documentation: [Microsoft Docs - Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/)
- Troubleshooting Azure AD Errors: [Azure AD Troubleshooting](https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-fundamentals-errors)

By following these steps and guidelines, you should be able to troubleshoot and resolve the AADSTS90125 error with the DebugModeEnrollTenantNotFound description effectively.