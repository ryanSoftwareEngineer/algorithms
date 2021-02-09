'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''

class Solution:
    def maxProfit(self, prices):
        # keep track of lowest and highest
        # if new low is found set new_low to that and new_highest to 0
        # if new_highest - new_low  > previous, then update
        low = high  = prices[0]
        summ = 0
        for val in prices:
            if val < low:
                low = high = val
            if val > high:
                high = val
                summ = max(summ, high-low)
        print(summ)
        return summ

input = [7,1,5,3,6,4]
a = Solution()
a.maxProfit(input)
# output: 5 