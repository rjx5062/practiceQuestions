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

        c = collections.Counter(nums)
        ans = []

        for i in range(1, len(nums) + 1):
            if c[i] > 1:
                ans.append(i)
            if c[i] == 0:
                ans.append(i)

        print(ans)
        return ans


if __name__ == "__main__":
    s1 = Solution()
    s1.repeatmissNumber([3, 1, 2, 5, 4, 6, 7, 5])
