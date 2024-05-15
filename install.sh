#!/bin/bash

if [ "$(id -u)" != "0" ]; then
    red_sudo=$(tput setaf 1) # Set text color to red
    echo -e "\[${red_sudo}\]You need to run this program with sudo. Please !.\[${reset}\]"
    exit 1
fi
clear

sudo apt-get update 
sudo apt-get install -y nodejs
sudo apt-get install openssh-client
sudo apt-get update
sudo apt-get install -y npm
