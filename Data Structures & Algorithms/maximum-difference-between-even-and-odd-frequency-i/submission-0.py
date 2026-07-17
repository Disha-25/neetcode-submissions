class Solution:
    def maxDifference(self, s: str) -> int:
        count = Counter(s)
        res = float("-inf")
        # Counter({'a': 5, 'b': 2, 'c': 1})
        for odd in count.values():
            # print(freq) # 5,2,1
            if odd % 2 == 0: continue
            for even in count.values():
                if even % 2 == 1: continue
                res = max(res, odd - even)
        return res

            