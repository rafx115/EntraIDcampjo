# AADSTS80013: OnPremisePasswordValidationTimeSkew - The authentication attempt couldn't be completed due to time skew between the machine running the authentication agent and AD. Fix time sync issues.


## Troubleshooting Steps
**Troubleshooting Guide for Error Code AADSTS80013: OnPremisePasswordValidationTimeSkew**

**Initial Diagnostic Steps:**
1. **Identify the Error Code:** Note down the error code AADSTS80013.
2. **Check Time Synchronization:** Verify the time settings on both the machine running the authentication agent and the Active Directory (AD) server.
3. **Review Logs:** Look in the event logs or authentication logs for any related messages.
4. **Understand the Environment:** Determine the setup of your on-premise authentication agent and its connection to AD.

**Common Issues that Cause this Error:**
1. **Time Skew:** Time difference between the machine running the authentication agent and the AD server.
2. **Network Latency:** Delays in network communication can lead to time synchronization issues.
3. **Misconfigured Timezones:** Incorrect timezone settings on the machines.
4. **Authentication Agent Configuration:** Improper configuration of the on-premise authentication agent.

**Step-by-Step Resolution Strategies:**
1. **Verify Time Settings:**
   - Ensure that the time and time zone settings on both the machine running the authentication agent and the AD server are accurate.
   - Use a reliable time server for synchronization.

2. **Address Time Skew:**
   - Correct the time difference between the system running the authentication agent and the AD server.
   - Manually synchronize time on the affected machines if needed.

3. **Check Network Connectivity:**
   - Ensure that the network connection between the machine running the authentication agent and the AD server is stable and reliable.
   - Address any network latency issues.

4. **Configuration Check:**
   - Review the configuration settings of the on-premise authentication agent.
   - Ensure that the agent is set up to communicate securely with the AD server.

**Additional Notes or Considerations:**
- **Power Cycling:** Sometimes, a simple restart of the machine running the authentication agent or the AD server can resolve time synchronization issues.
- **Firewall Rules:** Check for any firewall rules or restrictions that might be blocking time synchronization traffic.
- **Regular Monitoring:** Implement a regular time synchronization check to prevent future occurrences of time skew issues.

**Documentation for Guidance:**
For further guidance on troubleshooting time synchronization issues in the context of Azure AD authentication errors, refer to the official Microsoft documentation:
- [Azure AD error codes and troubleshooting](https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-how-to-common-error-codes)