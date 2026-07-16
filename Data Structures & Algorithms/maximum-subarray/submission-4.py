class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Brute Force - O(n^2)
        # n = len(nums)
        # maxSum = nums[0]
        # if len(nums)==1: return nums[0]
        # for i in range(n):
        #     subArrSum = 0
        #     for j in range(i, n):
        #         subArrSum += nums[j]
        #         if maxSum < subArrSum: maxSum = subArrSum
        # return maxSum

        # Optimized - O(n)
        maxSum = -1001
        subArrSum = 0
        for num in nums:
            if subArrSum < 0: subArrSum = 0
            subArrSum += num
            maxSum = max(maxSum, subArrSum)
        return maxSum