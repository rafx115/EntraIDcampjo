
# AADSTS65005: MisconfiguredApplication - The app required resource access list doesn't contain apps discoverable by the resource, or the client app has requested access to resource, which wasn't specified in its required resource access list or Graph service returned bad request or resource not found. If the app supports SAML, you might have configured the app with the wrong Identifier (Entity). To learn more, see the troubleshooting article for errorAADSTS650056.


## Troubleshooting Steps
# AADSTS65005 Troubleshooting Guide

## Error Description
**Error Code:** AADSTS65005  
**Description:** Misconfigured Application - The app required resource access list doesn't contain apps discoverable by the resource, or the client app has requested access to a resource that wasn't specified in its required resource access list or Graph service returned bad request or resource not found. If the app supports SAML, you might have configured the app with the wrong Identifier (Entity).

---

## Initial Diagnostic Steps
1. **Verify the Error Message**: Capture the full error response, as it may contain additional context or detailed error messages. 

2. **Check Application Registration**: Go to the Azure portal and navigate to Azure Active Directory > App registrations. Locate your application and verify its settings.

3. **Review Required Resource Access**: In the app registration, go to "API permissions" and check the required permissions. Ensure that all required resources are correctly specified.

4. **SAML Configuration Check**: If your application is SAML-enabled, review the SAML configuration, including the Identifier (Entity ID) settings.

5. **Check for Typos or Misconfiguration**: Verify that there are no typographical errors in your configuration settings.

---

## Common Issues That Cause this Error
1. **Incomplete or Inaccurate API Permissions**: The application may not have the necessary permissions added to access the requested resource.

2. **Incorrect SAML Configuration**: The SAML settings (like Identifier/Entity ID) may be incorrect, leading to failures in the authentication flow.

3. **Missing or Misconfigured Redirect URIs**: The redirect URI specified during the application configuration doesn't match the one used during the OAuth flow.

4. **Resource Not Found**: The resource being accessed may not be available or may have been deleted or renamed.

5. **Invalid Scopes**: Requested scopes may not be valid or might not align with what is defined in Azure.

---

## Step-by-Step Resolution Strategies
1. **Verify Application Permissions**:
   - Go to Azure Active Directory > App registrations.
   - Select your application.
   - Click on "API permissions" and ensure that all required resources and permissions are listed.
   - If missing, click "Add a permission" and include the necessary resources.

2. **SAML Configuration**:
   - Navigate to the app's "Single sign-on" section.
   - Double-check the Identifier (Entity ID) against what is expected by the Identity Provider (IdP).
   - Ensure that all other SAML settings like Assertion Consumer Service URL, etc., are correctly configured.

3. **Update Redirect URIs**:
   - Verify Redirect URIs under Azure AD > App registrations > Your app > Authentication.
   - Ensure that the URI you are using during login corresponds to one of the registered URIs.

4. **Test Access to Resources**:
   - Use Graph Explorer (https://developer.microsoft.com/en-us/graph/graph-explorer) to test access to the resource.
   - Make sure that the resource is available and that you can retrieve data.

5. **Monitor Activity Logs**: 
   - Check the Sign-in logs in Azure AD to see if there are any further insights regarding the authentication failures.

---

## Additional Notes or Considerations
- Always ensure to test in a development or staging environment before applying changes to production.
- If multiple applications are interacting, ensure that their permissions complement each other.

---

## Documentation for Guidance
1. [Azure Active Directory App Registrations](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)
2. [API permissions in Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-app-permissions)
3. [Configure SAML-based single sign-on](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-v2-aspnet-core)
4. [Azure AD Sign-in logs](https://docs.microsoft.com/en-us/azure/active-directory/reports-monitoring/concept-sign-ins)
5. [Microsoft Graph API documentation](https://docs.microsoft.com/en-us/graph/overview)

**Test Links:** Ensure that the guides and tutorials are accessible and updated by visiting the above links.

---

## Advice for Data Collection
- Capture and log the full error messages you encounter, including any request IDs or correlation IDs for Azure support.
- Document the exact steps leading to the error for better context when seeking assistance.
- Make screenshots of configurations in the Azure portal related to API permissions and SAML settings to assess changes easily.

By following this comprehensive guide, you should be able to diagnose and resolve the AADSTS65005 error effectively.