#!/usr/bin/env bash

###############################################
# wifi_cycler.sh: Reset to a wifi 	      #
# Author: Oz Tamir (TheOzTamir@gmail.com)     #
###############################################

echo 'Disabling Wi-Fi...'
networksetup -setairportpower en0 off
echo 'Sleeing for a second...'
sleep 1s
echo 'Enabling Wi-Fi...'
networksetup -setairportpower en0 on