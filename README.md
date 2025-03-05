# Kali Tool Installer

This script (`kali-tools`) automates the process of installing Kali Linux tools on a Debian-based system, such as Ubuntu. It adds the Kali Linux repository, installs necessary GnuPG keys, updates the package list, and installs the specified tool from the Kali repository.

## Requirements

Before using this tool, ensure you have the following:

- Python 3.x
- `sudo` privileges on the system
- An internet connection
- A Debian-based system (e.g., Ubuntu)

## Installation

1. Clone this repository or download the script.

```bash
git clone https://github.com/infant06/kalitools.git
cd kalitools
```

2. Make Symlink the script to `/usr/local/bin/` to make it globally accessible:

```bash
sudo ln -s kali.py /usr/local/bin/kali-tools
```

3. Make the script executable:

```bash
sudo chmod +x /usr/local/bin/kali-tools
```

4. Verify that Python 3 is installed:

```bash
python3 --version
```

5. Install required dependencies if they are not already installed:

```bash
sudo apt update
sudo apt install -y wget
```

## Usage

To install a Kali Linux tool, use the following command:

```bash
sudo kali-tools install <tool_name>
```

### Parameters:

- `<tool_name>`: The name of the Kali Linux tool you want to install (e.g., `burpsuite`).

For example, to install Burp Suite:

```bash
sudo kali-tools install burpsuite
```

This command will:

1. Add the Kali Linux repository to your system (if not already added).
2. Install the GnuPG key to authenticate Kali Linux packages.
3. Install the specified tool (e.g., Burp Suite) from the Kali repository.

### Available Tools:

You can install any tool available in the Kali Linux repository, such as:

- `burpsuite`
- `nmap`
- `aircrack-ng`

For a complete list of available tools, visit [Kali Linux Tools](https://tools.kali.org/tools-listing).

## Script Overview

1. **Add Kali Repository**: Adds the Kali Linux repository to the system to allow installation of Kali tools.
2. **Install GnuPG**: Installs the GnuPG package required to authenticate the Kali repository.
3. **Add Kali Public Key**: Downloads and installs the Kali public key for package verification.
4. **Set Package Priority**: Sets the Kali Linux package priority to avoid interfering with existing system packages.
5. **Install Tool**: Installs the specified tool from the Kali repository.

## Troubleshooting

- If you encounter any issues with missing dependencies, make sure to update your system:

```bash
sudo apt update && sudo apt upgrade
```

- If the script fails to execute, ensure you have proper permissions (`sudo`) and that your system is compatible with the Kali repository.

## License

This project is licensed under the MIT License.

