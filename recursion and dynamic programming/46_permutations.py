'''
Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.

Example:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
'''


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(nums, index, answers):
            if index == len(nums) - 1:
                answers.append(nums[:])
                return
            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                helper(nums, index + 1, answers)
                nums[index], nums[i] = nums[i], nums[index]

        answers = []
        helper(nums, 0, answers)
        return answers
