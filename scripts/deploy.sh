#!/bin/bash

set -ev

# Install or update needed software
apt-get update -y
apt-get install -yq git python3 python3-pip python3-distutils
pip install --upgrade pip virtualenv

# Account to own server process
if id "pythonapp" &>/dev/null; then
    echo 'User pythonapp exists'
else
    echo 'User pythonapp not found'
    useradd -m -d /home/pythonapp pythonapp
fi

# Python environment setup
virtualenv -p python3 /opt/animated-potato/env
/bin/bash -c "source /opt/animated-potato/env/bin/activate"
/opt/animated-potato/env/bin/pip install -r /opt/animated-potato/requirements.txt

# Set ownership to newly created account
chown -R pythonapp:pythonapp /opt/animated-potato

# Put supervisor configuration in proper place
cp /opt/animated-potato/systemd-config/special-app-metrics.service /lib/systemd/system/special-app-metrics.service

# Start service via systemctl
systemctl daemon-reload
systemctl enable special-app-metrics
systemctl start special-app-metrics