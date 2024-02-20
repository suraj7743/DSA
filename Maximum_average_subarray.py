# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

# # 



# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75


class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        first=sum(nums[0:k])
        temp=[first]
        for i in range(1,len(nums)):
            if (i-1 +k >=len(nums)):
                break
            else:
                temp.append((temp[i-1]-nums[i-1]+nums[i-1+k]))
        return max(temp)/k


nums = [1,12,-5,-6,50,3]
k = 4
s1=Solution()
result =s1.findMaxAverage(nums=nums, k=k)
print(result)

        