# AADSTS50124: ClaimsTransformationInvalidInputParameter - Claims Transformation contains invalid input parameter. Contact the tenant admin to update the policy.


## Troubleshooting Steps
### Error Code: AADSTS50124 - ClaimsTransformationInvalidInputParameter

#### Initial Diagnostic Steps:
1. **Confirm the Error**: Ensure that the error code AADSTS50124 with the description "Claims Transformation contains invalid input parameter" is indeed being displayed during attempts to access Azure AD services.
  
2. **Review Logs**: Check Azure AD service logs for more detailed error information that may provide insights into the specific input parameter causing the issue.

3. **Validate User Input**: If user input is involved in the process triggering the error, verify that the input conforms to expected formats or policies.

#### Common Issues that Cause this Error:
- Incorrect input parameters supplied to Azure AD claims transformation policies.
- Issues with claims transformation logic or policy configurations.
- Lack of required permissions to modify claims transformation policies.

#### Step-by-Step Resolution Strategies:
1. **Check Claims Transformation Policies**:
   - Access Azure AD portal and navigate to the relevant claims transformation policy.
   - Review the policy configurations and parameters to identify the potential input parameter causing the error.
  
2. **Update Policy Parameters**:
   - Work with the tenant admin to update the claims transformation policy with correct and valid input parameters.
   - Ensure that the policy aligns with the expected formats and requirements.

3. **Test the Updated Policy**:
   - After updating the policy, test the Azure AD service to verify if the error has been resolved.
   - Conduct thorough testing to ensure the policy changes function as intended without errors.

4. **Verify Permissions**:
   - If the error persists, validate that the user attempting to modify the policy has the necessary permissions.
   - Ensure that appropriate access rights are granted to manage claims transformation policies.

#### Additional Notes or Considerations:
- **Audit Trails**: Keep a record of changes made to claims transformation policies for future reference and troubleshooting.
- **Collaboration**: Work closely with tenant admins or Azure support if required for resolving complex policy issues.

#### Documentation for Guidance:
- **Azure AD Claims Transformation Policies**: Microsoft documentation provides detailed information on configuring claims transformation policies. Refer to the [Azure AD documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/transform-claims) for guidance on creating and managing claims transformation policies.

By following these troubleshooting steps and collaborating with relevant stakeholders, you should be able to diagnose and resolve the error code AADSTS50124 related to claims transformation in Azure AD efficiently.