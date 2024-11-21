list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list[0:6])

tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(tuple[-1:-11:-1])

dict = {
    'A':100,
    'B':200,
    'C':300
}

dict['B'] = 400
dict['D'] = 500
print(dict)

x = set(range(3, 31, 3))
print(x)

s = "python is simple"
print(s[15:9:-1])
print(s[-11:-17:-1])
print(s[7:9])
