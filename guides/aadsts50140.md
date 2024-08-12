# AADSTS50140: KmsiInterrupt - This error occurred due to "Keep me signed in" interrupt when the user was signing-in. This is an expected part of the sign in flow, where a user is asked if they want to remain signed into their current browser to make further logins easier. For more information, seeThe new Microsoft Entra sign-in and “Keep me signed in” experiences rolling out now!. You canopen a support ticketwith Correlation ID, Request ID, and Error code to get more details.


## Troubleshooting Steps
Certainly! Below is a comprehensive troubleshooting guide for the error code AADSTS50140, which relates to the "Keep me signed in" feature during the sign-in process. 

### Troubleshooting Guide for AADSTS50140

#### 1. Initial Diagnostic Steps

- **Check System Status**: Confirm that there are no outages reported on the Microsoft 365 Service Health Dashboard or Microsoft Azure Service Health Dashboard.
- **Browser Compatibility**: Ensure that users are using a supported browser (such as the latest versions of Chrome, Edge, or Firefox) with up-to-date settings enabled.
- **Network Connection**: Check the user's internet connection and ensure that it is stable and secure.
- **Clear Browser Cache and Cookies**: Advise users to clear their browser cache and cookies, as corrupted data can interfere with sign-in processes.

#### 2. Common Issues that Cause this Error

- **User Interaction Required**: This error often arises when user interaction is required for signing into the "Keep me signed in" option.
- **Browser Extensions**: Extensions such as ad blockers or privacy tools can interfere with the sign-in process.
- **Cookies and Site Data Settings**: Users may have disabled cookies or have set their browser to block third-party cookies.
- **Session Expiry Issues**: If the session has expired, the user might encounter this error while trying to re-authenticate.
- **Conditional Access Policies**: There may be specific Conditional Access policies that impact the sign-in experience for the user.

#### 3. Step-by-Step Resolution Strategies

1. **User Education**:
   - Explain to users the nature of the “Keep me signed in” feature and what it entails. Specifically, inform them that they may need to click on the prompt that appears during sign-in.

2. **Browser Settings**:
   - Instruct the user to check their browser settings:
     - Ensure cookies are enabled for both first-party and third-party cookies.
     - Disable any browser extensions, especially those related to security and privacy.

3. **Session Management**:
   - Advise users to log out completely from their Microsoft accounts and try to log in again.
   - Encourage them to use an "incognito" or "private browsing" mode to see if the issue persists.

4. **Conditional Access Policies**:
   - Review Conditional Access policies in Azure Active Directory that may influence the user’s sign-in experience.

5. **Check Identity Protection**:
   - Ensure that the user's account is not flagged or under review by Azure Identity Protection.

#### 4. Additional Notes or Considerations

- **Browser Specificity**: Some users may have issues on specific browsers; testing the sign-in process in different browsers can help identify the source of the issue.
- **Mobile Applications**: If this error occurs in mobile applications, verify that the app is updated to the latest version and that it's configured properly for sign-in.

#### 5. Documentation References

- Microsoft Documentation on Azure Active Directory: [Azure Active Directory Documentation](https://docs.microsoft.com/en-us/azure/active-directory/)
- Understanding the “Keep me signed in” experience: [Keep me signed in experience](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-howto-keep-me-signed-in)

#### 6. Advice for Data Collection

- **Event Viewer Logs**: Check the Event Viewer logs for any related issues under the "Windows Logs" -> "Application" section. Look for any errors that refer to sign-in failures.
- **Nettrace**: Collect network traces using the Microsoft Network Tracing Tool to gather evidence of requests during the sign-in process. This can help identify where the process fails.
- **Fiddler**: Use Fiddler to capture HTTP(S) traffic when the user attempts to log in. Analyze the request and response traffic to identify any potential redirection issues or errors in the payload.

#### Conclusion

If the above steps do not resolve the issue, consider collecting and sharing the specified correlation ID, request ID, and error code with Microsoft Support for further analysis. This information will assist in pinpointing the exact cause of the problem.

By following these detailed diagnostic and resolution strategies, the majority of issues related to error code AADSTS50140 can be effectively addressed.