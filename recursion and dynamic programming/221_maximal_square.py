'''
https://leetcode.com/problems/maximal-square/
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
'''

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [int(x) for x in matrix[0]]
        dp_prev =  0
        max_so_far = max(dp)
        for row in range(1, len(matrix)):
            dp_prev = dp[0]
            dp[0] = int(matrix[row][0])
            max_so_far = max(max_so_far, dp[0])
            for col in range(1, len(matrix[row])):
                val = int(matrix[row][col])
                if val ==0:
                    dp_prev = dp[col]
                    dp[col] =0
                else:
                    temp_dp = min(dp[col], dp[col-1], dp_prev)
                    dp_prev = dp[col]
                    dp[col] = temp_dp +1
                    max_so_far = max(max_so_far, dp[col])
        return max_so_far**2
