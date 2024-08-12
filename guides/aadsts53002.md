# AADSTS53002: ApplicationUsedIsNotAnApprovedApp - The app used isn't an approved app for Conditional Access. User needs to use one of the apps from the list of approved apps to use in order to get access.


## Troubleshooting Steps
Certainly! The error code AADSTS53002 indicates that the application used by the user is not an approved app for Conditional Access in Azure Active Directory (Azure AD). Here is a detailed troubleshooting guide to help you resolve this issue.

### Troubleshooting Guide for AADSTS53002

#### Initial Diagnostic Steps

1. **Verify User's Access**:
   - Confirm that the user encountering the error has the appropriate permissions for accessing the application.
   - Ensure the user is assigned the necessary roles to use Conditional Access policies.

2. **Check Conditional Access Policies**:
   - Review the Conditional Access policies configured in Azure AD.
   - Identify if there are specific policies that apply to the user or the application being accessed.

3. **Identify the Application in Use**:
   - Determine which application the user is attempting to access that triggered the error.
   - This could be a third-party application or a custom-built app.

#### Common Issues That Cause This Error

1. **Unapproved Applications**:
   - The application being used may not be listed as an approved app in the Conditional Access configuration.

2. **Improper Configuration of Conditional Access**:
   - Conditional Access policies need to specify which applications are approved. If the application is not included, this error will occur.

3. **User Agent Issues**:
   - Sometimes, the user’s browser or application is not recognized as a compliant or approved application by Conditional Access.

4. **Inappropriate Conditional Access Settings**:
   - Some settings may lock out certain users or group memberships inadvertently.

#### Step-by-Step Resolution Strategies

1. **Review Current Conditional Access Policies**:
   - Go to the Azure portal: `https://portal.azure.com`
   - Navigate to **Azure Active Directory** > **Security** > **Conditional Access**.
   - Identify and review the active policies.
   - Check the **Cloud apps or actions** section to see if the intended application is listed.

2. **Add the Application to Approved List**:
   - If the application being accessed is not approved, add it to the **Cloud apps** in the corresponding Conditional Access Policy.
   - Save changes and enforce the new policy.

3. **Confirm User Agent Compliance**:
   - In the Conditional Access policy settings, confirm the assigned conditions and check the **Device platforms** and **Client apps** sections to ensure the user is within the requirements.

4. **Test the Configuration**:
   - Have the user attempt to access the application again to check if the error persists.

5. **Contact Application Vendor**:
   - If the issue continues, and the application is a third-party service, contact the vendor for support, as they might have specific requirements for Conditional Access.

6. **Adjust User Groups**:
   - Check if the user is part of the correct group that has permissions for the application.
   - Modify group memberships as necessary.

#### Additional Notes or Considerations

- **Review Licensing**: Ensure that your organization has the required license level since some Conditional Access features might need higher-tier subscriptions.
- **Logging and Monitoring**: Enabling sign-in logs can help identify if additional events are associated with this error.
- **Testing Tools**: Use tools like the Azure AD Sign-in diagnostic in the Azure portal to analyze the failed sign-in events.

#### Documentation for Guidance

- Azure AD Conditional Access Policies: [Microsoft Documentation](https://docs.microsoft.com/en-us/azure/active-directory/conditional-access/overview)
- Troubleshoot Conditional Access Policies: [Troubleshooting Guide](https://docs.microsoft.com/en-us/azure/active-directory/conditional-access/troubleshooting)
- Overview of Approved Applications for Conditional Access: [Approved Applications](https://docs.microsoft.com/en-us/azure/active-directory/conditional-access/concept-conditional-access-architecture)

#### Advice for Data Collection

- If needed, collect logs and traces for further analysis:
  - **Event Viewer Logs**: Check the Application and System logs on the user’s device for any related errors.
  - **NetTrace**: Use tools like Wireshark or Fiddler to capture network traffic while trying to access the affected application. Look for HTTP requests and responses that might indicate where the failure occurs.
  - **Fiddler**: Record a Fiddler session when trying to access the application for detailed HTTP traffic, and check for any error codes or issues in the responses.

This guide should provide a comprehensive approach for troubleshooting error AADSTS53002 related to Conditional Access in Azure Active Directory.