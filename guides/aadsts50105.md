
# AADSTS50105: EntitlementGrantsNotFound - The signed in user isn't assigned to a role for the signed in app. Assign the user to the app. To learn more, see the troubleshooting article for errorAADSTS50105.


## Troubleshooting Steps
Certainly! The AADSTS50105 error indicates that the user trying to access an application in Azure Active Directory (AAD) does not have the necessary role or permission assigned. To troubleshoot this error, follow the detailed guide below.

### **Troubleshooting Guide for AADSTS50105**

#### **1. Initial Diagnostic Steps**
- **Identify the Application**: Determine which application the user is trying to access when the error occurs.
- **Check User Sign-in Details**: Verify that the user is signed in with the appropriate account that should have access to the application.
- **Reproduce the Error**: Attempt to sign in using the same credentials to confirm that the error consistently occurs.

#### **2. Common Issues That Cause This Error**
- **User Not Assigned to the Application**: The most common issue is that the user has not been assigned the required role to access the application.
- **Application Not Properly Configured**: The application might not have proper configurations or role assignments set up in AAD.
- **License Assignment Issues**: The user might lack the necessary licenses associated with the roles required for the application.
- **Conditional Access Policies**: The application could have conditions preventing access based on certain policies that the user does not meet.

#### **3. Step-by-step Resolution Strategies**

**Step 1: Verify User's Role and Access**
- Go to the Azure portal: [https://portal.azure.com](https://portal.azure.com).
- Navigate to **Azure Active Directory** > **Users**.
- Search for the user in question and select their profile.
- Check under **Assigned roles** to see if the user is assigned the necessary roles for the application.

**Step 2: Assign the User to the Application**
- Go to **Azure Active Directory** > **Enterprise applications**.
- Locate the application causing the error and select it.
- Navigate to **Users and groups** from the left navigation menu.
- Click on **Add user**.
- Search for and select the user to assign them to the application.
- Choose the role they need (if applicable) and then click **Assign**.

**Step 3: Review Application Permissions**
- Within the same application settings, go to the **Permissions** section and ensure that the needed delegated permissions are granted.
- If required, grant admin consent for the permissions.

**Step 4: License Check**
- Ensure that the user has the required license for the application being accessed. Go to the user's profile and check assigned licenses.

**Step 5: Analyze Conditional Access Policies**
- Navigate to **Security** > **Conditional Access** in Azure AD to review any policies that may restrict the application access for the user.
- Ensure that the user meets the conditions listed in any policies that might restrict their access.

#### **4. Additional Notes or Considerations**
- **Role Assignment Propagation**: Changes in role assignments may take some time to propagate. If changes have been made, advise the user to wait a few minutes before trying to log in again.
- **Role Scope**: Ensure that the roles assigned specifically allow for the actions the user needs to perform in the application.
- **Multi-Tenant Applications**: If the application is multi-tenant, ensure that the user is part of the guest access if necessary.

#### **5. Documentation for Guidance**
- [Assign users to an application in Azure AD](https://learn.microsoft.com/en-us/azure/active-directory/manage-apps/add-users-application)
- [Assign Azure AD roles to users](https://learn.microsoft.com/en-us/azure/active-directory/roles/how-to-assign-roles)
- [Conditional Access in Azure AD](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/overview)

#### **6. Advice for Data Collection**
If further troubleshooting is needed, consider collecting the following data:
- **Event Viewer Logs**: Check for any relevant application or security logs on the user's machine.
- **Network Trace (NetTrace)**: Use tools like NetMon or Wireshark to capture network traffic when the user attempts to authenticate.
- **Fiddler**: Use Fiddler to see HTTP requests and responses during the login process. Check for any related error messages or status codes returned by the authentication API.

By following these steps, you should be able to troubleshoot and potentially resolve the AADSTS50105 error.