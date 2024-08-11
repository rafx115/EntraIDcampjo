# AADSTS80013: OnPremisePasswordValidationTimeSkew - The authentication attempt couldn't be completed due to time skew between the machine running the authentication agent and AD. Fix time sync issues.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS80013

**Error Description:**
AADSTS80013 indicates a problem with time synchronization between the machine running the authentication agent and Active Directory (AD). If the authentication attempt fails because of this time skew, it may prevent users from logging in successfully.

---

### Initial Diagnostic Steps

1. **Check the Error Message**: Confirm the exact error code and message in the logs or user feedback.
  
2. **Review System Time Settings**: 
   - On the server running the authentication agent (e.g., Azure AD Connect), check the date and time settings.
   - Use the command `date` in Windows command prompt to see the current date and time.
  
3. **Check Time Synchronization**: 
   - Determine if the server’s time is synchronized with an NTP (Network Time Protocol) server.
   - Verify against the Windows Time Service settings using `w32tm /query /status`.

4. **Check AD Time Settings**:
   - Log into a Domain Controller (DC) and check its time configuration.
   - Make sure the DC’s time is correct using the same command used for the authentication agent.

5. **Log Analysis**: 
   - Review Azure AD Connect logs for any additional context around the error.
   - Use Event Viewer to look for related events under `Applications and Services Logs > Microsoft > AzureADConnect`.

---

### Common Issues that Cause This Error

1. **Time Skew**: The time difference between the authentication agent and the Domain Controller exceeds acceptable limits (usually 5 minutes).

2. **NTP Configuration Issues**: The server may not be correctly configured to sync with a reliable time source.

3. **Daylight Saving Time**: Differences in how servers handle DST vs. real-time can cause a time mismatch.

4. **Network Issues**: Connectivity problems could prevent the server from syncing time with external NTP servers.

5. **VM Time Sync Settings**: If running in a virtual environment, time synchronization settings might be misconfigured.

---

### Step-by-Step Resolution Strategies

#### Step 1: Synchronize Time

- **For Windows Server**:
  1. Open an elevated command prompt.
  2. Check the current time source:
     ```
     w32tm /query /source
     ```
  3. Ensure it points to a valid NTP server. If not, set it:
     ```
     w32tm /config /manualpeerlist:"time.windows.com,0x1" /syncfromflags:manual /reboot
     ```

- **For Domain Controller**:
  1. Again, use the command:
     ```
     w32tm /query /status
     ```
  2. Change the NTP server if required:
     ```
     w32tm /config /manualpeerlist:"time.windows.com,0x1" /syncfromflags:manual /reboot
     ```

#### Step 2: Verify and Adjust Windows Time Service

- Restart the Windows Time service on both machines:
  ```
  net stop w32time
  net start w32time
  ```

- Force synchronization:
  ```
  w32tm /resync
  ```

#### Step 3: Check for Firewall or Networking Issues

- Ensure that TCP port 123 (NTP) is open on firewalls between the time server and the machines requiring time synchronization.

#### Step 4: Validate Configuration

- Use `w32tm /monitor` to see the time status of all machines in the AD environment.
- Ensure all relevant machines report correct times.

---

### Additional Notes or Considerations

- **Regular Monitoring**: Implement monitoring solutions to regularly verify time synchronization across all authenticated machines and domain controllers.
  
- **Document Environment Variables**: Note the OS version, AD configuration, and if the server is physical or virtual during troubleshooting.

- **Group Policies**: Review any group policies that might affect time synchronization.

---

### Documentation for Guidance

- [Time Synchronization in Windows](https://docs.microsoft.com/en-us/windows-server/networking/windows-time-service)
- [Azure AD Connect Troubleshooting](https://docs.microsoft.com/en-us/azure/active-directory/hybrid/tshoot-authentication)

**Test Documentation Accessibility**:
1. Visit the URLs listed directly in a web browser to ensure they are currently accessible.

---

### Advice for Data Collection

Before proceeding with the resolution steps, collect the following data:

1. **Time and Date Settings**: Take screenshots of time settings from the authentication agent and Domain Controller.
2. **NTP Configuration**: Document the output of `w32tm /query /status` and `w32tm /query /source`.
3. **Event Logs**: Gather related event logs from both the agent and the Domain Controller pertaining to time sync and AAD authentication.
4. **Network Configuration**: Take note of network settings, especially related to firewalls and NTP server accessibility.

By systematically following these steps and considerations, you should be able to resolve the AADSTS80013 error effectively.

Category: Other