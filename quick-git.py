#!/usr/bin/env python3
import sys
import subprocess

def run_command(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print("Error running command:", " ".join(cmd))
        print("Output:", result.stdout)
        print("Error:", result.stderr)
        sys.exit(result.returncode)

if __name__ == "__main__":
    # Check if a commit message was provided as an argument
    if len(sys.argv) > 1:
        commit_message = " ".join(sys.argv[1:])
    else:
        commit_message = input("Enter your commit message: ").strip()
        if not commit_message:
            print("No commit message provided. Exiting.")
            sys.exit(1)

    run_command(["git", "add", "."])
    run_command(["git", "commit", "-m", commit_message])
    run_command(["git", "push"])
    print("Changes have been pushed successfully!")
