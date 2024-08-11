
# AADSTS90015: QueryStringTooLong - The query string is too long.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS90015: QueryStringTooLong

**Error Code Description**: AADSTS90015 indicates that the query string in the URL is too long for Azure Active Directory (AAD) to process. This commonly occurs in contexts where a lot of data is passed in the URL, such as during authentication requests or callback URLs.

---

### Initial Diagnostic Steps
1. **Reproduce the Issue**:
   - Attempt to reproduce the error by navigating to the URL or performing the action that triggers the error.
   - Take note of the exact URL causing the error for analysis.

2. **Check the Length of the Query String**:
   - Measure the length of the query string (the part after the `?` in the URL). Azure has limitations on URL lengths, generally around 2048 characters for GET requests.

3. **Inspect Logs**:
   - Review server logs, application logs, or Azure AD logs to find any additional context or user actions leading to the error.

---

### Common Issues that Cause this Error
1. **Excessive State Parameters**: The state parameter often holds information about the user session or application state and may accumulate unnecessary data.
   
2. **Large Payloads in URLs**: When passing complex parameters or large lists of items via query strings, the cumulative size can exceed the limit.

3. **Improper Redirects**: Applications that improperly assemble redirect URLs can inadvertently add excessive query parameters.

4. **Use of URL Encoding**: Sometimes, data that could be sent via POST requests is sent via GET, mistakenly increasing the URL length through encoding.

---

### Step-by-Step Resolution Strategies
#### Step 1: Optimize Query String Usage
- **Reduce Unnecessary Parameters**:
  - Review the URL construction and eliminate any unnecessary parameters being passed in the query string.

- **Use POST Requests for Large Payloads**:
  - If passing a large amount of data, consider switching from GET to POST which allows sending data in the body of the request.

#### Step 2: Modify Redirect and State Management
- **Shorten State Parameter**:
  - If using state parameters, ensure they are concise. Avoid sending unnecessary session or application data.

- **Reevaluate Redirection Logic**:
  - Review your application’s redirect logic to ensure it does not add extraneous query parameters.

#### Step 3: Encryption or Encoding
- **Consider Encrypting State Information**:
  - If session information must be passed, consider encrypting it instead of sending it in a plain string format.

#### Step 4: Testing
- After implementing the changes, test to ensure that the error no longer occurs. Take note of query string lengths to ensure they remain within acceptable limits.

---

### Additional Notes or Considerations
- Keep in mind that URL length limits can vary slightly based on different browsers and web servers. It is best practice to stay well below the threshold to avoid issues across different environments.
- Monitor the application for changes, as future updates or user inputs can inadvertently lead to increased query string lengths.

---

### Documentation for Guidance
- [Microsoft Documentation on Azure Active Directory Errors](https://learn.microsoft.com/en-us/azure/active-directory/develop/reference-aad-errors)
- [Best Practices for Secure Application Development](https://learn.microsoft.com/en-us/azure/architecture/best-practices/)
- [HTTP Request Length Limits Documentation](https://learn.microsoft.com/en-us/iis/configuration/system.webserver/serverruntime/#maximumurllength)

---

### Test Documentation Reachability
You can reach the Azure documentation pages for the error details at [Microsoft AAD Errors Reference](https://learn.microsoft.com/en-us/azure/active-directory/develop/reference-aad-errors). Navigate there to verify the content.

---

### Advice for Data Collection
- Create a log of the specific requests that failed, including:
  - The full URL requested.
  - The length of the query string.
  - Any relevant user actions leading up to the error.
- Utilize monitoring tools (like Application Insights) to gain insights into user behavior and application performance.
- Consider capturing screenshots or error messages to document the issue and approach.

---

By following these steps, you should be able to identify and resolve issues related to the AADSTS90015 error effectively. If problems persist, consider reaching out to Microsoft Support for assistance.