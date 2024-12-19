import re
# NameAge = '''
# Janice is 22 and Theon is 33
# Gabriel is 44 and Joey is 21
# '''
# ages = re.findall(r'\d{1,3}', NameAge)
# names = re.findall(r'[A-Z][a-z]*', NameAge)

# ageDict = {}
# x = 0

# for name in names:
#     ageDict[name] = ages[x]
#     x+=1
# print(ageDict)

# if re.search("inform", "we need to inform him with the latest information"):
#     print("there is inform")

# allinform = re.findall("inform", "we need to inform him with the latest information")

# for i in allinform:
#     print(i)

# str = "we need to inform him with the latest information"

# for i in re.finditer('inform', str):
#     loctup = i.span()
#     print(loctup)

# s = "Sat, hat, mat, pat"
# alls = re.findall("[Shmp]at", s)

# for i in alls:
#     print(i)

# s = "sat, hat, mat, pat"
# alls = re.findall("[^h-m]at", s)

# for i in alls:
#     print(i)

# randstr = '''
# keep the blue flag
# flying high
# chelsea
# '''
# print(randstr)
# regex = re.compile("\n")
# randstr = regex.sub(" ", randstr)
# print(randstr)

# num = '12345 1256 56734'
# print("Matches", len(re.findall("\d{5,7}", num)))

#\w[a-zA-Z0-9]
#\W[^a-zA-Z0-9]

phn = "412-254-2256"

if re.search("\d{3}-\d{3}-\d{4}" ,phn):
    print("it is a number")
