# x = {1: 'a', 2: 'b', 3: 'c'}
# print(x)
# print(type(x))
# Dict = {100: 'python', 101: 'java', 103: '.Net'}
# print(Dict)
# print(Dict[100])
# print(Dict[101])
# print(Dict[103])
# Dict[102] = 'javaScript'
# print(Dict)
# s = set()
# print(type(s))

class MyClass:
    def __init__(self, name):
        self.name = name

    def instance_method(self):
        print(f"{self.name}, good morning")

    @classmethod
    def class_method(cls, place):
        print(f"Hello palle and {place}")

    @staticmethod
    def static_method(num1, num2):
        print(f"The sum of {num1} and {num2} is {num1 + num2}")


# Creating an instance of MyClass
obj = MyClass("John")

# Calling the instance method
obj.instance_method()  # Output: John, good morning

# Calling the class method
MyClass.class_method("there")  # Output: Hello palle and there

# Calling the static method
MyClass.static_method(5, 7)  # Output: The sum of 5 and 7 is 12

