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
""" Floyd's Cycle Algorithm Revision Required """




from typing import *
class Solution:

    def findDuplicate(self, nums: List[int]) -> int:
        # Finding the intersection in Floyd's Linked List Cycle

        slow_ptr, fast_ptr = 0, 0

        while True:
            slow_ptr = nums[slow_ptr]
            fast_ptr = nums[nums[fast_ptr]]
            if slow_ptr == fast_ptr:
                break

        # Finding the start of Floyd's cycle which will alway be our repeated number

        new_ptr = 0

        while True:
            slow_ptr = nums[slow_ptr]
            new_ptr = nums[new_ptr]
            if slow_ptr == new_ptr:
                break

        print(slow_ptr)
        return slow_ptr


if __name__ == "__main__":

    s1 = Solution()
    s1.findDuplicate([3, 1, 3, 4, 2])
