# AADSTS50013: InvalidAssertion - Assertion is invalid because of various reasons - The token issuer doesn't match the API version within its valid time range -expired -malformed - Refresh token in the assertion isn't a primary refresh token. Contact the app developer.


## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS50013: InvalidAssertion

#### Initial Diagnostic Steps:
1. Confirm the specific context in which the error is occurring (e.g., during authentication, token validation, API calls).
2. Ensure that the issuer of the token matches the expected value and that the token is within its valid time range.
3. Check if the refresh token in the assertion being used is a primary refresh token.

#### Common Issues Causing the Error:
1. Token issuer mismatch with API version
2. Expired token
3. Malformed token
4. Non-primary refresh token in the assertion

#### Step-by-Step Resolution Strategies:
1. Verify the Token Issuer:
   - Ensure that the token issuer matches the expected issuer for the API being accessed.
   - Check the API version specified in the token and verify it against the API's requirements.

2. Validate Token Expiry and Format:
   - Confirm that the token has not expired. If it has, obtain a new token.
   - Check the token structure for any formatting issues or anomalies.

3. Primary Refresh Token:
   - Ensure that the refresh token in the assertion is a primary refresh token.
   - Obtain a primary refresh token if necessary and use it in the assertion.

4. Contact the App Developer:
   - If the above steps do not resolve the issue, reach out to the developer responsible for the app or authentication service for further assistance.

#### Additional Notes or Considerations:
- It's important to check the documentation or guidelines provided by the authentication service or API provider for specific troubleshooting steps.
- Regularly monitor and manage your tokens to prevent issues related to expiry and token validity.

#### Documentation for Guidance:
- Microsoft Azure Active Directory documentation: [Token Validation Error Codes](https://docs.microsoft.com/en-us/azure/active-directory/develop/reference-aadsts-errors)
- Your specific API or authentication service's documentation for handling token assertions and refresh tokens.

By following these steps and considering the common issues related to Error Code AADSTS50013, you can troubleshoot and resolve token assertion-related problems effectively. If you encounter difficulties, don't hesitate to contact the app developer or seek further support.