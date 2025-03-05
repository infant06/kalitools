# Kali Repository Setup Script

This script (`add_kali_repo.py`) automates the process of adding the Kali Linux repository to a Debian-based system, allowing you to install Kali tools using `apt install`.

## Requirements

Before using this script, ensure you have the following:

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

2. Run the script to add the Kali repository and install the required keys:

```bash
sudo python3 kali.py
```

3. Update your package list to reflect the new repository:

```bash
sudo apt update
```

## Usage

Once the repository is added, you can install Kali tools using the standard `apt` command:

```bash
sudo apt install <package-name>
```

For example, to install Burp Suite:

```bash
sudo apt install burpsuite
```

### Available Tools

You can install any tool available in the Kali Linux repository, such as:

- `burpsuite`
- `nmap`
- `aircrack-ng`

For a complete list of available tools, visit [Kali Linux Tools](https://tools.kali.org/tools-listing).

## Troubleshooting

- If you encounter issues with missing dependencies, run:

```bash
sudo apt update && sudo apt upgrade
```

- If you see a GPG key error, manually add the Kali public key:

```bash
wget -q -O - https://archive.kali.org/archive-key.asc | sudo apt-key add -
```

- If the repository is not recognized, ensure the `/etc/apt/sources.list.d/kali.list` file exists and contains:

```bash
deb https://http.kali.org/kali kali-rolling main non-free contrib
```

## License

This project is licensed under the MIT License.

