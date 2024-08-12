
# AADSTS50199: CmsiInterrupt - For security reasons, user confirmation is required for this request. Interrupt is shown for all scheme redirects in mobile browsers.No action required. The user was asked to confirm that this app is the application they intended to sign into.This is a security feature that helps prevent spoofing attacks. This occurs because a system webview has been used to request a token for a native application.To avoid this prompt, the redirect URI should be part of the following safe list:http://https://chrome-extension:// (desktop Chrome browser only)


## Troubleshooting Steps
Certainly! The AADSTS50199 error relates to security measures that Azure Active Directory (AAD) implements to ensure that users are aware of requests that may involve sensitive authentication processes. This error is particularly relevant in mobile contexts and may lead users to feel confused when prompted for confirmation.

### Troubleshooting Guide for AADSTS50199

#### Initial Diagnostic Steps
1. **Identify the Environment**: Determine whether the error is occurring in a mobile browser or desktop environment. This error is more prominent in mobile browsers.
2. **Check Sign-In Context**: Establish whether the user is trying to authenticate with a web application or a native application through a system webview.
3. **Review Redirect URI**: Look at the redirect URI used during the authentication process. Ensure that it’s included in AAD’s whitelist.

#### Common Issues That Cause This Error
1. **Use of System Webview**: The authentication request is being made through a system webview rather than a browser, which can trigger the confirmation prompt.
2. **Invalid Redirect URI**: The redirect URI used is not registered or recognized by Azure AD as a safe domain.
3. **Browser Compatibility**: Certain specific browser settings or behaviors (like pop-up blockers) can cause issues with redirects.
4. **Authentication Library Misconfiguration**: Issues with how authentication libraries (like MSAL) are configured may lead to improper redirect URIs.

#### Step-by-Step Resolution Strategies
1. **Ensure Safe Redirect URIs**:
   - Go to the Azure portal.
   - Navigate to Azure Active Directory > App Registrations.
   - Select the application encountering the error.
   - Check the "Redirect URIs" section for proper entries. If needed, add the necessary redirect URIs, ensuring they conform to the safe listed format.
   
2. **Avoid Using System Webview**: 
   - If the application allows, configure it to use a default browser instead of a system webview for authentication. This can often be done through settings in the application invoking the authentication flow.
  
3. **User Confirmation**:
   - Communicate to users that they may see an interrupt prompt asking for consent and reassure them it's a security feature.

4. **Update Authentication Libraries**:
   - Ensure that you are using the latest version of any relevant authentication libraries (like MSAL or ADAL).
   - Review their documentation for configuration pertaining to redirect URIs and browser compatibility.

5. **Test Across Browsers**: 
   - Test the sign-in process across different browsers (Chrome, Safari, Firefox) and devices to determine if the problem is isolated to specific environments.

#### Additional Notes or Considerations
- **Educate Users**: Inform users about why they might see this prompt and reassure them that it’s a standard security feature.
- **Application Permissions**: Make sure the permissions for the application have been set correctly in the Azure AD app registration.

#### Documentation for Guidance
- [Microsoft Azure AD Authentication Documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/)
- [Use the Microsoft Authentication Library (MSAL)](https://docs.microsoft.com/en-us/azure/active-directory/develop/msal-overview)
- [Redirect URIs in Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/develop/scenario-desktop-acquire-token-overview)

#### Advice for Data Collection
- **Event Viewer Logs**: Review application logs in the Event Viewer to extract any messages related to sign-in failures.
- **Network Traces**: Use a tool like **Fiddler** to capture network requests and responses during the authentication process. Look for clues in the request and response payloads, particularly around redirect URIs.
- **Nettraces**: Collect network traces using tools like **Wireshark** if the issue persists, which may provide insights into the failure points during the authentication flow.

Implementing the above strategies and considerations will help in troubleshooting and resolving the AADSTS50199 error effectively.