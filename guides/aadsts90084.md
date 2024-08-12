# AADSTS90084: OrgIdWsFederationGuestNotAllowed - Guest accounts aren't allowed for this site.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS90084

The error code AADSTS90084 indicates that a guest account does not have permission to access the specified resource because the organization does not allow guest accounts for the site.

#### Initial Diagnostic Steps

1. **Understand the Context**:
   - Confirm the exact scenario in which the error occurs (e.g., specific application, service, during sign-in).
   - Identify whether the user attempting to access the site is a guest user.

2. **Check Tenant Settings**:
   - Ensure you have the appropriate permissions to view or modify tenant settings in Azure AD.
   - Identify if the tenant allows guest access, check Admin Portal settings.

3. **Collect User Information**:
   - Gather user details (such as their email and role).
   - Determine their account type (guest vs. member).

#### Common Issues that Cause this Error

1. **Guest Access Disabled**:
   - Organization policies may explicitly disallow guest access to certain applications or resources.

2. **Misconfigured Applications**:
   - The application may not be configured to accept guest users.

3. **Conditional Access Policies**:
   - There may be specific Conditional Access policies that restrict guest access.

4. **Group Membership**:
   - The user may not be part of the correct groups that allow access to the resource.

#### Step-by-Step Resolution Strategies

1. **Check Azure AD Guest Access Settings**:
   - Navigate to Azure Active Directory -> Users -> User settings.
   - Review "External collaboration settings" to see if guest access is allowed.

2. **Modify App Permissions**:
   - For applications that have restricted access, log into Azure Portal.
   - Go to Azure Active Directory -> Enterprise applications.
   - Locate the application, click on it, then select "Users and groups" to manage user access.
   - Invite guest users and ensure they have been granted access.

3. **Review Conditional Access Policies**:
   - Under Azure Active Directory, navigate to Security -> Conditional Access.
   - Verify that no policies are blocking guest access to the application.

4. **Group Membership Verification**:
   - Ensure the guest user is part of the required groups that provide access to the resource.
   - Navigate to "Groups" in Azure AD and check membership.

5. **Admin Action Required**:
   - If settings do not align with access needs, an Azure AD Global Administrator may need to adjust policies or settings.

#### Additional Notes or Considerations

- **Guest Policy Impact**: Changes to guest user policies can take some time to propagate across Azure AD services.
- **Azure AD Licensing**: Ensure that the Azure AD tier being used supports guest user access; some features may require higher licensing.

#### Documentation for Guidance

- [Configure Guest Access in Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/external-identities/what-is-guest-access)
- [Azure AD Application Permissions](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-app-permissions)
- [Conditional Access in Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/conditional-access/overview)

#### Advice for Data Collection

1. **Event Viewer Logs**:
   - Collect logs from the Event Viewer where any potential authentication issues may be logged:
     - Navigate to `Event Viewer -> Applications and Services Logs -> Microsoft -> Windows -> AAD`.

2. **Network Trace**:
   - Use NetTrace to capture and analyze network traffic.
   - Ensure to filter for logs concerning Azure AD or the application in question.

3. **Fiddler**:
   - Utilize Fiddler to monitor HTTP/HTTPS calls from the application you're testing.
   - Look specifically for requests that result in an AADSTS90084 error.

By following this troubleshooting guide, you'll be equipped to identify and resolve issues related to the AADSTS90084 error in an organized manner.