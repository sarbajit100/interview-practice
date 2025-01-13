# Problem 1:
def twoSum(nums, target):
    # Hash map to store value and its index
    num_dict = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))

# Problem 2:
def isValid(s):
    # my_list to keep track of opening brackets
    my_list = []
    # Mapping of closing to opening brackets
    bracket = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in bracket.values():  # If it's an opening bracket
            my_list.append(char)
        elif char in bracket:  # If it's a closing bracket
            if my_list and my_list[-1] == bracket[char]:
                my_list.pop()
            else:
                return False
        elif char in "',":  # Neutral characters
            continue  # Ignore neutral characters
        else:
            return False  # Invalid character

    return not my_list  # my_list should be empty if valid

# Problem 3:
from collections import Counter
import heapq

def frequent(nums, k):
    # Step 1: Count frequencies using Counter
    freq_map = Counter(nums)
    
    # Step 2: Use a heap to extract top k frequent elements
    return [item for item, _ in heapq.nlargest(k, freq_map.items(), key=lambda x: x[1])]

nums = [1,1,1,2,2,3]
k = 2
print(frequent(nums, k))

