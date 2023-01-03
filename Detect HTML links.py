import re
n = int(input())
pattern = r'<a\shref=\"(.+?)\".*?>([^<]*?)</'
#.+? means 1to any indexe . bste pare ? mane specially first and laste
for i in range(n):
    st=input()
    match= re.findall(pattern,st)
    print(match)
    for l,t in match:
        print(f'{l},{t.strip()}')


#https://stackoverflow.com/questions/3075130/what-is-the-difference-between-and-regular-expressions
