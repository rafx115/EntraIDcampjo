# AADSTS90081: OrgIdWsFederationMessageInvalid - An error occurred when the service tried to process a WS-Federation message. The message isn't valid.


## Troubleshooting Steps
Certainly! The error code AADSTS90081 refers to an issue with processing a WS-Federation message in an Azure Active Directory (AAD) scenario. Below is a comprehensive troubleshooting guide.

### Troubleshooting Guide for AADSTS90081

#### Initial Diagnostic Steps
1. **Confirm the Environment**: 
   - Verify if this is occurring in a test, development, or production environment.
  
2. **Identify the Federation Setup**: 
   - Check whether the organization is using WS-Federation for authentication via Active Directory Federation Services (AD FS) or another identity provider.

3. **Reproduce the Error**: 
   - Try to reproduce the error while monitoring any specific steps or configurations that may trigger it.

4. **Check Application Logs**: 
   - Examine the application’s logs for any preceding error messages or anomalies that could provide context.

5. **Inspect User Accounts**:
   - Validate whether the user accounts attempting to login are properly synchronized and have valid credentials.

#### Common Issues that Cause This Error
1. **Invalid WS-Federation Message**:
   - Malformed tokens or unexpected data within the WS-Federation message can lead to this error.

2. **Configuration Mismatch**:
   - Differences in the WS-Federation endpoint configurations between the identity provider and relying party (the application) could be problematic.

3. **Expired or Stale Tokens**:
   - Old tokens or sessions could lead to invalid messages during the authentication process.

4. **Clock Skew**:
   - Significant time differences between the servers can result in invalid timestamps in tokens.

5. **Certificate Issues**:
   - Problems with signing certificates can invalidate the WS-Federation token signature.

6. **User Principal Name Issues**:
   - Mismatches in the UPN or claims that are being sent versus what the application expects.

#### Step-by-Step Resolution Strategies
1. **Validate Configuration**:
   - Check both AD FS and the application configuration to ensure they match correctly:
     - **Endpoints**: Validate the WS-Federation endpoints.
     - **Metadata**: Ensure correct federation metadata URLs are configured.
    
2. **Check Token Signing Certificates**:
   - Ensure that the signing certificate used by AAD or the identity provider hasn’t expired and is correctly configured on both ends.
   - If the certificate has changed, make sure the updated one is published to the relying party.

3. **Inspect Event Logs**:
   - On the AD FS server:
     - Open Event Viewer and navigate to `Applications and Services Logs` -> `AD FS`.
     - Check for relevant warnings or errors that coincide with the login attempts.
  
4. **Monitor Clock Settings**:
   - Validate system times across clients, federation services, and AAD to reduce or eliminate clock skew.

5. **Re-create the Federation Trust** (if applicable):
   - As a last resort, if changes have been made or configuration issues persist, consider re-creating the federation trust between the identity provider and Azure AD.

6. **Review Claims Rules**:
   - Ensure the claim rules defined in AD FS are sending the correct claims in the expected format.

#### Additional Notes or Considerations
- **Token Types**: Ensure that the application is set up to accept the specific type of tokens issued by AD FS and verify if the token contains all the necessary claims.
- **User Permissions**: Check that users have the correct permissions and are authorized to perform actions via this authentication path.

#### Documentation for Reference
- [Azure AD Authentication Methods](https://learn.microsoft.com/en-us/azure/active-directory/develop/authentication-scenarios)
- [WS-Federation Protocol](https://learn.microsoft.com/en-us/dotnet/framework/security/ws-federation)
- [Become familiar with AD FS](https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/ad-fs-overview)
- [Troubleshoot Token Signing](https://learn.microsoft.com/en-us/azure/active-directory/develop/troubleshoot-generate-authentication-tokens)

#### Advice for Data Collection
- **Event Viewer Logs**:
  - Look for entries in the AD FS application logs that correlate with the user’s failed sign-in attempts.
  
- **Network Trace**:
  - Use tools like `nettracer` or Fiddler to capture authentication packets if needed to analyze the WS-Federation messages flowing during the attempt.

- **Analyze Fiddler Logs**:
  - Capture and inspect details in the Fiddler logs to examine the HTTP requests and responses for anomalies in the WS-Federation protocol flow.

By following these troubleshooting steps, you should be able to identify and resolve the causes of the AADSTS90081 error effectively.