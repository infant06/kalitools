import os
import subprocess

def run_command(command):
    """Runs a shell command and checks for errors."""
    process = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if process.returncode != 0:
        print(f"Error: {process.stderr}")
        return False
    print(process.stdout)
    return True

def add_kali_repository():
    """Adds the Kali Linux repository to the system."""
    print("Adding Kali repository...")
    command = "echo 'deb http://http.kali.org/kali kali-rolling main non-free contrib' | sudo tee /etc/apt/sources.list.d/kali.list"
    return run_command(command)

def add_kali_gpg_key():
    """Imports the Kali Linux GPG key."""
    print("Adding Kali GPG key...")
    command = "wget -q -O - https://archive.kali.org/archive-key.asc | sudo tee /etc/apt/trusted.gpg.d/kali-archive-key.asc"
    return run_command(command)

def update_package_list():
    """Updates the package list."""
    print("Updating package list...")
    return run_command("sudo apt update")

def main():
    if not add_kali_repository():
        print("Failed to add Kali repository.")
        return
    if not add_kali_gpg_key():
        print("Failed to add Kali GPG key.")
        return
    if not update_package_list():
        print("Failed to update package list.")
        return
    
    print("Kali repository added successfully. You can now install packages using 'sudo apt install <package-name>'.")

if __name__ == "__main__":
    main()
