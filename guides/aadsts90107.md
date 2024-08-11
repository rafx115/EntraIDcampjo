# AADSTS90107: InvalidXml - The request isn't valid. Make sure your data doesn't have invalid characters.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS90107 Error Code: InvalidXml

#### Initial Diagnostic Steps:
1. **Verify the Request:** Check the request being sent to ensure it adheres to the expected format.
   
2. **Review XML Data:** Check the XML data involved in the request for any invalid characters or formatting issues.
   
3. **Review Request Parameters:** Inspect the parameters being used in the request and ensure they are correctly formatted.

#### Common Issues that Cause this Error:
1. **Invalid Characters:** The presence of special characters, unsupported symbols, or malformed data in the XML content.
   
2. **Incorrect XML Structure:** Errors in the XML structure, such as missing tags, incorrect nesting, or unexpected data format.
  
3. **Encoding Issues:** Problems related to encoding the XML data or using incompatible character sets.

#### Step-by-Step Resolution Strategies:
1. **Validate XML Content:** Use an XML validator tool to ensure the XML data in the request is valid and follows the correct schema.
   
2. **Sanitize Data:** Remove any invalid characters, non-ASCII symbols, or unsupported elements from the XML content.
   
3. **Check Encoding:** Verify that the XML content is encoded properly, and the character set used is supported by the system.

#### Additional Notes or Considerations:
- **Error Details:** The error message provides specific information about the issue, such as the type of validation failure (InvalidXml).
  
- **Consult API Documentation:**  The API documentation for the service you are using should have guidelines and examples on how to format XML requests correctly.

#### Documentation for Guidance:
- Microsoft Identity Platform documentation can offer specific guidance on troubleshooting AADSTS errors: [Microsoft Identity Platform Documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/reference-aadsts-error-codes)

By following these detailed troubleshooting steps, you can effectively address the AADSTS90107 error associated with InvalidXml in your application's authentication flow.