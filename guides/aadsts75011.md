# AADSTS75011: NoMatchedAuthnContextInOutputClaims - The authentication method by which the user authenticated with the service doesn't match requested authentication method. To learn more, see the troubleshooting article for errorAADSTS75011.


## Troubleshooting Steps
Certainly! The error code **AADSTS75011** occurs when there is a mismatch between the authentication method used by the user and the authentication methods that are requested or expected by the service. This can often happen when Conditional Access policies are in place, or when specific authentication contexts are expected based on how the application is configured. 

Here’s a detailed troubleshooting guide to resolve this issue:

### 1. Initial Diagnostic Steps
- **Check the Error Message**: Review the full error message to understand the context—specifically what authentication method was used and what was expected.
- **Log Analysis**: Gather logs from the application attempting the authentication, as logs may indicate which authentication method was attempted and if there were any discrepancies.

### 2. Common Issues that Cause This Error
- **Conditional Access Policies**: Policies may be in place that require specific authentication methods (e.g., Multi-Factor Authentication) that were not met during the sign-in.
- **User Account Configuration**: The user’s account may be configured to require certain authentication methods that are not being utilized.
- **Application Configuration**: The application may be configured to require particular claims or authentication contexts that are not being satisfied.
- **Token Lifetime**: Sometimes, the tokens issued may be stale or not cover the necessary scopes or claims.

### 3. Step-by-Step Resolution Strategies

#### Step 1: Check Conditional Access Policies
1. **Navigate to Azure AD**: Go to the Azure portal and navigate to Azure Active Directory.
2. **Access Conditional Access**: Under Security, access Conditional Access policies.
3. **Review Policies**: Check for any policies that might impact user authentication methods and ensure that the user's account complies with the requirements.

#### Step 2: Review User Account Details
1. **Check Authentication Methods**: In Azure AD, go to Users, find the affected user, and review their authentication methods configured under "Authentication methods."
2. **Ensure Compliance**: Make sure that the user’s account is set up to meet the expected authentication methods of the application.

#### Step 3: Validate Application Configuration
1. **Inspect App Registration**: Go to Azure Active Directory > App registrations and select the problematic application.
2. **Review Authentication Settings**: Check the authentication settings and supported authentication scenarios (e.g., single sign-on options).
3. **Check Required Claims**: Confirm that the application’s manifest specifies the required claims and that there’s a match with what the user’s authentication context provides.

#### Step 4: Test Authentication Methods
1. **Using an incognito window**: Attempt the sign-in from a private browser session to eliminate cached credentials.
2. **Audit sign-in logs**: Use Azure AD sign-in logs to see if the user is receiving the correct authentication prompts and if errors are logged.

#### Step 5: Work with Support
- **Escalate if needed**: If you cannot locate the cause of the error, consider raising a ticket with Azure support with detailed logs and descriptions of the troubleshooting steps that have been followed.

### 4. Additional Notes or Considerations
- Ensure that users are trained on any new authentication methods implemented as part of Conditional Access policy changes.
- Monitor reports for failed sign-ins regularly to identify patterns that could indicate wider configuration issues.

### 5. Documentation References
- For detailed guidance regarding Conditional Access and multi-factor authentication: [Microsoft Docs - Conditional Access](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/)
- For Azure AD sign-in logs: [Microsoft Docs - Sign-in logs](https://learn.microsoft.com/en-us/azure/active-directory/reports-monitoring/concept-sign-ins)

### 6. Testing Documentation Reachability
- Check the links provided for accessing Microsoft documentation. Here's a quick test directive: Open the links provided above in your browser to confirm they lead to the desired documentation.

### 7. Advice for Data Collection
- Collect detailed logs from both the user side and the application side during authentication attempts.
- Gather information on the specific authentication methods available to the user and any changes in policy or application configuration.
- Document error messages, timestamps of failures, and context in which the error occurs to assist in troubleshooting.

By following these steps, you should be able to identify and resolve the AADSTS75011 error effectively. Always ensure that users are educated about the authentication processes in place to mitigate similar issues in the future.