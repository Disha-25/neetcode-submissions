class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i,j = 0,0
        n, m = len(word), len(abbr)
        while i<n and j<m:
            if abbr[j].isalpha():
                if word[i]!=abbr[j]:
                    return False
                i+=1
                j+=1
            else:
                if abbr[j] == '0':
                    return False
                counter = 0
                while j<m and abbr[j].isdigit():
                    counter = counter*10 + int(abbr[j])
                    j+=1
                i+=counter
        return i == n and j == m
        
        