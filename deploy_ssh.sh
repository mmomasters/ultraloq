#!/bin/bash
# SSH Deployment script for Ultraloq project
# Usage: ./deploy_ssh.sh [user@host] [remote_path]
# Example: ./deploy_ssh.sh pi@192.168.1.100 /home/pi/ultraloq

if [ $# -lt 2 ]; then
    echo "Usage: $0 <user@host> <remote_path>"
    echo "Example: $0 pi@192.168.1.100 /home/pi/ultraloq"
    exit 1
fi

SSH_TARGET=$1
REMOTE_PATH=$2

echo "Deploying Ultraloq to ${SSH_TARGET}:${REMOTE_PATH}"

# Create remote directory
ssh ${SSH_TARGET} "mkdir -p ${REMOTE_PATH}"

# Copy project files
echo "Copying project files..."
scp -r utecio/ ${SSH_TARGET}:${REMOTE_PATH}/
scp check_lock_status.py ${SSH_TARGET}:${REMOTE_PATH}/
scp requirements.txt ${SSH_TARGET}:${REMOTE_PATH}/
scp config.py ${SSH_TARGET}:${REMOTE_PATH}/

# Install dependencies and run script
echo "Installing dependencies on remote host..."
ssh ${SSH_TARGET} << 'EOF'
cd ${REMOTE_PATH}
python3 -m pip install --user -r requirements.txt
echo "Installation complete!"
echo ""
echo "Before running, please edit ${REMOTE_PATH}/config.py with your credentials:"
echo "  - EMAIL: your Utec app email"
echo "  - PASSWORD: your Utec app password"
echo "  - LOCK_NAME: your lock's name"
echo ""
echo "To run the script:"
echo "  python3 ${REMOTE_PATH}/check_lock_status.py"
EOF

echo ""
echo "Deployment complete!"
