# AADSTS90004: InvalidRequestFormat - The request isn't properly formatted.

## Introduction

This guide will help resolve issues related to invalidrequestformat - the
request isn't properly formatted..

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

Troubleshooting Guide for AADSTS90004 Error Code - "InvalidRequestFormat - The
request isn't properly formatted."

1. Initial Diagnostic Steps: a. Verify and confirm the exact error message and
   code being displayed. b. Check if the error is consistent or intermittent. c.
   Confirm if the error occurs for specific users, specific applications, or all
   users attempting to access the resource.

2. Common Issues that Cause this Error: a. Missing or incorrect request
   parameters. b. Improperly formatted JSON or XML data in the request. c.
   Mismatch between the request content type and the expected format. d.
   Corrupted or incomplete request data.

3. Step-by-Step Resolution Strategies:

   Step 1: Validate Request Parameters

   * Check the request parameters to ensure they are correctly formatted and
     match the expected structure.
   * Verify that all required parameters are included and have appropriate
     values.

   Step 2: Validate JSON or XML Data

   * If the request includes JSON or XML data, validate that it is correctly
     formatted.
   * Use tools like JSONLint or XML validators to ensure the data is valid.

   Step 3: Verify Content-Type Header

   * Check the Content-Type header in the request to ensure it matches the
     expected format (e.g., application/json, application/xml).
   * Make sure the request body matches the specified content-type.

   Step 4: Review Request Data

   * Analyze the entire request payload and ensure there are no missing or
     malformed sections.
   * Consider capturing and reviewing the network traffic using tools like
     Fiddler or Wireshark for further insights.

   Step 5: Test with Sample Requests

   * Use sample requests provided by the service provider to compare with your
     current request format.
   * Execute test requests with valid data to isolate the issue and identify
     discrepancies.

4. Additional Notes or Considerations:
   * Check for any recent changes in the application or authentication flow that
     could have impacted the request format.
   * Collaborate with the API provider or application support team for guidance
     if the issue persists.
   * Consider implementing proper error handling mechanisms to provide detailed
     error responses for easier troubleshooting.

By following these troubleshooting steps, you should be able to identify and
resolve the AADSTS90004 error related to the "InvalidRequestFormat" issue
effectively.
