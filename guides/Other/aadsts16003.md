# AADSTS16003: SsoUserAccountNotFoundInResourceTenant - Indicates that the user hasn't been explicitly added to the tenant.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS16003 - SsoUserAccountNotFoundInResourceTenant

<<<<<<< HEAD:guides/Other/aadsts16003.md
The error code AADSTS16003 indicates that a user trying to sign in has not been explicitly added to the resource tenant. This can cause Single Sign-On (SSO) issues when dealing with Azure Active Directory (Azure AD). Heres a comprehensive guide to troubleshoot and resolve this issue.
=======
The error code AADSTS16003 indicates that a user trying to sign in has not been explicitly added to the resource tenant. This can cause Single Sign-On (SSO) issues when dealing with Azure Active Directory (Azure AD). Here�s a comprehensive guide to troubleshoot and resolve this issue.
>>>>>>> 8ca1440664e61dbdf9b1aa83f352634474c59c2f:guides/aadsts16003.md

---

### Initial Diagnostic Steps

1. **Error Confirmation**: 
   - Ensure that the error code `AADSTS16003` was received during the login process.
  
2. **User Identification**:
   - Note the specific user account experiencing the issue (email address or UPN).

3. **Tenant Verification**: 
   - Confirm the correct tenant that the user is attempting to access.
<<<<<<< HEAD:guides/Other/aadsts16003.md
   - Compare the users domain with the domain(s) associated with the resource tenant.
=======
   - Compare the user�s domain with the domain(s) associated with the resource tenant.
>>>>>>> 8ca1440664e61dbdf9b1aa83f352634474c59c2f:guides/aadsts16003.md

---

### Common Issues that Cause this Error

1. **User Not Added to the Resource Tenant**:
<<<<<<< HEAD:guides/Other/aadsts16003.md
   - The users account may not exist in the Azure Active Directory (AAD) of the resource tenant.
=======
   - The user�s account may not exist in the Azure Active Directory (AAD) of the resource tenant.
>>>>>>> 8ca1440664e61dbdf9b1aa83f352634474c59c2f:guides/aadsts16003.md

2. **Synchronization Issues**:
   - If using Azure AD B2B, the invitation to access the resource tenant may not have been sent or accepted.

3. **User Principal Name (UPN) Mismatch**:
   - The user may have a different UPN or email address in their source tenant compared to what is expected in the resource tenant.

4. **Access Policies**:
   - Policies may restrict access or require specific groups/roles to be assigned.

5. **Domain Verification**:
   - The email domain may not be verified or associated with the AAD environment.

---

### Step-by-Step Resolution Strategies

#### Step 1: Verify User Account Presence

1. **Log into Azure Portal**:
   - Navigate to Azure Active Directory.

2. **Check User List**:
   - In the AAD, go to **Users** and check if the user attempting to log in is listed.
   - If not, proceed to Step 2.

#### Step 2: Add User to Resource Tenant

1. **Invite User**:
   - In the Azure Portal, go to **Users** -> **New guest user**.
   - Enter the user's email and send an invitation.

2. **Check Invitation Status**:
   - Ensure that the user has accepted the invitation. If not, resend the invitation.

#### Step 3: Validate Domain Settings

1. **Check Domain Verification**:
<<<<<<< HEAD:guides/Other/aadsts16003.md
   - Validate that the users email domain is verified in the resource tenant under **Azure Active Directory** -> **Custom domain names**.
=======
   - Validate that the user�s email domain is verified in the resource tenant under **Azure Active Directory** -> **Custom domain names**.
>>>>>>> 8ca1440664e61dbdf9b1aa83f352634474c59c2f:guides/aadsts16003.md

#### Step 4: Confirm UPN

1. **Match UPNs**:
<<<<<<< HEAD:guides/Other/aadsts16003.md
   - Ensure that the users UPN in their original tenant matches the one being used in the resource tenant.
   
2. **Update UPN if Necessary**:
   - If theres a mismatch, update the users UPN and ensure they use the correct credentials.
=======
   - Ensure that the user�s UPN in their original tenant matches the one being used in the resource tenant.
   
2. **Update UPN if Necessary**:
   - If there�s a mismatch, update the user�s UPN and ensure they use the correct credentials.
>>>>>>> 8ca1440664e61dbdf9b1aa83f352634474c59c2f:guides/aadsts16003.md

#### Step 5: Review Access Policies

1. **Check Conditional Access Policies**:
   - Review any Conditional Access policies that may prevent access to the tenant for the user.
   - Ensure the user is in an allowed group or role if necessary.

---

### Additional Notes or Considerations

- **Log Levels**: Configure Azure AD sign-in logs to get more detailed log information. This can be helpful for analyzing the context of the login failures.
- **Error Context**: Check for any additional error messages or codes that accompany the AADSTS16003 error; they may provide further insights.

---

### Documentation and Guidance

- **Microsoft Azure Documentation**:
  - [Managing users in Azure Active Directory](https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/users)
  - [Add a guest user to your Azure AD tenant](https://docs.microsoft.com/en-us/azure/active-directory/external-identities/what-is-b2b)
  - [Troubleshoot Azure AD sign-in issues](https://docs.microsoft.com/en-us/azure/active-directory/userhelp/sign-in-help)

### Test Document Reachability

- **Testing Documentation**: Open the URLs mentioned in the documentation section to ensure they are accessible.

---

### Advice for Data Collection

1. **Capture Logs**: Collect sign-in logs from Azure AD to analyze failed sign-in attempts and get more context around the error.
2. **Gather User Details**: Document relevant details for the user encountering issues, e.g., UPN, email, tenant information.
3. **Query Audit Logs**: Check the Azure AD Audit logs to see actions performed on the user account.

By following this troubleshooting guide, you should be able to resolve the AADSTS16003 error effectively. If the issue persists after following these steps, consider reaching out to Microsoft Support for further assistance.

Category: Other