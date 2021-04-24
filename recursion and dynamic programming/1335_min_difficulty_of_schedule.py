'''
You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the i-th job, you have to finish all the jobs j where 0 <= j < i).

You have to finish at least one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the d days.

The difficulty of a day is the maximum difficulty of a job done in that day.

Given an array of integers jobDifficulty and an integer d. The difficulty of the i-th job is jobDifficulty[i].

Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.

Example 1:
Input: jobDifficulty = [6,5,4,3,2,1], d = 2
Output: 7
Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
Second day you can finish the last job, total difficulty = 1.
The difficulty of the schedule = 6 + 1 = 7

Example 2:
Input: jobDifficulty = [7,1,7,1,7,1], d = 3
Output: 15
'''


# attempt one: memoization and recursion
# we're trying to find all possible combinations of the different ways we can partition an array
# if d =2 we want to cut the array in two parts
# consider the array [6,5,4,3,2,1] and d =2
# we want to try the following combinations:
# [6][5,4,3,2,1]
# [6,5][4,3,2,1]
# [6,5,4][3,2,1]
# [6,5,4,3][2,1]
# [6,5,4,3,2][1]
# so we create a recursive call for [6],[5,4,3,2,1] we test the score for this partition
# then we increment index by one and try [6,5], [4,3,2,1] and test the score again
# so on and so forth.

class Solution:
    def minDifficulty(self, jobs: List[int], d: int) -> int:
        if d > len(jobs): return -1

        def helper(jobs, index, d, cache):
            if (index, d) in cache:
                return cache[(index, d)]
            if d == 1:
                cache[(index, 1)] = max(jobs[index:])
                return cache[(index, 1)]
            answer = float(inf)
            maxsofar = 0
            for i in range(index, len(jobs) - (d - 1)):
                maxsofar = max(jobs[index:i + 1])
                a = helper(jobs, i + 1, d - 1, cache)
                answer = min(answer, maxsofar + a)

            cache[(index, d)] = answer
            return answer

        return helper(jobs, 0, d, {})
