# AADSTS80001: OnPremiseStoreIsNotAvailable - The Authentication Agent is unable to connect to Active Directory. Make sure that agent servers are members of the same AD forest as the users whose passwords need to be validated and they are able to connect to Active Directory.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS80001 - OnPremiseStoreIsNotAvailable

#### Error Description
The error code `AADSTS80001` indicates that the Authentication Agent is unable to connect to Active Directory (AD). This error may occur in scenarios where Azure Active Directory (AAD) is integrating with on-premises Active Directory for user authentication and validation. 

### Initial Diagnostic Steps

1. **Identify the Scope of the Issue:**
   - Determine if the issue is affecting all users or specific users.
   - Check if other services dependent on Active Directory are functioning normally.
  
2. **Review Agent Status:**
   - Confirm that the Azure AD Connect or the Authentication Agent service is running and has started successfully on the server where it is hosted.

3. **Verify Network Connectivity:**
   - Check if the server running the Authentication Agent can communicate with the domain controllers (DCs) of your AD.

### Common Issues that Cause this Error

1. **Network Connectivity Issues:**
   - Firewalls blocking communication between the Authentication Agent and Active Directory.
   - Network issues that prevent the agent from reaching the AD domain controllers.

2. **Service Account Permissions:**
   - The service account used by the Authentication Agent may not have the required permissions to connect to Active Directory.
  
3. **Agent Configuration:**
   - Misconfiguration in the Authentication Agent settings.
   - The Agent might not be properly registered with Azure AD.

4. **Domain Controller Issues:**
   - Domain controllers may be down or encountering issues preventing authentication.

5. **Forest Trust Issues:**
   - If multiple forests are in use, ensure proper trust relationships are established and functioning.

### Step-by-Step Resolution Strategies

1. **Check Agent Service:**
   - On each Authentication Agent server, check that the `Microsoft Azure AD Authentication Agent Service` is running. Restart the service if necessary.

2. **Validate Network Connectivity:**
   - Use `ping` and `nslookup` to test connectivity with the domain controllers.
   - Check firewall rules to ensure that required ports for LDAP/LDAPS (389/636) are open.

3. **Check Agent Configuration:**
   - Use the Azure AD Connect wizard or configuration tool to verify the settings of the Authentication Agent are correct.
   - Ensure the server is a member of the same AD forest.

4. **Review Service Account Permissions:**
   - Log in with the service account used by the Authentication Agent and check its permissions in Active Directory.
   - Ensure that the account is not locked out and has sufficient rights.

5. **Check Domain Controllers:**
   - Log in to domain controllers and ensure that they are functioning correctly.
   - Check the event logs on domain controllers for any related errors.
  
6. **Test Other Authentication Methods:**
   - If applicable, test other authentication methods (like Hashing) to determine if it is specific to the Authentication Agent.

### Additional Notes or Considerations

- It’s important to ensure that the Authentication Agent is installed on servers that are located in the same network as the domain controller or have reliable network connections to them. 
- If you're using multiple forests, ensure that the corresponding Authentication Agents are installed in each forest.

### Documentation for Guidance

- **Azure AD Connect documentation:** [Install and configure Azure AD Connect](https://docs.microsoft.com/en-us/azure/active-directory/hybrid/understand-architecture)
- **Troubleshooting Azure AD Connect:** [Troubleshoot Azure AD Connect synchronization](https://docs.microsoft.com/en-us/azure/active-directory/hybrid/tshoot-connect-sync)

### Test Documentation Accessibility

- You can confirm the accessibility of the documentation pages mentioned above by visiting them directly in your web browser:
  - [Install and configure Azure AD Connect](https://docs.microsoft.com/en-us/azure/active-directory/hybrid/understand-architecture)
  - [Troubleshoot Azure AD Connect synchronization](https://docs.microsoft.com/en-us/azure/active-directory/hybrid/tshoot-connect-sync)

### Advice for Data Collection

- **Event Logs:** Collect logs from the Authentication Agent server, especially the application and system logs.
- **Network Logs:** Capture network traffic using tools like Wireshark to check for connectivity issues.
- **Agent Logs:** Enable verbose logging in the Authentication Agent for detailed diagnostic data.
- **AD Logs:** Review logs from Domain Controllers for any related authentication errors.
- **Permissions report:** Document the permissions and roles assigned to the service account.

By following this detailed troubleshooting guide, you should be able to identify and rectify the issues causing the `AADSTS80001 - OnPremiseStoreIsNotAvailable` error effectively.

Category: Other