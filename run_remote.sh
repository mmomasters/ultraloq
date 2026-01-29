#!/bin/bash
# Run check_lock_status.py remotely via SSH
# Usage: ./run_remote.sh [user@host] [remote_path]
# Example: ./run_remote.sh pi@192.168.1.100 /home/pi/ultraloq

if [ $# -lt 2 ]; then
    echo "Usage: $0 <user@host> <remote_path>"
    echo "Example: $0 pi@192.168.1.100 /home/pi/ultraloq"
    exit 1
fi

SSH_TARGET=$1
REMOTE_PATH=$2

echo "Running check_lock_status.py on ${SSH_TARGET}..."
echo ""

ssh ${SSH_TARGET} "cd ${REMOTE_PATH} && python3 check_lock_status.py"
