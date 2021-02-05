'''A message containing letters from A-Z can be encoded into numbers using the following mapping:
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "111" can have each of its "1"s be mapped into 'A's to make "AAA", or it could be mapped to "11" and "1" ('K' and 'A' respectively) to make "KA". Note that "06" cannot be mapped into 'F' since "6" is different from "06".
Given a non-empty string num containing only digits, return the number of ways to decode it.
The answer is guaranteed to fit in a 32-bit integer.
'''

class Solution:
    def numDecodings(self, s):
        if not s:
            return 0
        chars = list(s)
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        if int(chars[0]) > 0:
            dp[1] = 1
        for i in range(2, len(s) + 1):
            single = int(chars[i - 1])
            pair = int(chars[i - 2] + chars[i - 1])
            if single > 0:
                dp[i] += dp[i - 1]
            print(dp[i], single, pair)
            if pair > 9 and pair < 27:
                dp[i] += dp[i - 2]
        print(dp)
        return dp[-1]


s = "12413"
a = Solution()
print(a.numDecodings(s))
