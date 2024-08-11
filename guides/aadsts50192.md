# AADSTS50192: Invalid Request - RawCredentialExpectedNotFound - No Credential was included in the sign-in request. Example: user is performing certificate-based authentication (CBA) and no certificate is sent (or Proxy removes) the user's certificate in the sign-in request.


## Introduction

This guide will help resolve issues related to invalid request - 
rawcredentialexpectednotfound - no credential was included in the sign-in

request. example: user is performing certificate-based authentication (cba) and
no certificate is sent (or proxy removes) the user's certificate in the sign-in
request..


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


### Troubleshooting Guide for Error Code AADSTS50192: Invalid Request - RawCredentialExpectedNotFound


#### Initial Diagnostic Steps:

1. **Confirm the Authentication Method**: Check if the user is supposed to be
   performing certificate-based authentication (CBA) in this scenario.
2. **Review Sign-in Request**: Analyze the sign-in request to verify if a
   credential (certificate in this case) is missing.
3. **Check Proxy Settings**: Determine if the user's certificate is being
   removed by a proxy server.


#### Common Issues:

1. **Missing Credential**: The primary cause of this error is the absence of the
   required credential in the sign-in request.
2. **Proxy Interference**: If a proxy server is involved, it might be stripping
   off the user's certificate from the request.
3. **Misconfiguration**: Incorrect configuration of the authentication process
   can also lead to this issue.


#### Step-by-Step Resolution Strategies:

1. **User Certificate Check**:

   * Ensure that the user has a valid certificate for CBA.

   * Double-check if the certificate hasn't expired or been revoked.

2. **Proxy Inspection**:

   * Confirm if there is a proxy server in between that might be altering the

     request.
   * Check the proxy settings and configuration to ensure it's not causing the

     credential to be missing.

3. **Azure AD Configuration**:

   * Review the Azure AD settings to ensure that CBA is properly configured for

     the application.
   * Verify that the required authentication methods are set up correctly.

4. **Client-Side Troubleshooting**:
   * Instruct the user to retry the sign-in process while ensuring the

     certificate is sent successfully.
   * Clear any cached credentials or reconfigure the authentication setup on the

     client's end.


#### Additional Notes or Considerations:


* **User Education**: It can be beneficial to educate the user on the importance

  of maintaining their certificate for CBA.

* **Logs and Monitoring**: Keep an eye on logs and monitoring tools to track any

  unusual behavior or patterns leading to the credential being missing.

* **Ongoing Support**: If the issue persists, consider reaching out to Azure

  support for further assistance and guidance.

By following the steps outlined above, you should be able to diagnose and
resolve the AADSTS50192 error related to the missing credential in the sign-in
request efficiently.