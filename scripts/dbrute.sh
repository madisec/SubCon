#!/bin/bash
echo $1 | skubfinder -silent | rev | cut -d "." -f3 | rev | sort -u > ~/.subcon/dw
shuffledns -l ~/.subcon/dw -r ~/.subcon/resolver -silent 