class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [-1]*n
        maxi = 0
        for i in range(n-2,-1,-1):
            ans[i] = max(arr[i+1], maxi)
            maxi = ans[i]
        return ans