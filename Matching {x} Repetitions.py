Regex_Pattern = r'^[a-zA-Z02468]{40}[13579]{5}$'

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())