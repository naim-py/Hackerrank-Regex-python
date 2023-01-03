Regex_Pattern = r'^(Mr?s|[MDE]r)\.([A-Za-z]+)$'
#Mr?s=M ar por r othoba s hbe,and MDE ar por must r hbe
import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())