import re
txt= 'Naim is a simple man'
r = re.findall(r'\w+',txt)
print(r)
''''
re.findall()
Return all non-overlapping matches of pattern in string, 
as a list of strings. The string is scanned left-to-right,
 and matches are returned in the order found.

Example:


# A Python program to demonstrate working of 
# findall() 
import re

# A sample text string where regular expression  
# is searched. 
string = """Hello my Number is 123456789 and 
             my friend's number is 987654321"""

# A sample regular expression to find digits. 
regex = '\d+'

match = re.findall(regex, string)
print(match) 
'''''