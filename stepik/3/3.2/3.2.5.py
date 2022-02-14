#не робит
import re
import sys
pattern = r"human"
repl = "computer"
for line in sys.stdin:
    line = line.rstrip()
    re.sub(pattern, repl, line)
    print(line)
