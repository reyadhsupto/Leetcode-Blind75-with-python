class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curmax,curmin = 1,1
        for n in nums:
            temp = curmax
            curmax = max(curmax*n,curmin*n,n)
            curmin = min(temp*n,curmin*n,n)
            res = max(curmax,res)
        return res
        