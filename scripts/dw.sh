#!/bin/bash
echo $1 | ~/.subcon/bin/subfinder -all -silent | rev | cut -d "." -f3 | rev | sort -u