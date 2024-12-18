# Quick-Git 🚀
Quick-Git is a simple command-line tool that allows you to easily add, commit, and push your changes to GitHub with just one command. No more typing out multiple git commands every time—just one and done!

## Features
- Add, commit, and push in one swift command.
- Works system-wide once installed.
- Saves you time and keystrokes on every commit. 🙌

## Prerequisites
- Git installed on your system.
- Python 3 installed **(check by running python3 --version)**.

## Installation & Setup
1. Clone over the respository to your desktop

        git clone https://github.com/your-username/quick-git.git

Make sure to change **your-username** with your actual Github username. 

2. Move the Script to Your PATH: From inside the cloned repository directory, run:

        sudo mv quick_git.py /usr/local/bin/quick-git

3. Make the Script Executable::

        chmod +x /usr/local/bin/quick-git

## Usage
Simply run:

        quick-git "Your commit message here"

This will:

- Add all your changes (git add .)
- Commit with the provided commit message
- Push the changes to your current branch’s remote repository

### Example:

        quick-git "Fix bug in user login flow"

## Troubleshooting & Tips
- If you get a command not found error, ensure that /usr/local/bin is on your PATH. Typically it is by default on macOS.
- Make sure you have an initialized git repository (git init) and a remote set up (git remote add origin <URL>).
- If you prefer a shorter name or alias, you can rename or alias the script:

        alias qg='quick-git'

Then just run:
        
        qg "Short and sweet commit message"

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
MIT
