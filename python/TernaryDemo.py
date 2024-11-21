a = int(input('Enter a num: '))
b = int(input('Enter a num: '))
c = int(input('Enter a num: '))
# print('a is bigger' if a>b else 'b is bigger')

res = a if a>c else c if a>b else b if b>c else c
print(res)