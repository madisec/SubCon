#!/bin/bash
echo $1 | skubfinder -all -silent | rev | cut -d "." -f3 | rev | sort -u