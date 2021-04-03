'''
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of groups so that each group is a contiguous section all of the same character. Then for each group, say the number of characters, then say the character. To convert the saying into a digit string, replace the counts with a number and concatenate every saying.

For example, the saying and conversion for digit string "3322251": two 3's, three 2's, one 5, one 1 => 23321511

Example 2:
Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
'''


class Solution:
    def countAndSay(self, n: int) -> str:
        if n < 2:
            return '1'
        i = 2
        dp = "1"
        while i <= n:
            counter = 1
            newval = []
            for a in range(1, len(dp)+1):
                if a != len(dp):
                    if dp[a] == dp[a-1]:
                        counter+=1
                        continue
                newval.append(str(counter))
                newval.append(dp[a-1])
                counter = 1
            dp = newval
            i+=1
        return ''.join(dp)


class Solution_recursive:
    def countAndSay(self, n: int) -> str:
        path = self.helper(n)
        return ''.join(path)

    def helper(self, n):
        if n == 1:
            return ['1']
        phrase = self.countAndSay(n - 1)
        i = 1
        j = 0
        newphrase = []
        while i < len(phrase) + 1:
            if i < len(phrase):
                if phrase[i] == phrase[i - 1]:
                    i += 1
                    continue
            newphrase.append(str(i - j))
            newphrase.append(phrase[i - 1])
            j = i
            i += 1
        return newphrase
# input 5 = "111221"