import re
l=[]
for i in range(int(input())):
    sentence=input()
    l.append(sentence)
string = '\n'.join(l)   #[] braket uthanor jonne
for j in range(int(input())):
    sub_str=input()
    pattern= r'\w+{}\w+'.format(sub_str)
    match=re.findall(pattern,string)
    print(len(match))

