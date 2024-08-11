# AADSTS80012: OnPremisePasswordValidationAccountLogonInvalidHours - The users attempted to log on outside of the allowed hours (this is specified in AD).


## Troubleshooting Steps
#### Troubleshooting Guide: AADSTS80012 Error Code - OnPremisePasswordValidationAccountLogonInvalidHours

### Initial Diagnostic Steps:
1. Confirm that the error code AADSTS80012 you received is specifically related to the description "OnPremisePasswordValidationAccountLogonInvalidHours."
2. Verify the user's logon hours are properly configured in Active Directory (AD).
3. Check the time settings on the user's device to ensure they are accurate.
4. Confirm if other users are facing the same issue by testing multiple accounts.

### Common Issues:
1. **Incorrect Logon Hours**: Users are trying to log in outside of the permitted hours as set in Active Directory.
2. **Timezone Mismatch**: The user's device or AD may be in a different timezone causing logon hour discrepancies.
3. **AD Configuration**: Misconfiguration in the Active Directory settings can lead to this issue.

### Step-by-Step Resolution Strategies:
1. **User Communication**: Inform the user of the logon hours policy and request they try logging in during permitted hours.
2. **AD Check**:
   - Log in to the AD server.
   - Navigate to the user account properties.
   - Verify and update the logon hours to ensure they align with the organization's policy.
3. **Time Zone Verification**:
   - Check and synchronize the time zone settings on the user's device with the AD server.
4. **Test Access**:
   - Ask the user to attempt logging in during the permitted hours.
   - Monitor for successful login and recheck the logon hours settings if needed.
5. **Troubleshooting Tools**:
   - Use Microsoft's Azure AD Connect Health service to check for any synchronization issues between on-premises AD and Azure AD.
   
### Additional Notes or Considerations:
- Ensure the logon hours policy in the AD is clear and communicated to all users.
- Regularly review and update logon hours based on the organization's requirements.
- Educate users on the implications of logging in outside of permitted hours.

### Documentation:
- For more detailed step-by-step instructions, you can refer to Microsoft's official documentation on Active Directory logon hours configuration: [Setting Logon Hours in AD](https://docs.microsoft.com/en-us/powershell/module/addsadministration/set-aduser?view=windowsserver2019-ps)