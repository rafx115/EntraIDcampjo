
# AADSTS90010: NotSupported - Unable to create the algorithm.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS90010 Error Code

**Description**: AADSTS90010 - NotSupported: Unable to create the algorithm.

### Initial Diagnostic Steps:
1. **Verify Error Context:** Determine where and when the error occurs, whether during login, authentication, token issuance, or in a specific application scenario.
2. **Check Relevant Logs:** Examine application logs, Azure Active Directory logs, and API logs to gather more information on the error.
3. **Review Configuration:** Check if any recent changes in the application or Azure Active Directory configurations might have caused the algorithm creation failure.

### Common Issues Causing the Error:
1. **Unsupported Algorithm:** Incorrect or unsupported cryptographic algorithm used for token generation.
2. **Missing Dependencies:** Required libraries or components for the algorithm generation might be missing.
3. **Configuration Errors:** Inappropriate configuration settings related to algorithms in the Azure Active Directory application settings.

### Step-by-Step Resolution Strategies:
1. **Update Libraries and Dependencies:**
   - Ensure that all cryptographic libraries and dependencies used in the application are updated and compatible with the algorithms supported by Azure Active Directory.
   
2. **Review Algorithm Configuration Settings:**
   - Check the authentication algorithm settings in the Azure Active Directory application configuration.
   - Verify that the algorithm configurations match the expected algorithms supported by Azure Active Directory.
   
3. **Check Token Issuance Policies:**
   - Review the token issuance policies to ensure that they are set up correctly and are in line with Azure Active Directory requirements.
   
4. **Test with Default Algorithms:**
   - Try using default cryptographic algorithms supported by Azure Active Directory to see if the error persists.
   
5. **Consult Azure Active Directory Documentation:**
   - Refer to the official Azure Active Directory documentation regarding supported algorithms, configurations, and troubleshooting steps:
     [Azure Active Directory Documentation](https://docs.microsoft.com/en-us/azure/active-directory/)

### Additional Notes or Considerations:
- **Security Implications:** Make sure to follow best practices while troubleshooting to maintain the security of the Azure Active Directory environment.
- **Collaboration:** Involve relevant stakeholders such as developers, administrators, and security teams in the troubleshooting process for a comprehensive resolution.

### Documentation for Guidance:
For detailed guidance on Azure Active Directory error codes and troubleshooting, consult the Microsoft Azure documentation:
- [Azure Active Directory Troubleshooting and Error Codes](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/multi-tenant-troubleshoot-app-configuration)