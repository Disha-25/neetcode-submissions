class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
# Sol 1: Linear - O(m x n)
        # for arr in matrix:
        #     if target in arr: return True
        # return False

# Sol 2: Binary - O(log(m*n))
        # m = len(matrix)
        # n = len(matrix[0])
        # # searching which row can contain
        # firstRow = 0
        # lastRow = m-1
        # while firstRow <= lastRow:
        #     row = (firstRow + lastRow) // 2
        #     if target >= matrix[row][0] and target <= matrix[row][n-1]:
        #         return self.istargetInRow(matrix[row], target)
        #     elif target <= matrix[row][0]:
        #         lastRow = row - 1
        #     else:
        #         firstRow = row + 1
        # return False

# Sol 3: Binary - O(log(m*n)) One Pass
        m = len(matrix) # no of rows
        n = len(matrix[0]) # no of columns
        l, r = 0, m*n - 1
        while l<=r:
            mid = l + (r-l) // 2
            # map real indexes 
            row = mid // n
            col = mid % n
            if target < matrix[row][col]:
                r = mid - 1
            elif target > matrix[row][col]:
                l = mid + 1
            else:
                return True
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



