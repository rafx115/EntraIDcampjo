# AADSTS90055: TenantThrottlingError - There are too many incoming requests. This exception is thrown for blocked tenants.


## Introduction

This guide will help resolve issues related to tenantthrottlingerror - there are

too many incoming requests. this exception is thrown for blocked tenants..


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

  [Azure AD 
documentation](https://learn.microsoft.com/en-us/azure/active-directory/)
  for more details.


## Troubleshooting Steps

Troubleshooting steps could not be generated due to an error.


## Troubleshooting Steps

Troubleshooting steps could not be generated due to an error.


## Troubleshooting Steps

**Error Code: AADSTS90055 - TenantThrottlingError**

**Description:**\
This error indicates that the Azure Active Directory service has reached its
maximum capacity in handling incoming requests from a specific tenant. The
TenantThrottlingError occurs when too many requests are being made by a single
tenant within a short period of time, exceeding the allowed limit. This can
result in the tenant being blocked temporarily.

**Initial Diagnostic Steps:** 

1. **Verify Error:** Confirm that the error code AADSTS90055 is indeed being

   reported.
2. **Identify Tenant:** Determine the tenant for which the error is occurring.

3. **Check Service Status:** Ensure that Azure Active Directory services are

   functioning properly overall.
4. **Review Recent Changes:** Investigate any recent changes made to the

   involved tenant's configuration or authentication settings.
5. **External Factors:** Consider external factors such as network connectivity

   issues that may contribute to increased requests.

**Common Issues Leading to TenantThrottlingError:** 

1. **High Request Volume:** Excessive authentication or authorization requests

   from a single tenant can trigger throttling.
2. **Misconfigured Applications:** Poorly optimized applications may generate a

   large number of unnecessary requests.
3. **Bot Traffic:** Automated bots or scripts can contribute to high request

   volumes and trigger throttling.
4. **API Abuse:** Improper use of Azure AD APIs can lead to an influx of

   requests from a tenant.

**Step-by-Step Resolution Strategies:** 

1. **Reduce Request Volume:** Implement strategies to reduce the number of

   requests being sent by the affected tenant.
2. **Optimize Applications:** Review and optimize applications to minimize

   unnecessary requests and improve efficiency.
3. **Implement Retry Logic:** Incorporate retry logic in applications to handle

   throttling errors and mitigate the impact.
4. **Request Throttling:** Implement request throttling mechanisms within

   applications to regulate the volume of requests.
5. **Distribute Load:** Distribute the workload across multiple endpoints or

   servers to alleviate the burden on Azure AD services.
6. **Review Azure AD Settings:** Check Azure AD settings to ensure they align

   with best practices and adjust if necessary.
7. **Contact Support:** If the issue persists, contact Microsoft Support for

   further assistance and guidance.

**Additional Notes or Considerations:**


* **Monitoring and Alerts:** Set up monitoring for request volumes and errors to

  proactively identify potential throttling issues.

* **Compliance Considerations:** Ensure that any changes made adhere to relevant

  compliance and security requirements.

* **Educate Users:** Educate users on best practices to avoid triggering

  throttling errors inadvertently.

* **Scheduled Maintenance:** Plan periodic maintenance to optimize request

  handling and prevent long-term throttling issues.

By following these troubleshooting steps and strategies, you can address the
TenantThrottlingError (AADSTS90055) effectively and prevent recurrence in the
future.