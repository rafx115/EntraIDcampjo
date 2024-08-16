# Define the organizational unit (OU) where users will be created
$ou = "OU=TestUsers,DC=contoso,DC=com"

# Create the OU if it doesn't exist
if (-not (Get-ADOrganizationalUnit -Filter {Name -eq "TestUsers"})) {
    New-ADOrganizationalUnit -Name "TestUsers" -Path "DC=contoso,DC=com"
}

# Function to create a test user
function Create-TestUser {
    param (
        [string]$UserName,
        [string]$Password,
        [string]$Description
    )
    $securePassword = ConvertTo-SecureString $Password -AsPlainText -Force
    New-ADUser -Name $UserName -GivenName $UserName -Surname "Test" `
               -SamAccountName $UserName -UserPrincipalName "$UserName@contoso.com" `
               -AccountPassword $securePassword -PasswordNeverExpires $true `
               -Enabled $true -Description $Description -Path $ou
}

# Password for all test users (use a strong password in production)
$password = "P@ssw0rd123!"

# Create test users for each passwordless technology
Create-TestUser -UserName "FIDO2User" -Password $password -Description "Test user for FIDO2 authentication"
Create-TestUser -UserName "WHFBUser" -Password $password -Description "Test user for Windows Hello for Business"
Create-TestUser -UserName "AuthenticatorUser" -Password $password -Description "Test user for Microsoft Authenticator"

Write-Host "Test users created successfully."
