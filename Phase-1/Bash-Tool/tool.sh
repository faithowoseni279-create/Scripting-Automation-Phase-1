#!/bin/bash
# System Information Tool
# Shows basic information about the Linux system

# Shows how to use the tool
usage() {
    echo "Usage: ./tool.sh [option]"
    echo "  -a   show everything"
    echo "  -u   show hostname and uptime"
    echo "  -d   show disk usage"
    echo "  -m   show memory usage"
    echo "  -h   show this help"
}

# Shows the hostname and uptime
show_uptime() {
    echo "[Hostname]"
    hostname
    echo
    echo "[Uptime]"
    uptime -p
    echo
}

# Shows disk usage of the root partition
show_disk() {
    echo "[Disk Usage - Root Partition]"
    df -h /
    echo
}

# Shows memory usage
show_memory() {
    echo "[Memory Usage]"
    free -h
    echo
}

# Check which option the user typed
case "$1" in
    -a|"")
        show_uptime
        show_disk
        show_memory
        echo "Information check complete."
        ;;
    -u) show_uptime ;;
    -d) show_disk ;;
    -m) show_memory ;;
    -h) usage ;;
    *)
        echo "Error: unknown option '$1'"
        usage
        exit 1
        ;;
esac
