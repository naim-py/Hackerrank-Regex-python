p = r'^[^0-9][^aeiou][^bcDF][^\r\n\t\f][^AEIOU][^.,]$'
import re

print(str(bool(re.search(p, input()))).lower())