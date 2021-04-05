'''
Given a collection of numbers, nums, that might contain duplicates,
return all possible unique permutations in any order.
'''

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def helper(nums, combo, answers, target_length):
            if len(combo)== target_length:
                answers.append(combo[:])
                return
            for num in nums:
                if nums[num]>0:
                    nums[num]-=1
                    combo.append(num)
                    helper(nums, combo, answers, target_length)
                    combo.pop()
                    nums[num]+=1
        answers = []
        hashnums = Counter(nums)
        target_length = len(nums)
        helper(hashnums, [], answers, target_length)
        return answers