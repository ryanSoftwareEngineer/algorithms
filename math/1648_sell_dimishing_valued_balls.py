'''
You have an inventory of different colored balls, and there is a customer that wants orders balls of any color.
The customer weirdly values the colored balls. Each colored ball's value is the number of balls of that color you currently have in your inventory. For example, if you own 6 yellow balls, the customer would pay 6 for the first yellow ball. After the transaction, there are only 5 yellow balls left, so the next yellow ball is then valued at 5 (i.e., the value of the balls decreases as you sell more to the customer).
You are given an integer array, inventory, where inventory[i] represents the number of balls of the ith color that you initially own. You are also given an integer orders, which represents the total number of balls that the customer wants. You can sell the balls in any order.
Return the maximum total value that you can attain after selling orders colored balls. As the answer may be too large, return it modulo 109 + 7.
'''

# formula to find value of n + (n-1) + (n-2) ... (n-d) = ((n +d+1) * (n-d)) /2
# first attempt I used a priority queue and when popping I would just subtract n-d
# problem with this method is once column A hits column B in value, the two oscillate to lower value
# causing you to  calculate n + n-1  while column A and column B > column C

# this solution calculates the balls together when columns are equivalent

class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory.sort(reverse=True)
        inventory.append(0)
        answer = 0
        width = 0
        i = 0
        while orders > 0:
            width += 1
            if inventory[i] > inventory[i + 1]:
                n = inventory[i]
                d = inventory[i + 1]
                balls = width * (n - d)
                if balls < orders:
                    answer += width * ((n + d + 1) * (n - d)) // 2
                    orders -= balls
                else:
                    a, remainder = divmod(orders, width)
                    d = n - a
                    answer += width * ((n + d + 1) * (n - d)) // 2
                    answer += remainder * (d)
                    return answer % ((10 ** 9) + 7)
            i += 1
