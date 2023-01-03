p=r"(ok){3,}"
import re
print(str(bool(re.search(p,input()))).lower())