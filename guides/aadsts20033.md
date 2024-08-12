
# AADSTS20033: FedMetadataInvalidTenantName - There's an issue with your federated Identity Provider. Contact your IDP to resolve this issue.


## Troubleshooting Steps
Certainly! The error code AADSTS20033 indicates that there’s an issue with a federated Identity Provider, specifically that the tenant name in the federation metadata is invalid. Here's a comprehensive troubleshooting guide to help resolve this error.

### Troubleshooting Guide for AADSTS20033

#### Initial Diagnostic Steps
1. **Understand the Environment**: Confirm whether the issue is occurring for a single user or multiple users. Knowing this helps in determining whether the problem is user-specific or tenant-wide.
2. **Review the Error Message**: Ensure you have the exact error message, including the AADSTS error code and any accompanying details.
3. **Reproduce the Issue**: Attempt to reproduce the error, taking notes on the steps taken and the conditions under which the issue arises.

#### Common Issues That Cause This Error
1. **Incorrect Federation Metadata**: The metadata document of the federated identity provider may contain an incorrect tenant name.
2. **Expired or Invalid Certificates**: If certificates used for signing tokens are expired or invalid, it can lead to federation failures.
3. **Tenant Name Mismatch**: The tenant name specified in the federation metadata may not match the actual tenant in Azure Active Directory (Azure AD).
4. **Misconfigured Identity Provider Settings**: Configuration settings related to the Identity Provider might be incorrect or not updated.
5. **Network Issues**: Firewalls or similar network issues could prevent access to the identity provider’s federation metadata.

#### Step-by-Step Resolution Strategies
1. **Check Tenant Name**:
   - Verify the tenant name used in the federation metadata. This should match with the Azure AD tenant's name.
   - Use Azure Portal to look at the tenant settings to confirm the correct tenant name.

2. **Validate Federation Metadata**:
   - Access the federation metadata URL (e.g., `https://<your-idp>/.well-known/openid-configuration` or similar) and check for the correct tenant name.
   - Validate that the URLs and endpoints specified in the metadata are accurate.

3. **Review and Update Identity Provider Configuration**:
   - Ensure that the XML or configuration of the Identity Provider is correct. Contact your Identity Provider for verification if you suspect misconfiguration.
   - Look for any recent changes in the federation setup that might have caused discrepancies.

4. **Check Certificates**:
   - Review the certificates used for the federation. Ensure they are not expired and are properly configured in Azure AD.
   - Update or renew certificates if any issues are found.

5. **Test Network Connectivity**:
   - Use tools like `ping` or `tracert` to check connectivity to the identity provider.
   - Check for firewall rules that may be blocking access to the identity provider metadata URLs.

6. **Contact Your Identity Provider**:
   - If issues persist after checking all configurations, reach out to your Identity Provider for assistance. They can help verify that their service is correctly configured and operational.

#### Additional Notes or Considerations
- Always back up existing configurations before making changes.
- If this is a cloud application, ensure that DNS settings are updated accordingly if any infrastructure changes occurred.
- Be aware of any relevant Service Level Agreements (SLAs) or warranties on the Identity Provider's services.

#### Documentation Where Steps Can Be Found
- **Azure Active Directory Documentation**: [Azure AD Federation](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-federation).
- **Federation Metadata Documentation**: Microsoft provides extensive documentation on how to configure federation metadata.
- **Identity Provider Documentation**: Review the specific Identity Provider's documentation for instructions on configuration and troubleshooting.

#### Advice for Data Collection
If you’re still encountering issues, collect logs and additional diagnostic information:
1. **Event Viewer Logs**:
   - Check the Event Viewer on your AD FS server, looking specifically under the "Applications and Services Logs" for AD FS events.
   - Look for any warnings or errors related to token issuance or federation.

2. **Network Traces (NetTrace)**:
   - Use tools like Wireshark or built-in Windows tools to capture network packets while reproducing the issue. This can help identify connectivity problems.

3. **Fiddler**:
   - If you're using Fiddler, capture the traffic from your browser or application trying to authenticate, which can reveal any handshake or protocol-related issues.

By following the steps above, you should be able to diagnose and resolve the AADSTS20033 error effectively.