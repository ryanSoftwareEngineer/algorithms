'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

Example:
Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''


class Solution:
    def intToRoman(self, num: int) -> str:
        single = {1: "I", 4: "IV" ,5: "V", 9: "IX"}
        double = {1: "X", 4: "XL" ,5: "L", 9: "XC"}
        triple = {1: "C", 4: "CD", 5: "D", 9: "CM"}
        ans = ["M" ]* (num//1000)
        num %= 1000
        if num//100 > 0:
            digit = num//100
            self.add_digit(digit, triple, ans)
        num %=100
        if num//10 >0:
            digit = num // 10
            self.add_digit(digit, double, ans)
        num %= 10
        if num > 0:
            self.add_digit(num, single, ans)
        return ''.join(ans)

    def add_digit(self, digit, book, ans):
        if digit == 4 or digit == 9:
            ans.append(book[digit])
        else:
            if digit >= 5:
                ans.append(book[5])
                digit -= 5
            while digit > 0:
                ans.append(book[1])
                digit -= 1