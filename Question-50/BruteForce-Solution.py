"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

"""
"""
Input: x = 2.00000, n = 10
Output: 1024.00000

Input: x = 2.10000, n = 3
Output: 9.26100

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

"""




from typing import *
class Solution:

    def myPow(self, x: float, n: int) -> float:
        ans = 1
        new_n = abs(n)

        for i in range(new_n):
            ans *= x

        if n < 0:
            print(1/ans)
            return 1/ans
        else:
            print(ans)
            return ans


if __name__ == "__main__":
    s1 = Solution()
    s1.myPow(2.0, -2)
