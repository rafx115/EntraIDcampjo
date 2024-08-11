# AADSTS50013: InvalidAssertion - Assertion is invalid because of various reasons - The token issuer doesn't match the API version within its valid time range -expired -malformed - Refresh token in the assertion isn't a primary refresh token. Contact the app developer.


## Introduction

This guide will help resolve issues related to invalidassertion - assertion is

invalid because of various reasons - the token issuer doesn't match the api

version within its valid time range -expired -malformed - refresh token in the

assertion isn't a primary refresh token. contact the app developer..


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


### Troubleshooting Guide for AADSTS50013 Error Code


#### Initial Diagnostic Steps:

1. **Verify Token Issuer:** Check the token issuer to ensure it matches the API

   version and falls within the valid time range.
2. **Verify Refresh Token:** Ensure the refresh token in the assertion is a

   primary refresh token.
3. **Check Assertion Format:** Look for any expiration or formatting issues with

   the assertion.
4. **Review Integration Steps:** Confirm that the integration steps with Azure

   AD were followed correctly.


#### Common Issues:


* **Mismatched API Version:** The token issuer does not match the API version.

* **Expired Token:** The assertion contains an expired token.

* **Malformed Token:** Invalid formatting or structure of the assertion.

* **Incorrect Refresh Token:** Using a non-primary refresh token in the

  assertion.


#### Step-by-Step Resolution Strategies:

1. **Verify Token Issuer:** 

   * Ensure the token issuer matches the API version.

   * Check the validity of the token issuance time range.

2. **Refresh Token Check:** 

   * Use a primary refresh token in the assertion.

   * Check if the refresh token has the necessary permissions or scopes.

3. **Assertion Inspection:** 

   * Validate the assertion for any expiration or formatting issues.

4. **Developer Contact:**
   * If issues persist, contact the application developer for assistance.


#### Additional Notes or Considerations:


* **Update Integration:** Ensure that the application integrates with Azure AD

  correctly with the latest supported features and standards.

* **Token Expiry Management:** Implement proper token management practices to

  avoid expired tokens in assertions.

* **API Version Compatibility:** Stay updated with the supported API versions to

  avoid mismatches.

* **Primary Refresh Tokens:** Always use primary refresh tokens for assertions

  to prevent authentication issues.

By following these troubleshooting steps, you can effectively address the
AADSTS50013 error code related to the InvalidAssertion issue. If problems
persist, reaching out to the application developer for further assistance is
recommended.