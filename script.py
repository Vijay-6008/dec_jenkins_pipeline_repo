import subprocess

def main():
    print("Running Linux command from Python...")

    result = subprocess.run(
        "uptime",
        shell=True,
        capture_output=True,
        text=True
    )

    output = result.stdout

    print("System Uptime:")
    print(output)

    # Save output to file
    with open("build_output.txt", "w") as f:
        f.write("Linux System Uptime:\n")
        f.write(output)

    print("Output saved to build_output.txt")

if __name__ == "__main__":
    main()