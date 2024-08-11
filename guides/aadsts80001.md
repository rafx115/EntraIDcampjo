# AADSTS80001: OnPremiseStoreIsNotAvailable - The Authentication Agent is unable to connect to Active Directory. Make sure that agent servers are members of the same AD forest as the users whose passwords need to be validated and they are able to connect to Active Directory.

## Introduction
This guide will help resolve issues related to onpremisestoreisnotavailable - the authentication agent is unable to connect to active directory. make sure that agent servers are members of the same ad forest as the users whose passwords need to be validated and they are able to connect to active directory..

## Prerequisites
- Access to the Azure AD portal with administrator privileges.
- The user must have already set up MFA.

## Steps to Resolve

### Step 1: Initial Actions
1. Log in to the Azure AD portal.
2. Navigate to the "Users" section.
3. Select the affected user.
4. Perform necessary actions as described for the error.

### Step 2: Verify MFA Settings
1. Ensure that the user has MFA configured.
2. If necessary, guide the user through the MFA setup process.

## Troubleshooting
- Check for any Azure AD conditional access policies that might be affecting the MFA process.
- Consider any additional security measures that might be in place.

## Additional Notes
- Refer to the [Azure AD documentation](https://learn.microsoft.com/en-us/azure/active-directory/) for more details.


## Troubleshooting Steps
Troubleshooting steps could not be generated due to an error.

## Troubleshooting Steps
Troubleshooting steps could not be generated due to an error.

## Troubleshooting Steps
**Error Code:** AADSTS80001 - OnPremiseStoreIsNotAvailable

**Description:** The Authentication Agent is unable to connect to Active Directory. Ensure that agent servers are members of the same AD forest as the users whose passwords need to be validated and that they are able to connect to Active Directory.

**Initial Diagnostic Steps:**
1. Verify network connectivity between the Authentication Agent server and the Active Directory domain controllers.
2. Check the event logs on the Authentication Agent server for any relevant error messages.
3. Validate that the agent server is joined to the correct Active Directory forest.

**Common Issues:**
1. Network connectivity issues between the Authentication Agent server and Active Directory.
2. Misconfiguration of the Authentication Agent server's domain membership.
3. Incorrect DNS settings preventing successful communication with Active Directory.
4. Firewall or security settings blocking the connection between the agent server and Active Directory.

**Step-by-Step Resolution Strategies:**

1. **Validate Domain Membership:**
   - Verify that the Authentication Agent server is properly joined to the Active Directory domain. Rejoin the domain if necessary.

2. **Check Network Connectivity:**
   - Ensure that the agent server can reach the domain controllers over the network. Use tools like ping or tracert to troubleshoot connectivity issues.

3. **Review DNS Configuration:**
   - Confirm that the DNS settings on the Authentication Agent server are pointing to the correct domain controllers. Update DNS settings if needed.

4. **Check Firewalls and Security Settings:**
   - Temporarily disable firewalls or security software on the Authentication Agent server to see if they are blocking the connection to Active Directory. Adjust settings if necessary.

5. **Restart Services:**
   - Restart the Authentication Agent service on the server to refresh the connection with Active Directory.

6. **Update Authentication Agent Configuration:**
   - Check the configuration settings of the Authentication Agent to ensure that it is configured to connect to the correct Active Directory forest.

**Additional Notes or Considerations:**
- Ensure that the Authentication Agent server has the necessary permissions in Active Directory to read user information and validate passwords.
- Regularly monitor the event logs on the Authentication Agent server for any recurring issues related to communication with Active Directory.
- Consult with your IT team or a system administrator for assistance if the issue persists despite troubleshooting steps.
- Consider contacting the vendor or support resources for the Authentication Agent software for further assistance in resolving this error.