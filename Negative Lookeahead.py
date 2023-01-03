#\1 = Denotes the first matching group

Regex_Pattern = r"(.)(?!\1)"	# Do not delete 'r'.

import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)
print(match)
print("Number of matches :", len(match))

#ooooooooo=o jot gulai dina output actai
#['o']