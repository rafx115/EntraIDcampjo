
# AADSTS90093: GraphUserUnauthorized - Graph returned with a forbidden error code for the request.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS90093 - GraphUserUnauthorized

The error code AADSTS90093 indicates that a request to Microsoft Graph API has been denied due to insufficient permissions or authorization issues. This guide will help you diagnose and resolve the problem.

---

#### **1. Initial Diagnostic Steps**

- **Confirm the Error**: Verify that the error is indeed AADSTS90093, clearly noting the context in which it arises (e.g., API call, Azure app authentication).

- **Check Permissions**:
  - Review the permissions granted to the Azure AD application in the Azure portal.
  - Ensure that the application has the necessary permissions to access the user/resource you're trying to reach.

- **Review User Role**: Check if the user making the request has the necessary roles assigned to access the requested resource.

- **Identify the API Call**: Determine which Microsoft Graph API endpoint is being called when the error occurs. This will help to narrow down permission needs.

---

#### **2. Common Issues That Cause This Error**

- **Insufficient Permissions**:
  - The application does not have the required permissions to access the requested resource. For example, trying to access user data without User.Read.All permission.

- **Consent Not Granted**: Permissions may require admin consent and need to be granted explicitly.

- **Incorrect Scopes**: The scopes requested during the OAuth 2.0 flow may be incorrect or lacking.

- **User Not Assigned to App**: The user or group may not be assigned to the application.

---

#### **3. Step-by-Step Resolution Strategies**

**Step 1: Check Azure AD Application Permissions**
1. Log in to the [Azure Portal](https://portal.azure.com/).
2. Navigate to **Azure Active Directory** > **App registrations**.
3. Find and select your app.
4. Go to **API permissions**.
5. Ensure the necessary Microsoft Graph permissions are listed (e.g., User.Read, User.Read.All, etc.).
6. If permissions need to be added, click on **Add a permission** and choose Microsoft Graph.

**Step 2: Admin Consent**
1. After verifying or adding permissions, ensure that any permissions requiring admin consent are granted.
2. Click **Grant admin consent** to apply.

**Step 3: Review User Roles and Assignment**
1. Navigate to Azure Active Directory > **Users**.
2. Find the user experiencing the issue.
3. Confirm that the user is assigned to the application under **Assigned roles**.

**Step 4: Adjust OAuth Scope in Application Code**
1. Adjust the OAuth request to ensure that the requested scopes are correct.
2. Common examples of scopes for Graph API are `User.Read` or `User.Read.All`.

**Step 5: Testing the Configuration**
1. After changes have been made, test the application again to see if it resolves the error.

---

#### **4. Additional Notes or Considerations**

- **API Limits & Throttling**: Be aware of Microsoft Graph rate limits, which could cause temporary authorization issues if applications exceed call limits.

- **Service Principal**: If using a service principal for application access, ensure it has been granted the correct permissions.

- **Time Synchronization**: Confirm that time settings on client machines or servers are accurate, as authentication tokens may fail if the system time is significantly off.

---

#### **5. Documentation Reference**

- Microsoft Identity platform and API permissions: [Microsoft Documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/scenario-desktop-graph-overview)
- Microsoft Graph permissions reference: [Permission reference](https://docs.microsoft.com/en-us/graph/permissions-reference)

---

#### **6. Advice for Data Collection**

- **Event Viewer Logs**:
  - Check the event logs on the machine where the application runs. Look for application errors and warnings regarding authentication or permission issues.

- **Network Tracing**:
  - Use Fiddler or similar tools to capture the HTTP requests and responses to Microsoft Graph API. Review the requests to ensure the expected tokens and scopes are being sent.

- **NetTrace**: 
  - If the application is .NET-based, use tools like in-built logging or frameworks such as Application Insights to capture detailed runtime log data.

By following these steps systematically, you should be able to diagnose and resolve the AADSTS90093 error effectively. If issues persist, consider reaching out to Microsoft support for further assistance.