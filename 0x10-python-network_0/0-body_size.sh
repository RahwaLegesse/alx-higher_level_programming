#!/bin/bash
# takes in a URL and display in screen
curl -sI ALLOW $1 -L | grep "Allow" | cut -d " " -f2-
