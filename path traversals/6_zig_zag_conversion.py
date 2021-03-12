'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display
this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
'''

# create a matrix of rows
# set direction to increase
# for every iteration of string s ... append to matrix then either increase or decrease row number
# when row = 0 or numRows then change directon to increase row
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows >= len(s) or numRows == 1:
            return s
        cycle = 2*numRows-2
        result = []
        for i in range(numRows):
            for j in range(0, len(s)+1, cycle):
                if i > 0 and i < numRows-1 and j > 0:
                    result.append(s[j-i])
                if j+i < len(s):
                    result.append(s[j+i])
        return ''.join(result)


class attempt_one:
    # fill a matrix then iterate hte matrix in order
    def convert(self, s: str, numRows: int) -> str:
        if len(s) < 2:
            return s
        row = -1
        cycle = 2 * numRows - 2
        matrix = []
        for i, val in enumerate(s):
            if i % cycle == 0:
                row += 1
                matrix.append([])
            matrix[row].append(val)
        row = col = 0
        result = ''
        max_col = len(matrix) - 1
        while len(result) < len(s):
            # this is bad string concatenation for larger data sets, shoulda appended to list then ''.join(list) at the end
            result += matrix[row][col]
            if col > 0 and col < numRows - 1 and len(matrix[row]) > cycle - col:
                result += matrix[row][cycle - col]
            row += 1
            if row > max_col:
                row = 0
                col += 1
            if row == max_col and col > len(matrix[max_col]) - 1:
                row = 0
                col += 1
        return result