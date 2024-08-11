# AADSTS90038: NationalCloudTenantRedirection - The specified tenant 'Y' belongs to the National Cloud 'X'. Current cloud instance 'Z' does not federate with X. A cloud redirect error is returned.

## Introduction

This guide will help resolve issues related to nationalcloudtenantredirection -
the specified tenant 'y' belongs to the national cloud 'x'. current cloud
instance 'z' does not federate with x. a cloud redirect error is returned..

## Prerequisites

* Access to the Azure AD portal with administrator privileges.
* The user must have already set up MFA.

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

* Check for any Azure AD conditional access policies that might be affecting the
  MFA process.
* Consider any additional security measures that might be in place.

## Additional Notes

* Refer to the
  [Azure AD documentation](https://learn.microsoft.com/en-us/azure/active-directory/)
  for more details.

## Troubleshooting Steps

Troubleshooting steps could not be generated due to an error.

## Troubleshooting Steps

Troubleshooting steps could not be generated due to an error.

## Troubleshooting Steps

**Troubleshooting Guide for AADSTS90038 Error: NationalCloudTenantRedirection**

**Initial Diagnostic Steps:**

1. **Verify Tenant Information:** Check if the specified tenant ('Y'), current
   cloud instance ('Z'), and National Cloud ('X') are correctly identified.
2. **Check Federation Settings:** Confirm if the specified cloud instance ('Z')
   has federation configured with the National Cloud ('X').
3. **Review Authentication Flow:** Look into how authentication requests are
   handled between the tenant and the cloud instance.

**Common Issues that Cause this Error:**

1. **Misconfigured Federation:** Incomplete or incorrect federation setup
   between the current cloud instance and the National Cloud.
2. **Incorrect Tenant Selection:** Selecting a tenant that does not belong to
   the current cloud instance can trigger this error.
3. **Mismatch in Cloud Instances:** Trying to access a tenant from a different
   cloud instance that is not federated with the National Cloud.

**Resolution Strategies:**

1. **Check Federation Configuration:**
   * Ensure that the current cloud instance ('Z') is federated with the National
     Cloud ('X').
   * Verify the federation settings and update them if necessary to establish a
     connection.
2. **Tenant Selection Verification:**
   * Double-check the specified tenant ('Y') and ensure it belongs to the
     correct cloud instance.
   * Choose the appropriate tenant associated with the current cloud instance.
3. **Resolve Mismatch Issues:**
   * If you are trying to access a tenant from a different cloud instance,
     consider redirecting the request to the correct instance.
   * Ensure consistency in selecting tenants across different cloud instances.

**Additional Notes or Considerations:**

* **National Cloud Access:** Check if there are any restrictions or policies in
  place that might prevent access to tenants across different cloud instances.
* **Thorough Testing:** After making any changes to the federation settings or
  tenant selection, thoroughly test the authentication flow to ensure the error
  is resolved.
* **Documentation Review:** Refer to official documentation specific to your
  cloud provider for detailed guidelines on resolving this error code in the
  context of National Cloud Tenant Redirection.
