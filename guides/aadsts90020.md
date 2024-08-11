# AADSTS90020: The SAML 1.1 Assertion is missing ImmutableID of the user. Developer error - the app is attempting to sign in without the necessary or correct authentication parameters.


## Troubleshooting Steps
Here is a detailed troubleshooting guide for resolving the error code AADSTS90020 related to a missing ImmutableID in the SAML 1.1 Assertion:

### Initial Diagnostic Steps:
1. **Confirm the Error Message:** Make sure the error message indeed states that the SAML 1.1 Assertion is missing ImmutableID of the user.
2. **Check Authentication Parameters:** Verify that the app is providing the necessary and correct authentication parameters as expected by the identity provider.

### Common Issues:
- **Incomplete SAML Assertion:** The assertion sent by the app might be missing essential attributes, such as the ImmutableID.
- **Misconfigured App:** The app may not be properly configured to send the ImmutableID attribute in the SAML assertion.
- **Incorrect User Mapping:** There could be an issue with the mapping between the user's ImmutableID and their account in the app.

### Step-by-Step Resolution Strategies:

1. **Review SAML Assertion Configuration:**
   - Ensure that the SAML assertion includes the ImmutableID attribute.
   - Make sure the attribute is correctly mapped and formatted according to the identity provider's requirements.

2. **Check App Configuration:**
   - Review the app's SAML configuration settings to ensure the ImmutableID attribute is being included in the authentication requests.
   - Update the configuration if necessary to include the ImmutableID.

3. **Verify User Mapping:**
   - Check the user account in the app to ensure that the ImmutableID is correctly associated with the user's profile.
  
4. **Test Authentication Flow:**
   - Test the authentication flow again to see if the issue has been resolved after making the necessary adjustments.

### Additional Notes or Considerations:
- **Developer Collaboration:** Work closely with the developer responsible for the app to ensure the correct implementation of SAML assertions including ImmutableID.
- **Logging and Monitoring:** Implement logging mechanisms to track SAML assertion details and monitor authentication requests for any issues.

### Documentation for Guidance:
- Microsoft Azure Active Directory (AAD) Documentation:
  - [Troubleshoot SAML-based single sign-on](https://docs.microsoft.com/en-us/azure/active-directory/develop/single-sign-on-saml-protocol#troubleshoot-saml-based-single-sign-on)

By following these steps and considering the additional notes, you should be able to address the error code AADSTS90020 related to the missing ImmutableID in the SAML 1.1 Assertion effectively.