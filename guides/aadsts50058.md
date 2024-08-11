# AADSTS50058: UserInformationNotProvided - Session information isn't sufficient for single-sign-on. This means that a user isn't signed in. This is a common error that's expected when a user is unauthenticated and hasn't yet signed in.If this error is encountered in an SSO context where the user has previously signed in, this means that the SSO session was either not found or invalid.This error might be returned to the application if prompt=none is specified.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS50058

#### **Initial Diagnostic Steps:**
1. **Confirm the Error Message:**
   Verify that the error code is indeed AADSTS50058 and the description is "UserInformationNotProvided - Session information isn't sufficient for single-sign-on."

2. **User Sign-In Status:**
   Check if the user is authenticated or signed in. If the user is unauthenticated, the error may be expected.

3. **SSO Session Status:**
   Ensure the Single Sign-On (SSO) session for the user is valid and not expired.

#### **Common Issues:**
1. **User Not Signed In:**
   The error commonly occurs when the user is not signed in or authenticated.

2. **Invalid or Expired SSO Session:**
   If the user has previously signed in but encounters this error, the SSO session may be invalid or expired.

3. **Issue with prompt=none Parameter:**
   This error can also occur if the application specifies prompt=none, which can skip the user prompt for credentials and lead to this error.

#### **Resolution Strategies:**
1. **User Sign-In:**
   - Instruct the user to sign in or authenticate if they are currently unauthenticated.

2. **Refresh SSO Session:**
   - Have the user attempt to refresh the SSO session by logging out and then signing in again.

3. **Check SSO Configuration:**
   - Review the SSO configuration to ensure it is properly set up and that sessions are managed correctly.

4. **Adjust prompt Parameter:**
   - If the error occurs due to prompt=none, consider modifying the parameter to prompt the user for credentials as needed.

#### **Additional Notes or Considerations:**
- **Review Application Integration:**
  Ensure that the application is integrated properly with the identity provider and SSO settings.

- **Monitor SSO Sessions:**
  Regularly monitor and manage SSO sessions to prevent issues related to session expiration or invalidation.

- **Stay Updated:**
  Keep an eye on any updates or changes in the identity provider's documentation or notifications related to SSO configurations.

#### **Documentation for Guidance:**
- Microsoft Azure Active Directory documentation:
  - [Troubleshoot single sign-on issues in Microsoft Azure Active Directory](https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/troubleshoot-single-sign-on-issues)

By following these troubleshooting steps and considering the common issues, you should be able to address the AADSTS50058 error related to insufficient session information in a single sign-on context effectively.