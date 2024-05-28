#!/usr/bin/env bash

CP=$(whereis cp | awk '{print $2}')
ECHO=$(whereis echo | awk '{print $2}')
TEE=$(whereis tee | awk '{print $2}')
PYTHON3=$(whereis python3 | awk '{print $2}')

if [ "$EUID" -ne 0 ]
  then $ECHO "Please run as root"
  exit 1
fi

$ECHO "This script will install SWU as a systemd service on you system"
$ECHO -n "Do you want to continue ? [y/N]"

read -p ": " confirm

if [[ "$confirm" =~ ^([yY][eE][sS]|[yY])$ ]]; then
    $ECHO "Perfect, let's go !"
    $ECHO "FYI: You can delete the service by deleting the following file:"
    $ECHO "\t/usr/local/bin/swu/ folder"
    $ECHO "\t/etc/systemd/system/swu.service file"
else
    $ECHO "Bye ! :("
    exit 1
fi

##############

$ECHO "Copying script files to /usr/local/bin/swu/ ..."

destination_bin=/usr/local/bin/swu

$MKDIR -p $destination_bin
$CP -r -t $destination_bin .env requirements.txt main.py utils/ gunicorn_config

$ECHO "Script files copied !"

##############

$ECHO "Init python env..."

$PYTHON3 -m venv $destination_bin/.venv
$destination_bin/.venv/bin/pip3 install -r $destination_bin/requirements.txt

##############

$ECHO "Creating service file at /etc/systemd/system/swu.service ..."

$ECHO -e "[Unit]\nDescription=SWU service by Mijux\nAfter=multi-user.target\n" | $TEE /etc/systemd/system/swu.service
$ECHO -e "[Service]\nType=simple\Restart=always\nExecStart=/usr/local/bin/swu/.venv/bin/gunicorn --config gunicorn_config.py main:app\n" | $TEE -a /etc/systemd/system/swu.service
$ECHO -e "[Install]\nWantedBy=multi-user.target" | $TEE -a /etc/systemd/system/swu.service

$ECHO "File /etc/systemd/system/swu.service created"
