# System Information Tool

## Objective
A Bash tool that shows basic information about a Linux system: hostname, uptime, disk usage and memory usage. It helps a user quickly check the state of a machine.

## Features
- Shows hostname and uptime
- Shows disk usage of the root partition
- Shows memory usage
- Lets the user choose which section to show with options
- Has a help option (-h)
- Shows an error message when an unknown option is used

## Requirements
- Linux (tested on Kali Linux)
- Bash
- Standard commands: hostname, uptime, df, free

## How to Run
```bash
chmod +x tool.sh
./tool.sh
```

## Example Usage
```bash
./tool.sh        # full report
./tool.sh -a     # full report
./tool.sh -u     # hostname and uptime only
./tool.sh -d     # disk usage only
./tool.sh -m     # memory usage only
./tool.sh -h     # help
```

## Example Output
![Full report](screenshots/01-full-report.png)
![Memory only](screenshots/02-memory-only.png)
![Help menu](screenshots/03-help.png)
![Error handling](screenshots/04-error.png)

## Challenges Faced
- I got a syntax error when I edited the script, so I rewrote the file cleanly.
- Pasting did not work with Ctrl + V in the terminal. I used Ctrl + Shift + V.

## Future Improvements
- (write your own ideas here before you commit)
