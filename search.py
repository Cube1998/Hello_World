import re

a = 'abcade'
pattern = re.compile(r'a.c',re.S)
find = re.findall(pattern,a)
search = re.match(pattern,a)
if search:
	print search.string
if find:
	a = find[0]
	print a
else:
	print ("NOPE")
