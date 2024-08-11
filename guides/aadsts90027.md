# AADSTS90027: We are unable to issue tokens from this API version on the MSA tenant. Please contact the application vendor as they need to use version 2.0 of the protocol to support this.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS90027

#### Initial Diagnostic Steps:
1. Verify the current version of the API being used by your application.
2. Confirm that the MSA (Microsoft Account) tenant is configured correctly.
3. Check if the application vendor has updated their protocol version as required.
4. Review any recent changes or updates that may have impacted the authentication process.

#### Common Issues:
1. Outdated API version not supporting token issuance for MSA tenants.
2. Incorrect configuration of the application regarding Microsoft identity platform.
3. Lack of support for version 2.0 of the authentication protocol in the application.

#### Step-by-Step Resolution Strategies:
1. **Update API Version**:
   - Ensure that the application vendor has migrated to version 2.0 of the Microsoft identity platform protocol.
   - Update your application's authentication flow to support the newer protocol version.

2. **Configure MSA Tenant**:
   - Check the configuration settings of your application in the MSA tenant to ensure compatibility with version 2.0.
   - Make any necessary adjustments in the Azure portal to support the updated protocol.

3. **Communicate with Vendor**:
   - Reach out to the application vendor to inquire about their readiness to support version 2.0.
   - Request guidance or updates from the vendor to align with the required protocol version.

#### Additional Notes or Considerations:
- Ensure all stakeholders are informed of the need to transition to version 2.0 for seamless authentication.
- Regularly monitor for updates from both Microsoft and the application vendor regarding any changes in authentication protocols.

#### Documentation:
- Microsoft Identity Platform documentation provides a comprehensive guide on upgrading to version 2.0 and resolving related issues. You can find detailed steps and best practices at [Microsoft Identity Platform Documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-overview).

By following these steps and guidelines, you should be able to address the AADSTS90027 error and ensure seamless token issuance for MSA tenants in compliance with the updated authentication protocol requirements.