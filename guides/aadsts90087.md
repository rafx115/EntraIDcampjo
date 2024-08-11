# AADSTS90087: OrgIdWsFederationMessageCreationFromUriFailed - An error occurred while creating the WS-Federation message from the URI.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS90087 Error

**Error Description:**
AADSTS90087 indicates a failure in creating a WS-Federation message from a URI. This error is typically related to misconfigurations in the federated authentication setup within Azure Active Directory (Azure AD). 

---

### Initial Diagnostic Steps

1. **Check the Error Message:**
   - Review the full error message for context. It may provide specific details or clues about the issue.

2. **Identify the User’s Context:**
   - Determine if this error occurs for a specific user or multiple users.
   - Verify if the issue occurs for specific applications or across the organization.

3. **Confirm Network Connectivity:**
   - Ensure the client system has network connectivity and can reach Azure AD endpoints.

4. **Gather Logs:**
   - Collect any logs from the Identity Provider (IdP) and the application or service encountering the issue. Logs can provide insight into the specific failure.

---

### Common Issues That Cause AADSTS90087

1. **Incorrect or Malformed URIs:**
   - Check if the URI being used in the request is correctly formatted and properly matches the expected format in the Azure AD configuration.

2. **Misconfigured Application Registration:**
   - Ensure the application is correctly registered in Azure AD, and all necessary permissions and identifiers (e.g. Reply URLs, Redirect URIs) are correctly set up.

3. **Federation Metadata Issues:**
   - Issues with federation metadata could prevent correct message processing. Ensure that federation metadata is accessible and valid.

4. **Service Principal Name (SPN) Issues:**
   - If using a Service Account, ensure the SPN is correctly configured and permissions are granted as necessary.

5. **Policy Restrictions:**
   - Verify that any conditional access policies or identity protection policies don't inadvertently block the authentication.

---

### Step-by-Step Resolution Strategies

1. **Review and Validate the URI:**
   - Double-check the URI being used in the WS-Federation message for correctness. Ensure it aligns with the configured URIs in Azure AD.

2. **Check Azure AD Application Registration:**
   - Log in to the Azure portal.
   - Navigate to **Azure Active Directory > App registrations**.
   - Locate the affected application and verify the settings, especially:
     - Application (client) ID
     - Directory (tenant) ID
     - Reply URLs/Redirect URIs

3. **Verify Federation Metadata:**
   - Ensure that the federation metadata can be retrieved and is valid.
   - You can access the federation metadata endpoint to inspect its contents.

4. **Analyze Authentication Logs:**
   - Navigate to **Azure Active Directory > Sign-ins**.
   - Review the logs for any failed sign-in attempts to identify specific error messages or codes.

5. **Adjust Policies (if applicable):**
   - Check conditional access settings under **Azure Active Directory > Security > Conditional Access** to ensure that there are no restrictions preventing the login process.

6. **Consult Documentation:**
   - Refer to the official Azure documentation for WS-Federation and Azure AD configuration for more detailed guidance. Key sections may include:
     - [Configure WS-Federation](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-wsfederation)
     - [Application Registration](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)

---

### Additional Notes or Considerations

- **Test URL and Metadata Accessibility:**
  - Use tools such as `curl` or web browsers to ensure the metadata and specific endpoints are reachable from the network location of the user.

- **Consult Azure Support:**
  - If the issue persists, consider raising a ticket with Azure support for deeper investigation, especially if this is impacting production environments.

---

### Documentation and Resources Check

- Ensure that the documentation links provided above are functioning correctly. You can test links in your browser to confirm reachability.

---

### Advice for Data Collection

- Gather information from:
  - Azure AD sign-in logs.
  - Application logs or error logs indicating where the failure occurs.
  - Network traces (if applicable) that may show requests and responses between components in the authentication process.

By following this detailed guide, you should be able to diagnose and resolve the AADSTS90087 error effectively.