# AADSTS90107: InvalidXml - The request isn't valid. Make sure your data doesn't have invalid characters.


## Troubleshooting Steps
## Troubleshooting Guide for AADSTS90107 - InvalidXml

### Overview
The error code AADSTS90107 indicates an issue with the XML request being sent to Azure Active Directory (AAD). It suggests that there are invalid characters or unexpected formatting in the XML data. This guide provides a systematic approach to diagnosing and resolving the error.

### Initial Diagnostic Steps
1. **Identify the Context**:
   - Determine when and where the error occurs (e.g., during authentication, token requests, etc.)
   - Check if the error is reproducible consistently or if it's intermittent.

2. **Review the Error Message**:
   - Examine the complete error message and any additional details. Look for specific components mentioned that might help identify the problematic XML section.

3. **Check Logs**:
   - Review application logs where the error occurred. Logging frameworks might show more details about the XML being sent.

4. **Network Monitoring**:
   - Use tools like Fiddler or Postman to capture the outgoing request to AAD and inspect the raw XML being sent.

### Common Issues that Cause this Error
1. **Invalid Characters**:
   - Special characters (e.g., &, <, >, ', ") that are not properly escaped may lead to invalid XML.
   
2. **Malformed XML Structure**:
   - Missing closing tags or mismatched tags can result in invalid XML requests.

3. **Incorrect Encoding**:
   - The XML request must be properly encoded. If using UTF-8, ensure that the XML declaration is set appropriately.

4. **Empty or Missing Elements**:
   - Required XML elements are either empty or entirely missing.

5. **Whitespace Issues**:
   - Extra spaces, tabs, or new lines in unexpected places can sometimes lead to XML parsing failures.

### Step-by-Step Resolution Strategies
1. **Inspect the XML**:
   - Capture and examine the XML payload being sent. Look for issues with the structure and characters.

2. **Validate the XML**:
   - Use an XML validation tool or online XML validator to check for well-formedness and correctness.

3. **Escape Special Characters**:
   - Ensure that any special characters within the XML content are appropriately escaped. For example:
     - `&` should be `&amp;`
     - `<` should be `&lt;`
     - `>` should be `&gt;`
     - `"` should be `&quot;`
     - `'` should be `&apos;`

4. **Correct Encoding**:
   - Verify the encoding of the XML document. Ensure it is set to UTF-8, which is the expected encoding for AAD XML requests.

5. **Check Required Elements**:
   - Confirm that all required elements exist and contain valid data.

6. **Remove Unnecessary Whitespace**:
   - Trim whitespace before and after XML elements where applicable.

7. **Re-Test**:
   - After making changes, re-test the request to confirm that the error is resolved.

### Additional Notes or Considerations
- Ensure that your application is adhering to the latest AAD standards, as XML structure requirements may change over time.
- If multiple systems are involved, verify that all systems are generating XML in a compatible manner.
- If you're integrating with third-party systems, ensure their XML output is valid.

### Documentation for Guidance
- Microsoft Azure AD Documentation: [Azure Active Directory](https://learn.microsoft.com/en-us/azure/active-directory/)
- XML Best Practices: [XML Guide](https://www.w3schools.com/xml/xml_bestpractices.asp)

### Test Documentation Reachability
- Verify that the links provided for documentation are accessible by navigating to the URLs directly in your web browser to confirm they're reachable.

### Advice for Data Collection
- Collect XML samples that trigger the error.
- Capture the application logs and network requests (e.g., using Fiddler or Wireshark) that provide insights into the request being sent.
- Document the exact error code and messages you're receiving to aid in support or escalation if needed.

### Conclusion
Following the steps outlined in this troubleshooting guide for error code AADSTS90107 should help identify and resolve XML-related issues when interacting with Azure Active Directory. If persistent problems occur, consider reaching out to Microsoft Support for further assistance.