age = int(input("Enter Your Age: "))
gender = input("Enter Gender As M/F : ").lower()
days = int(input("Enter days in number"))
if 18 <= age < 30:
    if gender == 'm':
        print(days*700)
    elif gender == 'f':
        print(days*750)
    else:
        print("Enter appropriate gender")

elif 30 <= age <= 40:
    if gender == 'm':
        print(days*800)
    elif gender == 'f':
        print(days*850)
    else:
        print("Enter appropriate gender")

else:
    print("Enter appropriate Age")