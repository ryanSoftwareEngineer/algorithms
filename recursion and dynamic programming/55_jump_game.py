'''

Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
'''
class Solution():
    def canJump(self, nums):
        target = len(nums)-1
        for i in range(target, -1, -1):
            if nums[i]+ i >= target:
                target = i
        return target == 0


#my first attempt was a dfs / greedy design, taking the maximum step possible and iterating back when hitting a wall
# storing each index in visited[] this is reduced to o(n) run time but it's TLE and it uses xtra memory
class Solution2(object):
    def canJump2(self, nums):
        return len(self.util(nums, 0, [], set()))>0

    def util(self, nums, index, out, visited):
        if index in visited:
            return
        if index >= len(nums)-1:
            out.append(1)
            return out
        if nums[index] >= len(nums)-1:
            out.append(1)
            return out
        i = nums[index]
        visited.add(index)
        while i>=0  and len(out) <1:
            self.util(nums, index+i, out, visited)
            i-=1
        return out


a = Solution()
# array =[3,9,2,42,5,6]

array = [5,4,3,2,1,1]
print(a.canJump(array))