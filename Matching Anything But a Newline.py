pat = r"^...\....\....\....$"	# Do not delete 'r'.
#pat= \w{3}\.\w{3}\.\w{3}\.\w{3}
import re
import sys

test_string = input()
match = re.match(pat, test_string) is not None
print(str(match).lower())
