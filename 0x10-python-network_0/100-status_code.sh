#!/bin/bash 
# script that sends a request
curl -s -L -X HEAD -w "%{http_code}" "$1"
