# AADSTS90085: OrgIdWsFederationSltRedemptionFailed - The service is unable to issue a token because the company object hasn't been provisioned yet.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS90085

#### Error Description
**AADSTS90085** indicates that the service is unable to issue a token because the company object associated with the request hasn’t been provisioned yet. This typically occurs during a federation or single sign-on (SSO) process where an organization has not been fully set up in Azure Active Directory (AAD).

### 1. Initial Diagnostic Steps

**Check Error Context**
- Determine the context in which the error occurs. Is it during a login attempt, API call, or during SSO configuration?
- Note the exact time, application involved, and user identifiers.

**Review Azure AD Sign-in Logs**
- Navigate to Azure AD > Sign-ins in the Azure portal.
- Check for any sign-in failures and look for additional error codes or descriptions related to the failure.

**Verify Organizational Provisioning**
- Confirm that the organization exists in Azure AD.
- Check if the necessary attributes for the organization are configured correctly.

### 2. Common Issues that Cause This Error

- **Missing Organizational Entity**: The organization (company) associated with the login might not be provisioned in Azure AD.
- **Incorrect Federation Settings**: Misconfiguration in Federated Identity Providers (e.g., ADFS).
- **User Not Properly Assigned**: The specific user trying to authenticate may not be linked to a company or tenant.
- **Domain Verification Issues**: If the domain associated with the organization is not verified in Azure AD, it can lead to this error.
- **Intended Directory Missing**: The configuration expects requests to direct to a specific (but not provisioned) tenant or directory.

### 3. Step-by-Step Resolution Strategies

#### Step 1: Verify Organization Existence
- **Azure Portal**: Check Azure AD to see if the organization exists.
- **PowerShell**: Use PowerShell commands to list tenants and domains, confirming the organization is present.

#### Step 2: Check Federation Settings
- If using ADFS for federation, ensure it is configured properly.
  - Verify AD FS claims rules and the relying party trust settings.
  - Ensure the right Endpoint URLs are in place.

#### Step 3: User and Domain Verification
- Confirm that users trying to authenticate are properly set up in Azure AD.
- Ensure any custom domains used are verified within Azure AD.

#### Step 4: Deployment of Directory Service
- If the organization is not provisioned, proceed with the provisioning process:
  - Navigate to Azure AD, and initiate the directory service provisioning.
  - Assign users or import users from on-premises Active Directory if applicable.

#### Step 5: Contact Microsoft Support
- If the issue persists after following the above steps, reach out to Microsoft support for more context as it may require deeper investigation.

### 4. Additional Notes or Considerations

- **Multi-Tenant Applications**: Ensure the application is correctly set up for multi-tenant scenarios if applicable.
- **Admin Privileges Required**: Ensure you have adequate permissions to view and modify Azure AD settings.
- **Check Latest Service Health**: Sometimes the issue can be related to a service outage with Azure services. Review Azure Service Health.

### 5. Documentation for Guidance

**Microsoft Documentation Links**:
- [Azure AD Sign-in logs](https://learn.microsoft.com/en-us/azure/active-directory/reports-monitoring/concept-sign-ins)
- [Troubleshoot Azure AD sign-in errors](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/troubleshoot-sign-in-errors)
- [Set up federation with Azure AD](https://learn.microsoft.com/en-us/azure/active-directory/develop/active-directory-federation-protocols)

### 6. Advice for Data Collection

During troubleshooting, it may be helpful to gather logs and traces:

- **Event Viewer Logs**:
  - Check the Windows Event Viewer under Applications and Services Logs > Microsoft > IdentityManagement for detailed logs related to identity issues.

- **Network Traces**:
  - Use tools like NetTrace or Wireshark to capture network traffic and identify any network-related issues.

- **Fiddler for HTTP Traces**:
  - Utilize Fiddler to capture HTTP/HTTPS traffic to see the flow of requests and responses during authentication.

- **Azure Diagnostics**:
  - Enable Azure Diagnostics in your relevant resource groups to capture more logs and metrics for further analysis.

By following this troubleshooting guide, you should be able to diagnose and address the AADSTS90085 error effectively.