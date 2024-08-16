# Hyper-V Nested Virtualization Lab for Windows Hello for Business (WHFB) and Device Registration

## **Introduction**

This guide will walk you through setting up a Hyper-V nested virtualization lab
environment for testing Windows Hello for Business (WHFB) and Device
Registration Service (DRS). The lab will include configuring Active Directory
Federation Services (ADFS), Azure AD Connect, and related components to simulate
a hybrid identity environment.

## **Task 0: Verify a Domain Using MyWorkspace**

### Steps:

1. **Access MyWorkspace**:

   - Navigate to [MyWorkspace](https://myworkspace.microsoft.com/) and sign in.

2. **Create External Connectivity**:

   - In MyWorkspace, navigate to **External Connectivity**.
   - Add a public IP address to your workspace to configure the domain’s DNS.

3. **Create and Verify a Custom Domain**:
   - In Azure, go to **Custom Domains** under Azure AD.
   - Add a custom domain (e.g., `yourdomain.myworkspace.microsoft.com`).
   - Verify the domain by adding the provided TXT record to the DNS settings in
     MyWorkspace.

## **Task 1: Stop Previous VMs**

### Steps:

1. **Stop Azure AD Connect VMs**:
   - Access your Azure portal.
   - Stop any VMs related to previous labs, especially those running Azure AD
     Connect.

## **Task 2: Create an Azure Resource Group and Host VM**

### Steps:

1. **Create a Resource Group**:

   - In the Azure portal, create a new resource group named `WHFB-RG`.

2. **Create a Windows 11 Host VM**:
   - Go to **Create a resource** > **Windows 11 Virtual Machine**.
   - Use the following settings:
     - **Name**: `TestWHFB-Win11`
     - **Size**: `Standard_D8s_v4` (32GB RAM)
     - **Image**: Windows 11 Enterprise version 21H2 – Gen 2
     - **Disks**: Add a secondary SSD with 512 GB
     - **Allow RDP (Port 3389)**
   - Complete the setup, ensuring that RDP is enabled.

## **Task 3: Configure Secondary Drive and Download ISOs**

### Steps:

1. **Initialize and Format the Secondary Drive**:

   - Log in to the Host VM via RDP.
   - Open **Disk Management** and initialize the secondary drive (E:) as GPT.
   - Format the disk and assign it the letter `E:`.

2. **Download OS ISOs**:
   - Create a folder named `VMs` on the E: drive.
   - Download Windows Server 2022 and Windows 10 Enterprise ISOs from the
     [Microsoft Evaluation Center](https://www.microsoft.com/en-us/evalcenter/).

## **Task 4: Install Hyper-V on the Host VM**

### Steps:

1. **Enable Hyper-V**:
   - Go to **Control Panel** > **Programs** > **Turn Windows features on or
     off**.
   - Check **Hyper-V** and restart the machine to complete the installation.

## **Task 5: Create a NAT Gateway on Hyper-V**

### Steps:

1. **Configure NAT for External Connectivity**:

   - Open PowerShell as Administrator on the Host VM.
   - Run the following commands:
     ```powershell
     New-VMSwitch -Name VmNAT -SwitchType Internal
     New-NetNat –Name LocalNAT –InternalIPInterfaceAddressPrefix "192.168.1.0/24"
     Get-NetAdapter "vEthernet (VmNAT)" | New-NetIPAddress -IPAddress 192.168.100.1 -AddressFamily IPv4 -PrefixLength 24
     ```

2. **Verify NAT Configuration**:
   - Run `Get-NetNat` to ensure that the NAT gateway is properly configured.

## **Task 6: Create and Configure Nested VMs**

### Steps:

1. **Create Nested VMs**:

   - Use Hyper-V Manager on the Host VM to create the following VMs:
     - **DC01** (Windows Server 2022)
     - **ADFS01** (Windows Server 2022)
     - **AADConnect** (Windows Server 2022)
     - **Client01** (Windows 10 Enterprise)
     - **Client02** (Windows 10 Enterprise)

2. **VM Configuration**:

   - For each VM, use the following settings:
     - **Generation**: Select **Generation 2**
     - **Memory**: Allocate at least 4096 MB (use dynamic memory)
     - **Network**: Attach to the `VmNAT` switch
     - **Storage**: Attach the respective ISO file for OS installation

3. **Install OS and Basic Configuration**:
   - Install the operating system on each VM.
   - Set static IPs and disable IPv6 on each VM.

## **Task 7: Set Up Domain Controller (DC01)**

### Steps:

1. **Promote DC01 to a Domain Controller**:

   - On DC01, open **Server Manager**.
   - Add the **Active Directory Domain Services** role and promote the server to
     a domain controller.
   - Use `contoso.com` as the root domain name.

2. **Verify Domain Setup**:
   - After restarting DC01, ensure the domain is functioning properly.

## **Task 8: Install AD Certificate Services on DC01**

### Steps:

1. **Install ADCS**:

   - Add the **Active Directory Certificate Services** role on DC01.
   - Configure the CA settings with defaults.

2. **Create a Certificate Template for ADFS**:
   - Follow
     [Microsoft’s documentation](https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/design/ad-fs-design-and-planning)
     to create and publish a certificate template for ADFS.

## **Task 9: Install and Configure ADFS (ADFS01)**

### Steps:

1. **Install ADFS Role**:

   - On ADFS01, install the **Active Directory Federation Services** role.
   - Configure ADFS using the certificate template created in the previous step.

2. **Enable IdP Initiated Sign-On**:
   - Run the following command in PowerShell:
     ```powershell
     Set-AdfsProperties -EnableIdpInitiatedSignonPage $true
     ```
   - Verify ADFS setup by accessing the IdP initiated sign-on page.

## **Task 10: Install and Configure Azure AD Connect (AADConnect)**

### Steps:

1. **Install Azure AD Connect**:

   - Download and install Azure AD Connect on the AADConnect VM.
   - Select **Custom installation** and configure synchronization with your
     domain.

2. **Verify Synchronization**:
   - Confirm that domain synchronization is successful by checking the Azure
     portal.

## **Task 11: Configure Client Machines (Client01 and Client02)**

### Steps:

1. **Network Configuration**:

   - Configure the network settings on Client01 and Client02 with static IPs and
     DNS pointing to DC01.

2. **Join the Domain**:

   - Join both Client01 and Client02 to the `contoso.com` domain.

3. **Test ADFS Sign-On**:
   - Access the ADFS IdP initiated sign-on page from both clients to confirm
     successful login.

## **Task 12: Enable Azure AD Device Registration**

### Steps:

1. **Configure Device Options in Azure AD Connect**:

   - On AADConnect, open Azure AD Connect and select **Configure device
     options**.
   - Choose **Configure Hybrid Azure AD Join** and follow the wizard.

2. **Verify Device Registration**:
   - Ensure devices register automatically with Azure AD after joining the
     domain.

## **Task 13: Create Test Users for Passwordless Authentication**

### Steps:

1. **Create Test Users in AD**:

   - Create test users in Active Directory using a separate PowerShell script.

2. **Configure Passwordless Authentication**:

   - In Azure AD, configure each user for their respective passwordless
     authentication method (FIDO2, WHFB, Authenticator).

3. **Test Authentication Methods**:
   - Test each user by logging in using their designated passwordless method.
