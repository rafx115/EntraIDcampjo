
# AADSTS50002: NotAllowedTenant - Sign-in failed because of a restricted proxy access on the tenant. If it's your own tenant policy, you can change your restricted tenant settings to fix this issue.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS50002 - NotAllowedTenant

#### Initial Diagnostic Steps:
1. **Confirm the Error Code:** Make sure the error code you are encountering is indeed AADSTS50002.
   
2. **Identify the Tenant:** Determine whether the tenant in question is indeed yours or if it belongs to a different organization.

3. **Check Proxy Settings:** Verify that there are no restricted proxy settings that could be causing the issue.

#### Common Issues:
- **Tenant Policy Restrictions:** The error often occurs due to restricted proxy access set by the tenant's policies.
  
- **Proxy Configuration Issues:** Incorrect proxy settings or restrictions on the network could also lead to this error.

- **Misconfiguration of Tenant Settings:** Improperly configured tenant settings can prevent successful sign-in attempts.

#### Step-by-Step Resolution Strategies:
1. **Review Tenant Policies:**
   - If the tenant policy causing the restriction is within your control, log in to your tenant admin portal.
   - Navigate to the relevant policy settings that may be causing the issue.
   - Modify the policy to allow the necessary access for successful sign-ins. 

2. **Check Proxy Settings:**
   - Ensure that the proxy settings configured in your network are not restricting access to the tenant.
   - If necessary, adjust the proxy settings to allow the required connections.

3. **Verify User Access:**
   - Check if your user account has the necessary permissions and access rights to sign in.
    
4. **Clear Browser Cache:**
   - Clear your browser cache and cookies to eliminate any stored data causing conflicts during sign-in attempts.

#### Additional Notes or Considerations:
- It is essential to have the required permissions to modify the tenant policy settings.
  
- Reach out to your organization's IT support or system administrator for assistance if needed.

- For a detailed walkthrough of fixing tenant restrictions, refer to the Microsoft documentation [here](https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-tenant-restricted-proxy).

By following these steps and best practices, you should be able to address the AADSTS50002 error related to NotAllowedTenant successfully. If the issue persists, consider seeking further guidance from your IT department or Microsoft support.