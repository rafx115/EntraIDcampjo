# AADSTS53011: User blocked due to risk on home tenant.


## Troubleshooting Steps
### Troubleshooting Guide: Error Code AADSTS53011 - User blocked due to risk on home tenant

#### Initial Diagnostic Steps:
1. **Ask the User to Confirm Recent Activities:** Instruct the user to recall any recent actions or changes related to their account or security settings that might have triggered a block.
2. **Check Azure Active Directory (AAD) Sign-In Logs:** Review the AAD sign-in logs for any suspicious activities, failed login attempts, or unauthorized access.
3. **Verify User Account Status:** Ensure that the user's account is not disabled or flagged for any suspicious behavior in the Azure AD Admin Portal.

#### Common Issues:
- Recent security-related activities such as password changes or multiple failed login attempts can trigger risk-based policies.
- Unrecognized device or location trying to access the user's account can be a red flag.
- Expiration of user's access token or session might cause the error.

#### Step-by-Step Resolution Strategies:
1. **User Confirmation and Contact:**
    - Have the user confirm any recent changes or activities. If everything seems normal, ask them to reach out to their IT department or Azure AD administrator for further assistance.
2. **Check for Risk Events in Azure AD:**
    - Review the risk events in Azure AD's Identity Protection: 
    - Navigate to Azure AD portal > Security > Identity Protection > Risk Detections.
    - Look for any recent risk detections related to the user in question.
3. **Clear Browser Cache and Cookies:**
    - Instruct the user to clear their browser cache and cookies to ensure a fresh login session.
4. **Reset Password and Perform MFA:**
    - If allowed and necessary, guide the user to reset their password and go through Multi-Factor Authentication (MFA) to confirm their identity and unlock the account.
5. **Adjust Conditional Access Policies:**
    - Azure AD Admin can review and adjust Conditional Access policies to unblock the user based on risk factors. Modify policies to reduce sensitivity or require additional verification steps.
6. **Check for IP Blocklist:**
    - Ensure that the user's IP address is not on a blocklist that might be causing the issue.
7. **Request Re-Verification:**
    - If all else fails, request the user to re-verify their identity through a confirmation email or phone call.

#### Additional Notes or Considerations:
- Regularly review and update your organization's security policies and educate users on best practices to prevent such incidents.
- Implementing Azure AD Identity Protection and security baselines can help in proactively detecting and mitigating risks.
- Always ensure that users have the necessary permissions and access controls set up correctly.
- Monitor the Azure AD portal for any ongoing security alerts or issues.

#### Documentation:
- Azure AD Troubleshooting Guide: [Microsoft Azure AD Troubleshooting and Support Documentation](https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/troubleshoot-azure-active-directory) 
- Azure AD Identity Protection: [Azure AD Identity Protection Documentation](https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/)

By following these steps and considerations, you should be able to effectively troubleshoot and resolve the error code AADSTS53011 related to a user blocked due to risk on the home tenant.