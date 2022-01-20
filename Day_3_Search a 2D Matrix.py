# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        i, j = 0, n-1
        while i>=0 and j>=0 and i<m and j<n:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j-=1
            else:
                i+=1
        return False
