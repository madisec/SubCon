import argparse
import sys
import os
import pyfiglet

# make program figlet
figlet_program = pyfiglet.figlet_format("SubCon")
fp_tostring = str(figlet_program)

# Make argument for tools
parser = argparse.ArgumentParser(usage="subcon",
                                 prog=print(fp_tostring),
                                 description="SubCon is a tool for subdomains discovery",
                                 epilog="Powered by MadiSec")

parser.add_argument("-d",
                    dest="domain",
                    help="Domain for finding all subdomains.")

parser.add_argument("-f",
                    dest="full",
                    help="full automate subdomains discovery.")

parser.add_argument("-db",
                    dest="dbrute",
                    help="Only dynamic DNS brute force.")

parser.add_argument("-sb",
                    dest="sbrute",
                    help="Only Static DNS brute force.")

parser.add_argument("-si",
                    dest="simple",
                    help="Simpe subdomains discovery.")

parser.add_argument("-mw",
                    dest="mk",
                    help="Make subdomain wordlist.")

parser.add_argument("-o", 
                    dest="output",
                    help="Save output to file, such as .txt")
parser.add_argument("-v",
                    action="version",
                    version="version:   1.0.1")

args = parser.parse_args()

# Argument to variable
domain = args.domain
full = args.full
dbrute = args.dbrute
sbrute = args.sbrute
simple = args.simple
mk = args.mk
output = args.simple

