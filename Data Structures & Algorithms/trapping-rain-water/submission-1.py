class Solution:
    def trap(self, height: List[int]) -> int:
        # n = len(height)
        # res = 0
        # for i in range(n):
        #     lmax = rmax = height[i]
        #     for j in range(0, i):
        #         lmax = max(lmax, height[j])
        #     for j in range(i+1, n):
        #         rmax = max(rmax, height[j])
        #     res += min(lmax, rmax) - height[i]
        # return res

        n, res = len(height), 0
        lmax = height[0]
        rmax = height[-1]
        l, r = 0, n-1
        while l<=r:
            lmax = max(lmax, height[l])
            rmax = max(rmax, height[r])
            if lmax < rmax:
                res += min(lmax, rmax) - height[l]
                l+=1
            else:
                res += min(lmax, rmax) - height[r]
                r-=1
        return res

        
        
        