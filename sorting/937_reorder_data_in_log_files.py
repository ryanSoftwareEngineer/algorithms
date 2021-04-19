'''
You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

There are two types of logs:

Letter-logs: All words (except the identifier) consist of lowercase English letters.
Digit-logs: All words (except the identifier) consist of digits.
Reorder these logs so that:

The letter-logs come before all digit-logs.
The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
The digit-logs maintain their relative ordering.
Return the final order of the logs.

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
Explanation:
The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".
'''

# first approach writing custom coomparator. 
import functools
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def compare(a, b):
            arr1 = a.split(" ", 1)
            arr2 = b.split(" ", 1)
            if arr1[1] < arr2[1]:
                return -1
            elif arr1[1] > arr2[1]:
                return 1
            else:
                if arr1[0] < arr2[0]:
                    return -1
                elif arr1[0] > arr2[0]:
                    return 1
                else:
                    return 0
        digits = []
        letters = []
        for log in logs:
            if log.split(" ",1)[1][0].isalpha():
                letters.append(log)
            else:
                digits.append(log)
        letters = sorted(letters, key=functools.cmp_to_key(compare))
        print(letters, digits)
        return letters + digits