import re
import sys
pattern = r".{0,}z.{3}z.{0,}"
for line in sys.stdin:
    line = line.rstrip()
    if re.fullmatch(pattern, line) is not None:
        print(line)
