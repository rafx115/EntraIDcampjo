# AADSTS90056: BadResourceRequest - To redeem the code for an access token, the app should send a POST request to the/tokenendpoint. Also, prior to this, you should provide an authorization code and send it in the POST request to the/tokenendpoint. Refer to this article for an overview ofOAuth 2.0 authorization code flow. Direct the user to the/authorizeendpoint, which will return an authorization\_code. By posting a request to the/tokenendpoint, the user gets the access token. CheckApp registrations > Endpointsto confirm that the two endpoints were configured correctly.

## Introduction

This guide will help resolve issues related to badresourcerequest - to redeem
the code for an access token, the app should send a post request to
the/tokenendpoint. also, prior to this, you should provide an authorization code
and send it in the post request to the/tokenendpoint. refer to this article for
an overview ofoauth 2.0 authorization code flow. direct the user to
the/authorizeendpoint, which will return an authorization\_code. by posting a
request to the/tokenendpoint, the user gets the access token. checkapp
registrations > endpointsto confirm that the two endpoints were configured
correctly..

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
