# Step-by-Step Guide to Setting Up ADFS with Web Application Proxy (WAP) and Self-Signed Certificate

## Prerequisites:

- Windows Server machine (2016 or later) for ADFS installation.
- A separate Windows Server machine for the Web Application Proxy (WAP) role.
- Both servers should be domain members.

# Step-by-Step Guide: Setting Up a Lab Environment with Nested VMs in a Workspace

## 1. Creating the Primary VM in Your Workspace

### Step 1: Determine Available Resources

- **Workspace Configuration:**
  - Check the maximum resources (CPU, RAM, Storage) available for a VM in your
    workspace environment. Ideally, you should aim for at least:
    - **vCPUs:** 2 to 4 vCPUs
    - **RAM:** 8 to 16 GB
    - **Storage:** 50 to 100 GB SSD

### Step 2: Create the Primary VM

- **Configuration:**
  - Within your workspace, create a new virtual machine with the maximum
    allowable resources based on the workspace's limits.
  - Install Windows Server 2016 or later as the operating system on this VM.
- **Considerations:**
  - If your workspace restricts the VM's capabilities, prioritize CPU and RAM
    allocation over storage to ensure smooth operation of nested VMs.

## 2. Enabling Nested Virtualization

### Step 1: Enable Hyper-V Role on the Primary VM

- **Instructions:**
  - Install the Hyper-V role on the primary VM to allow for the creation of
    nested VMs.
  - Restart the VM to apply changes.

### Step 2: Configure the Primary VM for Nested Virtualization

- **Instructions:**
  - Enable nested virtualization by running the following PowerShell command on
    the host machine:
    ```powershell
    Set-VMProcessor -VMName <VMName> -ExposeVirtualizationExtensions $true
    ```
  - Replace `<VMName>` with the name of your primary VM.

## 3. Creating and Configuring Nested VMs

### Step 1: Create Nested VMs

- **Instructions:**
  - Use the Hyper-V Manager within the primary VM to create nested VMs.
  - Allocate resources based on the available capacity:
    - **Each VM:** 1 to 2 vCPUs, 4 GB RAM, 20 to 40 GB storage.
  - Install Windows Server on each nested VM.

### Step 2: Install Roles and Features

- **For Domain Controller VM:**

  - Install Active Directory Domain Services (ADDS).
  - Promote the VM to a Domain Controller and create a new domain for the lab
    environment.

- **For ADFS VM:**

  - Join the ADFS VM to the domain created in the Domain Controller VM.
  - Follow the steps in the original guide to install and configure ADFS.

- **For Web Application Proxy (WAP) VM:**
  - Join the WAP VM to the domain.
  - Install the Web Application Proxy role and configure it to work with the
    ADFS server.

## 4. Configuring the Lab Environment

### Step 1: Networking Configuration

- **Instructions:**
  - Ensure all nested VMs can communicate within the same network.
  - Configure DNS settings so that the Domain Controller VM can resolve domain
    names for other VMs.

### Step 2: Test Domain Connectivity

- **Instructions:**
  - Verify that all nested VMs can successfully join and authenticate within the
    domain.
  - Test network connectivity between the nested VMs to ensure they can
    communicate for ADFS and WAP configuration.

## 5. Testing ADFS and Web Application Proxy

### Step 1: Verify ADFS Functionality

- **Instructions:**
  - Test the ADFS setup to ensure it correctly authenticates and serves
    federation requests.

### Step 2: Verify WAP Functionality

- **Instructions:**
  - Ensure that the Web Application Proxy is correctly routing requests to the
    ADFS server.

### Step 3: Periodic Maintenance and Shutdown

- **Instructions:**
  - When the lab is not in use, pause or shut down the VMs to save resources and
    reduce costs.

---

This guide provides a detailed process for setting up a lab environment within
the constraints of a workspace, leveraging nested virtualization and focusing on
efficient resource usage. This approach allows you to build a functional lab for
ADFS and Web Application Proxy configuration without exceeding your workspace's
limitations.

## Step 2: Install ADFS Role on the Server

1. **Open Server Manager**

   - Log in to the server that will host ADFS.
   - Open **Server Manager**.

   _[Insert Image of Server Manager Opening]_

2. **Add Roles and Features**

   - Click on **Add roles and features**.
   - Click **Next** until you reach the **Server Roles** page.

   _[Insert Image of Add Roles and Features Wizard]_

3. **Select ADFS**

   - Select **Active Directory Federation Services** and click **Next**.

   _[Insert Image of ADFS Role Selection]_

4. **Complete the Installation**

   - Click **Next** through the wizard and click **Install**.
   - Wait for the installation to complete.

   _[Insert Image of Installation Progress]_

## Step 2: Create a Self-Signed Certificate

1. **Open PowerShell**

   - Open PowerShell as an administrator.

   _[Insert Image of PowerShell Opening]_

2. **Generate a Self-Signed Certificate**

   - Run the following command to generate a self-signed certificate:
     ```powershell
     New-SelfSignedCertificate -DnsName "adfs.yourdomain.com" -CertStoreLocation "Cert:\LocalMachine\My" -NotAfter (Get-Date).AddYears(5)
     ```
   - Replace `adfs.yourdomain.com` with your ADFS FQDN.

   _[Insert Image of PowerShell Command Execution]_

3. **Export the Certificate**

   - Open **mmc.exe** and add the **Certificates** snap-in for the local
     computer.
   - Navigate to **Personal > Certificates**, find the certificate you just
     created.
   - Right-click the certificate, select **All Tasks > Export**.

   _[Insert Image of MMC with Certificates Snap-In]_

   - Choose to export the private key, and save it as a `.pfx` file.

   _[Insert Image of Certificate Export Wizard]_

