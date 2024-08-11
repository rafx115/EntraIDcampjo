# AADSTS80001: OnPremiseStoreIsNotAvailable - The Authentication Agent is unable to connect to Active Directory. Make sure that agent servers are members of the same AD forest as the users whose passwords need to be validated and they are able to connect to Active Directory.


## Troubleshooting Steps
### Troubleshooting Guide for error code AADSTS80001: OnPremiseStoreIsNotAvailable

#### Initial Diagnostic Steps:
1. **Check Agent Server Connectivity**: Verify that the agent servers are connected to the network and can access the Active Directory.
2. **Validate Server Membership**: Confirm that the agent servers are members of the same Active Directory forest as the users needing authentication.
3. **Review Agent Configuration**: Ensure that the Authentication Agent configuration settings are correctly set up to connect to the Active Directory.

#### Common Issues Causing the Error:
1. **Network Connectivity Problems**: If the agent servers cannot reach the Active Directory due to network issues.
2. **Incorrect Forest Membership**: Agent servers not being part of the same Active Directory forest as the users.
3. **Misconfigured Agent Settings**: Incorrect configuration settings in the Authentication Agent causing the connection issue.

#### Step-by-Step Resolution Strategies:
1. **Verify Network Connectivity**:
   - Check the network connection on the agent servers to ensure they can reach the Active Directory.
   - Test network access using tools like ping or telnet to the Active Directory server.

2. **Confirm Forest Membership**:
   - Validate that the agent servers are indeed part of the same Active Directory forest as the users needing authentication.
   - Ensure there are no trust relationship issues between forests.

3. **Check Agent Configuration**:
   - Review the Authentication Agent configuration to confirm it's correctly set up to connect to the Active Directory.
   - Check for any misconfigured settings that might be causing the connection problem.

#### Additional Notes or Considerations:
- **Firewall Settings**: Make sure any firewalls between the agent servers and the Active Directory are configured to allow necessary traffic.
- **DNS Configuration**: Check DNS settings to ensure proper resolution between agent servers and Active Directory domain controllers.

#### Documentation for Guidance:
- Microsoft Azure Active Directory troubleshooting guide: [Troubleshooting AD FS issues](https://docs.microsoft.com/en-us/azure/active-directory/hybrid/tshoot-connect-connectivity)
- Microsoft Azure AD error code reference: [AADSTS80001 OnPremiseStoreIsNotAvailable](https://docs.microsoft.com/en-us/azure/active-directory/develop/reference-aadsts-error-codes#aadsts80001)