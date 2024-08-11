# AADSTS90093: GraphUserUnauthorized - Graph returned with a forbidden error code for the request.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS90093: GraphUserUnauthorized

#### Description:
When encountering the error code AADSTS90093 with the description "GraphUserUnauthorized - Graph returned with a forbidden error code for the request," it signifies that the user is not authorized to make the requested operation using Microsoft Graph API. This issue typically relates to permission settings or policy restrictions.

#### Initial Diagnostic Steps:
1. **Verify Permissions:** Check if the user making the request has the necessary permissions to access the target resources.
   
2. **Review Policies:** Look into any relevant policies or restrictions that might be blocking the user's access.

3. **Check API Endpoint:** Ensure that the API endpoint being accessed is correct and supported by the user's permissions.

#### Common Issues:
- Insufficient permissions assigned to the user or application in Azure AD.
- Policy restrictions preventing the user from accessing the resource.
- Incorrect API endpoint or invalid request parameters.

#### Step-by-Step Resolution Strategies:

1. **Confirm User Permissions:**
   - Check the Azure AD Portal to verify that the user or application has the required permissions (e.g., Application permissions, Delegated permissions) to access the Microsoft Graph API resources.

2. **Review Policies and Restrictions:**
   - Examine any Conditional Access Policies or Access Control Policies that could be restricting the user's access.
   - Ensure there are no Intune App Protection Policies limiting the user's interactions with the requested resources.

3. **Validate API Endpoint and Parameters:**
   - Double-check the API endpoint being used in the request to ensure it is valid.
   - Verify that the request parameters are correctly formatted and match the permissions granted to the user.

4. **Test with Graph Explorer:**
   - Use the Microsoft Graph Explorer tool to simulate the request and see if the error persists. This can help isolate the issue and identify any specific permission problems.

#### Additional Notes or Considerations:
- Ensure that the user's roles and permissions have been correctly set up in Azure AD.
- Check if there are any conflicting policies that might be overriding the user's permissions.
- Regularly review access policies and permissions to align with the organization's security requirements.

#### Documentation for Further Guidance:
- [Microsoft Graph permissions reference](https://docs.microsoft.com/en-us/graph/permissions-reference)
- [Azure AD Conditional Access documentation](https://docs.microsoft.com/en-us/azure/active-directory/conditional-access/overview)
- [Microsoft Graph Explorer tool](https://developer.microsoft.com/en-us/graph/graph-explorer)

By following these troubleshooting steps and recommendations, you can address the error code AADSTS90093 and resolve the GraphUserUnauthorized issue related to Microsoft Graph API permissions.