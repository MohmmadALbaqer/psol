#!/bin/bash

clear
echo '''
 _           _        _ _ 
(_)_ __  ___| |_ __ _| | |
| | '_ \/ __| __/ _` | | |
| | | | \__ \ || (_| | | |
|_|_| |_|___/\__\__,_|_|_|
'''

apt-get update 
apt-get install -y nodejs
apt-get install openssh-client
apt-get update
apt-get install -y npm
