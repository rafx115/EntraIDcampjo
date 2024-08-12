# AADSTS50135: PasswordChangeCompromisedPassword - Password change is required due to account risk.


## Troubleshooting Steps
Here’s a detailed troubleshooting guide for the error code AADSTS50135, which indicates that a password change is required due to account risk. 

### Troubleshooting Guide for AADSTS50135

#### **Initial Diagnostic Steps:**
1. **Verify the Error Message:**
   - Confirm the exact error code and message being received.
   
2. **Check User Status:**
   - Ensure the account showing the error is indeed the one you intend to manage.

3. **Identify Account State:**
   - Verify if the account is currently locked, on hold, or if there are any other restrictions.

4. **Review Recent Activity:**
   - Check for any recent unusual activity on the account that may have triggered the security measures.

#### **Common Issues That Cause This Error:**
1. **Suspicious Activity Detected:**
   - Unusual sign-in attempts or signs of compromise can trigger the need for a password change.

2. **Policy or Compliance Requirements:**
   - Organization policies may require password changes under certain conditions.

3. **Reset Required Due to Breaches:**
   - In case of known breaches affecting user credentials.

4. **Configuration Errors:**
   - Incorrect or outdated security settings related to the account or tenant.

#### **Step-by-Step Resolution Strategies:**
1. **Reset the Password:**
   - Advise the user to reset their password. This can usually be done through the company’s identity portal or directly through Azure AD.

   *Steps to reset:*
   - Go to the Azure Active Directory admin center.
   - Navigate to "Users".
   - Select the user affected by the error.
   - Initiate a password reset.

2. **Notify User of Security Policies:**
   - Inform the user about company policies that may require a change post a security incident.

3. **Review Security Logs:**
   - Access the Azure AD sign-in logs to view any suspicious activity related to the user's account.
   - Navigate to "Azure Active Directory" > "Sign-ins" in the Azure portal.

4. **Configure Conditional Access:**
   - Review any Conditional Access policies that might be enforcing this requirement and ensure they are correctly set.
   - Adjust risk-based conditional access policies as necessary based on your organization's requirements.

5. **Notify Admins and Security Teams:**
   - If this appears to be a widespread issue or if multiple users are affected, notify your system admins and security team to investigate further.

#### **Additional Notes or Considerations:**
- Educate users on security and how to recognize phishing attempts or social engineering tactics that could compromise their passwords.
- Ensure that users are aware of the proper steps to take if their account might have been compromised.

#### **Documentation for Further Guidance:**
- Microsoft Documentation on Azure Active Directory:
  - [Manage user passwords](https://docs.microsoft.com/en-us/azure/active-directory/users-groups-roles/users-assign-activate)
  - [Conditional Access overview](https://docs.microsoft.com/en-us/azure/active-directory/conditional-access/overview)

#### **Advice for Data Collection:**
1. **Event Viewer Logs:**
   - Look for relevant log entries under the "Application" and "Security" sections that may provide additional context related to the issue.
   - Capture logs during the time the error is generated.

2. **Network Traces:**
   - Use tools like NetTrace or Fiddler to capture network traffic and analyze authentication requests and responses for additional error details.

3. **Capture Fiddler Logs:**
   - Enable capture in Fiddler.
   - Reproduce the error, and save the logs for further analysis.

4. **Maintain User Anonymity:**
   - When collecting logs, ensure that sensitive information is masked and user privacy is respected.

By following this troubleshooting guide and performing these steps, you should be able to resolve issues related to the AADSTS50135 error code systematically.