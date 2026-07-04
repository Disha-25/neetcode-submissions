class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        """
        1
        1,1
        1,2,1
        1,3,3,1
        """
        for i in range(1, rowIndex + 1):
            newr = [1]
            for j in range(1, i):
                newr.append(row[j-1] + row[j])
            newr.append(1)
            row = newr
        return row
        