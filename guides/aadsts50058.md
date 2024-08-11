
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
