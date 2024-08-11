# AADSTS50194: Application '{appId}'({appName}) isn't configured as a multitenant application. Usage of the /common endpoint isn't supported for such applications created after '{time}'. Use a tenant-specific endpoint or configure the application to be multitenant.

## Introduction
This guide will help resolve issues related to application '{appid}'({appname}) isn't configured as a multitenant application. usage of the /common endpoint isn't supported for such applications created after '{time}'. use a tenant-specific endpoint or configure the application to be multitenant..

## Prerequisites
- Access to the Azure AD portal with administrator privileges.
- The user must have already set up MFA.

## Steps to Resolve

### Step 1: Initial Actions
1. Log in to the Azure AD portal.
2. Navigate to the "Users" section.
3. Select the affected user.
4. Perform necessary actions as described for the error.

### Step 2: Verify MFA Settings
1. Ensure that the user has MFA configured.
2. If necessary, guide the user through the MFA setup process.

## Troubleshooting
- Check for any Azure AD conditional access policies that might be affecting the MFA process.
- Consider any additional security measures that might be in place.

## Additional Notes
- Refer to the [Azure AD documentation](https://learn.microsoft.com/en-us/azure/active-directory/) for more details.


## Troubleshooting Steps
Troubleshooting steps could not be generated due to an error.

## Troubleshooting Steps
Troubleshooting steps could not be generated due to an error.

## Troubleshooting Steps
### Troubleshooting Guide for Error Code AADSTS50194:

#### **Initial Diagnostic Steps:**
1. **Confirm Application Configuration:** Verify that the application in question is intended to be used as a multitenant application.
2. **Review Creation Date:** Check the creation date of the application to ensure it meets the specified requirements.
3. **Check Endpoint Usage:** Verify if the usage of the `/common` endpoint is causing the issue.

#### **Common Issues:**
- Incorrect application configuration settings.
- Misuse of the `/common` endpoint with non-multitenant applications.
- Application created after a certain date without appropriate configuration for multitenancy.

#### **Resolution Strategies:**
1. **Configure the Application as Multitenant:**
   - Access the Azure portal and navigate to Azure Active Directory.
   - Locate and select the application ('{appId}') causing the issue.
   - In the application settings, enable the option to make it multitenant.
   
2. **Update Endpoint Usage:**
   - Replace the usage of the `/common` endpoint with a tenant-specific endpoint.
   - Ensure that the endpoint used aligns with the multitenant configuration of the application.

3. **Review Application Creation Date:**
   - If the application was created after a specific date mentioned in the error message, consider reconfiguring it as a multitenant application or using tenant-specific endpoints.

#### **Additional Notes/Considerations:**
- **API Permissions:** Check and ensure that the necessary API permissions are correctly configured for the multitenant application.
- **Testing and Validation:** After making changes, test the application with different tenants to ensure that the error has been resolved.
- **Documentation and Support:** Refer to official Microsoft documentation or seek support from Azure experts if additional assistance is needed.

By following these steps and considerations, you should be able to troubleshoot and resolve the error code AADSTS50194 related to multitenant application configuration in Azure Active Directory.