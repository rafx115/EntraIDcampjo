# AADSTS80001: OnPremiseStoreIsNotAvailable - The Authentication Agent is unable to connect to Active Directory. Make sure that agent servers are members of the same AD forest as the users whose passwords need to be validated and they are able to connect to Active Directory.


## Troubleshooting Steps
Certainly! Below is a detailed troubleshooting guide for the error code AADSTS80001 with the provided description.

---

### Troubleshooting Guide for AADSTS80001 - OnPremiseStoreIsNotAvailable

#### Initial Diagnostic Steps
1. **Review the Error Context:**
   - Ensure that you have a clear understanding of when and how this error occurs. Is it during a specific user authentication attempt or for multiple users?

2. **Check the Configuration:**
   - Verify that the Azure AD Application Proxy (if used) is configured correctly.

3. **Validate System Status:**
   - Check if the Authentication Agent service is running on the server.
   - Ensure your server is not experiencing any network issues.

#### Common Issues that Cause This Error
1. **Network Connectivity:**
   - The Authentication Agent cannot reach Active Directory due to network issues.

2. **Domain Membership:**
   - The server where the Authentication Agent is installed is not a member of the same Active Directory forest as the users.

3. **Firewall/Security Policies:**
   - Firewalls or security policies might be blocking necessary communication between the Authentication Agent and Active Directory servers.

4. **Agent Configuration Issues:**
   - Incorrect configuration settings for the Authentication Agent connected to Azure AD.

5. **Authentication Agent Outdated:**
   - The Authentication Agent might be out of date and requires an update.

6. **Service Account Permissions:**
   - The service account used to connect to Active Directory might lack the necessary permissions.

#### Step-by-Step Resolution Strategies
1. **Check the Authentication Agent:**
   - Log in to the server running the Authentication Agent.
   - Open the services management console and verify that the "Azure AD Authentication Agent" service is running.

2. **Verify Domain Membership:**
   - Ensure the server is correctly joined to the Active Directory domain.
   - Use the command `whoami /groups` to confirm the domain the server belongs to.

3. **Network Configuration:**
   - Ensure the server can communicate with the domain controllers:
     - Use `ping` to test connectivity.
     - Use `nslookup` to verify DNS resolution for the domain controllers.
   - Check for any network firewalls that may be blocking ports (typically TCP 389 for LDAP, TCP 636 for LDAPS).

4. **Review Firewall Rules:**
   - Confirm that both Windows Firewall and any external firewalls are configured to allow communication on necessary ports for Active Directory.

5. **Check Agent Configuration:**
   - Launch the Authentication Agent configuration tool.
   - Verify the settings for Azure AD connectivity and correct any discrepancies.

6. **Update the Authentication Agent:**
   - Check for updates for the Azure AD Authentication Agent.
   - Download and install the latest version.

7. **Verify Service Account Permissions:**
   - Confirm that the service account used for the agent has read permissions in Active Directory.

8. **Review Event Logs:**
   - Check Windows Event Viewer for errors related to the Authentication Agent under ‘Applications and Services Logs’ -> ‘Microsoft’ -> ‘AAD’ -> ‘Authentication Agent’.

#### Additional Notes or Considerations
- Ensure that time synchronization is correct between the server and domain controllers; mismatches can lead to authentication issues.
- Consider reviewing the Azure AD Connect settings if used, as it may affect how on-premise authentication is configured and functioning.
  
#### Documentation for Guidance
- [Microsoft Documentation on Azure AD Authentication Agent](https://docs.microsoft.com/en-us/azure/active-directory/hybrid/deploy/authentication-agent)
- [Azure AD Connect: Troubleshoot sign-in issues with Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/hybrid/tshoot-connect-issue)
  
#### Advice for Data Collection
1. **Event Viewer Logs:**
   - Collect logs from the Event Viewer focusing on Application and System logs, specifically entries related to the Azure AD Authentication Agent.

2. **NetTrace:**
   - Use NetSh or Wireshark to capture network traffic that may help diagnose connectivity issues.

3. **Fiddler:**
   - If needed, use Fiddler to inspect HTTP traffic and check for any errors or failed requests while attempting authentication.

4. **Collect Logs:**
   - Gather all logs for analysis. Use `Get-WinEvent` PowerShell cmdlet to export relevant logs for easier review.

---

By following this comprehensive guide, you should be able to identify and resolve issues leading to the AADSTS80001 error effectively. If the problem persists after these steps, consider contacting Microsoft support for further assistance.