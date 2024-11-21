dict = {10:'a', 20:'b', 30:'c'}
for i in dict:
    print(i, dict[i], sep='=')

my_tuple = (10, 20, 30, 40, 50, 60, 70, 80, 90)  # Example tuple

# Printing odd index elements of the tuple in reverse order
for i in range(len(my_tuple) - 1, -1, -1):
    if i % 2 != 0:
        print(my_tuple[i])