# AADSTS90107: InvalidXml - The request isn't valid. Make sure your data doesn't have invalid characters.


## Troubleshooting Steps
Here’s a detailed troubleshooting guide for error code **AADSTS90107**, which indicates an "InvalidXml" issue suggesting that the request isn't valid and may contain invalid characters. 

### Troubleshooting Guide for AADSTS90107

#### Initial Diagnostic Steps
1. **Identify the Context**: Determine where and when the error occurs. Is it during a login attempt via a web application, during an API call, or in another scenario?
2. **Collect Error Details**: Note the exact error message, stack trace (if available), and request data that led to the error.
3. **Monitor User Impact**: Check if the issue affects all users or specific accounts. This can help determine if it’s user-specific data causing the issue.

#### Common Issues That Cause This Error
1. **Invalid Characters in XML**: The presence of control characters, invalid escape sequences, or characters that are not permitted in XML.
2. **Malformed XML Structure**: Incorrect nesting, missing closing tags, or syntax errors in the XML.
3. **Encoding Issues**: Improper encoding may lead to characters that cannot be parsed correctly.
4. **Improperly Formatted Data**: Parameters sent in the request may include characters that conflict with XML structure, such as `<`, `>`, `&`, etc., without proper escaping.
5. **Configuration or API Changes**: Changes in API specifications or configuration may lead to incompatibilities with the current request structure.

#### Step-by-Step Resolution Strategies
1. **Validate XML Structure**:
   - Use an XML validator tool to check if the XML being sent in the request is well-formed.
   - Ensure no special characters are included without escaping them (e.g., `&` should be `&amp;`).

2. **Escape Special Characters**:
   - Properly escape any characters that are not valid in XML (e.g., `<` to `&lt;`, `>` to `&gt;`, and `&` to `&amp;`).

3. **Review Schema Requirements**:
   - Ensure that your XML adheres to the required schema. Validate it against the schema definition provided by Azure AD if available.

4. **Log and Analyze Request Payload**:
   - Enable logging on the client side to capture the full request payload that leads to the error. This helps identify any invalid inputs.

5. **Test with Minimal XML**:
   - Simplify the request XML and gradually reintroduce elements to isolate which part is causing the issue.

6. **Check Application Code**:
   - Review the code generating the XML. Look for string concatenations where user input could be directly inserted without sanitization.

7. **Review Azure AD Application Manifest**:
   - Check the application manifest in Azure AD for any misconfigurations that may relate to the requests being made.

8. **Monitor Network Traffic**:
   - If still unresolved, capture network traffic using tools like Fiddler or Wireshark to inspect the outgoing requests for anomalies.

#### Additional Notes or Considerations
- **Encoding Standard**: Ensure that the application uses UTF-8 encoding for XML documents, as other encodings may introduce invalid characters.
- **XML Namespace Issues**: If you're using namespaces in your XML, ensure they are correctly declared and utilized.

#### Documentation Where Steps Can be Found
- Azure AD Error Codes Documentation: [AADSTS Errors](https://docs.microsoft.com/en-us/azure/active-directory/develop/reference-aadsts-error-codes).
- XML Validation Tools: Consider online tools that validate against XML schemas.
- Azure AD Application Configuration: Refer to the [Azure AD Application Registration documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app).

#### Advice for Data Collection
1. **Event Viewer Logs**:
   - Check the Windows Event Viewer for any relevant logs under "Windows Logs" -> "Application" or "System" to capture application-specific issues.

2. **NetTrace**:
   - Use the .NET tracing facility for detailed logging. Ensure the `System.Net` tracing category is enabled, and capture the output to review any networking-related issues.

3. **Fiddler**:
   - Use Fiddler to capture HTTP requests/responses. Look for the exact XML request sent to Azure AD and identify any discrepancies in the data format.

By following the steps outlined in this guide, you should be able to diagnose and fix the `AADSTS90107` error effectively.