
# AADSTS20001: WsFedSignInResponseError - There's an issue with your federated Identity Provider. Contact your IDP to resolve this issue.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS20001: WsFedSignInResponseError

#### Initial Diagnostic Steps:
1. **Confirm Error**: Make sure the error code received is indeed AADSTS20001 with the description WsFedSignInResponseError.
2. **Check Identity Provider Status**: Verify the status of your federated Identity Provider (IDP) to ensure it is functioning normally.
3. **Review Recent Changes**: Determine if any recent changes have been made to the IDP configuration that might have caused the issue.

#### Common Issues that Cause this Error:
1. **Misconfigured IDP**: Incorrect settings or configurations on the IDP side.
2. **Expired or Invalid Certificates**: Certificates used for authentication may have expired or become invalid.
3. **Network Connectivity**: Issues with network connectivity between your application and the IDP.
4. **Mismatched Metadata**: Metadata configuration mismatch between your application and the IDP.
5. **IDP Outage**: Unavailability of the IDP due to maintenance or other reasons.

#### Step-by-Step Resolution Strategies:
1. **Contact IDP Support**: Follow the instructions in the error message and reach out to your IDP’s support team for assistance.
2. **Check Certificate Validity**: Ensure that the certificates used for authentication are valid and not expired.
3. **Review IDP Configuration**: Verify the configurations on the IDP side to ensure they align with the requirements of your application.
4. **Update Metadata**: Update the metadata configuration on both your application and the IDP to ensure they are in sync.
5. **Monitor Network Connectivity**: Check the network connectivity between your application and the IDP to identify and resolve any issues.

#### Additional Notes or Considerations:
- **Testing**: In a non-production environment, perform tests after each potential resolution step to validate the changes.
- **Documentation**: Refer to the documentation provided by your IDP for specific troubleshooting steps related to federated authentication errors.
- **Logging**: Enable detailed logging on both your application and the IDP to capture more information about the error for further analysis.

#### Documentation for Guidance:
- Microsoft Azure AD Documentation: [Troubleshoot federated identity setup issues in Azure Active Directory](https://docs.microsoft.com/en-us/azure/active-directory/hybrid/tshoot-connect-federated-identity)

By following these steps and considering the common issues that cause the AADSTS20001 error with the WsFedSignInResponseError description, you can effectively troubleshoot and resolve the problem with your federated Identity Provider.