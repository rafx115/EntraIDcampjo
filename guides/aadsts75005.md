# AADSTS75005: Saml2MessageInvalid - Microsoft Entra doesn’t support the SAML request sent by the app for SSO. To learn more, see the troubleshooting article for errorAADSTS75005.


## Troubleshooting Steps
AADSTS75005 indicates a problem with the SAML request that your application is sending to Microsoft Entra (Azure Active Directory). This message suggests that the request may not conform to what Microsoft expects. Here’s a detailed troubleshooting guide:

### **Troubleshooting Guide for AADSTS75005**

#### **Initial Diagnostic Steps**
1. **Check the Error Message**: Gather any additional context or information from the error response returned by Microsoft Entra. Look for any specifics in the SAML response or request.
   
2. **Review Application Configuration**: Verify the configuration of your application in the Azure portal. Ensure that all settings related to SSO and SAML are correctly configured.
   
3. **Inspect SAML Request**: Capture and examine the SAML request being sent from your application. This can be done using development tools or network tracing tools.

4. **Confirm Users and Access**: Check if the user experiencing the issue is part of the correct group and has access to the application.

#### **Common Issues That Cause This Error**
1. **Malformed SAML Request**: The SAML request does not conform to the expected format or schema. Check for extraneous characters, incorrect formatting, or missing fields.

2. **Invalid Relay State**: The relay state parameter may be malformed or not supported. 

3. **Unsupported Signature**: The signature on the SAML request may not be supported or may have been generated improperly.

4. **Certificate Issues**: The application may be using an expired or incorrect certificate for signing the SAML request.

5. **Endpoint Mismatches**: The SAML request might be sent to an incorrect endpoint.

6. **Application ID Issues**: The application identifier (AppID) in the SAML request might not match the one registered in Azure.

#### **Step-by-Step Resolution Strategies**
1. **Capture SAML Request**:
   - Use tools such as Fiddler or browser’s developer tools to capture the HTTP request being sent for SSO.

2. **Validate the SAML Request**:
   - Ensure that all necessary attributes are included in the SAML request.
   - Use an online SAML validator to check if your SAML request conforms to the expected structure.

3. **Check Application Configuration**:
   - Go to the Azure portal and navigate to Azure Active Directory → Enterprise applications.
   - Select your application and make sure all SAML settings are correct, including the SSO URL, Entity ID, and Certificate.

4. **Inspect Relay State**:
   - Make sure that your relay state is a valid URL and properly encoded if necessary.
   
5. **Examine Signing Certificates**:
   - Check that the certificates used to sign your SAML requests are valid, correctly configured, and not expired.

6. **Verify SSO Endpoint**:
   - Ensure the correct SSO URL endpoint is being used in your application.

7. **Review User Access and Licenses**:
   - Ensure that the user encountering the error has an appropriate license and access to the application.

8. **Consult Logs**:
   - Look into application logs for further exceptions or errors that could provide more context.

#### **Additional Notes or Considerations**
- Ensure that any caching mechanisms are cleared after making changes to SAML configurations.
- Consider enabling detailed logging in your application to capture more specific failures.

#### **Documentation Resources**
- Azure Active Directory SAML-based Single Sign-On: [Azure Documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/scenario-saml-sso-overview)
- Troubleshooting SAML SSO Issues: [Microsoft Troubleshooting Guides](https://docs.microsoft.com/en-us/azure/active-directory/develop/troubleshoot-saml-claims)

#### **Advice for Data Collection**
- **Event Viewer Logs**: On the application server, check the event viewer logs for errors related to your application or security.
- **Network Tracing**: Use tools like NetTrace or Fiddler to capture network traffic and look for details surrounding the SAML messages.
- **Application Logs**: Enhance logging for your application where SAML requests are constructed and sent, capturing both successful and failed requests. 

By following this guide, you should be able to diagnose and resolve issues related to the AADSTS75005 error. If you're still encountering issues after following these instructions, consider reaching out to Microsoft Support for more specialized help.