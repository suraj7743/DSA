# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

#  Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].


class Solution(object):
    def plusOne(self, digits):
        last_el= digits[len(digits)-1]
        length= len(digits)
        add_one = last_el+1
        if (add_one==10):
            flag = 0
            for i in range(length-1, -1 , -1):
                if (digits[i]==9):
                    flag=flag+1
                else:
                    break
            test = length-flag
            if (digits[test-1]!=9):
                digits[test-1]=digits[test-1]+1
                for i in range (test, length):
                    digits[i]=0
            else:
                digits[test]=1
                for i in range(test+1, length):
                    digits[i]=0
                digits.append(0)

        else:
            digits[length-1]= add_one
        return digits


s1=Solution()
digits = [8,9,9,9]
result = s1.plusOne(digits=digits)
print(result)