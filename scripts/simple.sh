#!/bin/bash

crt=$(curl -s https://crt.sh/q=$1&output=json | jq -r '.common-name')
suba=$(echo $1 | ~/.subcon/bin/./assetfinder -subs-only | grep $1 | sort -u)
subf=$(~/.subcon/bin/subfinder -d $1 -all -silent)
echo "$crt $suba $subf" | sort -u 