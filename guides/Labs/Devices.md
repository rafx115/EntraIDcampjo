Step-by-Step Guide to Testing Hybrid Join, Device Registration, and AAD Join
with Entra ID using Hyper-V and Nested VMs Prerequisites: A physical Windows
Server or Windows 10/11 machine with Hyper-V enabled. Access to Entra ID (Azure
AD) with the necessary permissions to register devices and configure Hybrid
Join. Windows Server ISO for setting up Domain Controllers (DCs) and other
required infrastructure. Internet access for connecting VMs to Azure AD. Step 1:
Enable Hyper-V and Configure Nested Virtualization 1.1 Enable Hyper-V on the
Host Machine Open Control Panel: Go to Control Panel > Programs > Turn Windows
features on or off. Enable Hyper-V: In the Windows Features dialog, check the
boxes for Hyper-V, Hyper-V Management Tools, and Hyper-V Platform. Click OK and
restart the machine if prompted. 1.2 Configure a Virtual Switch in Hyper-V Open
Hyper-V Manager:

Search for Hyper-V Manager in the Start menu and open it. Create a New Virtual
Switch:

In the Actions pane, click on Virtual Switch Manager. Choose External as the
switch type and click Create Virtual Switch. Configure the External Virtual
Switch:

Name: Give your switch a meaningful name, such as ExternalSwitch. External
Network: Select the physical network adapter that the VMs will use to access the
internet. Allow Management Operating System to share this network adapter: Check
this box if you want the host machine to also use this adapter for network
access. Click OK to create the virtual switch. 1.3 Create Nested VMs Create a
New VM in Hyper-V:

In Hyper-V Manager, click on New > Virtual Machine. Follow the wizard to create
a new virtual machine: Name: Enter a name for the VM, such as NestedVM1.
Generation: Select Generation 2 for better performance and features. Memory:
Allocate memory (at least 4 GB) to the VM. Network: Connect the VM to the
virtual switch created earlier (ExternalSwitch). Virtual Hard Disk: Create a new
virtual hard disk (VHDX). Installation Options: Choose to install an operating
system from an ISO file. Enable Nested Virtualization:

After creating the VM, open PowerShell as an administrator on the host machine.
Run the following command to enable nested virtualization on the VM: powershell
Copiar código Set-VMProcessor -VMName "NestedVM1"
-ExposeVirtualizationExtensions $true Install the Operating System:

Start the VM and follow the installation process to install the operating system
(Windows Server or Windows 10/11). After installation, configure the VM as
needed (e.g., setting up a static IP if required). Configure Nested VMs for
Additional Roles:

Repeat the above steps to create additional nested VMs for other roles such as
Domain Controllers or test clients (e.g., NestedVM_DC, NestedVM_Client). Step 2:
Set Up Domain Controller in a VM 2.1 Install Windows Server on the VM Create a
New VM for the Domain Controller (DC):

Follow the steps in 1.3 to create a new VM, name it NestedVM_DC, and install
Windows Server. Initial Configuration:

After installation, configure the network settings, set a static IP, and ensure
the VM can access the internet. 2.2 Promote the Server to a Domain Controller
Add Active Directory Domain Services (AD DS) Role:

Open Server Manager on NestedVM_DC. Click Add roles and features, select Active
Directory Domain Services, and complete the installation. Promote the Server to
a Domain Controller:

In Server Manager, click the notification flag and choose Promote this server to
a domain controller. Select Add a new forest and enter a Root domain name (e.g.,
test.local). Complete the wizard to promote the server to a DC and restart the
server. 2.3 Create a Domain Verify Domain Configuration: After the server
restarts, verify that the domain has been created by checking Active Directory
Users and Computers. Step 3: Configure Hybrid Azure AD Join 3.1 Configure Azure
AD Connect Install Azure AD Connect:

Download and install Azure AD Connect on NestedVM_DC or another server VM.
Choose Express Settings if it's a test environment. Set Up Hybrid Azure AD Join:

During the setup, select Configure Hybrid Azure AD Join. Enter your Azure AD
credentials and configure the synchronization settings to sync the on-premises
AD with Azure AD. 3.2 Configure GPO for Device Registration Open Group Policy
Management Console (GPMC):

On the NestedVM_DC, open GPMC. Create and Link a New GPO:

Create a new GPO named Device Registration. Navigate to Computer Configuration >
Policies > Administrative Templates > Windows Components > Device Registration.
Enable the policy Register domain-joined computers as devices. Link the GPO to
the Domain:

