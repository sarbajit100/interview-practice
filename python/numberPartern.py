# x = 1
# while x<=100:
#     if x%5 == 0 and x%3 == 0:
#         print("fizz buzz")
#     elif x%3 == 0:
#         print("fizz")
#     elif x%5 == 0:
#         print("buzz")
#     x+=1

# num = int(input("Enter a number"))
# rev = 0
# while num > 0:
#     r = num % 10
#     rev = rev * 10 + r
#     num = num // 10
# print(rev)

i=1

while i in range(1, 100):
    n=1
    while n in range(1, 100):
        if i//n == 0:
            print(i)
        