# AADSTS50034: UserAccountNotFound - To sign into this application, the account must be added to the directory. This error can occur because the user mis-typed their username, or isn't in the tenant. An application might have chosen the wrong tenant to sign into, and the currently logged in user was prevented from doing so since they did not exist in your tenant. If this user should be able to log in, add them as a guest. See docs here:Add B2B users.


## Troubleshooting Steps
**Troubleshooting Guide for Error Code AADSTS50034: UserAccountNotFound**

**Initial Diagnostic Steps:**
1. **Verify Username**: Check if the user has typed the correct username. Typos in the username can often lead to this error.
2. **Check User Account in Directory**: Ensure that the user account exists in the directory for the specific tenant.
3. **Confirm Tenant Selection**: Make sure the application is set to sign in to the correct tenant associated with the user's account.

**Common Issues:**
1. **Incorrect Username**: Users might mistype their username during login attempts.
2. **User Not Added to Directory**: The user may not be added to the Azure AD directory associated with the tenant.
3. **Application Using Wrong Tenant**: The application might be trying to sign in to a different tenant than the one the user is associated with.

**Step-by-Step Resolution Strategies:**
1. **Validate Username**: Have the user verify and re-enter their username to ensure accuracy.
2. **Add User to Directory**: If the user does exist but is not added to the directory, add them as a guest user in the Azure AD directory.
3. **Select Correct Tenant**: Ensure that the application is configured to sign in to the correct tenant. The user should be prompted to select the correct tenant if necessary.

**Additional Notes or Considerations:**
- For B2B scenarios, where external users need to access resources, adding them as guest users in the Azure AD directory is a common practice.
- It's essential to have proper permissions to manage users and access the Azure portal for implementing some of the solutions mentioned above.

**Documentation for Guidance:**
- Microsoft Docs: [Add B2B users](https://docs.microsoft.com/en-us/azure/active-directory/external-identities/b2b-get-started) provides detailed steps on how to add B2B users to your Azure AD directory for collaborating with external partners or users.