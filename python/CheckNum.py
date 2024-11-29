# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))
# num4 = int(input("Enter the fourth number: "))
# number = (num1, num2, num3, num4)

# def check_numbers (number):
#     count = 0

#     for num in number:
#         if 50 <= num <= 100:
#             count += 1

#     return count == 1

# result = check_numbers(number)

# if result:
#     print("I understand")
# else:
#     print("I didn't understand")

# num1 =int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))
# num4 = int(input("Enter the fourth number: "))

# if 50 < num1 < 100 or 50 < num2 < 100 or 50 < num3 < 100 or 50 < num4 < 100:
#     print("I understand")
# else:
#     print("I didn't understand")

# x = float(input("E:"))
# x=round(BMI,1)
# if 0<=x<=18.5:
#     print("Underweight")
# elif 18.5<x<=24.9:
#     print("Normal")
# elif 25.0<=x<=29.9:
#     print("Overweight")
# else:
#     print("obese")

# num = 90
# while num>= 65:
#     x=chr(num)
#     print(x)
#     num=num-1

# Print numbers from 1 to 100 in the specified format
# for i in range(1, 101, 10):
#     print(*range(i, i + 10))

# Print numbers from 1 to 100 in the specified format
# for i in range(1, 101):
#     print(i, end=' ')
#     if i % 10 == 0:
#         print()  # Print a new line after every 10 numbers
# def f1(*a):
#     for i in a:
#         print(i)



# f1(1, 2, 6, 4)


# def print_data(**b):
#     for value, key in b.items():
#         print(key, ":", value)


# # Example usage:
# data = {"name": "John", "age": 30, "city": "New York"}
# print_data(**data)

# import datetime

# def count_friday_13ths(start_year, end_year):
#     count = 0
#     for year in range(start_year, end_year + 1):
#         for month in range(1, 13):
#             if datetime.date(year, month, 13).weekday() == 4:
#                 count += 1
#     return count

# friday_13ths = count_friday_13ths(2000, 2099)
# print(friday_13ths)

# def upper_xvowels_sequence(text):
#     xvowels = "abeiout"
#     result = ""
#     i = 0
#     while i < len(text):
#         if text[i] in xvowels:
#             count = 1
#             while i + count < len(text) and text[i + count] == text[i]:
#                 count += 1
#             if count >= 2:
#                 result += text[i:i+count].upper()
#                 i += count
#             else:
#                 result += text[i]
#                 i += 1
#         else:
#             result += text[i]
#             i += 1
#     return result

# input_str = input("Enter a string: ")
# output_str = upper_xvowels_sequence(input_str)
# print(output_str)




