
# Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

# In the American keyboard:

# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".

# Input: words = ["adsdf","sfd"]
# Output: ["adsdf","sfd"]


class Solution(object):
    def findWords(self, words):
        first=['q', 'w', 'e','r','t','y','u','i','o','p']
        second=['a','s','d','f','g','h','j','k','l']
        third=['z','x','c','v','b','n','m']
        result =[]
        for ij in words:
            i = ij.lower()
            each_length=len(i)
            check_first=0
            check_second=0
            check_third=0

            for j in i:
                if j in first:
                    check_first=check_first+1
                if j in second:
                    check_second=check_second+1
                if j in third:
                    check_third=check_third+1
            if (check_first==each_length or check_second==each_length or check_third== each_length):
                result.append(ij)
        return result 
s1=Solution()
words = ["omk"]
result = s1.findWords(words=words)
print(result)