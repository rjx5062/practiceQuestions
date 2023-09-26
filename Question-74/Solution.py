"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

"""
"""
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

"""




from typing import *
class Solution:

    # def binarySearch(self, nums: List[int], left: int, right: int, target: int) -> bool:

    #     mid = (left + right) // 2

    #     while left <= right:
    #         if nums[mid] == target:
    #             return True
    #         elif nums[mid] < target:
    #             left = mid + 1
    #         else:
    #             right = mid - 1

    #     return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # Implementing Binary Search Algorithm for a 2-dimentional array

        left, right = 0, (len(matrix) * len(matrix[0])) - 1

        # mid = (left + right) // 2

        while left <= right:

            mid = (left + right) // 2

            row = mid // len(matrix[0])
            col = mid % len(matrix[0])

            if matrix[row][col] == target:
                print(True)
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1

        print(False)
        return False


if __name__ == "__main__":
    s1 = Solution()
    s1.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3)
