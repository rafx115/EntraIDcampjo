
# AADSTS50068: SignoutInitiatorNotParticipant - Sign out has failed. The app that initiated sign out isn't a participant in the current session.


## Troubleshooting Steps
**Troubleshooting Guide for Error Code AADSTS50068: SignoutInitiatorNotParticipant**

**Initial Diagnostic Steps:**
1. Confirm the application where the error occurred.
2. Check if the user is signed into the correct account.
3. Verify the current session participants and the app initiating sign-out.

**Common Issues:**
1. Incorrect configuration of the identity provider settings.
2. Mismatched session tokens or user sessions.
3. Changes in user authentication status during sign-out.
4. Inconsistent participant tracking in the session.
5. Improper handling of sign-out requests.

**Step-by-Step Resolution Strategies:**
1. **Check Application Configuration:**
   - Verify the registered Redirect URIs and Logout URLs in the app settings.
   - Ensure the application is correctly integrated with the identity provider (e.g., Azure AD).
   
2. **Confirm User Sign-In Status:**
   - Ensure the user initiating sign-out is signed in to the correct account.
   
3. **Review Current Session Participants:**
   - Check the participants in the session at the time of sign-out.
   - Confirm that the initiating app is an active participant in the session.
   
4. **Investigate Changes in Authentication Status:**
   - Review any recent changes in user authentication or session handling.
   - Check for expired tokens or invalidated sessions.

5. **Address Participant Tracking Issues:**
   - Debug the application to determine if there are issues tracking session participants.
   - Implement proper session management to ensure consistency in participant tracking.

6. **Handle Sign-out Requests Properly:**
   - Ensure the app follows the correct protocol for initiating and handling sign-out requests.
   - Implement any necessary mechanisms to validate sign-out initiation.

**Additional Notes or Considerations:**
- Error code AADSTS50068 indicates a specific issue related to sign-out initiation.
- Proper session management and participant tracking are crucial for resolving this error.
- Rechecking the app configuration details and user authentication status can help identify the root cause of the error.

**Documentation for Guidance:**
- Azure Active Directory documentation provides detailed information on troubleshooting common sign-in and sign-out issues: [Azure AD Troubleshooting documentation](https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-troubleshooting-authentication-errors-details#aadsts50068-signoutinitiatornotparticipant).