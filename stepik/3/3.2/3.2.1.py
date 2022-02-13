import sys
import re
pattern = r".{0,}(cat).{0,}(cat).{0,}"
for line in sys.stdin:
    line = line.rstrip()
    if re.match(pattern,line) is not None:
        print(line)
