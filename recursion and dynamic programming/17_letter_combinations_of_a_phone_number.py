'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
Return the answer in any order.

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
'''


class Solution:
    def letterCombinations(self, digits: str):
        if digits == "":
            return []
        book = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        answer = []
        self.backtrack(digits, book, [], 0, answer)
        return answer

    def backtrack(self, digits, book, path, n, answer):
        if n == len(digits):
            answer.append(''.join(path))
            return
        for num in book[digits[n]]:
            path.append(num)
            self.backtrack(digits, book, path, n + 1, answer)
            path.pop()