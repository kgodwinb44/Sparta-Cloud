# Shell commands

Checks the OS name
```
-uname
```
OS info

```
-uname --help
```

User info
-whoami

Exits the instance connection
-exit

Shells avaliable
-cat /etc/shells

Shows command history
-history

Pass in a link will get the img
-curl (used for transfer of data)

Requires a file to save as (--output file.name)
-wget (same as curl)

Instead of --output, -O
-file file.name

Shows info about the file
-mv file.name file.rename

Renames file
-rm file.name

Deletes file
-rm -r folder.name
Deletes folder
-touch file.name
Creates a file
-nano file.name
Enters the file, can add content .e.g text
-cat file.name
Shows the file content


## Required to run when a fresh shell or Linux
-sudo apt update -y (-y auto says yes to commands)
Updates the list of available packages from the repositories
-sudo apt upgrade -y
Upgrades the packages to the latest version
- sudo apt install tree -y
Install tree package
-tree
See folder structure
-sudo su
Install pacakge to access root directory
-sudo systemctl status package.name
Shows the status of the package
-sudo systemctl restart package.name (nginx)
Restarts the package
-sudo systemctl enable package.name
Starts the package automatically on boot

#!/bin/bash (Shebang)
At the top of bash scripts
tells which interpreter to run the script in (shell bash)

-sudo chmod +x install_nginx.sh
gives permission to run the script

./install_nginx.sh
runs the script

![](../images/upgrade_update.PNG)

## Linux does not care about file extension
## e.g. .txt is just a string name for the file
## Where as Windows, Mac does

