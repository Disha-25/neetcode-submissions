class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Linear - O(m x n)
        # for arr in matrix:
        #     if target in arr: return True
        # return False

        # Binary - 
        m = len(matrix)
        n = len(matrix[0])
        # searching which row can contain
        firstRow = 0
        lastRow = m-1
        while firstRow <= lastRow:
            row = (firstRow + lastRow) // 2
            if target >= matrix[row][0] and target <= matrix[row][n-1]:
                return self.istargetInRow(matrix[row], target)
            elif target <= matrix[row][0]:
                lastRow = row - 1
            else:
                firstRow = row + 1
        return False
            
    def istargetInRow(self, row: List[int], target) -> bool:
        left = 0
        right = len(row) - 1
        while left <= right:
            mid = (left+right)//2
            if target == row[mid]:
                return True
            elif target <= row[mid]:
                right = mid - 1
            else:
                left = mid +1
        return False