Link the Device Registration GPO to the domain (e.g., test.local). 3.3 Verify
Hybrid Azure AD Join Check the Device Registration Status: On a domain-joined VM
(e.g., NestedVM_Client), open PowerShell and run: powershell Copiar código
dsregcmd /status Check the Device State section to verify that the device is
Hybrid Azure AD Joined. Step 4: Set Up Azure AD Join on a Separate VM 4.1 Create
a New VM for Azure AD Join Create and Configure the VM: Create a new VM (e.g.,
NestedVM_AAD) using the steps outlined in Step 1.3. Ensure that this VM is not
joined to the on-premises domain. 4.2 Join the VM to Azure AD Join Azure AD
During Setup: During the Windows setup on NestedVM_AAD, select Join Azure AD.
Enter your Azure AD credentials to join the device to Azure AD. 4.3 Verify Azure
AD Join Check the Azure AD Join Status: On NestedVM_AAD, open PowerShell and
run: powershell Copiar código dsregcmd /status Check the Device State section to
confirm that the device is Azure AD Joined. Step 5: Test Device Registration and
Compliance 5.1 Test Device Registration in Azure AD Verify Device Registration:
Log in to the Azure Portal and navigate to Azure Active Directory > Devices.
Verify that both the Hybrid Azure AD Joined and Azure AD Joined devices are
listed. 5.2 Test Conditional Access Policies Create a Conditional Access Policy:
In the Azure Portal, go to Azure Active Directory > Security > Conditional
Access. Create a new policy that requires device compliance for accessing
specific resources (e.g., Office 365). 5.3 Verify Compliance and Registration
Check Compliance in Intune (Optional): If using Microsoft Intune, check the
compliance status of the devices in the Intune portal. Step 6: Monitor and
Troubleshoot Monitor Device Sync Status:

In Azure AD Connect, monitor the synchronization status to ensure devices are
syncing properly. Troubleshoot Common Issues:

Use the Event Viewer on the DC and the Azure Portal to diagnose any issues
related to device registration and hybrid join. Step 7: Create Test Users for
Passwordless Authentication in Entra ID Purpose: Create test users in the DC for
each type of passwordless technology in Entra ID, including FIDO2, WHFB, and
Microsoft Authenticator.

Step 1: Prepare the Script Open PowerShell on your Domain Controller (DC01) and
use the following script to create the test users:

powershell Copiar código

# Define the organizational unit (OU) where users will be created

$ou = "OU=TestUsers,DC=contoso,DC=com"

# Create the OU if it doesn't exist

if (-not (Get-ADOrganizationalUnit -Filter {Name -eq "TestUsers"})) {
New-ADOrganizationalUnit -Name "TestUsers" -Path "DC=contoso,DC=com" }

# Function to create a test user

function Create-TestUser { param ( [string]$UserName,
        [string]$Password,
[string]$Description
    )
    $securePassword = ConvertTo-SecureString $Password -AsPlainText -Force
    New-ADUser -Name $UserName -GivenName $UserName -Surname "Test" `
               -SamAccountName $UserName -UserPrincipalName "$UserName@contoso.com"
`               -AccountPassword $securePassword -PasswordNeverExpires $true`
-Enabled $true -Description $Description -Path $ou }

# Password for all test users (use a strong password in production)

$password = "P@ssw0rd123!"

# Create test users for each passwordless technology

Create-TestUser -UserName "FIDO2User" -Password $password -Description "Test
user for FIDO2 authentication" Create-TestUser -UserName "WHFBUser" -Password
$password -Description "Test user for Windows Hello for Business"
Create-TestUser -UserName "AuthenticatorUser" -Password $password -Description
"Test user for Microsoft Authenticator"

Write-Host "Test users created successfully." Step 2: Run the Script Execute the
Script:

Copy and paste the script into PowerShell on DC01, and run it. The script will
create an Organizational Unit (OU) named TestUsers and populate it with three
test accounts. Verify User Creation:

Open Active Directory Users and Computers on DC01. Navigate to the TestUsers OU
and verify that the users FIDO2User, WHFBUser, and AuthenticatorUser have been
created. Step 3: Configure Users for Passwordless Authentication Configure FIDO2
Security Key:

Log in to the Azure portal with your Global Admin account. Go to Azure Active
Directory > Security > Authentication Methods and enable FIDO2 security key
authentication. Assign FIDO2User to use FIDO2 as the authentication method.
Configure Windows Hello for Business:

Ensure that the WHFBUser is configured in a policy that supports Windows Hello
for Business. You can create a Group Policy or use Intune to enforce WHFB
settings. Configure Microsoft Authenticator:

Enable Microsoft Authenticator for AuthenticatorUser via Azure Active
Directory > Security > Authentication Methods. Configure the user to enroll in
MFA using the Microsoft Authenticator app. Step 4: Test Authentication Test
FIDO2 Authentication:

Log in with FIDO2User using a FIDO2 security key. Test Windows Hello for
Business:

Log in with WHFBUser using Windows Hello for Business. Test Microsoft
Authenticator:

Log in with AuthenticatorUser using the Microsoft Authenticator app.
