"""
You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your profit
by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum 
profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

"""
"""
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

"""




from typing import *
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        for i in range(0, len(prices)):
            tempMax = 0
            diff = 0
            for j in range(i, len(prices)):
                if (prices[j] > tempMax):
                    tempMax = prices[j]
                    diff = tempMax - prices[i]
            maxi = max(maxi, diff)
        print(maxi)
        return maxi


if __name__ == "__main__":
    s1 = Solution()
    s1.maxProfit([7, 1, 5, 6, 4, 3])
