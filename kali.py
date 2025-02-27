import os
import subprocess
import sys
import time

def run_command(command):
    """Runs a shell command and checks for errors."""
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    
    if process.returncode != 0:
        print(f"Error: {stderr.decode('utf-8')}")
        return False
    else:
        print(stdout.decode('utf-8'))
        return True

def add_kali_repository():
    """Adds the Kali Linux repository to the sources list."""
    print("Adding Kali repository to /etc/apt/sources.list.d/kali.list...")
    command = "sudo sh -c \"echo 'deb https://http.kali.org/kali kali-rolling main non-free contrib' > /etc/apt/sources.list.d/kali.list\""
    return run_command(command)

def install_gnupg():
    """Installs GnuPG package."""
    print("Installing GnuPG...")
    command = "sudo apt install -y gnupg"
    return run_command(command)

def add_kali_public_key():
    """Downloads and adds Kali Linux public key."""
    print("Adding Kali public key...")
    commands = [
        "wget 'https://archive.kali.org/archive-key.asc'",
        "sudo apt-key add archive-key.asc"
    ]
    for command in commands:
        if not run_command(command):
            return False
    return True

def set_kali_package_priority():
    """Sets Kali Linux package priority to avoid automatic installation."""
    print("Setting Kali package priority...")
    command = """
    sudo sh -c "echo 'Package: *' > /etc/apt/preferences.d/kali.pref;
    echo 'Pin: release a=kali-rolling' >> /etc/apt/preferences.d/kali.pref;
    echo 'Pin-Priority: 50' >> /etc/apt/preferences.d/kali.pref"
    """
    return run_command(command)

def update_packages():
    """Updates the package list."""
    print("Updating package list...")
    command = "sudo apt update"
    return run_command(command)

def install_tool(tool_name):
    """Installs the specified tool from the Kali Linux repository."""
    print(f"Installing {tool_name}...")
    command = f"sudo apt install -y -t kali-rolling {tool_name}"
    return run_command(command)

def create_desktop_entry(tool_name):
    """Creates a .desktop entry for the installed tool."""
    print(f"Creating desktop entry for {tool_name}...")
    desktop_entry = f"""[Desktop Entry]
Version=1.0
Name={tool_name}
Comment={tool_name} Web Application Security Testing
Exec={tool_name}
Icon={tool_name}
Terminal=false
Type=Application
Categories=Development;Security;
"""
    # Create a folder for Kali tools inside the app launcher directory
    app_launcher_dir = "/usr/share/applications/kali_tools"
    os.makedirs(app_launcher_dir, exist_ok=True)
    
    desktop_path = f"{app_launcher_dir}/{tool_name}.desktop"
    try:
        with open(desktop_path, "w") as f:
            f.write(desktop_entry)
        os.chmod(desktop_path, 0o755)
        print(f"Desktop entry for {tool_name} created successfully.")
        return True
    except Exception as e:
        print(f"Error creating desktop entry for {tool_name}: {e}")
        return False

def show_loading_animation():
    """Displays a loading animation (spinner)."""
    animation = ['|', '/', '-', '\\']
    for _ in range(30):  # Show animation for 30 iterations
        for frame in animation:
            sys.stdout.write(f"\rInstalling {frame}   ")
            sys.stdout.flush()
            time.sleep(0.1)

def print_logo():
    """Displays a logo for Kali Tools."""
    logo = """
   

░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░       ░▒▓███████▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░         ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░         ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        
░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░      ░▒▓█▓▒░         ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░       ░▒▓██████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░         ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░         ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░         ░▒▓█▓▒░   ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░▒▓███████▓▒░  
                                                                                                                      
                                                                                                                      

"""
    print(logo)

def main():
    """Main function to execute the setup."""
    if len(sys.argv) != 2:
        print("Usage: sudo python3 kali.py <tool_name>")
        return

    tool_name = sys.argv[1]

    # Print the KaliTools logo
    print_logo()
    
    print(f"Setting up Kali tools for: {tool_name}")
    
    # Check if we need to add the Kali repo (Only do it once)
    if not os.path.exists("/etc/apt/sources.list.d/kali.list"):
        if not add_kali_repository():
            print("Failed to add Kali repository.")
            return
        if not install_gnupg():
            print("Failed to install GnuPG.")
            return
        if not add_kali_public_key():
            print("Failed to add Kali public key.")
            return
        if not set_kali_package_priority():
            print("Failed to set Kali package priority.")
            return
        if not update_packages():
            print("Failed to update packages.")
            return

    # Show loading animation while installing
    show_loading_animation()

    # Install the requested tool
    if not install_tool(tool_name):
        print(f"Failed to install {tool_name}.")
        return
    
    # Create a desktop entry for the tool
    if not create_desktop_entry(tool_name):
        print(f"Failed to create desktop entry for {tool_name}.")
        return

    print(f"{tool_name} has been installed and should appear in the application launcher under 'Kali Tools'.")

if __name__ == "__main__":
    main()
