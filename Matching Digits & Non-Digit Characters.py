Regex_Pattern = r"\d\d\D\d\d\D\d\d\d\d"	# Do not delete 'r'.
#r"\\d{2}\\D\\d{2}\\D\\d{4}"
import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())