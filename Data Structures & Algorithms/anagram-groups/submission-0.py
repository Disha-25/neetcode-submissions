class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        
        for s in strs:
            count = [0] * 26 # a ...z
            for c in s:
                count[ord(c) - ord("a")]+=1
            ans[tuple(count)].append(s) #tuple(count)-> 1a 1c 1t, s-> act
        return list(ans.values())