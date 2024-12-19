# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]


# def reverseString(s):
#     """
#     :type s: List[str
#     :rtype: None Do not return anything, modify s in-place instead.
#     """
#     s.reverse()
#     return s

# Input: x = 123
# Output: 321

# Input: x = -123
# Output: -321

# Input: x = 120
# Output: 21

# def reverse(x):
#     """
#     :type x: int
#     :rtype: int
#     """
#     is_neg = x<0
#     x=abs(x)
#     res = 0
    
#     while x:
#         digit = x%10
#         x //= 10
#         res = res*10 +digit
        
#         if res > 2**31-1:
#             return 0
#     return res * -1 if is_neg else res
# print(reverse(123))

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

# Input: s = "leetcode"
# Output: 0

# Input: s = "loveleetcode"
# Output: 2

# Input: s = "aabb"
# Output: -1

# def firstUniqChar(self, s):
#     """
#     :type s: str
#     :rtype: int
#     """
#     char_count = {}
#     for char in s:
#         char_count[char] = char_count.get(char, 0) + 1

#     # Find the first character with a count of 1
#     for i, char in enumerate(s):
#         if char_count[char] == 1:
#             return i

#     return -1

#     for i in range(len(s)):
#         if s.count(s[i]) == 1:  # Check if the character appears only once
#             return i  # Return the index of the first unique character
#     return -1 

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# def isAnagram(self, s, t):
#     """
#     :type s: str
#     :type t: str
#     :rtype: bool
#     """
#     if len(s) != len(t):
#         return False
    
#     countS, countT = {}, {}
#     for i in range(len(s)):
#         countS[s[i]] = 1 + countS.get(s[i], 0)
#         countT[t[i]] = 1 + countT.get(t[i], 0)
#     for c in countS:
#         if countS[c] != countT.get(c, 0):
#             return False
#     return True

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.
# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

# def isPalindrome(self, s):
#     """
#     :type s: str
#     :rtype: bool
#     """
#     newString = ''
#     for i in s:
#         if i.isalnum():
#             newString += i.lower()
#     return newString == newString[::-1]

# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# Example 1:
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

# def strStr(self, haystack, needle):
#     """
#     :type haystack: str
#     :type needle: str
#     :rtype: int
#     """
#     if needle == "":
#         return 0
#     for i in range(len(haystack) +1 -len(needle)):
#         if haystack[i:len(needle)+i] == needle:
#             return i
#     return -1

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# def longestCommonPrefix(self, strs):
#     """
#     :type strs: List[str]
#     :rtype: str
#     """
#     res = ""
#     for i in range(len(strs[0])):
#         for s in strs:
#             if i == len(s) or s[i] != strs[0][i]:
#                 return res
#         res += s[i]
#     return res