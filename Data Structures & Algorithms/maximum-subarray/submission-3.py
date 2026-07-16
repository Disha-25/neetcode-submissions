class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maxSum = nums[0]
        if len(nums)==1: return nums[0]
        for i in range(n):
            subArrSum = 0
            for j in range(i, n):
                subArrSum += nums[j]
                if maxSum < subArrSum: maxSum = subArrSum
        return maxSum