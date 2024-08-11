# AADSTS90010: NotSupported - Unable to create the algorithm.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS90010: "NotSupported - Unable to create the algorithm."

#### Overview:
The AADSTS90010 error indicates that there was an issue with creating the cryptographic algorithm required during the authentication process. This can happen in Azure Active Directory (AAD) when there is an issue with the configuration of app registration or token settings.

---

### Initial Diagnostic Steps:

1. **Review Error Message:**
   - Look for any additional context in the error message, such as the specific context or application when the error occurred.

2. **Check Application Registration:**
   - Verify that the Azure AD application is correctly registered and configured in the Azure portal.

3. **Inspect Authentication Flows:**
   - Determine if there were any recent changes to the authentication flow or the APIs being accessed.

4. **Review Logs:**
   - Check any logs available from the application or Azure AD sign-in logs for any preceding errors leading to this issue.

---

### Common Issues that Cause This Error:

1. **Unsupported Algorithm:**
   - The specified signing or encryption algorithm in the app registration might not be supported by the Azure environment.

2. **Configuration Changes:**
   - Recent updates or changes made to the app's authentication settings (e.g., changing the app secret or certificate) might lead to this error.

3. **Token Settings Mismatch:**
   - Mismatched token lifetime settings or signature algorithms that are not configured properly can result in this error.

4. **Library Version Issues:**
   - Using outdated libraries or SDKs when interacting with Azure AD APIs can lead to unsupported algorithm issues.

---

### Step-by-Step Resolution Strategies:

1. **Validate Algorithm Support:**
   - Access the Azure AD documentation and verify which cryptographic algorithms are supported for your application.
   - Ensure your application is using one of these supported algorithms (e.g., RS256, HS256).

2. **App Registration Check:**
   - Navigate to the Azure portal.
   - Go to "Azure Active Directory" > "App registrations" > [Your Application].
   - Check under "Authentication" to ensure the correct redirect URIs and other settings are configured.
  
3. **Inspect Token Configuration:**
   - Go to the "Token configuration" tab under your app registration.
   - Review claims and ensure that the algorithms configured are supported.

4. **Update Dependencies:**
   - Ensure your application is using the latest version of any libraries or SDKs that interact with Azure AD. Update these libraries as necessary.

5. **Policy Validation:**
   - Check if any conditional access policies or identity protection policies might be interfering with the authentication flow.

6. **Recreate App Secret/Certificates:**
   - If you’re using secrets or certificates, try regenerating them in the "Certificates & secrets" section of your app registration.

7. **Test Authentication Flow:**
   - After making changes, test the application’s authentication flow to ensure that the error is resolved.

---

### Additional Notes or Considerations:

- Make sure to check if there are environment-specific configurations that could impact the algorithms used (e.g., if you are targeting different Azure clouds).
- Keep in mind that some legacy algorithms may be deprecated, so it’s essential to refer to updated documentation.

---

### Documentation for Guidance:

- Microsoft Authentication Libraries (MSAL) documentation: [MSAL documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/msal-overview)
- Azure AD Tokens documentation: [Understanding Azure AD Tokens](https://docs.microsoft.com/en-us/azure/active-directory/develop/access-tokens)
- Azure AD App Registration tutorial: [App Registration Overview](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)

---

### Test the Documentation Reachability:

To ensure that the documentation pages can be reached, perform the following:
1. Access each documentation link in a web browser.
2. Confirm that the pages load correctly without errors.

---

### Advice for Data Collection:

- Gather logs from your application, including any authentication attempts and resulting error messages.
- Collect Azure AD sign-in logs, which provide insights into sign-in attempts and any related failures.
- If relevant, document the specific authentication flows being used and the SDKs involved in the authentication process for a clearer understanding of the context.
- Prepare environment details, such as the app registration ID, tenant ID, and any specific configurations that could impact authentication.

---

By following this guide, you should be able to perform an effective diagnosis and resolution of the AADSTS90010 error. If issues persist after trying these steps, reach out to Microsoft Support for further assistance, providing the data collected for context.