#(.) for all character
Regex_Pattern = r"(?<![(aeiuoAEIOU])(.)"

import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))