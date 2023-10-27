#!/bin/bash
echo $1 | ~/.subcon/bin/subfinder -silent | rev | cut -d "." -f3 | rev | sort -u > ~/.subcon/dw
shuffledns -l ~/.subcon/dw -r ~/.subcon/resolver -silent 