
# AADSTS90038: NationalCloudTenantRedirection - The specified tenant 'Y' belongs to the National Cloud 'X'. Current cloud instance 'Z' does not federate with X. A cloud redirect error is returned.


## Troubleshooting Steps
### Troubleshooting Guide for AADSTS90038 Error

#### Overview of Error
The error code **AADSTS90038** indicates that there is an issue with tenant redirection in Azure Active Directory (AAD). Specifically, it suggests a mismatch between the cloud instance you are currently using and the national cloud the tenant belongs to, leading to a situation where the environment cannot federate due to this discrepancy.

---

### Initial Diagnostic Steps
1. **Confirm Tenant ID and Directory:**
   - Verify that you are using the correct tenant ID or domain name associated with your Azure AD directory. You may be trying to access a tenant that belongs to a different national cloud.

2. **Check Current Cloud Instance:**
   - Identify which Azure Environment you are currently connected to. Different national clouds include:
     - Azure Public
     - Azure China
     - Azure Germany
     - Azure Government

3. **Examine the Error Message:**
   - The error message specifically mentions both the tenant (Y) and the cloud instance (Z). Make note of both to aid further investigation.

---

### Common Issues Causing this Error
1. **Accessing the Wrong National Cloud:**
   - Attempting to access a tenant in a different national cloud without proper redirection or federation settings.

2. **Tenant Misconfiguration:**
   - The tenant may be misconfigured to allow access only from specific national clouds.

3. **Incorrectly Set URLs:**
   - Application or service URLs may point to the wrong cloud instance, leading to redirect issues.

4. **User Context:**
   - The user account you are trying to authenticate may not be associated with the correct tenant or national cloud.

---

### Step-by-Step Resolution Strategies

1. **Verify Tenant Information:**
   - Use Azure CLI or Azure PowerShell to confirm tenant details:
     ```bash
     az account show
     ```
   - Ensure the output correctly reflects the expected tenant information.

2. **Check Azure Service URLs:**
   - Confirm that your applications are targeting the right national cloud endpoints. For example:
     - Public: `https://login.microsoftonline.com`
     - Government: `https://login-us.microsoftonline.com`
     - Germany: `https://login.microsoftonline.de`
     - China: `https://login.chinacloudapi.cn`

3. **Access Control Review:**
   - Review the access control policies on the tenant to ensure they are set up to allow users from the current national cloud.

4. **User Assignment Review:**
   - Check if the user contacting the service or application is assigned the correct role in the tenant and belongs to the respective cloud.

5. **Contact Support:**
   - If the above steps do not work and you suspect a deeper issue with federation settings or cloud misconfigurations, reach out to Microsoft Support for assistance.

---

### Additional Notes or Considerations
- Ensure that the administrative access or permissions are correctly configured in both the tenant and the resource requiring access.
- Consider any recent changes in configurations, services, or policy updates that may have affected access.

---

### Documentation for Guidance
- Azure AD Documentation: [Manage Azure Active Directory tenants](https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/manage-tenants)
- Authentication and Authorization in Azure: [Microsoft Identity Platform Documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/)
- National Clouds Overview: [Azure National Clouds](https://docs.microsoft.com/en-us/azure/azure-government/)

---

### Advice for Data Collection
If you need to collect logs or data to assist in troubleshooting, consider the following methods:

1. **Event Viewer Logs:**
   - Look into the Event Viewer on the machine initiating the requests. Check under Applications and Service Logs > Microsoft > Windows > AzureAD for relevant logs.
   
2. **Network Tracing (NetTrace):**
   - Use `NetTrace` to capture network traffic:
     - Open Command Prompt as Administrator and run the following command:
       ```bash
       netsh trace start capture=yes traceFile=c:\path\to\trace.etl
       ```

3. **Fiddler:**
   - If you are debugging an application, consider using Fiddler to capture HTTP traffic:
     - Configure Fiddler to decrypt HTTPS traffic, allowing you to inspect requests and responses.

4. **Log and Error Capture:**
   - Ensure logging is enabled in your application to capture detailed error messages and diagnostic context surrounding the failures.

By following the above steps, you should be able to diagnose and resolve the AADSTS90038 error effectively.