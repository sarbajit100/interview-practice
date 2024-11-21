# x = int(input('Enter 1st number:'))
# y = int(input('Enter 2nd number:'))
# symbol = input('Enter A symbol')
#
# if symbol == '+':
#     print(x+y)
# elif symbol == '-':
#     print(x-y)
# elif symbol == '*':
#     print(x*y)
# elif symbol == '/':
#     print(x/y)
# else:
#     print('not a valid symbol')

# x = int(input('Enter 1st number:'))
# y = int(input('Enter 2nd number:'))
#
# if x > y:
#     print(f"{x} is bigger")
# elif y > x:
#     print(f"{y} is bigger")
# else:
#     print(f"{y} is Equal to {x}")

# x = input('Gender M for male and F for female:').lower()
# y = int(input('Enter Age:'))
#
# if x == 'm' and y >= 21:
#     print('eligible')
# elif x == 'f' and y >= 18:
#     print('eligible')
# else:
#     print('not eligible')

# y = int(input('Year:'))
# if y % 4 == 0:
#     if y % 100 == 0:
#         if y % 400 == 0:
#             print('leap year')
#         else:
#             print('not a leap year')
#     else:
#         print('not a leap year')
# else:
#     print('not a leap year')

# N = int(input('Enter a number:'))
#
# if N%3 == 0 or N%7 == 0:
#     if N%7 == 0:
#         if N % 7 == 0 and N % 3 == 0:
#             print('Instagram')
#         else:
#             print('Facebook')
#     else:
#         print('WhatsApp')
# else:
#     print('Google')

# I = input('Enter a letter:').lower()

# if I == 'a':
#     print('Android')
# elif I == 'b':
#     print('Bluetooth')
# elif I == 'c':
#     print('Connect')
# else:
#     print('Enter only A or B or C')

N = int(input('Enter a number:'))
if N % 7 != 0 or N % 3 != 0:
    if N%3 != 0:
        if N%7 != 0:
            print('google')
        else:
           print('Facebook') 
    else:
       print('Whatsapp')
else:
   print('instagram') 


