# listed=["3","6","7","10"]
# for i in range(len(listed)):
#     listed[i]= int(listed[i])
# listed.sort()
# print(listed)



# You are given an array of strings nums and an integer k. Each string in nums represents an integer without leading zeros.

# Return the string that represents the kth largest integer in nums.

# Note: Duplicate numbers should be counted distinctly. For example, if nums is ["1","2","2"], "2" is the first largest integer, "2" is the second-largest integer, and "1" is the third-largest integer.


# Input: nums = ["3","6","7","10"], k = 4
# Output: "3"
# Explanation:
# The numbers in nums sorted in non-decreasing order are ["3","6","7","10"].
# The 4th largest integer in nums is "3".


class Solution(object):
    def kthLargestNumber(self, nums, k):
        for i in range(len(nums)):
            nums[i]=int(nums[i])
        nums.sort()
        nums.reverse()
        return str(nums[k-1])
        

nums =["0","0"]
k=2
s1=Solution()
result = s1.kthLargestNumber(nums=nums, k=k)
print(result)
