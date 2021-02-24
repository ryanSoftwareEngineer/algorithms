'''
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of
all the elements of nums except nums[i].

Note: Please solve it without division and in O(n).
Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
'''

# nums 1 2 6 24
# ans 24 24 12 4
# ans = ans[1], nums[0] + ans[2], nums[1] + ans[3] ...
class Solution(object):
    def productExceptSelf(self, nums):
        product = 1
        result = [0]* len(nums)
        for a in range(len(nums)-1, -1, -1):
            product *= nums[a]
            result[a] = product
        result[0] = result[1]
        product = 1
        for a in range(1, len(nums)-1):
            product*= nums[a-1]
            result[a]= product * result[a+1]
        result[-1] = (product * nums[-2])
        return result


input =[1,2,3,4]
a = Solution()
a.productExceptSelf(input)