
# AADSTS90101: InvalidEmailAddress - The supplied data isn't a valid email address. The email address must be in the formatsomeone@example.com.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS90101 - Invalid Email Address

The error code AADSTS90101 indicates that the email address supplied does not conform to a valid format. This guide provides step-by-step troubleshooting strategies to resolve the issue.

#### Initial Diagnostic Steps

1. **Identify the Context**: Determine under what circumstances the error occurs. Is it during login, account creation, or something else?
2. **Review User Input**: Check the email address entered by the user. Look for any obvious typographical errors or formatting issues.
3. **Check Application Logs**: Look at the logs for the application where the error occurred to see if more context is provided.

#### Common Issues That Cause This Error

1. **Typographical Errors**: Spelling mistakes, incorrect domain names (e.g., `example@domain` instead of `example@example.com`).
2. **Invalid Characters**: Use of special characters or spaces not allowed in email addresses (e.g., `someone@exa mple.com`).
3. **Domain Errors**: Nonexistent domains (e.g., `someone@invalid.com`) or temporary disposable email addresses.
4. **Sign-Up Forms**: Front-end validation failures where email format isn't checked correctly before submission.
5. **Code Bugs**: In application logic that processes the email input may not validate it accurately.
6. **Use of Non-Existing Accounts**: Users may also attempt to log in with email addresses that do not exist in the directory.

#### Step-by-Step Resolution Strategies

1. **Validation of Input**:
   - Ensure the input email is correctly formatted (e.g., matches the regex `^[\w\.-]+@[\w\.-]+\.\w{2,6}$`).
   - Common format: `someone@example.com`.

2. **Correction of Data**:
   - If a typographical error is found, correct it and try again.
   - Remind users to avoid spaces or special characters outside of standard email format.

3. **Check Application Validation Logic**:
   - Review the client-side and server-side validation logic to ensure proper checking of email addresses.
   - Implement better validation mechanisms if needed.

4. **Consult Directory Logs**:
   - If possible, check the user directory (like Azure AD) to confirm if the email exists.

5. **User Guidance**:
   - Provide users with clear guidelines on how to enter their email address correctly.
   - Notify users about the valid domain formats and known issues with disposable email services.

6. **Testing**:
   - After making changes, test the email submission process with various valid and invalid email formats to ensure the system works as expected.

7. **Escalate if Necessary**:
   - If errors persist after you’ve validated inputs and corrected potential issues, consider reaching out to Azure support or your vendor for assistance.

#### Additional Notes or Considerations

1. **Email Format Standards**: Familiarize yourself with the RFC 5321 and RFC 5322 specifications for email format if you need deeper validation logic.
2. **User Education**: Providing information about valid email formats in user interfaces can reduce errors.
3. **Localization Issues**: If your application is multi-lingual, ensure that locale settings are not interfering with how email formats are validated.

#### Documentation for Guidance

- Azure Active Directory documentation:
  - [Overview of Azure AD Error Codes](https://learn.microsoft.com/en-us/azure/active-directory/develop/reference-aad-error-codes)
  - [Microsoft Error Codes and their Meanings](https://learn.microsoft.com/en-us/azure/active-directory/develop/authentication-scenarios#errors)
- General validation best practices:
  - [Email Validation Techniques](https://www.w3resource.com/python-exercises/python-python-function-exercise-40.php)

#### Advice for Data Collection

1. **Event Viewer Logs**:
   - Check application event logs on the server where the application runs for any events related to authentication failures.
   - Look for logs under Windows Logs > Application and System.

2. **Network Trace Tools**:
   - Use **Fiddler** or a similar tool to capture HTTP(S) requests and responses while attempting to authenticate. Look for any additional insights in the requests sent to the Azure authentication endpoint.
   - Enable logging in Fiddler to capture significant debugging data.

3. **Nettrace**:
   - If you are diagnosing networking issues, consider using `netsh trace` to capture network packets and analyze them for any connectivity issues with Azure services.

By following these steps, most issues leading to AADSTS90101 can be diagnosed and resolved effectively.