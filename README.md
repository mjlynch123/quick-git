## Installation & Setup

## Prerequisites

- Git installed on your system.
- Python 3 installed.
  - macOS/Linux: check with `python3 --version`
  - Windows: check with `python --version`

### macOS / Linux

1. Clone the repository to your desktop:

        git clone https://github.com/your-username/quick-git.git

Make sure to change **your-username** with your actual GitHub username.

2. Move the script to your PATH:

        sudo mv quick_git.py /usr/local/bin/quick-git

3. Make the script executable:

        chmod +x /usr/local/bin/quick-git

---

### Windows

1. Clone the repository to your desktop:

        git clone https://github.com/your-username/quick-git.git

Make sure to change **your-username** with your actual GitHub username.

2. Create a folder for command-line scripts, for example:

        C:\Users\YourName\Scripts

3. Move `quick_git.py` into that folder.

4. Rename the file from:

        quick_git.py

to:

        quick-git.py

5. Add the Scripts folder to your PATH:

- Press the Windows key
- Search for **Environment Variables**
- Click **Edit the system environment variables**
- Click **Environment Variables**
- Under **User variables**, select **Path**
- Click **Edit**
- Click **New**
- Add your scripts folder path:

        C:\Users\YourName\Scripts

- Click **OK** on all windows

6. Close and reopen PowerShell.

7. Test that it works:

        python C:\Users\YourName\Scripts\quick-git.py "test commit"

Optional: create a PowerShell alias so you can run it as `quick-git`.

Open your PowerShell profile:

        notepad $PROFILE

Add this line:

        function quick-git { python "C:\Users\YourName\Scripts\quick-git.py" $args }

Save the file, close PowerShell, reopen it, then run:

        quick-git "Your commit message here"
