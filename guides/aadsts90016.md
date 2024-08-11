
# AADSTS90016: MissingRequiredClaim - The access token isn't valid. The required claim is missing.


## Introduction

This guide will help resolve issues related to missingrequiredclaim - the access

token isn't valid. the required claim is missing..


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


### Troubleshooting Guide for Error Code AADSTS90016: MissingRequiredClaim


#### Initial Diagnostic Steps:

1. Verify the specific service or application where the error is occurring
   (e.g., Azure Active Directory, Microsoft 365, custom application).
2. Confirm the steps leading to the error to identify when and how the access
   token was issued.
3. Check the error logs or monitoring tools for any additional context or
   related errors.


#### Common Issues that Cause this Error:

1. **Incorrect Configuration**: Missing or incorrect configuration settings in
   the application or service.
2. **Token Expiration**: The access token might have expired.
3. **Insufficient Permissions**: The user or application might not have adequate
   permissions to access the required claim.
4. **Troubles in Token Issuance**: Issues during the token issuance process,
   like missing claims.


#### Step-by-Step Resolution Strategies:

1. **Check Token Claims**:

   * Verify the required claims in the access token against the service's

     expected claims.
   * Ensure that the necessary claims (e.g., roles, groups) are included in the

     token.

2. **Token Validation**:

   * Validate the access token using the service's token validation endpoint to

     ensure its integrity.
   * Check the token's expiration and audience to confirm its validity.

3. **Application Configuration**:

   * Review the application's configuration settings related to authentication

     and token issuance.
   * Ensure that the application is requesting the required claims during token

     acquisition.

4. **Permission Check**:

   * Confirm that the user or application has the necessary permissions to

     access the required claim.
   * Check the service's permission settings to ensure they align with the

     required claims.

5. **Refresh Token**:

   * If the access token has expired, obtain a new token by using a refresh

     token if available.
   * Implement token refresh logic to prevent such errors due to token

     expiration.

6. **Integration Testing**:
   * Conduct integration testing to verify that the application can successfully

     process and validate the access tokens.
   * Check for errors or misconfigurations in the application flow that could

     lead to missing claims.


#### Additional Notes or Considerations:


* **Error Monitoring**: Implement robust error monitoring and logging to track

  such errors for future analysis.

* **Token Caching**: Consider utilizing token caching mechanisms to optimize

  token handling and reduce potential issues.

* **Support Channels**: If troubleshooting steps do not resolve the issue,

  consider reaching out to the service provider's support for further
  assistance.