"""
For a given integer array/list 'ARR' of size 'N' containing all distinct values, find the total number of 
'Inversions' that may exist. An inversion is defined for a pair of integers in the array/list when the 
following two conditions are met.

A pair ('ARR[i]', 'ARR[jJ') is said to be an inversion when:

1. 'ARRi] > 'ARRLj]'
2. 'i' < 'j'
Where 'i' and 'j' denote the indices ranging from [0, 'N' ).

"""
"""
Input: nums = [3, 2, 1], n = 3
Output: 3
We have a total of 3 pairs which satisfy the condition of inversion. (3, 2), (2, 1) and (3, 1).

Input: nums = [2, 5, 1, 3, 4], n = 5
Output: 4
We have a total of 4 pairs which satisfy the condition of inversion. (2, 1), (5, 1), (5, 3) and (5, 4).

"""




from typing import *
class Solution():
    def countInversions(self, nums: List[int]) -> int:
        count = 0

        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    count += 1
        print(count)
        return count


if __name__ == "__main__":
    s1 = Solution()
    s1.countInversions([2, 5, 1, 3, 4])
