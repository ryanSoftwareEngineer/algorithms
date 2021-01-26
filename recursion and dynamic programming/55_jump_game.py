'''

Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
'''


# dfs approahc
def canJump(nums, index, out, visited):
    if index > len(nums)-1 or len(out)>0 or index in visited:
        return
    if index == len(nums)-1:
        out.append(1)
        return
    for i in range(nums[index], -1, -1):
        print(index, i, nums[index+i], visited)
        visited.add(index)
        canJump(nums, index+i, out, visited)
        visited.add(index+i)
    return out

array =[3,2,1,1,4]
print(canJump(array, 0, [], set()))
# outputs
# 0 3 1 set()
# 3 1 4 {0}
# 3 0 1 {0, 3, 4}
# 0 2 1 {0, 3, 4}
# 0 1 2 {0, 2, 3, 4}
# 0 0 3 {0, 1, 2, 3, 4}
# [1]
