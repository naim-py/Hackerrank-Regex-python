Regex_Pattern = r'^\d{2,}[a-z]*[A-Z]*$'
#input=14
import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
''''
w* : It will match the character w 0 or more times.
[xyz]* : It will match the characters x, y or z  0 or more times.
\d* : It will match any digit 0 or more times.
if begin with 2 or more digits(\d{2,})

'''''