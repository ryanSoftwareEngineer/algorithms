'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

ooo a solver might be a fun addition to this...
I'm thinking would prolly require loop to add value to blanks, validating then backtracking if validation fails and moving on to next
integer
'''


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        minis = {}

        for i, row in enumerate(board):
            rows = {}
            mini = 0
            if i > 5:
                mini += 6
            elif i > 2:
                mini += 3
            for j, col in enumerate(row):
                if board[i][j] == '.':
                    continue
                #  handle row case
                if col in rows:
                    return False
                rows[col] = j
                # handle col case
                if col in cols:
                    if j in cols[col]:
                        return False
                    cols[col].add(j)
                else:
                    cols[col] = set()
                    cols[col].add(j)
                tmp = mini
                if j > 5:
                    tmp = mini + 2
                elif j > 2:
                    tmp = mini + 1
                # handle mini block case
                if col in minis:
                    if tmp in minis[col]:
                        return False
                    minis[col].add(tmp)
                else:
                    minis[col] = set()
                    minis[col].add(tmp)
        return True
