# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.



# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

class Solution(object):
    def searchRange(self, nums, target):
        start =0
        end = len(nums)-1
        result=[-1,-1] # result [0] for first occurance and result [1] for last occurance
        start_last=0
        end_last=len(nums)-1
        while (start<=end):
            middle= start + ((end- start )//2)
            if (nums[middle]==target):
                 result[0]=middle
                 end = middle-1
            elif (nums[middle]<target):
                start = middle +1

            else:
                end= middle-1
        while (start_last<=end_last):
            middle= start_last + ((end_last- start_last )//2)
            if (nums[middle]==target):
                result[1]=middle
                start_last=middle+1
            elif (nums[middle]<target):
                start_last = middle +1

            else:
                end_last= middle-1
        return result 
    

nums = [5,7,7,8,8,10]
target = 8
s1=Solution()
arr=s1.searchRange(nums=nums, target=target)
print(arr)
        