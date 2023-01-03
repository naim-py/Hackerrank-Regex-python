import re
txt = "This is a python book"
x = re.search(r"^This.*book$",txt)
#for first(^) "This" and for end ($) "book":
print(x)
if x:
    print("Valid")
else:
    print("Invallid")

#+ <re.Match object; span=(0, 21), match='This is a python book'>
#* <re.Match object; span=(0, 21), match='This is a python book'>