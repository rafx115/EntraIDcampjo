# AADSTS65002: Consent between first party application '{applicationId}' and first party resource '{resourceId}' must be configured via preauthorization - applications owned and operated by Microsoft must get approval from the API owner before requesting tokens for that API. A developer in your tenant might be attempting to reuse an App ID owned by Microsoft. This error prevents them from impersonating a Microsoft application to call other APIs. They must move to another app ID they register.


## Troubleshooting Steps
# Troubleshooting Guide for AADSTS65002 Error Code

## Error Overview
Error code AADSTS65002 indicates that there is a consent issue between a first-party application and a first-party resource. Specifically, it suggests that the application in question is attempting to use an App ID owned by Microsoft without the necessary permissions, which leads to token request failures.

## Initial Diagnostic Steps
1. **Identify the Problematic Application**: 
   - Review the application ID provided in the error message (`{applicationId}`).
   - Ensure this ID corresponds to an application owned by your organization, not a Microsoft-owned application.

2. **Examine the Resource ID**:
   - Check the `{resourceId}` specified in the error message to verify if it’s a valid Microsoft resource that requires preauthorization.

3. **Access Logs**:
   - Look at the sign-in logs in Azure AD for more context regarding the failed token requests. This may provide additional insights into how the application is configured.

4. **Review Documentation**:
   - Check Microsoft documentation for AADSTS error codes and the processes surrounding consent and authorization.

## Common Issues that Cause this Error
1. **Using Microsoft’s App ID**:
   - The developer is trying to use an App ID that belongs to a Microsoft service instead of a custom registered application.

2. **Lack of Preauthorization**:
   - Applications trying to access certain APIs without proper preauthorization and consent from the API owner.

3. **Misconfiguration in Permissions**:
   - Required API permissions may not be granted to the application in Azure AD.

4. **End User Consent Not Provided**:
   - Even if permissions are granted, if user consent is required and not provided, token requests can fail.

## Step-by-Step Resolution Strategies
1. **Create a New App Registration**:
   - If you’ve determined that the App ID in use is owned by Microsoft, create a new App registration in Azure Active Directory.
     - Navigate to the Azure portal.
     - Select Azure Active Directory > App registrations > New registration.
     - Provide a name and redirect URI as necessary.

2. **Assign Required API Permissions**:
   - After registering the new application, navigate to the "API permissions" section:
     - Click on “Add a permission”.
     - Select the appropriate Microsoft APIs that your application needs to access.
     - Make sure to grant admin consent if necessary.

3. **Request Consent**:
   - If you are asking users to consent to the permissions, ensure that the proper consent framework is in place:
     - Use a consent URL format (for delegated permissions) to prompt users for consent.

4. **Inform and Deploy**:
   - Inform users and developers about the change and ensure they start using the new App ID for API calls.

5. **Test the Setup**:
   - After implementation, test the application to ensure it successfully requests tokens and interacts with the API without errors.

## Additional Notes or Considerations
- **Preconfigured Permissions**: Applications owned by Microsoft need necessary approvals and specific configurations, ensure you adhere to guidelines provided by the API owner if you are trying to access Microsoft APIs.
- **Impact on App Functionality**: Make sure that changing App IDs or permissions does not disrupt the functionality for end users.
- **Monitoring and Logging**: Implement monitoring and logging around token requests to catch similar issues early in the future.

## Documentation
Refer to the following documentation for guidance:
- [AADSTS error codes](https://docs.microsoft.com/en-us/azure/active-directory/develop/reference-aadsts-error-codes)
- [App registration overview](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)
- [API permissions in the Azure portal](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-permissions-and-consent)

### Test Documentation Accessibility
Make sure to verify the above URLs are reachable by navigating to them in a web browser.

## Advice for Data Collection
- Gather the following information to aid debugging:
  - The exact error message with `{applicationId}` and `{resourceId}`.
  - The detailed access logs corresponding to the failed authentication attempts.
  - Any relevant configuration settings from the Azure portal related to the app registration.
- Consider using tools such as Azure Monitor and Application Insights to track and log application behaviors over time.

By following these steps, you should be able to diagnose and remedy the issues causing AADSTS65002 errors effectively.