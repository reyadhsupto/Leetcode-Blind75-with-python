class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum, maxsum=0,float('-inf')
        for val in nums:
            cursum = max(cursum+val,val)
            maxsum = max(cursum,maxsum)
        return maxsum

        