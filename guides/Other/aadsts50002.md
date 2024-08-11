# AADSTS50002: NotAllowedTenant - Sign-in failed because of a restricted proxy access on the tenant. If it's your own tenant policy, you can change your restricted tenant settings to fix this issue.


## Troubleshooting Steps
# Troubleshooting Guide for AADSTS50002: NotAllowedTenant

The error code `AADSTS50002` indicates that a sign-in attempt failed due to restricted proxy access on the tenant. This typically occurs in a multi-tenant scenario where tenants may have policies in place to restrict access for various security and operational reasons. Below is a comprehensive troubleshooting guide to diagnose and resolve this error.

## Initial Diagnostic Steps

1. **Verify Tenant Information**: 
   - Ensure that the sign-in request is targeting the correct tenant. Confirm that the user is part of that tenant.
   
2. **Check User Credentials**:
   - Validate that the user is using the correct username and password.
   - Confirm that the account is active and not locked or expired.

3. **Consult with the Admin**:
   - If youre not the tenant administrator, contact the administrator to confirm any policies regarding restricted access.

4. **Diagnose Through Logs**:
   - Review sign-in logs and any related authentication logs for further details on the failure. This can provide insights into why access was restricted.

## Common Issues That Cause This Error

1. **Restricted Proxy Access Policies**:
   - Tenant security settings may prohibit certain users or applications from accessing resources.

2. **Conditional Access Policies**:
   - Enforcement of conditional access policies that may prevent access based on location, device compliance, or user group.

3. **User Not Assigned to Application**:
   - The user attempting to sign in may not have been assigned the necessary roles or permissions to access the application.

4. **Tenant Configuration Changes**:
   - Recent changes in tenant configuration by administrators may lead to unexpected access restrictions.

## Step-by-Step Resolution Strategies

### 1. Evaluate Restricted Authentication Policies

- **Login to Azure Portal**:
  - Go to Azure Active Directory > Security > Conditional Access.
- **Review Policies**:
  - Identify any policies that might restrict access based on the user's circumstances (location, device, etc.).
- **Modify if Necessary**:
  - Adjust or remove restrictive policies if you have the necessary permissions.

### 2. Adjust Tenant Settings

- **Access Tenant Settings**:
  - Azure Portal > Azure Active Directory > Properties > User settings.
- **Update Access Settings**:
  - If you're the admin, review the user settings and modify the 'users can invite guest users' or similar settings as required.

### 3. Assign Necessary Permissions

- **Application Registrations**:
  - Ensure the user is assigned to the application needing access. Go to Azure Active Directory > App registrations > [Your Application].
- **Check API Permissions**:
  - Make sure required permissions are granted for the application and consent given by an admin.

### 4. Clear Cache and Retry

- Encourage users to clear their browser cache and cookies or attempt to access the application through an incognito/private window to eliminate local caching issues.

## Additional Notes or Considerations

- If organizational policies do not allow you to make changes, reach out to the appropriate administrative personnel for support.
- Document all steps taken in case escalation is required.

## Documentation for Reference

- **Azure AD Conditional Access**: [Conditional access policies in Azure Active Directory](https://docs.microsoft.com/en-us/azure/active-directory/conditional-access/overview)
- **Understanding and Managing Roles**: [How to manage roles in Azure Active Directory](https://docs.microsoft.com/en-us/azure/active-directory/roles/roles)
- **Troubleshooting Azure AD SSO**: [Troubleshooting single sign on in Azure Active Directory](https://docs.microsoft.com/en-us/azure/active-directory/devices/overview)

### Test the Documentation

- Please verify the above links lead to the appropriate pages related to Azure Active Directory. Each should function correctly in a standard web browser.

## Advice for Data Collection

- **Collect Diagnostic Data**:
  - Gather logs from Azure AD sign-in, application access logs, and any relevant audit logs from the Azure portal.
  - If feasible, capture any user feedback regarding the context of the error, such as device type, network location, or specific action being attempted.

By following this troubleshooting guide, you can effectively diagnose and address the AADSTS50002 error, ensuring appropriate access while maintaining security compliance within your Azure AD tenant.

Category: Other