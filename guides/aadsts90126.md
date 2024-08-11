
# AADSTS90126: DebugModeEnrollTenantNotInferred - The user type isn't supported on this endpoint. The system can't infer the user's tenant from the user name.


## Troubleshooting Steps
Error Code: AADSTS90126
Description: DebugModeEnrollTenantNotInferred - The user type isn't supported on this endpoint. The system can't infer the user's tenant from the user name.

**Initial Diagnostic Steps:**
1. Verify that the user is using the correct credentials (username and password).
2. Check if the user is trying to access the correct endpoint and if the endpoint supports the user type.
3. Confirm that the user is associated with a valid tenant.
4. Ensure that there are no network connectivity issues that might be affecting the authentication process.
5. Review recent changes or updates that might have caused the issue.

**Common Issues that Cause this Error:**
1. Incorrect user type trying to access a particular endpoint.
2. Tenant information not inferred correctly from the user's credentials.
3. Misconfiguration of authentication settings.
4. Network issues affecting the communication between the user, the endpoint, and the authentication service.

**Step-by-Step Resolution Strategies:**

1. **Verify User Type and Endpoint Compatibility:**
   Ensure that the user type trying to access the endpoint is supported. If not, guide the user to the appropriate endpoint based on their user type.

2. **Check Tenant Information:**
   Verify that the user's tenant information is correctly associated with their username. If not, help the user provide the correct tenant information or guide them on how to correct it.

3. **Review Authentication Settings:**
   Check the authentication settings to ensure they are properly configured. Make sure that the authentication protocols, permissions, and user roles are set up correctly.

4. **Investigate Network Connectivity:**
   Address any network issues that might be hindering the communication between the user, endpoint, and authentication service. Test network connectivity and troubleshoot any connectivity problems.

5. **Monitor Logs and Error Messages:**
   Monitor logs and error messages generated during the authentication process to identify specific issues or error patterns that could provide more insight into the root cause of the problem.

**Additional Notes or Considerations:**
- Encourage the user to clear browser cache and cookies before attempting the login again.
- If the issue persists, the user may need to contact their administrator or IT support for further assistance.
- Regularly update and maintain authentication configurations and settings to prevent similar issues in the future.

**Documentation for Guidance:**
- Microsoft Azure Active Directory documentation provides detailed information and step-by-step guides for troubleshooting authentication issues. Users can refer to the official documentation for specific error codes and resolution steps: [Azure AD error codes and messages](https://docs.microsoft.com/en-us/azure/active-directory/develop/reference-aadsts-error-codes)