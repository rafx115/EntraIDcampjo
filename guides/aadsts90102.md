
# AADSTS90102: InvalidUriParameter - The value must be a valid absolute URI.


## Troubleshooting Steps
Troubleshooting guide for error code AADSTS90102 (InvalidUriParameter - The value must be a valid absolute URI):

**Initial Diagnostic Steps:**
1. Start by verifying the exact context in which the error occurs (e.g., during login, token acquisition, or API access).
2. Check the specific URI parameter value that is causing this error.
3. Ensure that there are no typos or incorrect syntax in the URI parameter.
4. Confirm if the URI provided is indeed an absolute URI (starts with a scheme such as http:// or https://).

**Common Issues Causing This Error:**
1. Incorrectly formatted or incomplete URI parameters.
2. Missing scheme (e.g., http:// or https://) in the URI.
3. Including special characters in the URI that are not properly encoded.
4. Using relative URIs instead of absolute URIs.

**Step-by-Step Resolution Strategies:**
1. Check the URI Parameter Value:
   - Verify the URI parameter value provided in the request for any errors.
   - Pay close attention to the syntax and ensure it is a complete absolute URI.

2. Ensure Proper URI Formatting:
   - Confirm that the URI starts with a scheme (http:// or https://) followed by the domain and path.
   - Make sure to encode special characters in the URI if necessary.

3. Test the URI:
   - Manually try to access the URI in a web browser to ensure it is a valid absolute URI.
   - If the URI does not load in the browser, correct the URI until it becomes valid.

4. Update the URI Parameter:
   - If the URI parameter value is indeed incorrect, update it with the correct absolute URI.
   - Double-check the URI parameter syntax before proceeding.

**Additional Notes or Considerations:**
- It's crucial to follow URI specifications and encoding rules to ensure compatibility with the Azure Active Directory (AAD) authentication system.
- Clear any caching that might be causing the incorrect URI to persist in subsequent requests.
- Ensure that the URI provided is accessible and properly configured on the server side.

**Documentation for Guidance:**
You can refer to the official Azure Active Directory documentation on handling errors and troubleshooting common issues like AADSTS90102. Detailed guidance can be found in the Microsoft Docs, particularly in the Azure AD error codes documentation section.

By following these diagnostic steps and resolution strategies, you should be able to address the error code AADSTS90102 related to an InvalidUriParameter effectively.