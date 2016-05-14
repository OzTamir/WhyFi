#!/usr/bin/env bash

###############################################
# power_cycle.sh: reboot a HOTBOX router 	  #
# Author: Oz Tamir (TheOzTamir@gmail.com)     #
###############################################

USERNAME='admin'
PASSWORD='admin'

# Get the IP of the router
get_ip() {
	ROUTER_IP=$(netstat -rn | grep default | grep -E -o '([0-9]{1,3}[\.]){3}[0-9]{1,3}')
	IFS='.' read -a ip <<< "$ROUTER_IP"
}

do_reboot() {
	LOGIN_URL="http://${ip[0]}.${ip[1]}.${ip[2]}.${ip[3]}/goform/login"
	REBOOT_URL="http://${ip[0]}.${ip[1]}.${ip[2]}.${ip[3]}/goform/RgSetup"
	ORIGIN_URL="http://${ip[0]}.${ip[1]}.${ip[2]}.${ip[3]}"
	REFERER_URL="http://${ip[0]}.${ip[1]}.${ip[2]}.${ip[3]}/RgSetup.asp"

	LOGIN_DATA="loginUsername=$USERNAME&loginPassword=$PASSWORD&rememberMe=rememberMe"
	POST_DATA="LocalIpAddressIP0=${ip[0]}&LocalIpAddressIP1=${ip[1]}&LocalIpAddressIP2=${ip[2]}&LocalIpAddressIP3=${ip[3]}&WanLeaseAction=0&WanConnectionType=0&MtuSize=0&RestoreFactoryNo1=0x00&ApplyRgSetupAction=0&ApplyRebootAction=1"

	# Reboot the router
	response="$(curl -s "$LOGIN_URL" \
	--data "$LOGIN_DATA" --compressed \
	| \
	curl -s "$REBOOT_URL" \
	-H 'Pragma: no-cache' \
	-H 'Origin: "$ORIGIN_URL" \
	-H 'Referer: "$REFERER_URL" \
	-H 'Cookie: login=`elho.`elho.r`wd' \
	-H 'Connection: keep-alive' \
	--data "$POST_DATA" \
	--compressed)"
}

# Do the reboot
get_ip
do_reboot

# Print the router's last message
result="$(echo "$response" | grep -E -o '<h1>([^<])*' | cut -c5-)"
echo $result