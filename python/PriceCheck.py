price = int(input("Enter price: "))

if price > 10000:
    print(price - (price * 20/100))
elif 7000 < price <= 10000:
    print(price - (price * 15/100))
else:
    print(price - (price * 10/100))


mark = int(input("Enter Mark in percentage: "))

if 0 <= mark < 40:
    print("Failed")
elif 40 <= mark < 55:
    print("Fair")
elif 55 <= mark < 65:
    print("Good")
elif 65 <= mark <= 100:
    print("Excellent")
else:
    print("Enter a valid number")
