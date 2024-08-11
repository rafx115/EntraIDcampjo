# AADSTS50058: UserInformationNotProvided - Session information isn't sufficient for single-sign-on. This means that a user isn't signed in. This is a common error that's expected when a user is unauthenticated and hasn't yet signed in.If this error is encountered in an SSO context where the user has previously signed in, this means that the SSO session was either not found or invalid.This error might be returned to the application if prompt=none is specified.

## Introduction
This guide will help resolve issues related to userinformationnotprovided - session information isn't sufficient for single-sign-on. this means that a user isn't signed in. this is a common error that's expected when a user is unauthenticated and hasn't yet signed in.if this error is encountered in an sso context where the user has previously signed in, this means that the sso session was either not found or invalid.this error might be returned to the application if prompt=none is specified..

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
Troubleshooting Guide for Error Code AADSTS50058 - UserInformationNotProvided:

Initial Diagnostic Steps:
1. Check if the user is correctly authenticated and signed in to the application.
2. Verify the configuration settings related to single sign-on (SSO) in the application and identity provider.

Common Issues that Cause this Error:
1. User is not signed in or authenticated.
2. SSO session is not found or is invalid.
3. Improper configuration of prompt=none parameter causing the error to occur.

Step-by-Step Resolution Strategies:

1. Sign-In Troubleshooting:
   a. Ask the user to sign in again and ensure they are successfully authenticated.
   b. Check if there are any issues with the sign-in flow or functionality of the application.

2. Verify SSO Session:
   a. Confirm that the SSO session is valid and has not expired.
   b. If using external identity providers, check if there are any issues with the SSO setup or configuration.

3. Check prompt=none Parameter:
   a. If the error occurs when prompt=none is specified in the request, consider removing this parameter to prompt the user for sign-in.
   b. If prompt=none is necessary for your application flow, ensure that the SSO session is properly managed and maintained.

4. Review Application and Identity Provider Configuration:
   a. Double-check the SSO settings and configurations in both the application and the identity provider.
   b. Ensure that the required user information is being provided during the authentication process.

Additional Notes or Considerations:
- It is crucial to handle this error gracefully in the application to guide the user on the necessary steps to resolve it.
- Consider logging detailed information about the error to aid in troubleshooting, such as timestamps and user actions leading to the error.
- If the issue persists, consider reaching out to the identity provider support for further assistance in diagnosing and resolving the problem.

By following these troubleshooting steps, you can address the AADSTS50058 error and ensure a smooth SSO experience for users accessing your application.