# AADSTS50068: SignoutInitiatorNotParticipant - Sign out has failed. The app that initiated sign out isn't a participant in the current session.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS50068 Error

The AADSTS50068 error indicates that a sign-out attempt has failed because the application that initiated the sign-out is not recognized as a participant in the current session. This can occur in various scenarios, particularly in environments using Azure Active Directory (Azure AD) and applications relying on OAuth2 or OpenID Connect protocols for authentication. Here's how you can troubleshoot this issue:

---

### Initial Diagnostic Steps:

1. **Verify the Error Context**: Identify when and where the error occurs. Note whether it happens during sign out, when launching the app, or after specific actions.
  
2. **Gather User Information**: Determine if the error affects one user or multiple users. Check if they are part of the same directory or organizational unit.
  
3. **Check Application Registration**: Ensure that the application initiating the sign-out has been correctly registered in Azure AD.

4. **Review Session State**: Investigate the session state to understand which applications are currently active within the session.

---

### Common Issues that Cause This Error:

1. **Application Configuration Issues**:
   - The application that initiated the sign-out may not be correctly registered.
   - The sign-out URL may not match the expected endpoint in Azure AD.

2. **Cross-Origin Issues**: If the sign-out is being initiated from a different domain than the one that started the authentication, Azure AD may not recognize it as a valid participant.

3. **Session Expiry**: The session may have expired or been invalidated, affecting the active session participants.

4. **Multiple Applications**: Apps that share the same session may have inconsistent configurations, leading to conflicts.

5. **Invalid Tokens**: Tokens may become invalid if they are not properly handled during the sign-in/sign-out process.

---

### Step-by-Step Resolution Strategies:

1. **Review Application Registration**:
   - Visit the Azure AD portal.
   - Go to "App registrations" and find the application initiating the sign-out.
   - Ensure that all URLs (sign-in and sign-out URLs) are correctly configured.

2. **Check for Multiple Sign-Ins**:
   - If multiple applications are involved, verify that all applications have proper permissions and are correctly configured to handle sign-out.

3. **Debugging Configuration Mistakes**:
   - Ensure that the application is listed as a participant in the "session" initiated by Azure AD.
   - Check for any update or change in permissions that might have caused the app to lose its participant status.

4. **Session Management**:
   - Invalidate any old sessions while ensuring only currently active applications are allowed.
   - Log out from all applications and clear browser sessions/cookies to see if that resolves the issue.

5. **Consider Cross-Origin Resource Sharing (CORS)**:
   - Ensure that your application is not triggering CORS issues and that CORS is properly configured in Azure.

---

### Additional Notes or Considerations:

- It's critical to ensure that applications share a common configuration for authentication to prevent conflicts.
- Regularly review application permissions and scopes to maintain a proper access chain.
- Test sign-out functionality in various browsers and environments to rule out browser-specific issues.

---

### Documentation for Guidance:

- **Azure AD Sign-In and Sign-Out Documentation**: [Microsoft Docs - Sign In and Out Users](https://docs.microsoft.com/en-us/azure/active-directory/develop/scenario-web-sign-in-overview)
- **Application Registration Essentials**: [Microsoft Docs - Azure AD App Registration](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)
- **Session Management Documentation**: [Microsoft Docs - Azure AD Session Management](https://docs.microsoft.com/en-us/azure/active-directory/develop/scenario-web-session)

---

### Advice for Data Collection:

1. **Event Viewer Logs**:
   - On Windows machines, check the Event Viewer under **Applications and Services Logs** -> **Microsoft** -> **Windows** -> **AzureAD** to find relevant logs.

2. **Network Tracing**:
   - Use tools like **Fiddler** or **Wireshark** to capture network traffic during the sign-out process. Look for failed requests and examine HTTP responses.

3. **.NET Trace**:
   - If using a .NET application, enable tracing to gather detailed information. Modify the application’s `web.config` or `appsettings.json` for logging.
   
4. **Azure Portal Logs**:
   - Review sign-in logs in the Azure AD portal for more insights about the sign-out event and participating applications.

By following this guide, you can effectively diagnose and resolve the AADSTS50068 error, ensuring seamless sign-out functionality for users in your Azure AD environment.