## Step 3: Configure ADFS

1. **Open the ADFS Configuration Wizard**

   - After installation, in Server Manager, click on the **Notifications** flag
     and select **Configure the federation service on this server**.

   _[Insert Image of ADFS Configuration Wizard]_

2. **Create the First Federation Server in a Federation Server Farm**

   - Select **Create the first federation server in a federation server farm**
     and click **Next**.

   _[Insert Image of Federation Server Farm Setup]_

3. **Specify the Federation Service Name**

   - Enter the **FQDN** you used for the self-signed certificate
     (`adfs.yourdomain.com`).
   - Click **Next**.

   _[Insert Image of Federation Service Name Configuration]_

4. **Select the SSL Certificate**

   - Choose the self-signed certificate you created in Step 2.
   - Enter a display name for the federation service and click **Next**.

   _[Insert Image of SSL Certificate Selection]_

5. **Specify a Service Account**

   - Use an existing domain service account or create a new one for ADFS.
   - Click **Next**.

   _[Insert Image of Service Account Configuration]_

6. **Configure the Database**

   - Select **Create a database on this server using Windows Internal Database**
     for a test environment.
   - Click **Next** and review the configuration settings.

   _[Insert Image of Database Configuration]_

7. **Complete the Setup**

   - Click **Next** to complete the setup and **Configure**.
   - Once the setup is complete, click **Close**.

   _[Insert Image of Setup Completion]_

## Step 4: Install the Web Application Proxy Role

1. **Open Server Manager on the WAP Server**

   - Log in to the server that will host the Web Application Proxy.
   - Open **Server Manager**.

   _[Insert Image of Server Manager Opening on WAP Server]_

2. **Add Roles and Features**

   - Click on **Add roles and features**.
   - Click **Next** until you reach the **Server Roles** page.

   _[Insert Image of Add Roles and Features Wizard on WAP Server]_

3. **Select Remote Access Role**

   - Choose **Remote Access** and click **Next**.

   _[Insert Image of Remote Access Role Selection]_

4. **Select Web Application Proxy**

   - Under **Role Services**, select **Web Application Proxy** and click
     **Next**.

   _[Insert Image of Web Application Proxy Selection]_

5. **Complete the Installation**

   - Click **Next** through the wizard and click **Install**.
   - Wait for the installation to complete.

   _[Insert Image of Installation Progress on WAP Server]_

## Step 5: Configure the Web Application Proxy

1. **Open the Web Application Proxy Configuration Wizard**

   - After installation, in Server Manager, click on the **Notifications** flag
     and select **Open the Web Application Proxy Wizard**.

   _[Insert Image of Web Application Proxy Configuration Wizard]_

2. **Connect to the ADFS Server**

   - In the wizard, enter the **ADFS** server's FQDN (`adfs.yourdomain.com`).
   - Enter credentials for an account that has administrative access to the ADFS
     server.

   _[Insert Image of ADFS Server Connection]_

3. **Specify an SSL Certificate**

   - Choose the same SSL certificate that you used for the ADFS server (this
     should be the same self-signed certificate you created earlier).

   _[Insert Image of SSL Certificate Selection in WAP Configuration]_

4. **Configure AD FS Proxy**

   - The wizard will automatically configure the WAP server as a proxy for ADFS.
     Click **Next** and complete the wizard.

   _[Insert Image of AD FS Proxy Configuration Completion]_

## Step 6: Publish a Web Application via the Web Application Proxy

1. **Open the Remote Access Management Console**

   - In Server Manager, go to **Tools** and select **Remote Access Management**.

   _[Insert Image of Remote Access Management Console]_

2. **Publish a New Web Application**

   - In the Remote Access Management Console, click on **Web Application Proxy**
     on the left pane, and then click **Publish**.

   _[Insert Image of Publish New Web Application]_

3. **Choose Preauthentication**

   - Select **Active Directory Federation Services (AD FS)** for
     preauthentication and click **Next**.

   _[Insert Image of Preauthentication Selection]_

4. **Provide Application Details**

   - Enter the **Name** and **External URL** of the web application you want to
     publish.
   - Specify the backend server URL (internal URL of the application) and click
     **Next**.

   _[Insert Image of Application Details Configuration]_

5. **Select the SSL Certificate**

   - Choose the SSL certificate that matches the external URL and click
     **Next**.

   _[Insert Image of SSL Certificate Selection for Application]_

6. **Complete the Publishing**

   - Review the settings and click **Publish**.

   _[Insert Image of Publishing Completion]_

## Step 7: Configure DNS and Firewall Settings

1. **DNS Configuration**

   - Ensure that the external FQDN (e.g., `adfs.yourdomain.com`) points to the
     public IP address of your WAP server.

   _[Insert Image of DNS Configuration]_

2. **Firewall Configuration**

   - Configure your firewall to allow HTTPS (TCP port 443) traffic to the WAP
     server's public IP.

   _[Insert Image of Firewall Configuration]_

## Step 8: Test the Configuration

1. **Access the Published Application**

   - From an external client, open a web browser and navigate to the external
     URL of the published application.
   - You should be redirected to the ADFS sign-in page.

   _[Insert Image of External Application Access]_

2. **Verify Access**

   - Sign in with your domain credentials and ensure you can access the internal
     application through the WAP.

   _[Insert Image of Sign-In Page]_
