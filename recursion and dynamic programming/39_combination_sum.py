'''
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
'''
# recursive

class Solution(object):
    def combinationSum(self, candidates, target):
        return self.__sum_util(candidates, [], 0, target, [])
    def __sum_util(self, nums, temp_arr, index, target, result):
        if target <0:
            return
        if target == 0:
            result.append(temp_arr[:])
            return
        for i in range(index, len(nums)):
            temp_arr.append(nums[i])
            self.__sum_util(nums, temp_arr, i, target-nums[i], result)
            temp_arr.pop()
        return result

cand = [2, 5, 7]
a = Solution()
b= a.combinationSum(cand, 12)
print(b)

'''
output: [[2, 2, 2, 2, 2, 2], [2, 5, 5], [5, 7]]
'''