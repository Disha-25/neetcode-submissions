class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        length = n*n
        
        freq = [0] * (length + 1)
        # freq = [0,0,0,0,0,0,...]
        for row in grid:
            for n in row:
                freq[n] += 1
        repeated = -1
        missing = -1
        for i in range(1, length + 1):
            if freq[i] == 2:
                repeated = i
            elif freq[i] == 0:
                missing = i
        
        return [repeated, missing]