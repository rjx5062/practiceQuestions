"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are 
adjacent, with the colors in the order red, white, and blue. We will use the integers 0, 1, and 2 to represent the 
color red, white, and blue, respectively. You must solve this problem without using the library's sort function.

"""
"""
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Input: nums = [2,0,1]
Output: [0,1,2]

"""
from typing import *

class Solution:
    def pushToFront(self, nums: List[int], insertIndex: int, removeIndex:int, element: int) -> None:
        nums.pop(0 + removeIndex)
        nums.insert(0 + insertIndex, element)
        
    def sortColors(self, nums: List[int]) -> None:
        last0Index = -1
        for i in range(0, len(nums)):
            if nums[i] == 2:
                continue
            elif nums[i] == 1:
                if last0Index == -1:
                    self.pushToFront(nums, 0, i, nums[i])
                else:
                    self.pushToFront(nums, last0Index + 1, i, nums[i])
            else:
                self.pushToFront(nums, 0, i, nums[i])
                last0Index += 1
        print(nums)
                
if __name__ == "__main__":
    s1 = Solution()
    s1.sortColors([2, 0, 1])
    