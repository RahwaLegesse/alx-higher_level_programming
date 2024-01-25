#!/bin/bash
# Get the byte size  URL.
curl -s "$1" | wc -c
