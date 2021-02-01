'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach
the bottom-right corner of the grid (marked 'Finish' in the diagram below). How many possible unique paths are there?
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m ==1 or n == 1:
            return 1
        result = [1]* n
        for i in range(1, m):
            for j in range(1, n):
                result[j]+= result[j-1]
            print(result)
        return result[-1]

# below was my 2nd attempt using memoization to speed up my first solution 
class Solution3:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.util(m, n, {})
    def util(self, m, n, map):
        if m< 0 or n< 0:
            return 0
        if (m,n) in map:
            return map[(m,n)]
        if m ==1 and n == 1:
            return 1
        map[(m,n)] = self.util(m-1, n, map)+ self.util(m, n-1, map)
        return map[(m,n)]
# below was my first attempt a backtracking solution it time limit exceeded
class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        res = self.util(m-1, n-1, [], set())
        return res or 1

    def util(self, m, n, path, res):
        if m <0 or n < 0:
            return 0
        if m == 0 and n == 0:
            res.add(tuple(path))
            print(path)
            return 1
        path.append((m-1, n))
        a = self.util(m-1, n, path, res)
        path.pop()
        path.append((m, n-1))
        b= self.util(m, n-1, path, res)
        path.pop()
        return a+b

a = Solution()
m = 7; n = 3
print(a.uniquePaths(m, n))

# prints
# [(0, 1), (0, 0)]
# [(1, 0), (0, 0)]
# 2