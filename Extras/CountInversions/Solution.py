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
    def merge(self, nums: List[int], low: int, mid: int, high: int) -> int:

        numInverse = 0
        left = low
        right = mid + 1
        print(nums, low, mid, high)

        while (left <= mid and right <= high):
            if nums[left] >= nums[right]:
                numInverse += ((mid - left) + 1)
                right += 1
            else:
                left += 1

        return numInverse

    def mergeSort(self, nums: List[int], low: int, high: int) -> int:

        numInverse = 0

        if low >= high:
            return numInverse

        mid = (low + high) // 2

        numInverse += self.mergeSort(nums, low, mid)
        numInverse += self.mergeSort(nums, mid + 1, high)

        numInverse += self.merge(nums, low, mid, high)

        return numInverse

    def countInversions(self, nums: List[int]) -> int:

        count = self.mergeSort(nums, 0, (len(nums) - 1))

        print(count)
        return count


if __name__ == "__main__":
    s1 = Solution()
    s1.countInversions([5, 4, 3, 2, 1])
