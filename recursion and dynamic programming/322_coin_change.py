'''
the famous classic variation of the knapsack problem
https://leetcode.com/problems/coin-change/
'''

#  first attempt:
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coinsset = set(coins)
        visited = {}

        def helper(target):
            if target < 0:
                return float(inf)
            if target in visited:
                return visited[target]

            if target in coinsset:
                return 1
            answer = float(inf)
            for coin in reversed(coins):
                answer = min(answer, helper(target - coin))
            visited[target] = answer + 1
            return answer + 1
        return helper(amount) if helper(amount) < float(inf) else -1

#  dp attempt

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [0 for i in range(amount + 1)]
        dp[0] = 0

        for i in range(1, amount + 1):
            dp[i] = float(inf)
            for coin in coins:
                # this check can be skipped if we iterate through coins first then for each coin iterate
                #  array [coin] -> amount
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin])
            dp[i] += 1
        return dp[-1] if dp[-1] < float(inf) else -1