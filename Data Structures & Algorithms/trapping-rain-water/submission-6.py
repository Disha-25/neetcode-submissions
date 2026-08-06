class Solution:
    def trap(self, height: List[int]) -> int:
        n, ans = len(height), 0
        lmax = height[0]
        rmax = height[-1]
        l, r = 0, n-1
        while l<=r:
            lmax = max(lmax, height[l])
            rmax = max(rmax, height[r])
            minimum = min(lmax, rmax)
            if height[l] <= height[r]:
                ans += minimum - height[l]
                l+=1
            else:
                ans += minimum - height[r]
                r -= 1
        return ans
        
        