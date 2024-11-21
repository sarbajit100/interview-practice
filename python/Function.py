def student(name, age,*email, address = "bangalore"):
    print(name)
    print(age)
    print(email)
    print(address)
student(
    input("Enter your name:"),
    input("Enter your age:"),
    input("Enter your email:"),
    input("Enter your confirm email:"),
    address=input("Enter your address:"),
)