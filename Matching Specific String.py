pat=r'hackerrank'
import re
s=input()
match = re.match(pat,s)
print("Number of matches :", len(match))