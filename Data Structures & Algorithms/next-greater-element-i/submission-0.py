class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = len(nums1)
        n2 = len(nums2)
        right = n2-1
        res = []
        for i in range(n1):
            currmax = -1
            for j in range(right, -1, -1):
                if nums2[j] == nums1[i]:
                    res.append(currmax)
                    break
                elif nums2[j]>nums1[i]:
                    currmax = nums2[j]
        return res