'''
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
'''
# x^n can be divided such that x^(n/2) * x^(n/2) = x^n continuously
# in this solution we essentially double n while doubling x until n == the n we're looking for
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n <0:git 
            return (1 / self.myPow(x, abs(n)))
        if n==0:
            return 1
        if n ==1:
            return x
        def helper(n, xval):
            i = 1
            prev = 1
            prev_val = xval
            while i < n:
                prev_val = xval
                xval*=xval
                prev = i
                i<<=1
            return prev_val, n-prev
        ans = 1
        while n > 0:
            a, n = helper(n, x)
            ans*=a
        return ans