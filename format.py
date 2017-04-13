#!/usr/bin/env python3

import sys, os, re

updateFile = open("domainslist.txt", "r")
output = open("d.txt", "w")

for line in updateFile:
	data = re.sub(".+?,", "", line)
	output.write(data)