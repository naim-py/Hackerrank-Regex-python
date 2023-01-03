import re
n=int(input())
p=r'<(\w+)'
l=[]
for i in range(n):
    st=input()
    match=re.findall(p,st)
    for j in match:
        l.append(j)
a=sorted(set(l))
print(';'.join(a))
