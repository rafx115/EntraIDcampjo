
# AADSTS50014: GuestUserInPendingState - The user account doesn’t exist in the directory. An application likely chose the wrong tenant to sign into, and the currently logged in user was prevented from doing so since they didn't exist in your tenant. If this user should be able to sign in, add them as a guest. For further information, please visitadd B2B users.


## Troubleshooting Steps
**Troubleshooting Guide for AADSTS50014 Error Code: GuestUserInPendingState**

**Initial Diagnostic Steps:**

1. **Confirm Tenant and User:** Verify the tenant the user is trying to sign into and ensure that the user account exists in that directory.
   
2. **Check Application Configuration:** Review the configuration of the application that the user is trying to sign into and make sure it is set up correctly to allow guest users.

3. **Authenticate User:** Ensure that the user attempting to sign in is using the correct credentials and that they have been added as a guest user if necessary.

**Common Issues that Cause this Error:**

1. **Incorrect Tenant Selection:** The application may be configured to point to the wrong tenant, causing the user to be redirected to the incorrect directory.

2. **User Not Added as Guest:** If the user is from a different organization, they need to be added as a guest user in the directory they are trying to sign into.

**Step-by-Step Resolution Strategies:**

1. **Verify Tenant:** Confirm that the user is attempting to sign into the correct tenant. If not, guide them to choose the right one before attempting to sign in again.

2. **Add as Guest:** If the user is from another organization, add them as a guest user in your directory. This can usually be done through the Azure Active Directory portal.

3. **Check Application Permissions:** Make sure that the application the user is trying to access is configured to allow guest users and has the necessary permissions set.

4. **Request User to Reauthenticate:** Ask the user to sign out and then sign back in, ensuring that they provide the correct credentials and select the appropriate tenant.

5. **Contact Support:** If the issue persists, reach out to the administrator or support team for the application or Azure Active Directory for further assistance.

**Additional Notes or Considerations:**

- If the user is still facing issues, it may be beneficial to review the application's documentation or contact the application developer for specific troubleshooting steps.
- Regularly monitor your Azure Active Directory for any unauthorized access attempts or unusual activity to prevent security breaches.

**Documentation for Guidance:**

- Microsoft Azure Active Directory Documentation: [B2B User Collaboration](https://docs.microsoft.com/en-us/azure/active-directory/b2b/fundamentals)

Following these steps should help diagnose and resolve the AADSTS50014 error code related to GuestUserInPendingState.