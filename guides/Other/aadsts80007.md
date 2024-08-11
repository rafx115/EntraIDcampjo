# AADSTS80007: OnPremisePasswordValidatorErrorOccurredOnPrem - The Authentication Agent is unable to validate user's password. Check the agent logs for more info and verify that Active Directory is operating as expected.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS80007 Error

**Description:**  
The error code `AADSTS80007` with the description `OnPremisePasswordValidatorErrorOccurredOnPrem` indicates that the Authentication Agent is unable to validate the user's password. This can prevent users from authenticating properly against Azure Active Directory (AAD) when using on-premises Active Directory.

---

### Initial Diagnostic Steps

1. **Check the Service Status:**
   - Verify the status of Azure services to make sure there are no ongoing outages or issues with the Azure Active Directory service that could impact authentication.

2. **Review Agent Logs:**
   - Check the logs for the Azure AD Authentication Agent. Logs are typically found at: `C:\Program Files\Microsoft Azure AD Authentication Agent\logs`. Look for recent entries related to user authentication.

3. **Validate Network Connectivity:**
   - Ensure that the Authentication Agent can reach the on-premises Active Directory and that external connectivity to Azure AD is also functioning properly.

4. **Test Basic Authentication:**
   - Try to authenticate a user directly against Active Directory using tools such as `dsquery`, `get-aduser`, or similar. This checks whether the user can be validated outside of the Authentication Agent.

---

### Common Issues That Cause This Error

1. **Authentication Agent Configuration:**
   - Incorrectly configured Authentication Agent, particularly regarding connections to the on-premises Active Directory.

2. **AD DS Availability:**
   - Active Directory Domain Services (AD DS) might be down or experiencing issues.

3. **Account Lockouts:**
   - The user account may be locked, expired, or invalid.

4. **Password Changes Not Replicated:**
   - New passwords may not have propagated throughout Active Directory or have not been synced correctly.

5. **Firewall and Network Issues:**
   - Network or firewall settings may be blocking connections between the Authentication Agent and the AD or Azure.

6. **Kerberos Issues:**
   - In cases where Kerberos authentication is set up, issues in service tickets can arise.

---

### Step-by-Step Resolution Strategies

1. **Validate Configuration of Authentication Agent:**
   - Open the Azure AD Authentication Agent configuration.
   - Verify that the agent is correctly configured with the proper credentials and settings for accessing the on-premises Active Directory.

2. **Check Active Directory Health:**
   - Use the `dcdiag` command to check the health of the Active Directory.  
   Command:  
   ```
   dcdiag /v
   ```

3. **Review User Account Status:**
   - Open Active Directory Users and Computers (ADUC).
   - Check the user's account for status indicators (locked, expired, etc.).

4. **Replicate Password Changes:**
   - If the user has recently changed their password, ensure that the change has been replicated throughout AD. Use the `repadmin` command to check replication status.  
   Command:  
   ```
   repadmin /showrepl
   ```

5. **Monitoring Network:**
   - Ensure that the Authentication Agent can communicate with your on-premises AD and Azure AD without being blocked by any firewall rules.
   - Use `ping` or `telnet` tests on necessary ports (generally TCP 389 for LDAP).

6. **Restart the Authentication Agent Service:**
   - Sometimes, simply restarting the Azure AD Authentication Agent service can resolve transient issues.  
   Command in PowerShell:  
   ```powershell
   Restart-Service "AzureADAuthenticationAgent"
   ```

---

### Additional Notes or Considerations

- Make sure that the system hosting the Authentication Agent has adequate permissions to query AD.
- Ensure that time synchronization is maintained across systems to prevent Kerberos authentication failures.
- Regularly review and update the Authentication Agent to the latest version for stability.
- If you have multiple Authentication Agents, ensure they’re all configured properly and are in good health.

---

### Documentation for Reference

- Azure AD Authentication Agent Documentation: [Overview of Azure AD Authentication Agent](https://learn.microsoft.com/en-us/azure/active-directory/hybrid/deploy-authentication-agent)
- How to check Active Directory Health: [Using DCDIAG](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/active-directory-diagnostic-tools)

*Note: Please verify that access to the above documentation is available as connections may vary based on your network settings and permissions.*

---

### Advice for Data Collection

- When troubleshooting, compile the following data:
  - Event logs from the Authentication Agent.
  - Error messages encountered during user authentication.
  - Outputs from `dcdiag` and `repadmin` commands.
  - Connectivity tests (ping, telnet) results.
  - Configuration settings of the Authentication Agent.

By following this troubleshooting guide, you will systematically address the AADSTS80007 error related to on-premises password validation and help restore functionality for users.

Category: Other