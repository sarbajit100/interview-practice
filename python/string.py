# def reverse_words(sentence):
#     words = sentence.split()  # Split the sentence into words
#     print(words)
#     reversed_words = words[::-1]  # Reverse the list of words
#     return ' '.join(reversed_words)  # Join the words back into a string

# # Test the function
# input_sentence = "Hello World from Python"
# result = reverse_words(input_sentence)
# print(result)  # Output: "Python from World Hello"

def reverse_words(sentence):
    my_list = list(sentence)
    l = 0
    r = len(sentence)-1
    while l<r:
        my_list[l], my_list[r] = my_list[r], my_list[l]
        l+=1
        r-=1
    # sentence1 = ''.join(my_list)
    return ''.join(my_list)


input_sentence = "Hello World from Python"
result = reverse_words(input_sentence)
print(result)