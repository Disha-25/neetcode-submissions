class Solution:
    def scoreOfString(self, s: str) -> int:
        # ord is used to get unique code value of any character
        # Time Complexity - O(n), Space Complexity - O(1)
        score = 0
        for i in range(len(s)-1):
            score += abs(ord(s[i+1]) - ord(s[i]))
        return score
        