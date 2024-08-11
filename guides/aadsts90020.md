
# AADSTS90020: The SAML 1.1 Assertion is missing ImmutableID of the user. Developer error - the app is attempting to sign in without the necessary or correct authentication parameters.


## Introduction

This guide will help resolve issues related to the saml 1.1 assertion is missing
immutableid of the user. developer error - the app is attempting to sign in

without the necessary or correct authentication parameters..


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


### Troubleshooting Guide for Error Code AADSTS90020

***


#### Initial Diagnostic Steps:

1. **Verify the Error Message**:
   * Check the error code AADSTS90020 along with the description mentioning the

     missing ImmutableID in the SAML 1.1 Assertion.
2. **Review Authentication Parameters**:
   * Check the authentication parameters being used by the application to

     identify any potential issues.
3. **Examine the SAML 1.1 Assertion**:
   * Verify the contents of the SAML 1.1 Assertion to confirm if the ImmutableID

     is missing for the user.
4. **Check Developer Configuration**:
   * Review the application's configuration to ensure that the correct

     authentication parameters are being used.

***


#### Common Issues Causing Error AADSTS90020:

1. **Missing ImmutableID**:
   * The primary cause of this error is the absence of the ImmutableID for the

     user in the SAML 1.1 Assertion.
2. **Invalid Authentication Parameters**:
   * Incorrect or missing authentication parameters can lead to this error.

3. **Misconfiguration in the Application**:
   * Improper setup or configuration of the application can cause authentication

     failures.

***


#### Resolution Strategies:

1. **Update SAML 1.1 Assertion**:

   * Ensure that the SAML 1.1 Assertion includes the ImmutableID for the user.

     Update the assertion if necessary.

2. **Revise Authentication Parameters**:

   * Double-check the authentication parameters used by the application and make

     any necessary adjustments to include the required details.

3. **Developer Check**:

   * Review the application code to ensure that it is correctly handling the

     authentication parameters and the SAML assertion.

4. **Test the Application**:
   * Test the application after making the above changes to confirm that the

     error has been resolved.

***


#### Additional Notes or Considerations:


* **ImmutableID Requirement**:

  * Understand the importance of ImmutableID in the authentication process and

    make sure it is included in the SAML assertions where needed.


* **Azure AD Documentation**:

  * Refer to the Azure AD documentation for more detailed information on

    handling SAML assertions and ImmutableID requirements.


* **Logging and Monitoring**:

  * Implement proper logging and monitoring mechanisms to track any future

    authentication issues effectively.

*** 

By following the detailed troubleshooting guide provided above, you should be
able to address the error code AADSTS90020 related to the missing ImmutableID in
the SAML 1.1 Assertion successfully. If you encounter any further issues,
consider reaching out to the application's support or the Azure AD support team
for additional assistance.