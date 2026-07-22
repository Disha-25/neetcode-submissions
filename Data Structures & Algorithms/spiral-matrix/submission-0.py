class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        res = []
        # 1 2 3
        # 4 5 6
        m = len(mat) # 2
        n = len(mat[0])  # 3
        top, bottom, left, right = 0, m-1, 0, n-1
        direction = 0
        while top <= bottom and right >= left:
            # move left to right
            if direction == 0:
                for i in range(left, right+1):
                    res.append(mat[top][i])
                top +=1
            # move top to bottom
            if direction == 1:
                for i in range(top, bottom +1):
                    res.append(mat[i][right])
                right -= 1
            # move right to left
            if direction == 2:
                for i in range(right, left-1, -1):
                    res.append(mat[bottom][i])
                bottom -= 1
            # move bottom to top
            if direction == 3:
                for i in range(bottom, top-1, -1):
                    res.append(mat[i][left])
                left += 1
            direction = (direction + 1) % 4
        return res
