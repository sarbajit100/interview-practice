class Employee:
    raise_amount = 1.04
    def __init__(self,first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount)
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

        
emp_1 = Employee("sarbajit", "rout", 5000)
emp_2 = Employee("pabitra", "kumar", 3000)

# print(emp_1.first)
# print(emp_2)
# print(Employee.fullname(emp_1))
# print(emp_1.fullname())
# print(emp_2.fullname())
print(emp_1.__dict__)

