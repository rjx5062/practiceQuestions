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
        new_n = abs(n)
        ans = 1
        while new_n > 0:
            if new_n % 2 == 0:
                x *= x
                new_n = new_n // 2

            else:
                ans *= x
                new_n -= 1

        if n < 0:
            print("ans", 1/ans)
            return 1/ans
        else:
            print("ans", ans)
            return ans


if __name__ == "__main__":
    s1 = Solution()
    s1.myPow(2.0, -2)
