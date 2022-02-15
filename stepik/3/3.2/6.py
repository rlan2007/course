#! /usr/bin/python3

import sys
import re

pattern = r"\bhuman\b"
repl = "computer"

#Считываем все строки по одной из стандартного потока ввода
for line in sys.stdin:
    line = line.rstrip()
    # process line
    line= re.sub(pattern,repl, line)  
    print(line)
