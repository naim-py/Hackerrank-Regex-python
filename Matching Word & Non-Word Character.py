p=r"\w{3}\W\w{10}\W\w{3}"
import re
print(str(bool(re.search(p,input()))).lower())