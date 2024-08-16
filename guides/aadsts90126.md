# AADSTS90126: DebugModeEnrollTenantNotInferred - The user type isn't supported on this endpoint. The system can't infer the user's tenant from the user name.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS90126

#### Description
The error code AADSTS90126 indicates that the system is unable to determine the user's tenant from the provided username, and consequently, the user type isn't supported on the endpoint being accessed. 

#### Initial Diagnostic Steps
1. **Verify the User's Email Address**:
   - Ensure the email address used for authentication is formatted correctly and belongs to an established Azure AD tenant.

2. **Check the Endpoint**:
   - Identify what endpoint the user is attempting to access. Some endpoints are restricted based on user type (personal Microsoft accounts vs. work/school accounts).

3. **User Account Type Confirmation**:
   - Confirm whether the user is trying to access a resource that requires a work/school account versus a personal Microsoft account.

4. **Tenant Information**:
   - Ensure that the user exists in the Azure Active Directory (AAD) tenant in question. Use the Azure portal to search for the user.

#### Common Issues that Cause This Error
1. **Account Type Mismatch**:
   - The user may be trying to authenticate using a personal Microsoft account when the application expects a work/school account.

2. **User Not Present in Tenant**:
   - The user's account does not exist in the tenant; they may need to be invited or created in Azure AD.

3. **Incorrect Username**:
   - The username or email may be misspelled or includes incorrect domain parts.

4. **Forbidden API or Endpoint**:
   - The application or API the user is trying to access may impose restrictions on certain account types.

5. **Config Error in Azure AD**:
   - Incorrect configurations may lead to access issues, including API permissions that are misconfigured.

#### Step-by-Step Resolution Strategies
1. **Verify Username**:
   - Confirm the username or email address being used for authentication is accurate and belongs to a supported account. 

2. **Determine Account Type**:
   - Check if the account is a personal account or a work/school account:
     - Use `Get-AzureADUser` in PowerShell or check in Azure Portal for user type.

3. **Confirm User Exists in AAD**:
   - In the Azure portal, navigate to "Azure Active Directory" > "Users" and search for the account.

4. **Invite or Create User**:
   - If the user does not exist in the tenant, consider inviting them (for external users) or creating a new account in Azure AD.

5. **Check Application Registration**:
   - Ensure that the application registration in Azure AD supports the necessary user types and scopes required.

6. **Update Authentication Flow**:
   - If using code for authentication, ensure that the authentication flow correctly specifies the user type (work/school or personal).

7. **Use Azure Logs for Insight**:
   - Check the Azure Active Directory sign-in logs to obtain more context on the failure.

#### Additional Notes or Considerations
- Be aware that Azure AD supports different account types, and confusion can arise between personal Microsoft accounts and organizational accounts.
- Ensure that you are using the correct OAuth theme or endpoint if you are developing or configuring access.
- Users outside of the organization may need to be explicitly invited with the "Guest" role to access organizational resources.

#### Documentation for Guidance
- **Azure Active Directory User Account Types**: [Microsoft Docs: Understand Azure AD authentication](https://docs.microsoft.com/en-us/azure/active-directory/develop/authentication-scenarios)
- **Setting Up Azure AD B2B**: [Azure Active Directory B2B](https://docs.microsoft.com/en-us/azure/active-directory/external-identities/what-is-b2b)
- **Navigating Azure AD Logs**: [Sign-in logs in Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/reports-monitoring/concept-sign-ins)

#### Advice for Data Collection
- **Event Viewer Logs**: Check the application logs in the Event Viewer for any relevant entries or errors.
- **Network Tracing**: Use tools like Fiddler or Wireshark for network tracing to determine the exact requests being made during authentication.
- **NetTrace**: Follow up with NetTrace if you are running into network-related issues or when debugging authentication flows on clients.
   
These tools can help gather critical data to further analyze the authentication issues and provide additional insights into the error.