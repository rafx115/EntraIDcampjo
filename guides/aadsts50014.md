
# AADSTS50014: GuestUserInPendingState - The user account doesn’t exist in the directory. An application likely chose the wrong tenant to sign into, and the currently logged in user was prevented from doing so since they didn't exist in your tenant. If this user should be able to sign in, add them as a guest. For further information, please visitadd B2B users.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS50014 Error

**Error Code**: AADSTS50014  
**Description**: GuestUserInPendingState - The user account doesn’t exist in the directory. An application likely chose the wrong tenant to sign into, and the currently logged-in user was prevented from doing so since they didn't exist in your tenant. If this user should be able to sign in, add them as a guest.

---

#### Initial Diagnostic Steps:

1. **Identify the User**: Determine which user is encountering the error. Gather their email, username, and any specific details about their account.

2. **Check Tenant Identification**: Verify that the application or service trying to authenticate is configured to point to the correct Azure Active Directory (AAD) tenant.

3. **Review the Event Logs**: Check your Azure AD Sign-ins audit logs for entries related to this user's login attempt. This can provide more context on the error.

4. **Verify Tenant Access**: Ensure that the user is trying to access a resource that is correctly configured to allow guest users.

---

#### Common Issues That Cause This Error:

1. **Incorrect Tenant Selected**: The application may be pointing to the wrong Azure AD tenant where the guest user does not exist.

2. **Pending Invitation**: The user has accepted an invitation but has not yet been fully provisioned or their status is still ' Pending'.

3. **User Not Added as Guest**: The user attempting to sign in is not added as a guest user in the Azure Active Directory.

4. **Expired Invitation**: The invitation sent to the user might have expired, requiring a new invitation to be sent.

5. **Domain Verification Issues**: The email domain of the user hasn’t been verified within the tenant.

---

#### Step-by-Step Resolution Strategies:

1. **Confirm Tenant Selection**:
   - Ensure that the application (like Office 365, SharePoint, etc.) is using the intended Azure AD tenant.
   - If necessary, switch accounts to the correct tenant using the Azure sign-in page.

2. **Check User Status**:
   - Navigate to Azure Portal > Azure Active Directory > Users, and search for the user.
   - If the user appears but shows a `pending` status, you may need to resend the invitation.

3. **Add Guest User**:
   - Go to Azure Active Directory.
   - Click on "Users", then select "New guest user".
   - Fill in the user's email and any other required information, then send the invitation.

4. **Resend Invitation**:
   - If the user appears in the list but is marked pending:
     - Click on the user, and select "Resend invitation".

5. **Check Invitation Expiration**:
   - Ensure the invitation has not expired. If it has expired, you will need to resend a new invitation.

6. **Domain Verification**:
   - If the user’s domain is not verified, inspect the “Custom domain names” section in Azure AD and verify the domain.

---

#### Additional Notes or Considerations:

- Always communicate with the guest user to ensure they check their email for any invitations and confirm that they are accepting it correctly.
- Ensure that the user checks their spam/junk folders in case invitations or other emails were incorrectly routed.

---

#### Documentation for Guidance:

1. **Azure AD B2B Documentation**: [Add B2B users](https://docs.microsoft.com/en-us/azure/active-directory/external-identities/what-is-b2b)
2. **Troubleshooting Azure AD B2B**: [Troubleshoot Azure AD B2B](https://docs.microsoft.com/en-us/azure/active-directory/external-identities/faq-b2b)
3. **Check User Sign-in Events**: [Sign-in logs in Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/reports-monitoring/concept-sign-ins)

---

#### Advice for Data Collection:

1. **Event Viewer Logs**:
   - If you have access to Event Viewer on Windows, check under "Windows Logs" > "Application" and "Security" for any related errors to Azure AD sign-in attempts.

2. **Network Tracing (Nettrace)**:
   - Use tools like Fiddler or Wireshark to trace network calls, especially during a sign-in attempt to see if any network-level issues are resulting in the AADSTS50014 error.

3. **Fiddler for Debugging**:
   - If using Fiddler, capture the traffic by setting it up to intercept HTTPS traffic. Pay close attention to the requests related to the sign-in process. Look for any 403 or 404 errors that might indicate misconfigurations.

These actions may help diagnose networking or application misconfigurations leading to the AADSTS50014 error.

--- 

By following this troubleshooting guide, you should be able to identify the underlying cause of the AADSTS50014 error and apply the necessary fixes.