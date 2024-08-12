
# AADSTS50079: UserStrongAuthEnrollmentRequired - Due to a configuration change made by the admin such as a Conditional Access policy, per-user enforcement, or because the user moved to a new location, the user is required to use multifactor authentication. Either a managed user needs to register security info to complete multifactor authentication, or a federated user needs to get the multifactor claim from the federated identity provider.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS50079 Error

**Error Code:** AADSTS50079  
**Description:** UserStrongAuthEnrollmentRequired - The user must complete multifactor authentication due to a configuration change made by the admin, such as Conditional Access policy or per-user enforcement.

#### 1. Initial Diagnostic Steps

- **Confirm User Status:** Check that the user in question is still active and has not had their account disabled or deleted.
- **Profile Verification:** Ensure that the user's profile is complete and configured correctly in Azure Active Directory (AAD).
- **Conditional Access Policies Review:** Check if there are any Conditional Access policies that could trigger the requirement for multifactor authentication (MFA).

#### 2. Common Issues That Cause This Error

- **Pending MFA Registration:** The user has not registered their security information for multifactor authentication.
- **Configuration Changes:** Recent changes to Conditional Access policies or per-user MFA settings by an administrator.
- **Location-based Policies:** The user’s current sign-in attempt is from a different location or device that does not meet policy conditions.
- **Federated Authentication:** Issues with federated identity providers that might not be issuing the correct MFA claims.

#### 3. Step-by-Step Resolution Strategies

**Step 1: Verify Conditional Access Policies**
   - Navigate to Azure Active Directory > Security > Conditional Access.
   - Review the policies that have been applied to the user or the group that the user belongs to.
   - Ensure that MFA enforcement is intended for the user’s sign-in context.

**Step 2: Check MFA Registration Status**
   - Go to Azure Active Directory > Users.
   - Locate the user and check their authentication methods under "Authentication methods" or "User settings".
   - If MFA registration has not been completed, instruct the user to register their security info.

**Step 3: User Education on Registration Process**
   - Provide the user with the following steps for MFA registration:
     1. Sign into the My Account portal (https://myaccount.microsoft.com).
     2. Navigate to "Security info".
     3. Follow prompts to set up an additional authentication method (phone number, authenticator app, etc.).

**Step 4: Review Any Recent Changes**
   - Conduct a review of any changes made to Conditional Access or MFA configurations that might have affected the user's ability to sign in.

**Step 5: Check for Federated Login Issues**
   - If the user is federated, ensure their identity provider is functioning correctly and issuing the expected claims.
   - Consult the identity provider’s documentation regarding MFA claim issuance.

**Step 6: Test Sign-in from Different Devices/Networks**
   - Suggest the user try accessing their account from a known, trusted network to rule out location-based policy issues.

#### 4. Additional Notes or Considerations

- **User Training:** Educate users about the importance of MFA and the process for registering their multi-factor authentication methods.
- **Temporary Exceptions:** If immediate access is required, consider creating a conditional access policy to exclude the user temporarily while they complete the necessary setup.

#### 5. Documentation for Guidance

- [Azure Active Directory Conditional Access](https://docs.microsoft.com/en-us/azure/active-directory/conditional-access/)
- [MFA Registration Overview](https://docs.microsoft.com/en-us/azure/active-directory/authentication/howto-mfa-userstates#multi-factor-authentication)
- [Troubleshoot Multi-Factor Authentication](https://docs.microsoft.com/en-us/azure/active-directory/authentication/troubleshoot-mfa)

#### 6. Advice for Data Collection

- **Event Viewer Logs:**
  - Check the Event Viewer on the affected user’s device for any related authentication events. 
  - Look specifically under Windows Logs > Security for failed logon attempts.

- **Network Trace (Nettrace):**
  - Use `netsh trace start capture=yes` to capture a network trace during the authentication attempt. This can help provide insights about any network-related issues.

- **Fiddler HTTP Debugging:**
  - Install Fiddler and capture traffic related to the authentication attempt to identify if there are any network/request-related issues.
  
By following these guidelines, you can systematically address AADSTS50079 errors and help users complete their multifactor authentication requirements successfully.