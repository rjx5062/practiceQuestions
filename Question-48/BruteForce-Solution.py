"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise). You have to rotate the 
image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the 
rotation.

"""

"""
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

"""




from typing import *
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        newMatrix = []
        Row = len(matrix) - 1

        for i in range(0, len(matrix)):
            newMatrix.append([])
            for j in range(0, len(matrix[i])):
                newMatrix[i].append(matrix[i][j])

        # print(newMatrix)

        for i in range(0, len(newMatrix)):
            for j in range(0, len(newMatrix[i])):
                print(matrix[i][j], newMatrix[Row - j][i])
                matrix[i][j] = newMatrix[Row - j][i]

        # matrix.reverse()

        print(matrix)


if __name__ == "__main__":
    s1 = Solution()
    s1.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
