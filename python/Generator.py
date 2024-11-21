# def m1():
#     yield 20
#     yield 10
# a = m1()
# print(a)
# print(next(a))
# print(next(a))
# print(next(a))
def m1(x):
    while x >= 0:
        yield x
        x=x-1
a = m1(100)
print(a)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
for i in a:
    print(i)

