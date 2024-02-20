# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.


# Example 1:

# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
# Example 2:

# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false


class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        length = len(flowerbed)
        if (length==1 ):
            if (flowerbed[0]==0):
                return True
            else:
                if (n==0):
                    return True
                else:
                    return False

        if (flowerbed[0]==0 and flowerbed[1]==0):
            n=n-1
            flowerbed[0]=1
        for i in range(1, length-2):
            if (flowerbed[i]==0 and flowerbed[i-1]==0 and flowerbed[i+1]==0) :
                flowerbed[i]=1
                n= n-1

        if (flowerbed[-1]==0 and flowerbed[-2]==0):
            n=n-1
        if (n<=0):
            return True
        else:
            return False
        


flowerbed=[1,0,0,0,0,1]
n = 2
s1=Solution()
boolean = s1.canPlaceFlowers(flowerbed=flowerbed, n=n)
print(boolean)
