class A:
    def function_one(self):
        print("this is function one")
    def function_two(self):
        print("this is function Two")
class B(A):
    def function_two(self):
        print("this is function")
    def function_three(self):
        print("this is function Three")

b=B()
b.function_one()
b.function_two()
b.function_three()