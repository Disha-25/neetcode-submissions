class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        for i in range(n):
            lmax = rmax = height[i]
            for j in range(0, i):
                lmax = max(lmax, height[j])
            for j in range(i+1, n):
                rmax = max(rmax, height[j])
            res += min(lmax, rmax) - height[i]
        return res
        
        
        