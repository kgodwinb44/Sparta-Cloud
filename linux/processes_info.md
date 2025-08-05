# Linux Processes

## List Running Processes
```
ps aux or top or htop
```
- ps aux (Lists all running processes)
- top (Interactive real-time view of running processes)
- htop (Enhanced version of top (needs to be installed))

---

## List User Processes (Bash, Firefox, Python scripts)
```
ps -u user.name
```

---

## List System Processes (Scheduled tasks, background processes)
```
ps -A, ps -e
```

---

## Child Processes
- Child process is a processes created by a parent process
- E.g. When a shell runs ls, it creates a child processes to execute it
```
pstree or ps -ejH
```
- Shows process hierarchies

---

## Run a process in the Background
- Apply & to the command
- Sleep creates a process
```
sleep 60 &

jobs -l, shows the background proceses
```
- Provides a PID (Process ID)
- Job number e.g.[5]
- [1] 12345
- Notified when the process is completed


---

## End a process (Using Process ID)
- Gracefully
```
kill <PID>
```
- Forcefully
```
kill -9 <PID>
```
- Using name
```
pkill <name>
```

---

## Difference between Kill Signals
### SIGHUP (1)
- Used to restart a process
```
kill -1 <PID>
```
### SIGTERM (15) (Default kill)
- Stops the process and cleans up
```
kill -15 1234 or just kill 1234
```
### SIGKILL (9)
- Immediate termination, cannot be ignored or caught
```
kill -9 1234
```

---

## Linux Permissions
### Files/ Directories have 3 permission sets
- Owner
- Group
- Others
### Each set has 3 permissions
- r (read)
- w (write)
- x (execute)

---

## Long format permissions
- Shown with ls -l e.g.
```
drwxr-xr-x 1 Kyle 197121  0 Mar 26  2024  IISExpress/
lrwxrwxrwx 1 Kyle 197121 19 May 11  2021 'My Music' -> /c/Users/Kyle/Music/
```
- 1st char is file type (- = file, d = directory, l = symbolic link)
- Next 3: Owner permissions (rwx)
- Next 3: Group permissions (r-x)
- Next 3: Others permissions (r-x)

---

## Short format permissions
- Numeric format (octal)
- Each permission has a value
- Shown with stat -c "%a %n" *
```
777 My Music
755 Sparta
```
- r = 4
- w = 2
- x = 1
- Owner permission (4 + 2 + 1) (rwx)
- Group permission (4 + 0 + 1) (r-x)
- Other permission (4 + 0 + 1) (r-x)

---

## Examples of changing file permissions
- Owner executable only
```
chmod 700 file.name or chmod o+rwx file.name
```
- Setting read and write to Group
```
chmod 760 file.name or chmod g+rw file.name
```
- Remove write for Other
```
chmod 760 file.name or chmod o-w file.name
```
- Setting Other to rwx
```
chmod 767 file.name or chmod o+rwx
```

---

## Wildcards
- There are three basic wildcards:
- '*' allow zero or more characters of any type e.g. *example
- ? allow any single character
- [] allow a range of characters