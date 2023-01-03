Regex_Pattern = r'o(?=oo)'

import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)
print(match)
print("Number of matches :", len(match))

#ooo=['o']
#3 ta o te 1ta ['o'],3 ar por joita thakbe totota
#ooooooooo
#['o', 'o', 'o', 'o', 'o', 'o', 'o']