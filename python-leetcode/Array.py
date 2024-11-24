# Remove Duplicates from Sorted Array
# num = [1,5,6,8,5,1,9]
# nums = sorted(num)
# l=1
# for r in range(1,len(nums)):
#     if nums[r] != nums[r-1]:
#         nums[l] = nums[r]
#         l += 1
# print(l)

# Best Time to Buy and Sell Stock II
# prices = [7,1,5,3,6,4]
# def maxProfit(prices):
#     i=0
#     hi=0
#     lo=0
#     profit=0
#     n=len(prices)
#     while i<n-1:
#         while i<n-1 and prices[i]>=prices[i+1]:
#             i+=1
#         lo = prices[i]
#         while i<n-1 and prices[i]<=prices[i+1]:
#             i+=1
#         hi = prices[i]
#         profit += hi-lo
#     return profit
# print(maxProfit(prices))

# Rotate Array
# nums = [-1,-100,3,99] 
# k = 2
# def rotate(nums, k):
#     k=k%len(nums)
#     l,r=0,len(nums)-1
#     while l<r:
#         nums[l],nums[r] = nums[r],nums[l]
#         l,r = l+1,r-1
#     l,r=0,k-1
#     while l<r:
#         nums[l],nums[r] = nums[r],nums[l]
#         l,r = l+1,r-1
#     l,r=k,len(nums)-1
#     while l<r:
#         nums[l],nums[r] = nums[r],nums[l]
#         l,r = l+1,r-1
#     return nums
# print(rotate(nums, k))

# Contains Duplicate
# nums = [1,2,3,1]
# hasset = set()
# for n in nums:
#     if n in hasset:
#         print(True)
#     hasset.add(n)
#     print(False)

# Single Number
# nums = [2,2,1]
# a=0
# for n in nums:
#     a= a^n
# print(a)

# Intersection of Two Arrays II