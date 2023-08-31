"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.

"""
"""
Input: nums = [1,3,4,2,2]
Output: 2

Input: nums = [3,1,3,4,2]
Output: 3

"""




from typing import *
import collections
class Solution:

    def findDuplicate(self, nums: List[int]) -> int:

        c = collections.Counter(nums)

        for i in c.keys():
            if c[i] > 1:
                print(i)
                return i


if __name__ == "__main__":

    s1 = Solution()
    s1.findDuplicate([3, 1, 3, 4, 2])
