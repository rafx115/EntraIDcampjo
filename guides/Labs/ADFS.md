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
