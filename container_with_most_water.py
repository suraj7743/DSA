# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.



# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.


class Solution:
    def maxArea(self, height: list[int]) -> int:
        l=0
        r=len(height)-1
        answer =0
        while (l<=r):
            minimum=min(height[l], height[r])
            result = minimum*(r-l)
            if (result>answer):
                answer=result
            if (height[l]<=height[r]):
                l=l+1
            else:
                r=r-1
        return answer




height = [1,8,6,2,5,4,8,3,7]
s1=Solution()
print(s1.maxArea(height=height))
