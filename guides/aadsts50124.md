
# AADSTS50124: ClaimsTransformationInvalidInputParameter - Claims Transformation contains invalid input parameter. Contact the tenant admin to update the policy.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS50124

The error code AADSTS50124 with the description "ClaimsTransformationInvalidInputParameter - Claims Transformation contains invalid input parameter. Contact the tenant admin to update the policy." indicates that there is an issue with the claims transformation configuration in Azure Active Directory (Azure AD). This can occur during user sign-in attempts, particularly when custom policies (Identity Experience Framework) are involved.

#### Initial Diagnostic Steps

1. **Review Error Context**: Determine where and when the error occurs. Is it during a specific sign-in attempt or for specific users? Gather as much context as possible.

2. **Check Azure AD Logs**: Go to the Azure AD portal and check the sign-in logs. Look for the entry corresponding to the AADSTS50124 error, which may provide additional context or details.

3. **Identify the User and Application**: Note whether the error occurs for specific users or applications, which may help isolate the problem.

4. **Examine Custom Policies**: If you are using custom policies in Azure AD B2C, review the user journey and relevant claims transformations.

#### Common Issues that Cause This Error

1. **Incorrect Claims Transformation Configuration**: The input parameters expected by the claims transformation do not match the values being provided, either from the user attributes or from the application.

2. **Missing Required Parameters**: Some claims transformations may have required parameters that must be provided, and if these are missing, the error can occur.

3. **Syntax Errors**: There may be syntax errors in the policy file (e.g., in XML files if using Identity Experience Framework).

4. **User Attributes**: The attributes being transformed may not be available in the request context; they must be provided in the claims request.

5. **Outdated Policies**: If policies have been updated, users may still be trying to access older versions or combinations of policies leading to state mismatches.

#### Step-by-Step Resolution Strategies

1. **Review Claims Transformation Configuration**:
   - Go to Azure AD B2C > Identity Experience Framework.
   - Check the policy file and identify which claims transformations are used and whether the required input parameters are specified correctly.

2. **Use the Correct Input Parameters**:
   - Ensure that the input to the claims transformation matches what is defined in your policy. Adjust the user journey to provide any required claims.

3. **Test Policies**:
   - Validate your custom policy using the Azure AD B2C Policy validation service. This will help identify syntactic or semantic errors in the policy.

4. **Check Logs in Azure AD**:
   - Navigate to Azure AD > Sign-in logs and filter by date/time or error code (AADSTS50124) to find relevant entries.
   - Investigate any additional error information or user attributes that may have been in the request.

5. **Update and Redeploy Policies**:
   - If changes are made to the policy, ensure you properly upload and apply these changes in the Azure portal.
   - Re-test the user journey after updates.

6. **Contact Tenant Admin**:
   - If you do not have permissions to view or modify claims transformations, reach out to your tenant admin for assistance.

#### Additional Notes or Considerations

- Ensure that all policies have been published correctly after any updates.
- Test with multiple users to determine if the issue is specific to certain user attributes.
- Clear browser cookies/cache in case old tokens are being cached.

#### Documentation for Guidance

- [Azure AD B2C Custom Policies Overview](https://docs.microsoft.com/en-us/azure/active-directory-b2c/custom-policy-overview)
- [Claims Transformation Documentation](https://docs.microsoft.com/en-us/azure/active-directory-b2c/claims-transformations)
- [Troubleshooting Azure AD B2C Custom Policies](https://docs.microsoft.com/en-us/azure/active-directory-b2c/faq-custom-policies)

#### Advice for Data Collection

- **Event Viewer Logs**: Check the Windows Event Viewer for any related application or service errors that might provide additional context surrounding the time of the error.
- **Network Trace**: Use tools like Fiddler or built-in browser developer tools (F12) to capture HTTP requests/responses during the authentication flow. Look specifically at the requests sent to the Azure AD endpoints and the associated responses.
- **NetTrace**: If applicable, use Microsoft’s Network Tracing tool to capture low-level network activity that could contribute to the error.

By following this guide, you should be able to identify and resolve the issue related to the AADSTS50124 error effectively.