"""
You are given a read only array of n integers from 1 to n.
Each integer appears exactly once except A which appears twice and B which is missing.
Return A and B.
Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
Note that in your output A should precede B.

"""
"""
Input:[3 1 2 5 3] 
Output:[3, 4] 
A = 3, B = 4

"""




from typing import *
import collections
class Solution:
    def repeatmissNumber(self, nums: List[int]) -> List[int]:
        sumOfN, sumOfNSquare = 0, 0
        sumOfE, sumOfESquare = 0, 0

        for i in range(1, (len(nums) + 1)):
            sumOfN += i
            sumOfE += nums[i - 1]
            sumOfNSquare += i * i
            sumOfESquare += nums[i - 1] * nums[i - 1]

        rMinusm = sumOfE - sumOfN
        rPlusm = (sumOfESquare - sumOfNSquare)/(sumOfE - sumOfN)

        r = int((rPlusm + rMinusm)/2)
        m = int((rPlusm - rMinusm)/2)

        print([r, m])
        return [r, m]


if __name__ == "__main__":
    s1 = Solution()
    s1.repeatmissNumber([3, 1, 2, 5, 4, 6, 7, 5])
