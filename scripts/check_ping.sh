#!/usr/bin/env bash

###############################################
# check_ping.sh: check the currenty ping 	  #
# Author: Oz Tamir (TheOzTamir@gmail.com)     #
###############################################

PING_IP='8.8.8.8'

ping_response="$(ping -i 0.1 -c 1 "$PING_IP" | head -2 | tail -1)"

response_time="$(echo "$ping_response" | grep -ic -E -o 'time=.* ms')"

if [ $response_time -eq 1 ]
then
  echo "$ping_response" | grep -E -o 'time=.* ms' | cut -c6-
else
  echo 'N/A'
fi