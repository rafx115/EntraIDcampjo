
# AADSTS70018: BadVerificationCode - Invalid verification code due to User typing in wrong user code for device code flow. Authorization isn't approved.


## Troubleshooting Steps
## Troubleshooting Guide: Error Code AADSTS70018 - BadVerificationCode

### Initial Diagnostic Steps:
1. **Verify User Input**: Check if the user has indeed mistyped the verification code during the device code flow.
2. **Check Authorization Status**: Confirm if the authorization approval is pending or if it has been denied.
3. **Review Logs**: Look into any relevant error logs or event logs for further insights.
4. **Confirm Device Code Flow Steps**: Ensure all steps in the device code flow process were followed correctly.

### Common Issues:
- Typing error in the verification code.
- Delay in entering the verification code which might have expired.
- Authorization not approved by the user.
- Incomplete or incorrect device code flow process.

### Step-by-Step Resolution Strategies:
1. **Retype Verification Code**:
   - Ask the user to carefully re-enter the verification code given during the device code flow.

2. **Restart Device Code Flow**:
   - Initiate the device code flow process again to generate a new verification code.

3. **User Authorization**:
   - Ensure the user approves the authentication request when prompted.

4. **Time Sensitivity**:
   - Advise the user to enter the verification code promptly as it might have a time limit.

5. **Support Contact**:
   - Reach out to the support team for further assistance if the issue persists.

### Additional Notes or Considerations:
- Double-check the client settings and configurations for any discrepancies.
- Encourage users to pay attention to the verification code input and follow on-screen instructions accurately.

### Documentation for Guidance:
- Microsoft Azure Active Directory documentation:
  - [Troubleshoot device code flow errors](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-device-code#errorhandling)

Following the steps above should help in resolving the Error Code AADSTS70018 related to BadVerificationCode in the context of the device code flow.