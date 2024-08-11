# AADSTS80013: OnPremisePasswordValidationTimeSkew - The authentication attempt couldn't be completed due to time skew between the machine running the authentication agent and AD. Fix time sync issues.


## Introduction

This guide will help resolve issues related to
onpremisepasswordvalidationtimeskew - the authentication attempt couldn't be

completed due to time skew between the machine running the authentication agent
and ad. fix time sync issues..


## Prerequisites


* Access to the Azure AD portal with administrator privileges.

* The user must have already set up MFA.


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


* Check for any Azure AD conditional access policies that might be affecting the

  MFA process.

* Consider any additional security measures that might be in place.


## Additional Notes


* Refer to the

  [Azure AD 
documentation](https://learn.microsoft.com/en-us/azure/active-directory/)
  for more details.


## Troubleshooting Steps

Troubleshooting steps could not be generated due to an error.


## Troubleshooting Steps

Troubleshooting steps could not be generated due to an error.


## Troubleshooting Steps


### Troubleshooting Guide for Error Code AADSTS80013 - OnPremisePasswordValidationTimeSkew


#### Initial Diagnostic Steps:

1. Verify the error message: Ensure that the error code AADSTS80013 with the
   description related to time skew between the machine and AD is indeed
   displayed.
2. Check for the authentication agent logs or any other related logs for more
   detailed information.
3. Confirm the time settings on the machine running the authentication agent and
   Active Directory.


#### Common Issues Causing the Error:

1. Time synchronization discrepancies between the machine running the
   authentication agent and the Active Directory.
2. Incorrect timezone settings on either the authentication agent machine or the
   Active Directory.
3. Issues with NTP (Network Time Protocol) synchronization on the authentication
   agent machine or AD server.


#### Step-by-Step Resolution Strategies:

1. **Check Time Settings:** 

   * Validate the time settings on both the machine running the authentication

     agent and the AD server.
   * Ensure that both systems are using the correct time zone settings.

2. **Sync Time with NTP:** 

   * Utilize NTP to synchronize the time on the machine running the

     authentication agent and the AD server.
   * Verify NTP server configurations and connectivity.

3. **Restart Services:** 

   * Restart the authentication agent service and check if that resolves the

     time skew issue.
   * Consider restarting other relevant services on the machine and AD server.

4. **Update System Clock:**    * Manually adjust the system clock on the 
authentication agent machine to

     match the correct time.
   * Additionally, update the time on the Active Directory server if necessary.


#### Additional Notes or Considerations:


* **Firewall Settings:** Ensure that firewall rules do not block NTP traffic

  between the authentication agent machine and the AD server.

* **Network Configuration:** Check for any network latency that might be

  affecting time synchronization.

* **Intermittent Issues:** If the error is intermittent, consider setting up

  automated time synchronization tasks to address any potential drift over time.

By following these steps and guidelines, you should be able to address the
AADSTS80013 error related to time skew between the machine running the
authentication agent and Active Directory. If the issue persists, consider
involving your IT support team or relevant technical experts for further
assistance.