# AADSTS80013: OnPremisePasswordValidationTimeSkew - The authentication attempt couldn't be completed due to time skew between the machine running the authentication agent and AD. Fix time sync issues.


## Troubleshooting Steps
Certainly! Here's a detailed troubleshooting guide for the AADSTS80013 error code, specifically related to the "OnPremisePasswordValidationTimeSkew" issue.

### Troubleshooting Guide for AADSTS80013 Error Code

#### Overview
The error AADSTS80013 indicates that there is a time synchronization issue between the machine running the authentication agent (which is likely the AAD Connect) and Active Directory (AD). The time skew can prevent successful authentication attempts.

### 1. Initial Diagnostic Steps
- **Check the Error Message**: Ensure the error message specifically mentions "OnPremisePasswordValidationTimeSkew".
- **Confirm Time Settings**: Verify the date and time settings on the machine running the authentication agent.
- **Review Synchronization Logs**: Check the synchronization logs of AAD Connect for any warnings or errors that might indicate time synchronization issues.

### 2. Common Issues that Cause This Error
- **Time Drift**: The server running the authentication agent (AAD Connect) is not synchronized with the AD domain controller's time.
- **Time Zone Mismatch**: The time zone settings may differ between the authentication agent and AD servers.
- **NTP Configuration Issues**: Misconfiguration in Network Time Protocol (NTP) settings leading to time skew.
- **Daylight Saving Time (DST)**: Incorrect handling of DST changes can lead to skew.
- **Multiple Time Sources**: The machine or network may use multiple time sources leading to conflicts in time settings.

### 3. Step-by-Step Resolution Strategies
#### Step 1: Check and Fix Time Settings
1. **On the AAD Connect Server**:
   - Open **Command Prompt** as Administrator.
   - Run `w32tm /query /status` to check the current time source and status.
   - If there is a significant skew, reset time settings using:
     ```
     w32tm /resync
     ```

2. **Time Settings**:
   - Ensure time zone is set correctly:
     - Go to Control Panel -> Date and Time -> Time Zone, and set it correctly.
   - Ensure that "Synchronize with an Internet time server" is enabled (NTP):

   ```
   w32tm /config /manualpeerlist:"time.windows.com,0x1" /syncfromflags:manual /reliable:YES /update
   net stop w32time
   net start w32time
   ```

#### Step 2: Verify Time Synchronization on Domain Controllers
- Log onto your domain controllers and run the same `w32tm /query /status` command.
- Compare the time on the AAD Connect server with the primary domain controller (PDC) to ensure they match. 

#### Step 3: Check NTP Configuration
- Verify that NTP is properly configured to point to an appropriate time source (e.g., external time servers or internal NTP servers).
- Ensure that all involved machines use the same time source.

#### Step 4: Review Network and Firewall Settings
- Ensure that UDP port 123 (NTP) is open in the firewall settings on both the AAD Connect server and the domain controllers.
- Verify there are no network latencies affecting time sync.

### 4. Additional Notes or Considerations
- Be aware that significant time differences (more than 5 minutes) can cause authentication problems.
- When making changes to NTP settings, allow some time for synchronization to take effect.
- Consider enabling NTP logging for troubleshooting purposes if the problem persists.

### 5. Documentation for Guidance
- Microsoft Official Documentation on NTP Configuration:
  - [Configure Windows Time Service](https://docs.microsoft.com/en-us/windows-server/networking/windows-time-service)
- Azure AD Connect Troubleshooting Guide:
  - [Azure AD Connect documentation](https://docs.microsoft.com/en-us/azure/active-directory/hybrid/active-directory-aadconnect)

### 6. Advice for Data Collection
- **Event Viewer Logs**: Check the Event Viewer on both the AAD Connect server and domain controllers (under "Windows Logs" > "Application") for relevant warnings or errors related to time services or authentication.
  
- **Network Tracing**:
  - Use **Nettrace** or **Wireshark** to capture network packets if you're suspecting network issues affecting time sync.

- **Fiddler**: While Fiddler is primarily used for HTTP debugging, it could be useful to capture and analyze traffic to Azure AD if you're facing additional authentication issues.

By following this troubleshooting guide, you should be able to diagnose and resolve the AADSTS80013 error efficiently. Always ensure that time synchronization is maintained across your systems to avoid such errors in the future.