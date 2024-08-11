
# AADSTS90092: GraphNonRetryableError


## Troubleshooting Steps
## Troubleshooting Guide for AADSTS90092: GraphNonRetryableError

AADSTS90092 is an error code indicating a *GraphNonRetryableError*, suggesting that there is a non-retryable problem with the request to Microsoft Graph API or Azure Active Directory (AAD). This error typically occurs due to misconfigurations, permissions issues, or resource states that can't be recovered without manual intervention.

### Initial Diagnostic Steps
1. **Check Error Message Details**: Review the full error message for specific details that may indicate the source of the issue.
2. **Identify Context**: Determine the context in which the error occurred:
   - When was it first reported?
   - What action was being performed (i.e., signing in, accessing a resource, etc.)?
   - Which application or user was attempting the action?

3. **Verify Service Status**: Check the Azure status page for any ongoing outages or incidents that might be affecting AAD or Microsoft Graph:
   - [Azure Status Page](https://status.azure.com)

### Common Issues That Cause This Error
1. **Insufficient Permissions**: The application or user does not have the necessary permissions to access the requested resource.
2. **Invalid Token**: The access token might be invalid, expired, or incorrectly scoped.
3. **Resource Not Found**: The resource being accessed may not exist or is not accessible by the requesting party.
4. **Model or Policy Issues**: Issues related to the application's registration or policies such as Conditional Access, consent issues, or compliance policies.
5. **Account Issues**: Problems with the user's account, such as being disabled or not having the required licenses assigned.

### Step-by-Step Resolution Strategies
1. **Check Permissions**:
   - Review the application's permissions in Azure AD.
   - Ensure that all required permissions are granted and consented.
   - Use the Azure portal to view the API permissions and check for any warning signs.
   - Request admin consent if permissions require it.

2. **Validate Access Token**:
   - Use tools like [jwt.ms](https://jwt.ms) to decode your JWT (JSON Web Token).
   - Check if the token has expired or if it contains the correct scopes for the operation.

3. **Verify Resource Existence**:
   - Ensure that the resource you are trying to access exists in the directory (such as a user, group, or application).
   - Validate the URL or identifier being used in the Graph API request.

4. **Review Application Registration**:
   - Go to the Azure portal and navigate to Azure Active Directory > App registrations.
   - Check for any issues in the registration, such as misconfigured redirect URIs or implicit flow settings.

5. **Examine Conditional Access Policies**:
   - Check if there are any Conditional Access policies being applied to the user or application that may deny access.
   - Ensure that the user meets all policy requirements.

6. **User Account Health**:
   - Check the user's account status in Azure AD to ensure it is enabled, has the necessary licenses, and is in good standing.

### Additional Notes or Considerations
- Non-retryable errors like AADSTS90092 often indicate a need for manual code adjustments, user remediation, or changes to application settings.
- Test the changes in a non-production environment when possible to avoid disrupting user access.

### Documentation and Resources
- [Microsoft Identity platform documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/)
- [Microsoft Graph documentation](https://docs.microsoft.com/en-us/graph/)
- [Understanding Azure Active Directory Error Codes](https://docs.microsoft.com/en-us/azure/active-directory/develop/reference-aad-error-codes)

### Test Documentation Accessibility
- Ensure that the documentation links provided are accessible and functioning:
  - Open [Microsoft Identity platform documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/) to verify.
  - Open [Microsoft Graph documentation](https://docs.microsoft.com/en-us/graph/) to verify.

### Advice for Data Collection
- **Gather Logs**: Collect application logs, Azure AD sign-in logs, and any error codes or messages returned by the API.
- **User Feedback**: Ask affected users for details such as what they were doing when the error occurred, including links to specific resources.
- **Reproduce the Issue**: If possible, try to replicate the error with a test user and application to gather more context around what is triggering the error.

By following this troubleshooting guide, you should be better equipped to diagnose and resolve issues associated with the AADSTS90092 error.