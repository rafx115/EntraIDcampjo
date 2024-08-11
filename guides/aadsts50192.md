
# AADSTS50192: Invalid Request - RawCredentialExpectedNotFound - No Credential was included in the sign-in request. Example: user is performing certificate-based authentication (CBA) and no certificate is sent (or Proxy removes) the user's certificate in the sign-in request.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS50192: Invalid Request - RawCredentialExpectedNotFound

#### Initial Diagnostic Steps:

1. **Confirm the User's Authentication Method**: Verify if the user is indeed using certificate-based authentication (CBA) to sign in.
   
2. **Review Sign-In Request**: Check the details of the sign-in request to ensure that the required credentials, such as the user's certificate, are included.

3. **Analyze Sign-In Flow**: Understand the process flow of the authentication request to identify any potential points where the credential may be missing or removed.

#### Common Issues:

- **Missing Credential**: The user's certificate is not provided in the sign-in request.
- **Credential Interception**: A proxy or intermediary removes the user's certificate from the sign-in request.
- **Invalid Certificate Format**: The certificate provided is not in the correct format or cannot be properly validated.

#### Step-by-Step Resolution Strategies:

1. **Ensure Certificate Presence**: Validate that the user's certificate is included in the sign-in request.

2. **Bypass Proxies**: If proxies are known to interfere with the sign-in request, consider bypassing or reconfiguring them to maintain the integrity of the request.

3. **Check Certificate Format**: Verify that the user's certificate is in the correct format and meets the requirements for CBA.

4. **Reattempt Sign-In**: Ask the user to initiate the sign-in process again, ensuring that the necessary credentials are included.

#### Additional Notes or Considerations:

- **Proxy Configuration**: Review proxy settings and rules to prevent interference with the authentication process.
- **Certificate Validity**: Confirm that the user's certificate is valid and has not expired.

#### Documentation for Guidance:

- **Microsoft Azure Active Directory Documentation**: [Troubleshoot common Azure Active Directory sign-in errors](https://docs.microsoft.com/en-us/azure/active-directory/hybrid/tshoot-sign-in-errors/aadst-error-code-chart#errorCode0x50192)

By following these troubleshooting steps and considering the common issues related to error code AADSTS50192, you can effectively address the "Invalid Request - RawCredentialExpectedNotFound" error in the context of certificate-based authentication.