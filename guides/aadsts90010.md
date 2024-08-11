
# AADSTS90010: NotSupported - Unable to create the algorithm.


## Introduction

This guide will help resolve issues related to notsupported - unable to create

the algorithm..


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

Here is a detailed troubleshooting guide for resolving the AADSTS90010 error
code with the description "NotSupported - Unable to create the algorithm."


### Initial Diagnostic Steps:

1. **Confirm the Error:** Ensure that you are consistently encountering the

   AADSTS90010 error with the specific description mentioned.
2. **Check Impact:** Determine whether the error affects all users or is limited

   to certain user accounts.
3. **Review Recent Changes:** Investigate any recent changes in your

   authentication or authorization settings that could have triggered this
   error.


### Common Issues Causing This Error:

1. **Unsupported Algorithm:** The error may occur due to the use of an

   unsupported hashing or encryption algorithm in the authentication process.
2. **Misconfigured Authentication Policies:** Incorrect configurations related

   to token issuance, encryption, or signing can lead to this error.
3. **Outdated Libraries or SDKs:** The use of outdated or incompatible

   authentication libraries or SDKs may result in algorithm-related errors.


### Step-by-Step Resolution Strategies:

1. **Update Libraries and SDKs:** 

   * Ensure that all authentication libraries and SDKs used in your application

     are up to date.
   * Check for compatibility with the authentication services you are

     integrating with.

2. **Review Authentication Policies:** 

   * Verify the algorithms used for hashing, encryption, and token signing in

     your authentication setup.
   * Align the algorithm requirements with the specific authentication service

     (such as Azure Active Directory) you are working with.

3. **Validate Token Configuration:** 

   * Double-check the token issuance policies to confirm if the algorithms being

     used are supported.
   * Adjust the token configuration to use supported algorithms if necessary.

4. **Test with Different Algorithms:** 

   * Experiment with different algorithms supported by your authentication

     service to see if the error persists.
   * Choose algorithms that are in line with industry best practices and

     security standards.

5. **Enable Detailed Logging:**    * Enable detailed logging in your 
authentication service to capture more

     information about the algorithm creation failure.
   * Analyze the logs to pinpoint the exact step or component where the error

     occurs.


### Additional Notes or Considerations:


* **Consult the Documentation:** Refer to the official documentation of your

  authentication service for algorithm requirements and best practices.

* **Engage Support:** If the issue persists after following the troubleshooting

  steps, consider reaching out to the support team of the authentication service
  for further assistance.

* **Security Considerations:** Ensure that any changes made to resolve the error

  maintain the security and integrity of the authentication process.

By following these troubleshooting steps and strategies, you should be able to
address the AADSTS90010 error related to algorithm creation failure effectively.