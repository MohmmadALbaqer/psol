#!/bin/bash

if [ "$(id -u)" != "0" ]; then
    red_sudo=$(tput setaf 1) # Set text color to red
    echo -e "\[${red_sudo}\]You need to run this program with sudo. Please !.\[${reset}\]"
    exit 1
fi
clear
echo '''
 _           _        _ _ 
(_)_ __  ___| |_ __ _| | |
| | '_ \/ __| __/ _` | | |
| | | | \__ \ || (_| | | |
|_|_| |_|___/\__\__,_|_|_|
'''

sudo apt-get update 
sudo apt-get install -y nodejs
sudo apt-get install openssh-client
sudo apt-get update
sudo apt-get install -y npm
