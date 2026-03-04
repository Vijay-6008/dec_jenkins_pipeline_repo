import subprocess
import sys

def run_linux_command(cmd):
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            check=True,
            text=True,
            capture_output=True
        )
        print("Command Output:\n", result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        sys.exit(1)

def main():
    print("Running Linux Integration via Python...\n")
    
    # Example Linux commands
    run_linux_command("uname -a")
    run_linux_command("df -h")
    
    print("\nPython + Linux Integration Successful!")

if __name__ == "__main__":
    main()