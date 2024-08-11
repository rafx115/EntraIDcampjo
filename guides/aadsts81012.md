
# AADSTS81012: DesktopSsoMismatchBetweenTokenUpnAndChosenUpn - The user trying to sign in to Microsoft Entra ID is different from the user signed into the device.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS81012 Error Code

#### Initial Diagnostic Steps:
1. **Confirm Device and User Credentials**: Verify that the user attempting to sign in to Microsoft Entra ID matches the user currently logged into the device.
2. **Check for Cached Credentials**: Ensure there are no cached credentials causing a mismatch between the token UPN (User Principal Name) and the chosen UPN.

#### Common Issues Leading to Error AADSTS81012:
1. **User Switching**: Users switching between different accounts or profiles on the device.
2. **Cached Credentials**: Cached credentials stored on the device that conflict with the current user's login.
3. **Mismatch in UPN**: A discrepancy between the UPN provided during sign-in and the device's current user account.

#### Resolution Strategies:
1. **Sign Out and Sign In Again**:
   - Have the user sign out of Microsoft Entra ID and then sign in again to ensure the correct user is associated.
  
2. **Clear Cached Credentials**:
   - Clear cached credentials on the device to prevent any conflicts.

3. **Verify User's UPN**:
   - Check that the UPN used during sign-in matches the correct user profile on the device.

#### Additional Notes or Considerations:
- **User Education**: Instruct users on how to properly log in and the importance of using the correct credentials.
- **Device Management**: Consider implementing policies or tools to manage user profiles and prevent unauthorized access.

#### Documentation for Further Guidance:
- **Microsoft Azure Active Directory Error Codes Documentation**: [AADSTS81012 Error Code Reference](https://docs.microsoft.com/en-us/azure/active-directory/develop/reference-aadsts-error-codes)

By following these troubleshooting steps and considering the common issues outlined, you should be able to address the AADSTS81012 error code related to DesktopSsoMismatchBetweenTokenUpnAndChosenUpn effectively. If the issue persists, consult the official documentation for more in-depth assistance.