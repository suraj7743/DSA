# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.





# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2


class Solution(object):
    def searchInsert(self, nums, target):
        l , r = 0, len(nums)-1
        while(l<=r):
            middle = (l+r)//2

            if (nums[middle]==target):
                return middle
            if (target>nums[middle]):
                l=middle+1
            else:
                r=middle-1
        return l 
target = 7
nums=[1,3,5,6]
s1=Solution()
result = s1.searchInsert(nums, target=target)
print(result)

